import os
import time as s
from datetime import datetime
import webbrowser
import sys

# setting up variables etc.
os.environ['API_USER'] = 'd.koot'
os.environ['API_PASSWORD'] = '1919##'

version = "v1.1.0"
now = datetime.now()
cs_input = ""
allSettings = ("logs", "devoverview")

USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')

def ct():
    os.system('clear')

def enter():
    print("")

# code stuff
ct()
print("> LOGIN < | Home | Apps | Settings")
print("Welcome back, please enter your credentials")

insertedUser = input("Username: ")

if insertedUser == USER:
    print()
else:
    ct()
    print("Username invalid. The program has automatically shut down.")
    exit()

insertedPass = input("Password: ")


if insertedPass == PASSWORD:
    ct()
    loop_variable = "TRUE"
else:
    ct()
    print("Password invalid. The program has automatically shut down.")
    exit()

print("Loading module...")
s.sleep(0.3)
ct()

while loop_variable == "TRUE":
    ct()
    current_time = now.strftime("%H:%M:%S")
    print("[logged in] | > HOME < | Apps | Settings | " + current_time +"")
    print("Welcome back, " + insertedUser + ".")
    print("")

    print("Choose an action to perform. Type 'help' for a list of commands.")
    cmd = input("> ")

    if cmd == "help":
        ct()
        print("List of commands")
        print("     home | opens the 'Home' tab")
        print("     apps | opens the 'Apps' tab")
        print(" settings | opens the 'Settings' tab")
        print("")
        print("Type anything into the console to head back to home.")
        headbackHome = input("> ")
    elif cmd == "home":
        pass
    elif cmd == "apps":
        while cmd == "apps":
            ct()
            current_time = now.strftime("%H:%M:%S")
            print("[logged in] | Home | > APPS < | Settings | " + current_time +"")
            print("")
            print("Type 'back' to head back to the main console.")
            print("")

            print("Console-logger                 (cs) | console-log anything for later use (EXPIRIMENTAL)")
            print("Browser redirector             (br) | Speaks for itself. Type anything into here and it will automatically redirect you to Google with given input.")
            print("Current dashboard information (cdi) | Shows current information about the dashboard.")

            print("")
            app_selector = input("> ")
            if app_selector == "br":
                ct()
                current_time = now.strftime("%H:%M:%S")
                print("[logged in] | Home | > APPS < | Settings | " + current_time +"")
                print("                     -> > BROWSER REDIRECTOR < | Current dashboard information | Console-logger")
                print("")
                insertURL = input("Insert your search query here: ")
                webbrowser.open_new("https://www.google.com/search?client=firefox-b-d&q=" + insertURL + "")
            elif app_selector == "cdi":
                ct()
                current_time = now.strftime("%H:%M:%S")
                print("[logged in] | Home | > APPS < | Settings | " + current_time +"")
                print("                     -> Browser redirector | > CURRENT DASHBOARD INFORMATION < | Console-logger")
                print("")
                print("     Version: " + version + "")
                print("   Developer: The Celt")
                print("Current time: " + current_time + "")
                print("Current user: " + insertedUser + "")
                print("Coding language: Python " + sys.version + "")
                print("")
                print("Type anything into the console to head back to the APPS tab.")
                headbackApps = input("> ")
            elif app_selector == "cs":
                ct()
                print("[logged in] | Home | > APPS < | Settings | " + current_time +"")
                print("                     -> Browser redirector | Current dashboard information | > CONSOLE-LOGGER <")
                print("")
                print("What do you want to console-log? Note that you can log only one thing at a time.")
                cs_input = input("> ")
                UserWarning("[console-logged by user] " + cs_input + "")
                ct()
                print("[logged in] | Home | > APPS < | Settings | " + current_time +"")
                print("                     -> Browser redirector | Current dashboard information | > CONSOLE-LOGGER <")
                print("")
                print("Logged '" + cs_input + "'. Go to the SETTINGS tab to view your logged information.")
                print("")
                print("Type anything into the console to head back to the APPS tab.")
                headbackCS = input("> ")
            elif app_selector == "back":
                cmd = "home"
                pass
    elif cmd == "settings":
        while cmd == "settings":
            ct()
            current_time = now.strftime("%H:%M:%S")
            print("[logged in] | Home | Apps | > SETTINGS < | " + current_time +"")
            print("")
            print("Type 'back' into the console to head back to home.")
            print("")
            print("logs         | view saved information user entered in the CONSOLE-LOGGER app.")
            print("devoverview  | overview of all ongoing development")
            print("")
            setting_selector = input("> ")
            if setting_selector == "logs":
                ct()
                if cs_input != "":
                    print("[logged in] | Home | Apps | > SETTINGS < | " + current_time +"")
                    print("                             -> > LOGS < | Development overview")
                    print("")
                    print("Logged by user " + insertedUser + ".")
                    print("")
                    print("'" + cs_input + "'")
                    print("")
                    print("Type anything into the console to head back to the SETTINGS tab.")
                elif cs_input == "":
                    ct()
                    print("[logged in] | Home | Apps | > SETTINGS < | " + current_time +"")
                    print("                             -> > LOGS < | Development overview")
                    enter()
                    print("No logs have been inserted yet. Go to the CONSOLE-LOGGER app in the APPS tab to create one!")
                    enter()
                    print("Type anything into the console to head back to the SETTINGS tab.")

                headbackSETTINGS = input("> ")
            elif setting_selector == "devoverview":
                ct()
                print("[logged in] | Home | Apps | > SETTINGS < | " + current_time +"")
                print("                             -> Logs | > DEVELOPMENT OVERVIEW <")
                enter()
                print("OVERALL DEVELOPMENT OVERVIEW")
                enter()
                print("Version: " + version + "")
                enter()
                print("BACKLOG")
                print("--")
                print("Put all functions, apps, tabs etc. in seperate python files and implement them into the main.py file, as functions to simplify code")
                print("Website (not sure yet)")
                print("Get more devs on the project (undecided as of now)")
                enter()
                enter()
                print("TO-DO")
                print("--")
                print("None")
                enter()
                enter()
                print("IN PROGRESS")
                print("--")
                
                print("Adding a developer mode to the SETTINGS tab")
                print("Implementing the enter() function into all code instead of using print()")
                print("Setting up Github page")
                enter()
                enter()
                print("DONE")
                print("--")
                print("Frame for code, overall project")
                enter()
                enter()
                print("Type anything into the console to head back to the SETTINGS tab.")
                headbackSETTINGS = input("> ")


                #               gonna put all available settings down below, dont worry
            elif setting_selector not in allSettings:
                ct()
                print("Given input is not an (available) setting.")
                print("")
                print("You will be redirected back to the SETTINGS tab in 5 seconds.")
                s.sleep(5)
            elif setting_selector == "back":
                cmd = "home"
                pass