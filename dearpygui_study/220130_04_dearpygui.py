# ImportError: libGL.so.1: cannot open shared object file: No such file or directory
# apt-get install ffmpeg libsm6 libxext6  -y

from dearpygui.core  import *
from dearpygui.simple import *
import os
import pandas as pd

# it seems that I can't use dearpygui inside a container...
# there is not interactive window

# Glfw Error 65544: X11: The DISPLAY environment variable is missing
# Glfw Error 65537: The GLFW library is not initialized
# Glfw Error 65537: The GLFW library is not initialized
# Glfw Error 65537: The GLFW library is not initialized
# python3: /home/appveyor/projects/dearpygui/Dependencies/glfw/src/window.c:531: glfwSetWindowPos: Assertion `window != NULL' failed.
# Aborted (core dumped)

set_main_window_pos(0,0)
set_main_window_size(1300, 720)
set_global_font_scale(1.1)
add_additional_font("Inconsolata.otf")
# Dark, Light, Classic, Dark Grey, Cherry, Purple, Gold, Red
# set_theme("Gold")
set_theme("Dark")


def mostrar_logger(sender,data):
    show_logger()  

def mostrar_debug(sender,data):
    show_debug()


with window("janela principal"):
    with menu_bar("Barra de Menu"):
        with menu("Arquivo"):
            add_menu_item("Salvar")
            add_menu_item("Salvar Como")

        with menu("Configurações"):
            add_menu_item("Fonte")

        add_menu_item("Log",callback=mostrar_logger)
        add_menu_item("Ajuda")
        add_menu_item("Debug",callback=mostrar_debug)



def add_widgets(sender, data):

    with window("Secondary Window"): # simple
        add_button("New Button 2")
        add_button("New Button")
        add_button("New Button 3", parent="Secondary Window")

def delete_widgets(sender, data):
    delete_item("Secondary Window")
    delete_item("New Button")

def delete_children(sender, data):
    delete_item("Secondary Window", children_only=True)



with window("Tutorial"):
    add_button("Add Window and Items", callback=add_widgets)
    add_button("Delete Window and Children", callback=delete_widgets)
    add_button("Delete Window's Children", callback=delete_children)



















set_primary_window("janela principal",True)

start_dearpygui()