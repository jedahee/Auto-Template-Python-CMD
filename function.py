# Author: Jesús Daza Hernández
# Nick: jedahee02
# Email: jdaza.her@gmail.com
# Details: Script that contain the functionallity (Function class)
# Description: This script can create the structure folder or templates for projects 
#              with technologies like Bootstrap 5, Tailwind, 
#              HTML / CSS / JS, JQuery (Normal version, Mobile version, UI version)

class Function():
    def __init__(self, directory_name, file_name):
        self.directory_name = directory_name
        self.file_name = file_name

        self.options = {1: "Select project", 
                        2: "Set folder name and file name",
                        3: "Create template", 
                        0: "Exit"}
        self.projects = {
            "Bootstrap": {
                "(last) version_0": 5,
            },
            "Tailwind": {
                "(last) version_0": 3,
            },
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

    def print_options(self):
        print("\n<-- OPTIONS (Select a numeric index) -->\n")
        for key, value in self.options.items():
            print("-> "+str(key)+" <- " + value)
        
    def print_projects(self):
        print("\n <-- TEMPLATES --> \n")
        for key, value in self.projects.items():
            print("--> "+key)

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
