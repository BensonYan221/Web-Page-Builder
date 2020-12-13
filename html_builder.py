"""
Author: Benson Yan
Filename: html_builder.py
Description: CS 1 Project
"""
from input import *
from helper import *
import sys


def build_html(globals_var):
    """
    If the function detected that there are no parameters in the configuration (exclude the run file itself), then
    run wizard mode, else run website mode.
    :param globals_var: the dictionary which stored all the user input.
    :return: the html(s) created.
    """
    html_code = ""
    if len(sys.argv) <= 1:
        html_content = wizard_mode(globals_var['PARAGRAPHS'])
        html_content.title = globals_var["TITLE"]
        html_code += "<!DOCTYPE html> \n"
        html_code += "<html>\n"
        html_code += "<head> \n"
        html_code += "<title>"
        html_code += html_content.title
        html_code += "\n</title>\n"
        html_code = get_style(globals_var, html_code)
        html_code += "</head> \n<body>\n"
        html_code += "<h1>"
        html_code += html_content.title
        html_code += "\n</h1>\n"
        html_code += "<hr/>\n"
        for para in html_content.body:
            if para is not None:
                html_code = html_code + "\n<h2>" + para.title + "\n</h2>\n"
                html_code = html_code + "\n<p>" + str(para.content) + "\n</p>\n"
                if len(para.images) > 0:
                    for image in para.images:
                        html_code = html_code + "<img src= \"" + image.src + "\" width =\"" \
                                    + image.width + "\" class=\"center\">\n"
        html_code += "</body>\n</html>"
        with open("index.html", "w+") as f:
            f.write(html_code)
            print("Your web page has been saved as index.html.")
    else:
        html_lst = []
        html_content_lst = []
        for i in range(1, len(sys.argv)):
            html_content = HTML("", [])
            website_input_file = read_file(sys.argv[i])
            html_content.title = str(website_input_file[0])
            html_content = website_mode(html_content, website_input_file)
            html_content_lst.append(html_content)
            html_lst.append((sys.argv[i].replace('txt', 'html'), html_content.title))
        for i in range(len(html_lst)):
            html_code = ""
            html_content = html_content_lst[i]
            html_code += "<!DOCTYPE html> \n"
            html_code += "<html>\n"
            html_code += "<head> \n"
            html_code += "<title>"
            html_code += html_content.title
            html_code += "\n</title>\n"
            html_code = get_style(globals_var, html_code)
            html_code += "</head> \n<body>"
            html_code += "<h1>"
            html_code += html_content.title
            html_code += "\n</h1>\n"
            html_code += "<hr/>\n"
            html_code += "<p align= \"center\">"
            for h in html_lst:  # HyperLink
                if h is not None:
                    s = h[0]
                    t = h[1]
                    html_code += "<a href=\""
                    html_code += s
                    html_code += "\">"
                    html_code += t
                    html_code += "</a>---"
            html_code += "\n</p>"
            for para in html_content.body:
                if para is not None:
                    html_code = html_code + "\n<h2>" + para.title + "\n</h2>\n"
                    html_code = html_code + "\n<p>" + str(para.content) + "\n</p>\n"
                    if len(para.images) > 0:
                        for image in para.images:
                            html_code = html_code + "<img src= \"" + image.src + "\" width =\"" \
                                        + image.width + "\" class=\"center\">\n"
            html_code += "\n</body>\n</html>"

            with open(html_lst[i][0], "w+") as f:
                f.write(html_code)
                print("Your web page has been saved as " + html_lst[i][0])


def main():
    user_inputs = prompts_iter()
    build_html(user_inputs)


if __name__ == '__main__':
    main()
