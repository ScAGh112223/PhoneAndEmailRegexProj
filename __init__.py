'''Installs and imports dependencies

@usage:
    In you file, add the following: 
    from __init__ import *
    This will install dependencies if not installed and import them if they are installed.
    A list of dependencies can be found on line 18 of __init__.py
    Access dependecies like you would with normal imports.
Note: Autofill and intellisense will not be available for dependencies.
'''

import importlib, subprocess # Used to reliably import dependecies as variables
import sys, re, pprint, signal, platform # Import dependecies that dont need to be or cannot be installed

# __all__ allows the variables or module names in it to be accessed from any file that import __init__.*
__all__ = ["sys", "re", "pprint", "signal", "platform"] # Initialize __all__ with dependencies that are needed for both init and main.py

dependecies = ["pyperclip", "requests", "uuid", "readchar", "xlsxwriter", "pathlib"] # List of dependecies

# Special code to install selenium as the other code does not work with this.
# This is due to 'webdriver' being another module inside of the selenium module, which means that it cannot be imported with importlib or __import__()
try:
  # Import webdriver, By, WebDriverWait(for waiting for site load) and EC(also for waiting for site load), then add them to __all__
  from selenium import webdriver
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  from selenium.webdriver.common.by import By

  __all__.extend(["webdriver", "By", "WebDriverWait", "EC"])
except ImportError: # If selenium need to be installed, install and then import and add to __all__
  subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)

  from selenium import webdriver
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  from selenium.webdriver.common.by import By

  __all__.extend(["webdriver", "By", "WebDriverWait", "EC"])

for dependencyName in dependecies: # Go through needed dependecies
    try: # try except to check if package is already installed (to save on load times)
        # make a vairable with the name of the dependecy which is needed as __all__ only accepts variable names and that name is how you access that dependecy.
        # Example: if i set the name to "dep" and install XlsxWriter, i would need to use "dep" to access it in main.py
        exec(f"{dependencyName} = importlib.import_module('{dependencyName}')")
        __all__.append(dependencyName) # Append dependecy to __all__
    except ImportError: # If package is not installed
        try: # Try except in case installation fails
            # Run pip install and disable stdout as well as stderr so that the user doesn't see pip progress
            subprocess.check_call([sys.executable, "-m", "pip", "install", dependencyName],
                                  stdout=subprocess.DEVNULL,
                                  stderr=subprocess.STDOUT)

            exec(f"{dependencyName} = importlib.import_module('{dependencyName}')") # Install dependecy (explained in line 10 and 11)
            __all__.append(dependencyName) # Append dependecy to __all__
        except Exception as e:
            print(f"Failed to update/install {dependencyName}.\nError Message: {e}\nExiting program.") # Print and error message
            sys.exit(-1) # Exit with error code
