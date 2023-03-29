import sys, subprocess # Import subprocess to make a subprocess and sys to run a executable

def install(dependecies: list):
    '''Installs provided pip packages.

    @parameters:
        dependecies - list of packages to install
    @returns:
        Tuple of -1 and error message if an error occurs otherwise 0'''

    for dep in dependecies: # Go through demanded dependecies
        try: # Try except in case installation fails
            # Run pip install and disable stdout as well as stderr so that the user doesn't see pip progress
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep],
                                  stdout=subprocess.DEVNULL,
                                  stderr=subprocess.STDOUT)
        except Exception as e:
            return (-1, e) # Return -1 and error message in case something goes wrong
    return 0 # Return 0 when all dependecies have been installed
