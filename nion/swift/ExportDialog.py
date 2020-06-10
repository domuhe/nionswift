# standard libraries
import functools
import gettext
import logging
import operator
import os
import re
import traceback
import unicodedata
#dmh
from datetime import date
import logging

# third party libraries
# None

# local libraries
from nion.swift.model import ImportExportManager
from nion.ui import Dialog
from nion.ui import UserInterface
from nion.ui import Window

_ = gettext.gettext


class ExportDialog(Dialog.OkCancelDialog):

    def __init__(self, ui: UserInterface.UserInterface, parent_window: Window.Window):
        super().__init__(ui, ok_title=_("Export"), parent_window=parent_window)

        io_handler_id = self.ui.get_persistent_string("export_io_handler_id", "png-io-handler")

        self.directory = self.ui.get_persistent_string("export_directory", self.ui.get_document_location())

# DMH 200610: commented out block due to merge conflicts
#    def __init__(self, ui):
#        super(ExportDialog, self).__init__(ui, ok_title=_("Development Export"))
#
#        io_handler_id = self.ui.get_persistent_string("export_io_handler_id", "png-io-handler") 
#        logging.info("ExportDialog - io_handler_id: " + str(io_handler_id))
#        logging.info("ExportDialog - Init get_document_location: "+ str(self.ui.get_document_location()))
#        self.directory = self.ui.get_persistent_string("export_directory", self.ui.get_document_location())   # last selected export directory
#        logging.info("ExportDialog - Init self.directory: " + str(self.directory))
#        # DMh crude with no checks
#        #today = date.today()
#        #self.directory = "/home/dorothea/Programming/Exports/" + str(today.year) 
#        #logging.info("Init changed self.directory: " + str(self.directory))        

        self.writer = ImportExportManager.ImportExportManager().get_writer_by_id(io_handler_id)
        logging.info("exportdialog - writer: " + str(self.writer))

        directory_column = self.ui.create_column_widget()

        title_row = self.ui.create_row_widget()
        title_row.add_spacing(13)
        title_row.add(self.ui.create_label_widget(_("Export Folder: "), properties={"font": "bold"}))
        title_row.add_stretch()
        title_row.add_spacing(13)

        show_directory_row = self.ui.create_row_widget()
        show_directory_row.add_spacing(26)
        directory_label = self.ui.create_label_widget(self.directory)     # Label shows last selected directory
        show_directory_row.add(directory_label)
        show_directory_row.add_stretch()
        show_directory_row.add_spacing(13)

        choose_directory_row = self.ui.create_row_widget()
        choose_directory_row.add_spacing(26)
        choose_directory_button = self.ui.create_push_button_widget(_("Choose..."))   #  Button to choose export dir
        choose_directory_row.add(choose_directory_button)
        choose_directory_row.add_stretch()
        choose_directory_row.add_spacing(13)

        directory_column.add(title_row)
        directory_column.add(show_directory_row)
        directory_column.add(choose_directory_row)

        file_types_column = self.ui.create_column_widget()

        title_row = self.ui.create_row_widget()
        title_row.add_spacing(13)
        title_row.add(self.ui.create_label_widget(_("File Type: "), properties={"font": "bold"}))
        title_row.add_stretch()
        title_row.add_spacing(13)

        file_types_row = self.ui.create_row_widget()
        file_types_row.add_spacing(26)
        writers = ImportExportManager.ImportExportManager().get_writers()
        logging.info("Exportdialog - writers " + str(writers))
        file_types_combo_box = self.ui.create_combo_box_widget(items=writers, item_getter=operator.attrgetter("name"))
        file_types_combo_box.current_item = self.writer
        file_types_row.add(file_types_combo_box)
        file_types_row.add_stretch()
        file_types_row.add_spacing(13)

        file_types_column.add(title_row)
        file_types_column.add(file_types_row)

        option_descriptions = [
            [_("Include Title"), "title", True],
            [_("Include Microscopist"), "microscopist", True],
            [_("Include Date"), "date", True],
            [_("Include Dimensions"), "dimensions", True],
            [_("Include Sequence Number"), "sequence", True],
            [_("Include Prefix:"), "prefix", False]
        ]

        self.options = dict()

        options_column = self.ui.create_column_widget()

        title_row = self.ui.create_row_widget()
        title_row.add_spacing(13)
        title_row.add(self.ui.create_label_widget(_("Filename: "), properties={"font": "bold"}))
        title_row.add_stretch()
        title_row.add_spacing(13)

        individual_options_column = self.ui.create_column_widget()
        for option_decription in option_descriptions:
            label, option_id, default_value = option_decription
            self.options[option_id] = self.ui.get_persistent_string("export_option_" + option_id,
                                                                    str(default_value)).lower() == "true"
            check_box_widget = self.ui.create_check_box_widget(label)
            check_box_widget.checked = self.options[option_id]

            def checked_changed(option_id_, checked):
                self.options[option_id_] = checked
                self.ui.set_persistent_string("export_option_" + option_id_, str(checked))

            check_box_widget.on_checked_changed = functools.partial(checked_changed, option_id)
            individual_options_column.add_spacing(4)
            individual_options_column.add(check_box_widget)
            if option_id == "prefix":
                self.prefix_edit_widget = self.ui.create_text_edit_widget(properties={"max-height": 35})
                individual_options_column.add(self.prefix_edit_widget)

        options_row = self.ui.create_row_widget()
        options_row.add_spacing(26)
        options_row.add(individual_options_column)
        options_row.add_stretch()
        options_row.add_spacing(13)

        options_column.add(title_row)
        options_column.add(options_row)

        column = self.ui.create_column_widget()
        column.add_spacing(12)
        column.add(directory_column)
        column.add_spacing(4)
        column.add(options_column)
        column.add_spacing(4)
        column.add(file_types_column)
        column.add_spacing(16)
        column.add_stretch()

        def choose() -> None:       #action being called when clicking on "choose" button
            logging.info("Choose dir:" + str(self.directory))
            existing_directory, directory = self.ui.get_existing_directory_dialog(_("Choose Export Directory"),
                                                                                  self.directory)
            logging.info(str(existing_directory) + " self.directory: " + str(directory))
            if existing_directory:
                self.directory = existing_directory
                directory_label.text = self.directory
                self.ui.set_persistent_string("export_directory", self.directory)

        choose_directory_button.on_clicked = choose

        def writer_changed(writer) -> None:
            self.ui.set_persistent_string("export_io_handler_id", writer.io_handler_id)
            self.writer = writer

        file_types_combo_box.on_current_item_changed = writer_changed

        self.content.add(column)

    def do_export(self, display_items):
        directory = self.directory
        writer = self.writer
        if directory:
            # dmh sort  display_items by  creation time before this!
          for index, display_item in enumerate(display_items):
                data_item = display_item.data_item
                #logging.info(str(data_item))
                try:
                    components = list()
                    if self.options.get("prefix", False):
                        components.append(str(self.prefix_edit_widget.text))
                    # DMH 200610:  commented out the following block due to merge conflicts
                    ##dmh Have changed order of title string components
                    ## BUT how change sequence of display items
                    ##dmhlogging.info("Start: " + str(components))
                    ##dmhlogging.info(str(self.options))
                    #if self.options.get("date", False):
                    #    components.append(data_item.created_local.isoformat("_","auto").replace(':', ''))                    

                    if self.options.get("title", False):
                        title = unicodedata.normalize('NFKC', data_item.title)
                        title = re.sub('[^\w\s-]', '', title, flags=re.U).strip()
                        title = re.sub('[-\s]+', '-', title, flags=re.U)
                        components.append(title)
                    logging.info(str(data_item.get_metadata_value("stem.session.microscopist")))
                    if self.options.get("microscopist",False):
                        components.append(str(data_item.get_metadata_value("stem.session.microscopist")))
                    if self.options.get("dimensions", False):
                        components.append(
                            "x".join([str(shape_n) for shape_n in data_item.dimensional_shape]))                         
                    if self.options.get("sequence", False):
                        components.append(str(index))                           
                    filename = "_".join(components)
                    logging.info(str(filename))
                    extension = writer.extensions[0]
                    path = os.path.join(directory, "{0}.{1}".format(filename, extension))
                    # this actually saves the files ?
                    ImportExportManager.ImportExportManager().write_display_item_with_writer(self.ui, writer, display_item, path)
                except Exception as e:
                    logging.debug("Could not export image %s / %s", str(data_item), str(e))
                    traceback.print_exc()
                    traceback.print_stack()
