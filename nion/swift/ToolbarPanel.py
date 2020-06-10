# standard libraries
import gettext
import pkgutil
import weakref
###DMh 20191121
import operator
import logging
from nion.utils import Model
from nion.swift import Workspace

# third party libraries
# None


# local libraries
from nion.swift import Panel
from nion.ui import CanvasItem
from nion.utils import Geometry
###DMH trying to add own combobox with popupabouttobeshown
#from nion.ui import UserInterface
#from PyQt5 import QtCore

_ = gettext.gettext


   
#class MyComboBoxWidget(UserInterface.ComboBoxWidget):

    #popupAboutToBeShown = QtCore.pyqtSignal()

    #def showPopup(self):
    #    self.popupAboutToBeShown.emit()
    #    super(ComboBox, self).showPopup()

class ToolbarPanel(Panel.Panel):

    
    def __init__(self, document_controller, panel_id, properties):
        super(ToolbarPanel, self).__init__(document_controller, panel_id, _("Toolbar"))

        self.widget = self.ui.create_column_widget()

        toolbar_row_widget = self.ui.create_row_widget()

        # see https://www.iconfinder.com

        ui = document_controller.ui

        document_controller_weak_ref = weakref.ref(document_controller)

        icon_size = Geometry.IntSize(height=24, width=32)
        border_color = "#CCC"

        margins = Geometry.Margins(left=2, right=2, top=3, bottom=3)        

        tool_palette_grid_canvas_item = CanvasItem.CanvasItemComposition()
        tool_palette_grid_canvas_item.layout = CanvasItem.CanvasItemGridLayout(size=Geometry.IntSize(height=2, width=6), margins=margins)

        pointer_tool_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/pointer_icon.png")), border_color=border_color)
        pointer_tool_button.size = icon_size
        pointer_tool_button.tool_tip = _("Pointer tool for selecting graphics")

        hand_tool_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/hand_icon.png")), border_color=border_color)
        hand_tool_button.size = icon_size
        hand_tool_button.tool_tip = _("Hand tool for dragging images within panel")

        line_tool_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/line_icon.png")), border_color=border_color)
        line_tool_button.size = icon_size
        line_tool_button.tool_tip = _("Line tool for making line regions on images")

        rectangle_tool_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/rectangle_icon.png")), border_color=border_color)
        rectangle_tool_button.size = icon_size
        rectangle_tool_button.tool_tip = _("Rectangle tool for making rectangle regions on images")

        ellipse_tool_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/ellipse_icon.png")), border_color=border_color)
        ellipse_tool_button.size = icon_size
        ellipse_tool_button.tool_tip = _("Ellipse tool for making ellipse regions on images")

        point_tool_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/point_icon.png")), border_color=border_color)
        point_tool_button.size = icon_size
        point_tool_button.tool_tip = _("Point tool for making point regions on images")

        line_profile_tool_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/line_profile_icon.png")), border_color=border_color)
        line_profile_tool_button.size = icon_size
        line_profile_tool_button.tool_tip = _("Line profile tool for making line profiles on images")

        interval_tool_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/interval_icon.png")), border_color=border_color)
        interval_tool_button.size = icon_size
        interval_tool_button.tool_tip = _("Interval tool for making intervals on line plots")

        spot_tool_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/spot_icon.png")), border_color=border_color)
        spot_tool_button.size = icon_size
        spot_tool_button.tool_tip = _("Spot tool for creating spot masks")

        wedge_tool_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/wedge_icon.png")), border_color=border_color)
        wedge_tool_button.size = icon_size
        wedge_tool_button.tool_tip = _("Wedge tool for creating wedge masks")

        ring_tool_button = CanvasItem.BitmapButtonCanvasItem( CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/annular_ring.png")), border_color=border_color)
        ring_tool_button.size = icon_size
        ring_tool_button.tool_tip = _("Ring tool for creating ring masks")

        lattice_tool_button = CanvasItem.BitmapButtonCanvasItem( CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/lattice_icon.png")), border_color=border_color)
        lattice_tool_button.size = icon_size
        lattice_tool_button.tool_tip = _("Lattice tool for creating periodic lattice masks")

        tool_palette_grid_canvas_item.add_canvas_item(pointer_tool_button, Geometry.IntPoint(x=0, y=0))
        tool_palette_grid_canvas_item.add_canvas_item(hand_tool_button, Geometry.IntPoint(x=0, y=1))
        tool_palette_grid_canvas_item.add_canvas_item(line_tool_button, Geometry.IntPoint(x=1, y=0))
        tool_palette_grid_canvas_item.add_canvas_item(ellipse_tool_button, Geometry.IntPoint(x=1, y=1))
        tool_palette_grid_canvas_item.add_canvas_item(rectangle_tool_button, Geometry.IntPoint(x=2, y=0))
        tool_palette_grid_canvas_item.add_canvas_item(point_tool_button, Geometry.IntPoint(x=2, y=1))
        tool_palette_grid_canvas_item.add_canvas_item(line_profile_tool_button, Geometry.IntPoint(x=3, y=0))
        tool_palette_grid_canvas_item.add_canvas_item(interval_tool_button, Geometry.IntPoint(x=3, y=1))
        tool_palette_grid_canvas_item.add_canvas_item(spot_tool_button, Geometry.IntPoint(x=4, y=0))
        tool_palette_grid_canvas_item.add_canvas_item(wedge_tool_button, Geometry.IntPoint(x=4, y=1))
        tool_palette_grid_canvas_item.add_canvas_item(ring_tool_button, Geometry.IntPoint(x=5, y=0))
        tool_palette_grid_canvas_item.add_canvas_item(lattice_tool_button, Geometry.IntPoint(x=5, y=1))

        modes = "pointer", "hand", "line", "rectangle", "ellipse", "point", "line-profile", "interval", "spot", "wedge", "ring", "lattice"
        self.__tool_button_group = CanvasItem.RadioButtonGroup([pointer_tool_button, hand_tool_button, line_tool_button, rectangle_tool_button, ellipse_tool_button, point_tool_button, line_profile_tool_button, interval_tool_button, spot_tool_button, wedge_tool_button, ring_tool_button])
        def tool_mode_changed(tool_mode):
            self.__tool_button_group.current_index = modes.index(tool_mode)
        self.__tool_mode_changed_event_listener = document_controller.tool_mode_changed_event.listen(tool_mode_changed)
        self.__tool_button_group.current_index = modes.index(document_controller.tool_mode)
        self.__tool_button_group.on_current_index_changed = lambda index: setattr(document_controller_weak_ref(), "tool_mode", modes[index])
        tool_mode_changed(document_controller.tool_mode)

        new_group_button = self.ui.create_push_button_widget()
        new_group_button.tool_tip = _("New Group")
        new_group_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/new_group_icon.png"))
        new_group_button.on_clicked = lambda: document_controller_weak_ref().perform_action("project.add_group")

        delete_button = self.ui.create_push_button_widget()
        delete_button.tool_tip = _("Delete")
        delete_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/delete_icon.png"))
        delete_button.on_clicked = lambda: document_controller_weak_ref().perform_action("window.delete")

        export_button = self.ui.create_push_button_widget()
        export_button.tool_tip = _("Export")
        export_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/export_icon.png"))
        export_button.on_clicked = lambda: document_controller_weak_ref().perform_action("file.export")

        view_palette_grid_canvas_item = CanvasItem.CanvasItemComposition()
        view_palette_grid_canvas_item.layout = CanvasItem.CanvasItemGridLayout(size=Geometry.IntSize(height=2, width=2), margins=margins)

        fit_view_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/fit_icon.png")), border_color=border_color)
        fit_view_button.size = icon_size
        fit_view_button.on_button_clicked = lambda: document_controller_weak_ref()._fit_view_action.trigger()
        fit_view_button.tool_tip = _("Zoom to fit to enclosing space")

        fill_view_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/fill_icon.png")), border_color=border_color)
        fill_view_button.size = icon_size
        fill_view_button.on_button_clicked = lambda: document_controller_weak_ref()._fill_view_action.trigger()
        fill_view_button.tool_tip = _("Zoom to fill enclosing space")

        one_to_one_view_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/1x1_icon.png")), border_color=border_color)
        one_to_one_view_button.size = icon_size
        one_to_one_view_button.on_button_clicked = lambda: document_controller_weak_ref()._one_to_one_view_action.trigger()
        one_to_one_view_button.tool_tip = _("Zoom to one image pixel per screen pixel")

        two_to_one_view_button = CanvasItem.BitmapButtonCanvasItem(CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/2x1_icon.png")), border_color=border_color)
        two_to_one_view_button.size = icon_size
        two_to_one_view_button.on_button_clicked = lambda: document_controller_weak_ref()._two_to_one_view_action.trigger()
        two_to_one_view_button.tool_tip = _("Zoom to two image pixels per screen pixel")

        view_palette_grid_canvas_item.add_canvas_item(fit_view_button, Geometry.IntPoint(x=0, y=0))
        view_palette_grid_canvas_item.add_canvas_item(fill_view_button, Geometry.IntPoint(x=0, y=1))
        view_palette_grid_canvas_item.add_canvas_item(one_to_one_view_button, Geometry.IntPoint(x=1, y=0))
        view_palette_grid_canvas_item.add_canvas_item(two_to_one_view_button, Geometry.IntPoint(x=1, y=1))

        toggle_filter_button = self.ui.create_push_button_widget()
        toggle_filter_button.tool_tip = _("Toggle Filter Panel")
        toggle_filter_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/filter_icon.png"))        
        toggle_filter_button.on_clicked = lambda: document_controller_weak_ref()._toggle_filter_action.trigger()
        
        tool_palette_widget = ui.create_canvas_widget(properties={"height": 54, "width": 164})
        tool_palette_widget.canvas_item.add_canvas_item(tool_palette_grid_canvas_item)

        tool_group_widget = self.ui.create_row_widget()
        tool_group_widget.add(tool_palette_widget)

        commands_group_widget = self.ui.create_row_widget()
        commands_group_widget.add(new_group_button)
        commands_group_widget.add(delete_button)
        commands_group_widget.add(export_button)

        view_palette_widget = ui.create_canvas_widget(properties={"height": 54, "width": 68})
        view_palette_widget.canvas_item.add_canvas_item(view_palette_grid_canvas_item)

        view_group_widget = self.ui.create_row_widget()
        view_group_widget.add(view_palette_widget)

        filter_group_widget = self.ui.create_row_widget()
        filter_group_widget.add(toggle_filter_button)
        
        ### DMH Workspace buttons and combobox section
        
        ## DMH 20191115: defines workspace related buttons and actions
        def workspace_button_action(number_panels):
            """ selects the corresponding action depending on which workspace button was clicked
                and then updates the workspace items in the workspace combobox
            """
            if number_panels == 1:
                document_controller_weak_ref()._1panel_workspace_action.trigger()
                self.update_workspace_list_combobox()  
            elif number_panels == 2:
                document_controller_weak_ref()._2panel_workspace_action.trigger()
                self.update_workspace_list_combobox()  
            elif number_panels == 4:
                document_controller_weak_ref()._4panel_workspace_action.trigger()
                self.update_workspace_list_combobox()  
            elif number_panels == 9:
                document_controller_weak_ref()._9panel_workspace_action.trigger()
                self.update_workspace_list_combobox()  
            elif number_panels == 16:
                document_controller_weak_ref()._16panel_workspace_action.trigger()
                self.update_workspace_list_combobox()  
            elif number_panels == 20:
                document_controller_weak_ref()._20panel_workspace_action.trigger()  
                self.update_workspace_list_combobox()  
            elif number_panels == 0:
                self.update_workspace_list_combobox()
            elif number_panels == 999:
                document_controller_weak_ref()._deletepanel_workspace_action.trigger()
                #self.update_workspace_list_combobox("delete")
            #_update_workspace_list_combobox("new")           
            #self.update_workspace_list_combobox("new")           
            logging.info("workspace_button_action clicked")    

        # define buttons that create new workspaces:
        workspace_update_button = self.ui.create_push_button_widget()
        workspace_update_button.tool_tip = _("Refresh list of available workspaces")
        workspace_update_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/update.png"))
        workspace_update_button.on_clicked = lambda: workspace_button_action(0)
        workspace_delete_button = self.ui.create_push_button_widget()
        workspace_delete_button.tool_tip = _("Delete current workspace")
        workspace_delete_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/deletepanel.png"))
        workspace_delete_button.on_clicked = lambda: workspace_button_action(999)        
        workspace_1_button = self.ui.create_push_button_widget()
        workspace_1_button.tool_tip = _("Open new 1 panel workspace")
        workspace_1_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/1panel.png"))
        workspace_1_button.on_clicked = lambda: workspace_button_action(1)
        workspace_2_button = self.ui.create_push_button_widget()
        workspace_2_button.tool_tip = _("Open new 2 panel workspace")
        workspace_2_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/2panel.png"))
        workspace_2_button.on_clicked = lambda: workspace_button_action(2)
        workspace_4_button = self.ui.create_push_button_widget()
        workspace_4_button.tool_tip = _("Open new 4 panel workspace")
        workspace_4_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/4panel.png"))
        workspace_4_button.on_clicked = lambda: workspace_button_action(4)
        workspace_9_button = self.ui.create_push_button_widget()
        workspace_9_button.tool_tip = _("Open new 9 panel workspace")
        workspace_9_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/9panel.png"))
        workspace_9_button.on_clicked = lambda: workspace_button_action(9)
        workspace_16_button = self.ui.create_push_button_widget()
        workspace_16_button.tool_tip = _("Open new 16 panel workspace")
        workspace_16_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/16panel.png"))
        workspace_16_button.on_clicked = lambda: workspace_button_action(16)
        workspace_20_button = self.ui.create_push_button_widget()
        workspace_20_button.tool_tip = _("Open new 20 panel workspace")
        workspace_20_button.icon = CanvasItem.load_rgba_data_from_bytes(pkgutil.get_data(__name__, "resources/20panel.png"))
        workspace_20_button.on_clicked = lambda: workspace_button_action(20)      
        
        ## DMH: workspace list combobox
        def _get_workspace_list():
            """ creates a list of currently available workspaces [(workspace name, workspace uuid)] """
            workspace_list_items = []
            for workspace in document_controller.document_model.workspaces:
                logging.info("get_workspace_list called, workspaces: " + str(workspace.name) + " " + str(workspace.uuid))
                workspace_list_items.append((str(workspace.name), str(workspace.uuid)))    
            return workspace_list_items           

        def _update_workspace_list_combobox(change_type):
            """ updates workspace_list_items in combobox and changes to relevant workspace
                depending on whether a workspace was created, deleted, renamed, selected by some external function
            """
            # save current selected workspace list item
            old_workspace_index = self.workspace_list_combobox.current_index
            # get current workspace_list
            workspace_list = _get_workspace_list()
            # get current indexed workspace list
            workspace_list_indexed = {item[1]: index for index, item in enumerate(workspace_list)}  
            # re-set items in combobox
            self.workspace_list_combobox.items = workspace_list
            # change to new workspace
            if change_type == "new":
                # change to newly created workspace (a new workspace is added to the end)
                _change_workspace(workspace_list[-1])                
            elif change_type == "delete":
                # change to workspace to prior item in the list (this is sure to exist)
                _change_workspace(workspace_list[old_workspace_index - 1])
            # set current_index to the item (equals to item with workspace_uuid)
            self.workspace_list_combobox.current_index = workspace_list_indexed[str(document_controller.document_model.workspace_uuid)]

            logging.info("_update_workspace_list_combobox, current_index: " + str(self.workspace_list_combobox.current_index))
            logging.info("_update_workspace_list_combobox, items: " + str(self.workspace_list_combobox.items))
            logging.info("_update_workspace_list_combobox, indexed: " + str(workspace_list_indexed))
        
        def _change_workspace(selected_item):                                 # (workspace.name, workspace.uuid)     
            """ changes workspace to selected workspace in combobox (= workspace_list_item)"""        
            logging.info("changed_workspace called, workspace: " + str(selected_item))           
            # Iterate over available workspaces and pick the one that corresponding workspace.name equals workspace_list_item.
            # Then change workspace to this one.
            for workspace in document_controller.document_model.workspaces:
                #logging.info("workspace_changed workspace.uuid: " + str(workspace.uuid) + " workspace_list_item: " + str(workspace_list_item[1]))
                # workspace uuid is 2nd element of item
                if str(workspace.uuid) == str(selected_item[1]):                    
                    #change workspace
                    document_controller.workspace_controller.change_workspace(workspace)
                   
        # create a dictionary with key : index pairs (workspace object: index)
        #workspace_list_indexed = {item[1]: index for index, item in enumerate(self.get_workspace_list())}   
        workspace_list_indexed = {item[1]: index for index, item in enumerate(ToolbarPanel.static_get_workspace_list(document_controller))} 
        logging.info("workspace_list_indexed: " + str(workspace_list_indexed))        
        # create drop down list (combobox) with workspace_list_items
        self.workspace_list_combobox = self.ui.create_combo_box_widget(items=self.get_workspace_list(), item_getter=operator.itemgetter(0))
        self.workspace_list_combobox.tool_tip = _("Select Workspace")
        logging.info("combobox created object: " + str(self.workspace_list_combobox))
        # set the current selected workspace in drop down list as current index
        self.workspace_list_combobox.current_index = workspace_list_indexed[str(document_controller.document_model.workspace_uuid)]        
        logging.info("current_index: " + str(self.workspace_list_combobox.current_index))                
        # change workspace when drop down selection changes:
        #workspace_list_combobox.on_current_item_changed = _change_workspace 
        self.workspace_list_combobox.on_current_item_changed = self.change_workspace     
        logging.info("workspace_list_combobox.items " + str( self.workspace_list_combobox.items))     

        ## DMH 20191115: create workspace list and group widgets
        workspace_list_widget = self.ui.create_row_widget()
        workspace_list_widget.add(ui.create_label_widget(_("Workspace:"), properties={"width": 85}))     
        workspace_list_widget.add(self.workspace_list_combobox)
        logging.info("workspace_list_widget row_widget created ----------- object: " + str(workspace_list_widget))    
        workspace_list_widget.add(workspace_update_button)
        workspace_list_widget.add(workspace_delete_button)
        workspace_group_widget = self.ui.create_row_widget()
        workspace_group_widget.add(workspace_1_button)
        workspace_group_widget.add(workspace_2_button)
        workspace_group_widget.add(workspace_4_button)
        workspace_group_widget.add(workspace_9_button)
        workspace_group_widget.add(workspace_16_button)
        workspace_group_widget.add(workspace_20_button)

        ### end DMH workspace section       
        
        toolbar_row_widget.add_spacing(12)
        toolbar_row_widget.add(tool_group_widget)
        toolbar_row_widget.add_spacing(12)
        toolbar_row_widget.add(commands_group_widget)
        toolbar_row_widget.add_spacing(12)
        toolbar_row_widget.add(view_group_widget)
        toolbar_row_widget.add_spacing(12)
        toolbar_row_widget.add(filter_group_widget)
        toolbar_row_widget.add_spacing(12)
        ### DMH 20191115: adds the workspace list and group widgets to the toolbar
        toolbar_row_widget.add(workspace_list_widget)
        toolbar_row_widget.add_spacing(12)        
        toolbar_row_widget.add(workspace_group_widget)
        toolbar_row_widget.add_spacing(12)
        ### end DMH
        toolbar_row_widget.add_stretch()

        self.widget.add(toolbar_row_widget)


            
    # these are instance methods:
    #works
    def get_workspace_list(self):
        """ creates a list of currently available workspaces [(workspace name, workspace uuid)] """
        workspace_manager = Workspace.WorkspaceManager()
        logging.info("panelids " + str(workspace_manager.panel_ids))
        workspace_list_items = []
        for workspace in self.document_controller.document_model.workspaces:
            logging.info("get_workspace_list called, workspaces: " + str(workspace.name) + " " + str(workspace.uuid))
            workspace_list_items.append((str(workspace.name), str(workspace.uuid)))    
        return workspace_list_items        

    
    #works                
    def change_workspace(self, selected_item):                                 # (workspace.name, workspace.uuid)     
        """ changes workspace to selected workspace in combobox (= selected_item)"""        
        logging.info("changed_workspace called, workspace: " + str(selected_item))     
        # DC.DM.workspaces is a list with the workspace objects
        logging.info("DC.DM.workspaces: " + str(self.document_controller.document_model.workspaces))
        # Iterate over available workspaces and pick the one that corresponding workspace.name equals workspace_list_item.
        # Then change workspace to this one.
        for workspace in self.document_controller.document_model.workspaces:
            #logging.info("workspace_changed workspace.uuid: " + str(workspace.uuid) + " workspace_list_item: " + str(selected_item[1]))
            # workspace uuid is 2nd element of item
            if str(workspace.uuid) == str(selected_item[1]):                    
                #change workspace
                self.document_controller.workspace_controller.change_workspace(workspace)
                    
    #works when workspace_list_combobox defined as attribute                
    def update_workspace_list_combobox(self):
        """ updates workspace_list_items in combobox and changes to relevant workspace
            depending on whether a workspace was created, deleted, renamed, selected by some external function
        """
        # save current selected workspace list item
        old_workspace_index = self.workspace_list_combobox.current_index  
        old_workspace_list = self.workspace_list_combobox.items
    
        # get new workspace_list
        workspace_list = self.get_workspace_list()
        # get new indexed workspace list
        workspace_list_indexed = {item[1]: index for index, item in enumerate(workspace_list)}  
        # re-set items in combobox to new workspace list
        self.workspace_list_combobox.items = workspace_list
        logging.info("update_workspace_list_combobox oldidx: " + str(old_workspace_index) + " oldlen: " + str(len(old_workspace_list)) + " newlen " + str(len(workspace_list)))

        # change to new workspace
        if len(old_workspace_list) < len(workspace_list):
        #if change_type == "new":
            # a new workspace is added to the end
            self.change_workspace(workspace_list[-1])
        elif len(old_workspace_list) > len(workspace_list):
        #change_type == "delete":
            # change to workspace to item in the list (this is sure to exist)
            logging.info("update workspace list oldlen > newlen")
            self.change_workspace(workspace_list[old_workspace_index - 1])
        else:
            # renamed workspace: don't have to changed current index
            pass            
        # set current_index to the item (equals to item with workspace_uuid)
        self.workspace_list_combobox.current_index = workspace_list_indexed[str(self.document_controller.document_model.workspace_uuid)]

        logging.info("update_workspace_list_combobox, current_index: " + str(self.workspace_list_combobox.current_index))
        logging.info("update_workspace_list_combobox, items: " + str(self.workspace_list_combobox.items))
        logging.info("update_workspace_list_combobox, indexed: " + str(workspace_list_indexed))
            



    def static_get_workspace_list(document_controller):
        """ creates a list of currently available workspaces [(workspace name, workspace uuid)] """
        workspace_manager = Workspace.WorkspaceManager()
        logging.info("panelids " + str(workspace_manager.panel_ids))
        workspace_list_items = []
        for workspace in document_controller.document_model.workspaces:
            logging.info("static_get_workspace_list called, workspaces: " + str(workspace.name) + " " + str(workspace.uuid))
            workspace_list_items.append((str(workspace.name), str(workspace.uuid)))    
        return workspace_list_items       

    def close(self):
        self.__tool_mode_changed_event_listener.close()
        self.__tool_mode_changed_event_listener = None
        super().close()
