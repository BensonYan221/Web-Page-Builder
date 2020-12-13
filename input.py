"""
Author: Benson
"""
from html_builder import *
from helper import *


def prompts_iter():
    """
    Prompts for user input and store all of them in a dictionary.
    :return: Dictionary stores all the user inputs.
    """
    globals_var = dict()

    globals_var['color_set'] = set_color_options(file="color.txt")

    if len(sys.argv) <= 1:

        globals_var['TITLE'] = input("What is the title of your website? ")

        print("Background Color")
        globals_var['BACKCOLOR'] = proceed_color(globals_var['color_set'])

        print("You will now choose a font.")
        globals_var['FONTSTYLE'] = font_display()

        print("Paragrapgh Text Color")
        globals_var['FONTCOLOR'] = proceed_color(globals_var['color_set'])

        print("Heading Color")
        globals_var['HEADCOLOR'] = proceed_color(globals_var['color_set'])

        globals_var["PARAGRAPHS"] = input_body()

    else:
        print("Background Color")
        globals_var['BACKCOLOR'] = proceed_color(globals_var['color_set'])

        print("You will now choose a font.")
        globals_var['FONTSTYLE'] = font_display()

        print("Paragrapgh Text Color")
        globals_var['FONTCOLOR'] = proceed_color(globals_var['color_set'])

        print("Heading Color")
        globals_var['HEADCOLOR'] = proceed_color(globals_var['color_set'])

    return globals_var


# globals_var = prompts_iter()
# build_html(globals_var)
