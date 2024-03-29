# Author: Jesús Daza
# Nick: jedahee
# Email: jdaza.her@gmail.com
# Details: Script that contain the functionallity (Function class)
# Description: This script can create the structure folder or templates for projects 
#              with technologies like Bootstrap 5, Tailwind, 
#              HTML / CSS / JS, JQuery (Normal version, Mobile version, UI version)

# IMPORT
# ------

# External
# --------
import sys
import os
import platform
import webbrowser

class Function():

    # Constructor
    def __init__(self, folder_name, file_name, path):

        # Attributes
        # ----------
        self.folder_name = "new_folder"
        self.file_name = "new_file"
        
        if platform.system() == "Linux":
            self.path = "/home"
        elif platform.system() == "Windows":
            self.path = "C:/"


        self.options = {
            1: "Select project", 
            2: "Set folder name and file name",
            3: "Create template", 
            0: "Exit"
        }
        
        self.projects = {
            "Bootstrap": {
                "(last) version_0": "5.1.3",
            },
            "Tailwind": {},
            "HTML": {
                "preprocessor_0": "CSS",
                "preprocessor_1": "SCSS",
                "preprocessor_2": "Less",
            },
            "JQuery": {
                "version_0": "Normal",
                "version_1": "Mobile",
                "version_2": "UI",
            },

        }

    # Method: Create a folder in the path specified
    def create_folder(self):
        try:
            os.mkdir(self.path + "/" + self.folder_name)
            return True;
        except (PermissionError):
            print("\n ERROR: Permission denied, can not create project in this path > " + self.path + " \n") 
            return False;

    # Method: Create the template of the selected project
    def create_template(self, project, version):
        if (self.create_folder() == True):
            if project == "Bootstrap":
                self.create_html_bootstrap(version)
                self.create_css()
                self.create_js()
            elif project == "Tailwind":
                self.create_html_tailwind()
                self.create_css()
                self.create_js()
            elif project == "HTML":
                self.create_html()
                
                if version == "CSS":
                    self.create_css()
                elif version == "SCSS":
                    self.create_scss()
                elif version == "Less":
                    self.create_less()
                
                self.create_js()
            
            elif project == "JQuery":
                self.create_html_jquery(version)
            
            print(">> *** Project created successfully *** <<")

    # Method: Create the HTML file of the selected project
    def create_html(self):
        content = ''' 
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="''' + self.file_name + '''.css">
    <title>Document</title>
</head>
<body>
    <!-- Auto-generated with autoTemplate -->        
    <script src="''' + self.file_name + '''.js"></script>
</body>
</html>
        '''
        
        file = open(self.path + "/" + self.folder_name + "/" + self.file_name + ".html", "w+")
        file.write(content)
        file.close()

    # Method: Create the HTML template with the BOOTSTRAP link
    def create_html_bootstrap(self, version):
        content = ''' 
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="''' + self.file_name + '''.css">
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@'''+version+'''/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Document</title>
</head>
<body>
    <!-- Auto-generated with autoTemplate -->
    <p class="display-1">Auto-generated with autoTemplate</p>        
    <script src="''' + self.file_name + '''.js"></script>
</body>
</html>
        '''
        file = open(self.path + "/" + self.folder_name + "/" + self.file_name + ".html", "w+")
        file.write(content)
        file.close()

    # Method: Create the HTML template with the JQUERY link
    def create_html_jquery(self, version):
        link_jquery_normal = '<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>'
        link_jquery_ui = '<script src="https://code.jquery.com/ui/1.13.1/jquery-ui.min.js" integrity="sha256-eTyxS0rkjpLEo16uXTS0uVCS4815lc40K2iVpWDvdSY=" crossorigin="anonymous"></script>'
        link_jquery_mobile = '<script src="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js" integrity="sha256-Lsk+CDPOzTapLoAzWW0G/WeQeViS3FMzywpzPZV8SXk=" crossorigin="anonymous"></script>'
        
        if (version == "Normal"):
            link_selected = link_jquery_normal
        elif (version == "Mobile"):
            link_selected = link_jquery_mobile
        elif (version == "UI"):
            link_selected = link_jquery_ui

        content = ''' 
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="''' + self.file_name + '''.css">
    <title>Document</title>
</head>
<body>
    <!-- Auto-generated with autoTemplate -->        
    <script src="''' + self.file_name + '''.js"></script>

    <!-- JQuery Link -->

    ''' + link_selected + '''
    
</body>
</html>
        '''
        file = open(self.path + "/" + self.folder_name + "/" + self.file_name + ".html", "w+")
        file.write(content)
        file.close()

    # Method: Create the HTML template with the TAILWIND link
    def create_html_tailwind(self):
        content = ''' 
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="''' + self.file_name + '''.css">
    <script src="https://cdn.tailwindcss.com"></script>

    <title>Document</title>
</head>
<body>
    <!-- Auto-generated with autoTemplate -->
    <h1 class="text-3xl font-bold underline">
        Auto-generated with autoTemplate
    </h1>        
    <script src="''' + self.file_name + '''.js"></script>
</body>
</html>
        '''
        file = open(self.path + "/" + self.folder_name + "/" + self.file_name + ".html", "w+")
        file.write(content)
        file.close()

    # Method: Create the CSS file of the selected project
    def create_css(self):
        content = ''' 
/* Auto-generated with autoTemplate */

/* RESET */
*, button, input, textarea, select {
    box-sizing: border-box;
    outline: none;
    border: none;
    list-style: none;
    text-decoration: none;
    text-emphasis: none;
}
        '''
        file = open(self.path + "/" + self.folder_name + "/" + self.file_name + ".css",  "w+")
        file.write(content)
        file.close()

    # Method: Create the JS file of the selected project
    def create_js(self):
        content = ''' 
// Auto-generated with autoTemplate

window.onload = function(e) {
    console.log('Auto-generated with autoTemplate')
}
        '''
        file = open(self.path + "/" + self.folder_name + "/" + self.file_name + ".js", "w+")
        file.write(content)
        file.close()

    # Method: Create the SCSS file of the selected project
    def create_scss(self):
        content = ''' 
/* Auto-generated with autoTemplate */

/* RESET */
*, button, input, textarea, select {
    box-sizing: border-box;
    outline: none;
    border: none;
    list-style: none;
    text-decoration: none;
    text-emphasis: none;
}
        '''
        file = open(self.path + "/" + self.folder_name + "/" + self.file_name + ".scss", "w+")
        file.write(content)
        file.close()

    # Method: Create the LESS file of the selected project
    def create_less(self):
        content = ''' 
/* Auto-generated with autoTemplate */

/* RESET */
*, button, input, textarea, select {
    box-sizing: border-box;
    outline: none;
    border: none;
    list-style: none;
    text-decoration: none;
    text-emphasis: none;
}
        '''
        file = open(self.path + "/" + self.folder_name + "/" + self.file_name + ".less", "w+")
        file.write(content)
        file.close()

    # Method: Sets the path where the project will be created
    def set_path(self, path):
        self.path = path if os.path.exists(path) else ""
        return self.path

    # Method: Sets the filename
    def set_fileName(self, file_name):
        self.file_name = file_name if file_name != "" else self.file_name

    # Method: Sets the foldername
    def set_folderName(self, folder_name):
        self.folder_name = folder_name if folder_name != "" else self.folder_name

    # Method: Get and show the info from de the project
    def get_info(self, project, details_project):
        print("Path: " + str(self.path), end="\t")
        print("Folder name: " + str(self.folder_name))
        print("File name: " + str(self.file_name), end="\t")
        print("Project:  " + project + " (" + details_project + ") ")

    # Method: Show the differents options to pick of each project
    def print_keys_from_projects(self, project):
        i = 0

        for value in self.projects[project].values():
            print("["+ list(self.projects[project].keys())[i] +"] -> " + str(value))
            i += 1

    # Method: Check that the 'option' parameter is inside of the 'array' parameter
    def in_array(self, option, array):
        return option in array;

    # Method: Show menu options
    def print_options(self):
        for key, value in self.options.items():
            print("-> "+str(key)+" <- " + value)
        
    # Method: Show the differents projects to pick
    def print_projects(self):
        for key, value in self.projects.items():
            print("--> "+key)

    # Method: Show menu
    def print_menu(self):
        print(""" 


         █████  ██    ██ ████████  ██████  ████████ ███████ ███    ███ ██████  ██       █████  ████████ ███████ 
        ██   ██ ██    ██    ██    ██    ██    ██    ██      ████  ████ ██   ██ ██      ██   ██    ██    ██      
        ███████ ██    ██    ██    ██    ██    ██    █████   ██ ████ ██ ██████  ██      ███████    ██    █████   
        ██   ██ ██    ██    ██    ██    ██    ██    ██      ██  ██  ██ ██      ██      ██   ██    ██    ██      
        ██   ██  ██████     ██     ██████     ██    ███████ ██      ██ ██      ███████ ██   ██    ██    ███████ 
                                                                                                                
                                                                                                                
        ████████████████████████████████████████████████████████████████████████████████████████████████████████

        Author: jedahee02                  Description: This script can create the structure folder or templates for projects
                                                        with technologies like Bootstrap 5, Tailwind, HTML / CSS / JS, 
                                                        JQuery (Normal version, Mobile version, UI version)
        """)
