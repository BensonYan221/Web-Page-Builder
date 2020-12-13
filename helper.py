"""
Author: Benson
"""
import turtle as t
from dataclass_help import *


def read_file(file):  # general reading file each line and return in a list.
    """
    Reads file line by line and store lines into a list.
    :param file: filename given
    :return: List with all the lines in the file.
    """
    data = []
    with open(file) as f:
        for line in f:
            data.append(line.strip())
    return data


def set_color_options(file):
    """
    Opens the file and store all the information into a sets
    :param file: filename given.
    :return: A set that are ready to do the valid check on color.
    """
    color_set = set()
    for line in read_file(file):
        line = line.split()
        color_set.add(line[0].lower())
        # .lower() is a built in python function to convert the strings from input to all lowercase.
        color_set.add(line[1].lower())
    return color_set


def color_error_check(variable, color_set):
    """
    Helper function which helps to do the valid check on color.
    :param variable: the color input from the user
    :param color_set: the set created.
    :return: Boolean
    """
    if variable in color_set:
        return True
    else:
        return False


def proceed_color(color_set):
    """
    Keep prompting user for the valid format for the color code.
    :param color_set: the set created.
    :return: the valid checked color.
    """
    while True:
        color = input("Choose the name of the color, or in format \"#XXXXXX\" : ").strip().lower()
        if color_error_check(color, color_set) is True:
            break
        print("Illegal format")
    return color


def font_display():
    """
    If user input is "yes" then displays the font examples with turtle. After the display tab is closed, proceed to else
    Else print the options in the command line and prompt for the options.
    :return: the font options that user choose.
    """
    fonts = ["Arial", "Comic Sans MS", "Lucida Grande", "Tahoma", "Verdana", "Helvetica", "Times New Roman"]
    font_bool = input("Do you want to see what the fonts look like? [yes]").lower().strip()
    print("Close the window when you have made your choice.")
    print('Choose a font by its number.')
    if font_bool == "yes":
        t.up()
        t.goto(-50, 50)
        t.setup(200, 200)
        t.ht()
        # hide the turtle
        for i in range(len(fonts)):
            t.down()
            t.tracer(0, 0)
            t.write(fonts[i], font=(fonts[i], 14, "normal"))
            t.up()
            t.right(90)
            t.forward(20)
            t.left(90)
            t.down()
            print(i, ":", fonts[i], "size 14")
        t.done()

    else:
        for i in range(len(fonts)):
            print(i, ":", fonts[i], "size 14")
    while True:
        try:
            font_selected = int(input(">>"))
        except ValueError:
            print("Please enter number from 0-6")
            continue
        if font_selected > 6 or font_selected < 0:
            print("Index out of range: Please select numbers from 0 - 6 only.")
        else:
            break
    font_option = fonts[font_selected]
    return font_option


def import_images():
    """
    helper functions for input_body(), prompts user for importing images and store them in a list. If "yes",
    prompt the user for the image filename. After the first "yes", goes into a while loop prompting user
    if the user wants to add another images until the input is not "yes".
    :return: A list of images from the user input.
    """
    images = []
    images_bool = input("Do you want to add images? [yes]").lower().strip()
    if images_bool == "yes":
        images_filename = input("Image file name: ")
        images.append(Image(images_filename, "60%"))
        while input("Do you want to add another image? [yes]").lower().strip() == "yes":
            images_filename = input("Image file name: ")
            images.append(Image(images_filename, "60%"))
    return images


def input_body():
    """
    Use the data structure from helper file, Paragraph store "title", "content", List"images".
    paragraphs is the list that store Paragrapgh set by set. This function also prompts user for the title and the content
    of the paragrapgh until the input from the prompt whether they want to add another paragrapgh is not "yes".
    :return: A list of Paragragh
    """
    paragraphs = []

    while True:
        paragraph = Paragraph('', '', [])

        print("Title of your paragraph: ")
        paragraph.title = input()

        print("Content of your paragrapgh (single line) ")
        paragraph.content = input()

        paragraph.images = import_images()

        paragraphs.append(paragraph)
        if input("Do you want to add another paragraph to your website? [yes]").lower().strip() != "yes":
            break
    return paragraphs


def get_style(globals_var, html_code):
    """
    String manipulation from the style_template.txt. This function simple replace the command inside <style> from
    the html like @BACKCOLOR with the user input variable of BACKCOLOR.
    :param globals_var: the dictionary of the user input.
    :param html_code: the code that writes the html file.
    :return: html_code
    """
    data = read_file("style_template.txt")
    for line in data:
        line = line.split()
        for i in range(len(line)):
            if line[i][0] == "@":
                line[i] = globals_var[line[i][1:len(line[i]) - 1]] + line[i][-1]
            html_code += line[i] + ' '
        html_code += '\n'
    return html_code


def create_image(web_image):
    """
    Give a default size(30%) of the image input.
    :param web_image: the image input.
    :return: the image input with the default size.
    """
    if len(web_image) == 3:
        return Image(str(web_image[1]), str(web_image[2]))
    else:
        return Image(str(web_image[1]), "100%")


def create_par(web_par):
    """
    This uses in the website mode. This function loops over the line to find key words and does coordinate job.
    :param web_par: the line in paragraph input for website mode.
    :return: Paragrapgh
    """
    new_paragraph = Paragraph('', '', [])
    new_paragraph.title = ' '.join(web_par[0].split(' ')[1:])
    for i in range(1, len(web_par)):
        if web_par[i] == '':
            continue
        if web_par[i] == "!new_paragraph":
            return new_paragraph
        elif web_par[i].split()[0] == "!image":
            new_paragraph.images.append(create_image(web_par[i].split()))
        else:
            new_paragraph.content += web_par[i]
    return new_paragraph


def website_mode(html_content, website_content):
    """
    Store everything into the HTML.body when the line reaches to "!new_paragraph" every time.
    :param html_content: the HTML data structure which has "title" and List"body".
    :param website_content: the list of all lines from the given filename.
    :return: HTML
    """
    for i in range(len(website_content)):
        if website_content[i] == "!new_paragraph":
            html_content.body.append(create_par(website_content[i + 1:]))
    return html_content


def wizard_mode(paragraphs):
    """
    Store the user inputs on the title, content, images in the Paragraph into the data structure HTML.
    :param paragraphs: all title, content and List[Images]
    :return: the HTML data structure for implementing the <body> in html
    """
    wiz_par = HTML("", [])
    for i in range(len(paragraphs)):
        wiz_par.body.append(paragraphs[i])
    return wiz_par
