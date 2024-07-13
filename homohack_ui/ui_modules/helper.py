# helper.py - 01:38 am - 2024-07-13

def set_theme(lib): # change colors if you want lol
    with lib.theme() as theme:
        with lib.theme_component() as theme_component:
            lib.add_theme_style(lib.mvStyleVar_WindowRounding, 2)
            lib.add_theme_style(lib.mvStyleVar_ChildRounding, 2)
            lib.add_theme_style(lib.mvStyleVar_FrameRounding, 1.5)
            lib.add_theme_style(lib.mvStyleVar_GrabRounding, 1)
        
            lib.add_theme_color(lib.mvThemeCol_WindowBg, (60, 50, 80), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_TitleBg, (70, 60, 100), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_TitleBgActive, (70, 60, 100), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_Border, (80, 70, 100), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_BorderShadow, (50, 40, 60), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_ScrollbarBg, (70, 60, 90), category=lib.mvThemeCat_Core)
            
            lib.add_theme_color(lib.mvThemeCol_Button, (70, 60, 100), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_ButtonHovered, (70, 60, 110), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_ButtonActive, (70, 60, 120), category=lib.mvThemeCat_Core)
            
            lib.add_theme_color(lib.mvThemeCol_Header, (90, 80, 120), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_HeaderHovered, (110, 100, 140), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_HeaderActive, (130, 120, 160), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_PopupBg, (80, 70, 110), category=lib.mvThemeCat_Core)
            
            lib.add_theme_color(lib.mvThemeCol_FrameBg, (80, 70, 110), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_FrameBgHovered, (100, 90, 130), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_FrameBgActive, (120, 110, 150), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_ChildBg, (70, 60, 100), category=lib.mvThemeCat_Core)
            
            lib.add_theme_color(lib.mvThemeCol_SliderGrab, (140, 120, 170), category=lib.mvThemeCat_Core)
            lib.add_theme_color(lib.mvThemeCol_SliderGrabActive, (160, 140, 190), category=lib.mvThemeCat_Core)
            
            lib.add_theme_color(lib.mvThemeCol_CheckMark, (140, 120, 170), category=lib.mvThemeCat_Core) 
    lib.bind_theme(theme)

def set_tab(lib, tab, tabs): # just changes the tab, nothing else lol
    for current_tab in tabs:
        if current_tab == tab:
            lib.show_item(current_tab)
        else:
            lib.hide_item(current_tab)