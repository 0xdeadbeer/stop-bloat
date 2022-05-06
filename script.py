#!/usr/bin/python3 
import os
import sys 

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

class FunctionCalls: 

    def show_bloated_packages(): 
        print ("Show bloated packages")
    
    def add_package(package, category): 
        print ("Add package | " + package + " - " + category)
    
    def add_category(category): 
        print ("Add category | " + category)
    
    def remove_package(package, category): 
        print ("Remove package | " + package + " - " + category) 
    
    def remove_category(category): 
        print ("Remove category | " + category) 
    
    def search(package): 
        print ("Seach | " + package) 
    
    def search_category(category): 
        print ("Search category | " + category) 
    
    def block_package(package): 
        print ("Block package | " + package) 
    
    def block_category(category): 
        print ("Block category | " + category) 
    
    def block_full(): 
        print ("Block full")
    
    def unblock_package(package): 
        print ("Unblock pacakge | " + package) 

    def unblock_category(category): 
        print ("Unblock category | " + category) 
    
    def unblock_full(): 
        print ("Unblock full") 

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
                "command": "adb -s $$$ shell",
                "args": 1,
                "command_type": "linux_command"
            }
        },
        "lists": {
            "type": "commands_collection",
            "description": "Manage lists of bloatware packages", 
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
        },
        "block": {
            "type": "commands_collection",
            "description": "identity Block/Disable the packages on the targeted device", 
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
        },
        "unblock": {
            "type": "commands_collection",
            "description": "Unblock/Enable the packages on the targeted device", 
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
        },
    }

    # primary commands 

    def help_page(self): 
        print ("help page")
    
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

        num = 0 
        main_command = command[num] 
        main_command_info = self.commands.get(main_command)
        if main_command_info is None:
            print ("[!!] Command not found")
            return 
        else: 
            while "type" in main_command_info:
                num += 1  
                try:
                    main_command = command[num]
                except Exception: 
                    self.help_page() 
                    print ("[!!] Command used incorrectly")
                    return 
                
                main_command_info = main_command_info.get(main_command)
                if main_command_info is None:
                    print ("[!!] Command not found")
                    return 
            
            if type(main_command_info) is not dict or "identity" not in main_command_info:
                print ("[!!] Command not found") 
                return 

            args_num = main_command_info["args"] 
            supplied_args = len(command)-(num+1)
            if (args_num != supplied_args): 
                print ("[!!] Incorrect number of command arguments applied,\nMake sure you read the documentation on how to use each command") 
                self.help_page() 
                return 
            
            # if it is a normal usable command, lets execute it 
            if (main_command_info["command_type"] == "function_call"):

                args = self.function_call_get_args(command, num, args_num)

                function_calls = FunctionCalls()
                function_class = "self." if (main_command_info["identity"] == "primary_command") else "function_calls"

                try: 
                    eval(function_class + main_command_info["command"] + "(" + args + ")")
                except Exception as e: 
                    print ("[!!] Exception when trying to execute the command " + main_command_info["command"])
                    print (e) 
                    return
            elif (main_command_info["command_type"] == "linux_command"):
                args = self.linux_command_get_args(command, num, args_num)
                linux_command = main_command_info["command"]

                for i in range(0, args_num): 
                    linux_command = linux_command.replace("$$$", args[i])

                print ("[!DEBUG] Executing Command: " + linux_command)
                line() 

                os.system(linux_command)
            else:
                print ("[!!] Command type is incorrect/unknown") 
                print ("[!!] Command type -> " + str(main_command_info["command_type"]))
                return # bad

def main(): 
    
    commands_manager = Commands()
    
    clear_terminal()
    banner()
    line()
    break_line()

    print ("[Hint] Type 'help' to view the help page")

    break_line()

    while True: 
        command = input("[SB] command > ")
        commands_manager.execute(command)

    # os.system("adb shell pm list packages -s")

if __name__ == "__main__":
    main() 