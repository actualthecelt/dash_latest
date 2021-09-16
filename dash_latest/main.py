import os
import time as s
from datetime import date, datetime
import webbrowser
import sys
import inspect

# setting up variables etc.
os.environ['API_USER'] = 'd.koot'
os.environ['API_PASSWORD'] = '1919##'

version = "v1.1.2"
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
cs_input = ""
allSettings = ("logs", "devoverview", "back")
allCommands = ("home", "back", "settings", "apps", "kill", "help")
allVariables = locals()

USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')

def exists_var(var_name):
    frame = inspect.currentframe()
    try:
        return var_name in frame.f_back.f_locals or var_name in globals()
    finally:
        del frame

def ct():
    os.system('clear')

def enter():
    print("")

def checkdate():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

def rest(n):
    s.sleep(n)

# code stuff
ct()
print("> LOGIN < | Home | Apps | Settings | " + current_time + "")
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
rest(0.3)
ct()

while loop_variable == "TRUE":
    ct()
    checkdate()
    print("[logged in] | > HOME < | Apps | Settings | " + current_time +"")
    print("Welcome back, " + insertedUser + ".")
    enter()

    print("Choose an action to perform. Type 'help' for a list of commands.")
    cmd = input("> ")
    # help
    if cmd == "help":
        ct()
        print("List of commands")
        print("     home | opens the 'Home' tab")
        print("     apps | opens the 'Apps' tab")
        print("     kill | shuts down the program")
        print(" settings | opens the 'Settings' tab")
        enter()
        print("Type anything into the console to head back to home.")
        headbackHome = input("> ")
    # home cmd
    elif cmd == "home":
        pass
    # apps
    elif cmd == "apps":
        while cmd == "apps":
            ct()
            checkdate()
            print("[logged in] | Home | > APPS < | Settings | " + current_time +"")
            enter()
            print("Type 'back' to head back to the main console.")
            enter()
            print("Console-logger                 (cs) | console-log anything for later use (EXPIRIMENTAL)")
            print("Browser redirector             (br) | Speaks for itself. Type anything into here and it will automatically redirect you to Google with given input.")
            print("Current dashboard information (cdi) | Shows current information about the dashboard.")

            enter()
            app_selector = input("> ")
            if app_selector == "br":
                ct()
                checkdate()
                print("[logged in] | Home | > APPS < | Settings | " + current_time +"")
                print("                     -> > BROWSER REDIRECTOR < | Current dashboard information | Console-logger")
                print("")
                insertURL = input("Insert your search query here: ")
                webbrowser.open_new("https://www.google.com/search?client=firefox-b-d&q=" + insertURL + "")
            elif app_selector == "cdi":
                ct()
                checkdate()
                print("[logged in] | Home | > APPS < | Settings | " + current_time +"")
                print("                     -> Browser redirector | > CURRENT DASHBOARD INFORMATION < | Console-logger")
                enter()
                print("     Version: " + version + "")
                print("   Developer: The Celt")
                print("Current time: " + current_time + "")
                print("Current user: " + insertedUser + "")
                print("Coding language: Python " + sys.version + "")
                enter()
                print("Type anything into the console to head back to the APPS tab.")
                headbackApps = input("> ")
            elif app_selector == "cs":
                ct()
                checkdate()
                print("[logged in] | Home | > APPS < | Settings | " + current_time +"")
                print("                     -> Browser redirector | Current dashboard information | > CONSOLE-LOGGER <")
                enter()
                print("What do you want to console-log? Note that you can log only one thing at a time.")
                cs_input = input("> ")
                ct()
                checkdate()
                print("[logged in] | Home | > APPS < | Settings | " + current_time +"")
                print("                     -> Browser redirector | Current dashboard information | > CONSOLE-LOGGER <")
                enter()
                print("Logged '" + cs_input + "'. Go to the SETTINGS tab to view your logged information.")
                enter()
                print("Type anything into the console to head back to the APPS tab.")
                headbackCS = input("> ")
            elif app_selector == "back":
                cmd = "home"
                pass
    # settings
    elif cmd == "settings":
        while cmd == "settings":
            ct()
            checkdate()
            print("[logged in] | Home | Apps | > SETTINGS < | " + current_time +"")
            enter()
            print("Type 'back' into the console to head back to home.")
            enter()
            print("        logs | view saved information user entered in the CONSOLE-LOGGER app.")
            #print("     protips | enables/disables protips")
            print(" devoverview | overview of all ongoing development")
            enter()
            setting_selector = input("> ")
            if setting_selector == "logs":
                ct()
                checkdate()
                if cs_input != "":
                    print("[logged in] | Home | Apps | > SETTINGS < | " + current_time +"")
                    print("                             -> > LOGS < | Development overview")
                    enter()
                    print("Logged by user " + insertedUser + ".")
                    enter()
                    print("'" + cs_input + "'")
                    enter()
                    print("Type anything into the console to head back to the SETTINGS tab.")

                elif cs_input == "":
                    print("[logged in] | Home | Apps | > SETTINGS < | " + current_time +"")
                    print("                             -> > LOGS < | Development overview")
                    enter()
                    print("No logs have been inserted yet. Go to the CONSOLE-LOGGER app in the APPS tab to create one!")
                    enter()
                    print("Type anything into the console to head back to the SETTINGS tab.")

                headbackSETTINGS = input("> ")
            elif setting_selector == "devoverview":
                ct()
                checkdate()
                print("[logged in] | Home | Apps | > SETTINGS < | " + current_time +"")
                print("                             -> Logs | > DEVELOPMENT OVERVIEW <")
                enter()
                print("OVERALL DEVELOPMENT OVERVIEW")
                enter()
                print("Version: " + version + "")
                enter()
                print("KNOWN BUGS")
                print("--")
                enter()
                enter()
                print("BACKLOG")
                print("--")
                print("Put all functions, apps, tabs etc. in seperate python files and implement them into the main.py file, as functions to simplify code")
                print("Add a developer mode to the SETTINGS tab")
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
                print("[BUG] Time variable displaying time during launch program instead of showing realtime")
                print("Set up a SQLite database for login data, easier access to variables and more")
                enter()
                enter()
                print("DONE")
                print("--")
                print("Frame for code, overall project")
                print("Implementing the enter() function into all code instead of using print()")
                print("Setting up Github page")
                enter()
                enter()
                print("Type anything into the console to head back to the SETTINGS tab.")
                headbackSETTINGS = input("> ")
            elif setting_selector not in allSettings:
                ct()
                print("Given input is not an (available) setting.")
                enter()
                print("You will be redirected back to the SETTINGS tab in 5 seconds.")
                rest(5)
            elif setting_selector == "back":
                cmd = "home"
                pass
    elif cmd == "kill":
        ct()
        print("Shut down the program.")
        exit()
    elif cmd not in allCommands:
        ct()
        print("Given input is not an (available) command.")
        enter()
        print("You will be redirected back to the HOME tab in 5 seconds.")
        rest(5)