# Author: Jesús Daza Hernández
# Nick: jedahee02
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
import sys, os

# VARIABLES
# ---------

# Strings
folder_name = ""
file_name = ""
project_option = ""

# Integers
opc = -1

# Floats

# Booleans

# Arrays


# Initializing objects
func = fc.Function(folder_name, file_name)

func.print_menu()

# LOOP
# ----
while (opc != 0):
    opc = -1

    try:
        
        while (opc < 0 or opc > len(func.options) - 1):
            func.print_options()

            opc = input(">> ")
            opc = int(opc)

            if (opc < 0 or opc > len(func.options) - 1):
                print("\n ERROR: You must introduce a number between 0 and " + str(len(func.options) - 1) + "\n")
    except:
        print("\n ERROR: You must select a numeric index option\n")

    if (opc == 0):
        print("\n### Bye! :) ###") 
    elif (opc == 1):
        func.print_projects()
        project_option = input(">> ")

        if (project_option in func.projects.keys()):
            print("\n")

            for value in func.projects[project_option].values():
                print("[preprocessor] -> " + str(value))
            
            print("\n")
        
        else:
            print("\nERROR: You must select a right option\n")

            while (project_option not in func.projects.keys()):
                project_option = input(">> ")

                if (project_option in func.projects.keys()):
                    print("\n")
            
                    for value in func.projects[project_option].values():
                        print("[preprocessor] -> " + str(value))
                    
                    print("\n")
                else:
                    print("\nERROR: You must select a right option\n")


    elif (opc == 2):
        pass
    elif (opc == 3):
        pass
        
        

