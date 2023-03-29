import re
import readline # Regex for email and phone number detection
import sys, signal # Sys and signal for disabling the Traceback after Ctrl+C from displaying
import installDependencies as id # Custom script that installs pip packages
import pprint as pp
import uuid

id.install(["pyperclip", "requests", "XlsxWriter", "readchar"]) # Run install command in case pyperclip and requests are not properly installed

import pyperclip # Import after install commad
import requests # Import after install command
import xlsxwriter # Import after install
import readchar

# Detecting phone numbers
def find_PhoneNumbers(i: str):
  '''Picks out all phone numbers from the given string.
  
  @params i - string to detect phone numbers from
  @returns a list of all the detected phone numbers.'''

  # Regex pattern for supported countries
  res = re.findall(r'''\+?1?\(?\d\d\d\)?-?\s?\d\d\d-?\s?\d\d\d\d|  # Canada
    \+?1?-?\s?\(?2?6?8?\)?-?\s?\(?\d\d\d\)?-?\s?\d\d\d\d| # USA countrues that use NANP
    \+?5?2?-?\s?\(?\d?\d?\d?\d?\)?-?\s?\d\d\s?\d\d?-?\s?\d?\d?-?\d?\d?| # Mexico
    \d\d\d\d?-?\s?\d?\d?-?\d?\d?| # Emergency Numbers
    \+?\s?9?1?\s?\(?\d\d\d\)?-?\s?\d?\d?\)?-?\s?\(?\d\d\d\d\d\)?\d?\d?\)? # India''', i, re.VERBOSE)

  return res # Return found numbers

# Detecting emails
def find_Email(i: str):
  '''Picks out all emails from the given string.
  
  @params i - string to detect phone numbers from
  @returns a list of all the detected emails.'''

  # Pattern for emails
  res = re.findall(r'''[a-zA-Z0-9\.\+-~_]*\@[a-zA-Z0-9\.\+-~_]*\.[a-zA-Z0-9\.\+-~_]*''', i) # Apply email pattern
  res = [re.sub("(mailto:)|(<a>)|(</a>)|(<br>)|(<br)|>|(x27;)", "", e) for e in res] # Remove some of the html tags that can be included while reading from website
  res = sorted(set(res)) # Remove duplicates which can also occur when reading from websites

  return res # Return found emails

def save_To_Sheet(d: list):
  book = xlsxwriter.Workbook(f"PaEDd-{uuid.uuid4()}.xlsx")
  sheet = book.add_worksheet()
  
  for r, val in enumerate(d):
    sheet.write(r+1, 0, f"Index {r}")
    sheet.write(r+1, 1, val)
  
  sheet.write(0, 0, f"Email index ({len(d)} in total)")
  sheet.write(0, 1, f"Email address")

  book.close()

def exit_interface(dat):
  print("Do you wish to save all extracted phones and emails of this session as a spreadsheet?(y/n)? ", end="")
  sv = readchar.readchar().strip().lower()

  if (sv == "y"): save_To_Sheet(dat)
  sys.exit(0)

# Function that nicely prints detected emails and phone numbers
# Made into a function to avoid repeating it 3 times
def output_Interface(i: str):
    '''Prints results with a nice interface.

    @parameters:
        i - input data.

    @returns:
        nothing
    '''
    if(F == "p"):
        res = find_PhoneNumbers(i) # find numbers
      
        if res: 
          # Format all phone numbers with commas using list comprehension, join them into a string and remove the first redundant comma and space using [2:]
          numbers = ''.join([f", {p}" for p in res])[2:]
          print(f"Phone number(s) found: {numbers}") # Print numbers
          
          cp = input("Do you wish to copy the detected phone numbers to your clipboard?(y/n)").lower().strip() # Ask if the user wants to copy results
          if cp == "y": 
            pyperclip.copy(numbers) # Copy results to user's clipboard
            print("Result Copied!") # Inform user that the results have been copied
          return res
        else: 
          print("No phone numbers found.") # In case nothing is found
    elif F == 'e':
        res = find_Email(i) # find emails
        
        if res: 
          # Format all emails with commas using list comprehension, join them into a string and remove the first redundant comma and space using [2:]
          emails = ''.join([f", {p}" for p in res])[2:] 

          pp.pprint(f"Email(s) found: {emails}") # Print emails

          cp = input("Do you wish to copy the detected emails to your clipboard?(y/n)").lower().strip() # Ask if the user wants to copy results
          if cp == "y": 
            pyperclip.copy(emails) # Copy results to user's clipboard
            print("Result Copied!") # Inform user that the results have been copied
          return res
        else: 
          print("No emails found.") # In case nothing is found

# Only ask for input if file is being ran directly so that it can be used as a module
if (__name__ == "__main__"):
  # Supported countries and instructions
  print("Supported coutnries: Canada, India, Mexico, USA, Antigua and Barbuda, Jamaica, Bermuda, Dominican Republic. Ctrl+C to exit.\nUse Ctrl+Shift+V to paste.")
  print("Options for input type: \n1.Terminal\n2.File\n3.Website")

  totalSessionData = []
  signal.signal(signal.SIGINT, lambda x,y : exec("exit_interface(dat=totalSessionData)"))

  while True:
    FT = input("Enter your input type of choice: ").strip().lower() # Ask for input type
    F = input("\nDo you wish to find [p]hone numbers or [e]mails? ").lower().strip() # Ask for which functions to use

    ### INPUT TYPE ONE
    if (FT == "1"):
        i = input("Enter data: ").strip().lower()
        totalSessionData.append(output_Interface(i))

    ### INPUT TYPE TWO
    if (FT == "2"):
      filename = input("Enter the name/path of your file: ").strip().lower() # Ask for filename
      try: # Try except in case file does not exist
        with open(filename, "r") as file: # Open file
          i = file.read() # Read file data
          totalSessionData.append(output_Interface(i)) # Show interface with data read from file
      except FileNotFoundError:
          print("File not found, try again.") # Inform user that thier file could not be found

    ### INPUT TYPE THREE
    if (FT == "3"):
      url = input("Enter the url to your website: ").strip().lower() # Ask for URL
      try: # Try except in case an error occurs with reading url source
        # Send a get request to the url, which returns the a http response with the contents of the website.
        # Then access the http response's content with .content and after that, decode the bytes into a string for processing.
        i = requests.get(url).content.decode("utf-8")
        totalSessionData.append(output_Interface(i)) # Show interface with data read from website
      except requests.RequestException:
        print("Invalid URL") # Inform user that the URL is invalid
