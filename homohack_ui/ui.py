# sorry for the dogshit code, didn't put much effort into this
# dearpygui frameless window > https://www.unknowncheats.me/forum/valorant/600025-dearpygui-frameless-window.html
# ui im using for a cs2 pycheat

# libraries

import dearpygui.dearpygui as ui
import threading
import os

# modules

import ui_modules.helper as ui_helper
import ui_modules.math as math

# classes

class ui_settings: # all the sections / child windows will scale with the window size
    size = (500, 250) # x,y
    ui_dragging = False
    tabs = [ # give these actual names for better readability (dont forget to modify the button names aswell)
        "tab_1",
        "tab_2",
        "tab_3",
        "settings_tab",
    ]

class scaling:
    # sections offsets nd shit here incase you wanna change
    section_width = ui_settings.size[0] - 20
    section_height = ui_settings.size[1] - 75

    button_size = (80, 30) # x,y
    spacing_offset = 10
 
ui.create_context()
 
viewport = ui.create_viewport(title="window_title", width=ui_settings.size[0], height=ui_settings.size[1], decorated=False, resizable=False)
 
ui.setup_dearpygui()

with ui.window(label="window_title", width=ui_settings.size[0], height=ui_settings.size[1], no_collapse=True, no_move=True, no_resize=True, on_close=lambda: os._exit(0)) as win:
    
    current_spacing_offset = scaling.spacing_offset
    ui_helper.set_theme(ui)
    
    # automation would help me a lot but im sitting here at 01:45 am manually adding the spacing offset cuz icba :)
    ui.add_button(label="tab 1", width=scaling.button_size[0], height=scaling.button_size[1], pos=(current_spacing_offset, 28), callback=lambda: ui_helper.set_tab(ui, "tab_1", ui_settings.tabs))

    current_spacing_offset += scaling.button_size[0] + scaling.spacing_offset

    ui.add_button(label="tab 2", width=scaling.button_size[0], height=scaling.button_size[1], pos=(current_spacing_offset, 28), callback=lambda: ui_helper.set_tab(ui, "tab_2", ui_settings.tabs))

    current_spacing_offset += scaling.button_size[0] + scaling.spacing_offset

    ui.add_button(label="tab 3", width=scaling.button_size[0], height=scaling.button_size[1], pos=(current_spacing_offset, 28), callback=lambda: ui_helper.set_tab(ui, "tab_3", ui_settings.tabs))

    current_spacing_offset += scaling.button_size[0] + scaling.spacing_offset

    ui.add_button(label="settings", width=scaling.button_size[0], height=scaling.button_size[1], pos=(current_spacing_offset, 28), callback=lambda: ui_helper.set_tab(ui, "settings_tab", ui_settings.tabs))

    
    with ui.child_window(label="tab_1", tag="tab_1", width=scaling.section_width, height=scaling.section_height, pos=(10, 63), show=True) as aimbot_tab:
        
        ui.add_text("hello this is tab 1")
        
    with ui.child_window(label="tab_2", tag="tab_2", width=scaling.section_width, height=scaling.section_height, pos=(10, 63), show=False) as visuals_tab:
        
        ui.add_text("hello this is tab 2")
    
    with ui.child_window(label="tab_3", tag="tab_3", width=scaling.section_width, height=scaling.section_height, pos=(10, 63), show=False) as color_tab:
        
        ui.add_text("hello this is tab 3")
        
    with ui.child_window(label="settings_tab", tag="settings_tab", width=scaling.section_width, height=scaling.section_height, pos=(10, 63), show=False) as settings_tab:

        ui.add_text("hello this is the settings tab")
        ui.add_slider_float(label="drag speed", tag="drag_speed", width=60, default_value=0.1, min_value=0.01, max_value=1)
    
def is_dragging(_, data): # minimal changes here, all i did was uh make it possible to drag however fast you want, not sure y clarifey didnt do this
    if ui.is_mouse_button_down(0):
        y = data[1]
        if -2 <= y <= 19:
            ui_settings.ui_dragging = True
    else:
        ui_settings.ui_dragging = False

def drag_logic(_, data):
    if ui_settings.ui_dragging:
        pos = ui.get_viewport_pos()
        x = data[1]
        y = data[2]
        
        current_spacing_offset = pos[0]
        current_y = pos[1]
        
        speed = float(ui.get_value("drag_speed")) # customizable drag speed (uses lerping for smooth drag, idk looks nicer)
        interpolated_x = math.lerp(current_spacing_offset, pos[0] + x, speed)
        interpolated_y = math.lerp(current_y, pos[1] + y, speed)
        
        ui.configure_viewport(viewport, x_pos=interpolated_x, y_pos=interpolated_y)

with ui.handler_registry():
    ui.add_mouse_drag_handler(0, callback=drag_logic)
    ui.add_mouse_move_handler(callback=is_dragging)
 
ui.show_viewport()
ui.start_dearpygui()
ui.destroy_context()