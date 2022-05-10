#!/usr/bin/python3 
import os
import sys 

# global variables 
target_device = "Not set" 

def break_line(): 
    print ("") 

def line(): 
    print ("-" * 50)

def clear_terminal(): 
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def banner(): 
    break_line()
    print ("   _____ _              ____  _             _    ")
    print ("  / ____| |            |  _ \| |           | |   ")
    print (" | (___ | |_ ___  _ __ | |_) | | ___   __ _| |_  ")
    print ("  \___ \| __/ _ \| '_ \|  _ <| |/ _ \ / _` | __| ")
    print ("  ____) | || (_) | |_) | |_) | | (_) | (_| | |_  ")
    print (" |_____/ \__\___/| .__/|____/|_|\___/ \__,_|\__| ")
    print ("                 | |                             ")
    print ("                 |_|   by Kevin J         ")
    break_line() 


# classes 

class ControlSystem(): 
    def getCategories(self): 
        print ("nice")            

class FunctionCalls: 

    def __init__(self): 
        self.control_system = ControlSystem() 

    def add_package(self, package, category): 
        location = "./lists/" + category + "/personal-list.bloat"
        os.system("echo \"" + package + "\" >> " + location)

    def add_category(self, category): 
        location = "./lists/" + category + "/"
        os.system("mkdir " + location)

    def remove_package(self, package, category): 
        location = "./lists/" + category + "/"
        entries = os.listdir(location)
        for entry in entries: 
            _location = location + entry 
            print ("Trying > " + _location)
            with open(_location) as file: 
                if package in file.read(): 
                    command = "sed \'/" + package +"/d\' " + _location + " > " + location + "tmp.tmp; mv " + location + "tmp.tmp " + _location
                    print (command)
                    os.system(command) 
                    break

    def remove_category(self, category): 
        location = "./lists/" + category + "/" 
        os.system("rm -rf " + location) 

    def search(self, package): 
        location = "./lists/*/*"
        os.system("grep " + package + " " + location)

    def search_category(self, category): 
        location = "./lists/" 
        os.system("ls " + location + " | grep " + category)

    def block_package(self, package):
        global target_device  
        command = "adb -s " + target_device + " shell pm disable-user --user 0 " + package
        os.system(command) 

    def block_category(self, category): 
        global target_device 
        location = "./lists/" + category + "/" 
        entries = os.listdir(location)
        for entry in entries: 
            file_location = location + entry 
            file = open(file_location, "r")

            # for line in file 
            for line in file: 
                command = "adb -s " + target_device + " shell pm disable-user --user 0 " + line.strip() + " > /dev/null 2>&1 0>&1" 
                os.system(command)
                print ("[DEBUG] Blocking package: " + line.strip() + " from category: " + category) 

    def block_full(self): 
        global target_device 
        location = "./lists/" 
        directory_entries = os.listdir(location)
        for directory_entry in directory_entries: 
            directory_location = location + directory_entry + "/"
            file_entries = os.listdir(directory_location) 
            for entry in file_entries: 
                file_location = directory_location + entry 
                file = open(file_location, "r")

                # for line in file 
                for line in file: 
                    command = "adb -s " + target_device + " shell pm disable-user --user 0 " + line.strip() + " > /dev/null 2>&1 0>&1" 
                    os.system(command)
                    print ("[DEBUG] Blocking package: " + line.strip() + " from category: " + directory_entry) 

    def unblock_package(self, package): 
        global target_device  
        command = "adb -s " + target_device + " shell pm enable " + package
        os.system(command) 

    def unblock_category(self, category): 
        global target_device 
        location = "./lists/" + category + "/" 
        entries = os.listdir(location)
        for entry in entries: 
            file_location = location + entry 
            file = open(file_location, "r")

            # for line in file 
            for line in file: 
                command = "adb -s " + target_device + " shell pm enable " + line.strip() + " > /dev/null 2>&1 0>&1" 
                os.system(command)
                print ("[DEBUG] Blocking package: " + line.strip() + " from category: " + category) 
    
    def unblock_full(self): 
        global target_device 
        location = "./lists/" 
        directory_entries = os.listdir(location)
        for directory_entry in directory_entries: 
            directory_location = location + directory_entry + "/"
            file_entries = os.listdir(directory_location) 
            for entry in file_entries: 
                file_location = directory_location + entry 
                file = open(file_location, "r")

                # for line in file 
                for line in file: 
                    command = "adb -s " + target_device + " shell pm enable " + line.strip() + " > /dev/null 2>&1 0>&1" 
                    os.system(command)
                    print ("[DEBUG] Blocking package: " + line.strip() + " from category: " + directory_entry) 
    
    def connect_to_device(self, id): 
        global target_device
        target_device = id
    
    def output_target_device(self): 
        global target_device 
        print ("Target Device -> " + target_device)

class Commands: 
    commands = {
        "help": {
            "identity": "primary_command",
            "description": "Show the help manual",
            "command": "help_page",
            "command_type": "function_call",
            "args": 0
        },
        "quit": {
            "identity": "primary_command",
            "description": "Exit the script",
            "command": "exit",
            "command_type": "function_call", 
            "args": 0
        },
        "clear": {
            "identity": "primary_command",
            "description": "Clear the screen",
            "command": "clear_terminal",
            "command_type": "function_call",
            "args": 0
        },
        "banner": {
            "identity": "primary_command",
            "description": "Show the script's banner",
            "command": "show_banner",
            "command_type": "function_call",
            "args": 0
        },
        "device": {
            "type": "commands_collection",
            "description": "Manage devices",
            "commands": {
                "list": { 
                    "identity": "command",
                    "description": "List adb devices",
                    "command": "adb devices | tail -n +2 | head -n -1",
                    "command_type": "linux_command",
                    "args": 0,
                },
                "connect": {
                    "identity": "command",
                    "description": "Connect to a device",
                    "syntax": "device connect [id]",
                    "command": "connect_to_device",
                    "args": 1,
                    "command_type": "function_call"
                }, 
                "show:target": {
                    "identity": "command",
                    "description": "Shows the current target device",
                    "syntax": "device show:target",
                    "command": "output_target_device",
                    "args": 0,
                    "command_type": "function_call"
                }
            }
        },
        "lists": {
            "type": "commands_collection",
            "description": "Manage lists of bloatware packages",
            "commands": {
                "show": {
                    "identity": "command",
                    "description": "Show all of the packages alongside the categories",
                    "command": "tail -n +1 lists/*/*", 
                    "command_type": "linux_command",
                    "args": 0
                },
                "show:categories": {
                    "identity": "command",
                    "description": "Show all of the categories",
                    "command": "ls lists | egrep -v \'^d\'",
                    "command_type": "linux_command",
                    "args": 0,
                },
                
                "add": {
                    "identity": "command",
                    "description": "Add package to category", 
                    "syntax": "lists add [package] [category]",
                    "command": "add_package", 
                    "command_type": "function_call",
                    "args": 2
                }, 
                "add:category": {
                    "identity": "command",
                    "description": "Create a category",
                    "syntax": "lists add:category [category name]",
                    "command": "add_category",
                    "command_type": "function_call",
                    "args": 1
                }, 
                "remove": {
                    "identity": "command",
                    "description": "Remove package from category",
                    "syntax": "lists remove [package] [category]",
                    "command": "remove_package",
                    "command_type": "function_call",
                    "args": 2
                },
                "remove:category": {
                    "identity": "command",
                    "description": "Remove desired category (Even if it contains packages)",
                    "syntax": "lists remove:category [category name]",
                    "command": "remove_category",
                    "command_type": "function_call",
                    "args": 1
                },
                "search": {
                    "identity": "command",
                    "description": "Search for packages",
                    "syntax": "lists search [text]",
                    "command": "search",
                    "command_type": "function_call",
                    "args": 1
                },
                "search:category": {
                    "identity": "command",
                    "description": "Search for category", 
                    "syntax": "lists search:category [text]",
                    "command": "search_category",
                    "command_type": "function_call",
                    "args": 1
                }
            }
        },
        "block": {
            "type": "commands_collection",
            "description": "identity Block/Disable the packages on the targeted device", 
            "commands": {
                "package": {
                    "identity": "command",
                    "description": "Block a specific package",
                    "syntax": "block package [package name]",
                    "command": "block_package",
                    "args": 1, 
                    "command_type": "function_call"
                },
                "category": {
                    "identity": "command",
                    "description": "Block a specific category",
                    "syntax": "block category [category name]",
                    "command": "block_category",
                    "args": 1, 
                    "command_type": "function_call"
                },
                "full": {
                    "identity": "command",
                    "description": "Block all of the packages from all of the categories",
                    "syntax": "block full",
                    "command": "block_full",
                    "args": 0,
                    "command_type": "function_call"
                }
            }
        },
        "unblock": {
            "type": "commands_collection",
            "description": "Unblock/Enable the packages on the targeted device", 
            "commands": {
                "package": {
                    "identity": "command",
                    "description": "Unblock a specific package",
                    "syntax": "unblock package [package name]",
                    "command": "unblock_package",
                    "args": 1, 
                    "command_type": "function_call"
                },
                "category": {
                    "identity": "command",
                    "description": "Unblock a specific category",
                    "syntax": "Unblock category [category name]",
                    "command": "unblock_category",
                    "args": 1, 
                    "command_type": "function_call"
                },
                "full": {
                    "identity": "command",
                    "description": "Unblock all of the packages from all of the categories",
                    "syntax": "unblock full",
                    "command": "unblock_full",
                    "args": 0,
                    "command_type": "function_call"
                }
            }
        },
    }

    # primary commands 

    def help_print(self, spacing, string): 
        # print ("DEBUG -> " + str(spacing))
        print (("  " * spacing) + "- " + string) 
    def help_page(self): 
        print ("Help page")
        line()
        density = 0
        for index, command in enumerate(self.commands):
            target_command = self.commands[command] 
            if_collection = True if "type" in target_command and target_command["type"] == "commands_collection" else False 
            self.help_print (density, command + " -> " + self.commands[command]["description"])
            
            if (if_collection):  
                density += 1
                for command in target_command["commands"]:
                    self.help_print(density, command + " -> " + target_command["commands"][command]["description"])
                density -= 1
                break_line()

    def clear_terminal(self): 
        clear_terminal()

    def show_banner(self): 
        banner()
    
    def exit(self): 
        quit()

    # get arguments functions 

    def function_call_get_args(self, array, start, args_num):
        result = []
        for i in range(1, args_num+1): 
            result.append(array[start+i])
        
        for index,element in enumerate(result): 
            result[index] = "\"" + element + "\""

        result_str = ",".join(result)
        return result_str

    def linux_command_get_args(self, array, start, args_num): 
        result = [] 
        for i in range(1, args_num+1): 
            result.append(array[start+1])
        
        return result 


    # execute command function 

    def execute(self, command): 
        command = command.strip() 
        command = command.split(" ") 

        
        # get the command label
        num = 0 
        main_command = command[num]

        # get the object from the commands (from the first layer for now)
        main_command_info = self.commands.get(main_command)

        # if the command is not found 
        if main_command_info is None:
            print ("[!!] Command not found")
            return 

        # while the command is recognized as a commands_collection 
        while "type" in main_command_info and main_command_info["type"] == "commands_collection":
            num += 1 # increase the command to fetch 

            try:
                # try to get the next command 
                main_command = command[num]
            except Exception: # if fail the to get the next command the whole command is being used incorrectly 
                print ("[!!] Command used incorrectly")
                return 
            
            # save the object of the new subcommand
            main_command_info = main_command_info["commands"].get(main_command)
            if main_command_info is None: # if the command is not found 
                print ("[!!] Command not found")
                return 
        
        # once you worked out to the final command 
        # if its not a dictionary or it does not contain an identity, signal it as a "command not found" error
        if type(main_command_info) is not dict or "identity" not in main_command_info:
            print ("[!!] Command not found") 
            return 

        # get the required args number
        args_num = main_command_info["args"] 

        # formula to figure out how many arguments the user entered 
        supplied_args = len(command)-(num+1)
        
        # if the supplied args num is not the same as the required args num, theres problem here
        if (args_num != supplied_args): 
            print ("[!!] Incorrect number of command arguments applied,\nMake sure you read the documentation on how to use each command") 
            return 
        
        # if the command type is a function_call, we'll have to call a function 
        if (main_command_info["command_type"] == "function_call"):

            args = self.function_call_get_args(command, num, args_num)

            function_calls = FunctionCalls()
            function_class = "self." if (main_command_info["identity"] == "primary_command") else "function_calls."

            try: 
                eval(function_class + main_command_info["command"] + "(" + args + ")")
            except Exception as e: 
                print ("[!!] Exception when trying to execute the command " + main_command_info["command"])
                print (e) 
                return
        # if the command type is a linux_command, we'll have to execute a linux command 
        elif (main_command_info["command_type"] == "linux_command"):
            args = self.linux_command_get_args(command, num, args_num)
            linux_command = main_command_info["command"]

            for i in range(0, args_num): 
                linux_command = linux_command.replace("$$$", args[i])

            print ("[!DEBUG] Executing Command: " + linux_command)
            line() 

            os.system(linux_command)
        # else the command_type is unknown, and all you gotta do is signal an error to the user 
        else:
            print ("[!!] Command type is incorrect/unknown") 
            print ("[!!] Command type -> " + str(main_command_info["command_type"]))
            return # bad

# main program
def main(): 
    
    # variables 
    commands_manager = Commands()
    
    # initialize the program 
    clear_terminal()
    banner()
    line()
    break_line()

    # mini help 
    print ("[Hint] Type 'help' to view the help page")

    break_line()

    # command-line logic 
    while True: 
        command = input("[SB] command > ")
        commands_manager.execute(command)

# on start 
if __name__ == "__main__":
    main() 