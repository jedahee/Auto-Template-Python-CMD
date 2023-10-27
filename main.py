# Author: Jesús Daza
# Nick: jedahee
# Email: jdaza.her@gmail.com
# Details: Main script
# Description: Script that make yor structure folder project or template from 
#              differents technologies like Bootstrap 5, Tailwind, 
#              HTML / CSS / JS, JQuery (Normal version, Mobile version, UI version)

# IMPORT
# ------

# Internal
import function as fc

# External
# --------


# VARIABLES
# ---------

# Strings
folder_name = ""
file_name = ""
path = ""
project_selected = "HTML"
details_project_selected = "CSS"

# Integers
opc = -1
i = 0

# Floats

# Booleans

# Arrays


# Initializing objects
func = fc.Function(folder_name, file_name, path)

func.print_menu()

# LOOP
# ----
while (opc != 0):
    #Printing info
    print("\n<-- INFO -->\n")
    func.get_info(project_selected, details_project_selected)

    opc = -1

    # Validating option
    try:
        
        while (opc < 0 or opc > len(func.options) - 1):
            print("\n<-- OPTIONS (Select a numeric index) -->\n")
            func.print_options()

            opc = input(">> ")
            opc = int(opc)

            if (opc < 0 or opc > len(func.options) - 1):
                print("\n ERROR: You must introduce a number between 0 and " + str(len(func.options) - 1) + "\n")
    except:
        print("\n ERROR: You must select a numeric index option\n")

    # Log out
    if (opc == 0):
        print("\n### Bye! :) ###") 
    
    # Validating options from project selected
    elif (opc == 1):
        print("\n <-- TEMPLATES --> \n")
        func.print_projects()

        project_selected = input(">> ")

        while (project_selected not in func.projects.keys()):
            
            print("\nERROR: You must select a right option\n")
            project_selected = input(">> ")

        else:

            # Picking the project details (version, preprocessor...)
            if (len(func.projects[project_selected]) > 0):
                print("\n")
                func.print_keys_from_projects(project_selected)

                details_project_selected = input(" >> ")
                
                while not func.in_array(details_project_selected, func.projects[project_selected].values()):
                    print("\n ERROR: You must select a right option \n")
                    details_project_selected = input(" >> ")

    # Sets path, file name and folder name
    elif (opc == 2):
        path = input("(Ex.: /var/www) Path >> ")       
        
        while func.set_path(path) == "":
            print("\n ERROR: Path does not exist \n")
            path = input("(Ex.: /var/www) Path >> ") 

        folder_name = func.set_folderName(input("Folder name >> "))       
        file_name = func.set_fileName(input("File name >> "))
    
    # Creating templates
    elif (opc == 3):
        func.create_template(project_selected, details_project_selected)
        
