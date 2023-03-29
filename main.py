import re
import pyperclip
import sys, signal

# End the program without traceback if the user presses Ctrl+C(NOT MY CODE, copied)
signal.signal(signal.SIGINT, lambda x, y: exec("print("") \nsys.exit(0)")) 

# Detecting phone numbers
def find_PhoneNumbers(i: str):
  '''Picks out all phone numbers from the given string.
  
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
  
  @returns a list of all the detected emails.'''

  # Pattern for emails
  res = re.findall(r'''[a-zA-Z0-9\.\+-~_]*\@[a-zA-Z0-9\.\+-~_]*\.[a-zA-Z0-9\.\+-~_]*''', i)
  
  return res # Return found emails

# Only ask for input if file is being ran directly so that it can be used as a module
if (__name__ == "__main__"):
  # Supported countries and instructions
  print("Supported coutnries: Canada, India, Mexico, USA, Antigua and Barbuda, Jamaica, Bermuda, Dominican Republic. Ctrl+C to exit.\nUse Ctrl+Shift+V to paste.")
  while True:
    F = input("\nDo you wish to find [p]hone numbers or [e]mails? ").lower().strip() # Ask for which functions to use

    ########### ALTERNATE CODE FOR READING FROM FILE ----------------------------------------------------------------------------------

    FR = input("Do you wish to have the data read from a file(this is reccomended for data with multiple lines)?\nIf yes, enter filename otherwise leave blank. ").strip().lower()
    
    if (FR != ""):
      with open(FR, "r") as file:
        i = file.read()

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
          continue # End current loop iteration to prevent normal routine from executing
        else: 
          print("No phone numbers found.") # In case nothing is found
          continue # End current loop iteration to prevent normal routine from executing
      elif F == 'e':
        res = find_Email(i) # find emails
        
        if res: 
          # Format all emails with commas using list comprehension, join them into a string and remove the first redundant comma and space using [2:]
          emails = ''.join([f", {p}" for p in res])[2:] 

          print(f"Email(s) found: {emails}") # Print emails

          cp = input("Do you wish to copy the detected emails to your clipboard?(y/n)").lower().strip() # Ask if the user wants to copy results
          if cp == "y": 
            pyperclip.copy(emails) # Copy results to user's clipboard
            print("Result Copied!") # Inform user that the results have been copied
          continue # End current loop iteration to prevent normal routine from executing
        else: 
          print("No emails found.") # In case nothing is found
          continue # End current loop iteration to prevent normal routine from executing

    ########### ALTERNATE CODE FOR READING FROM FILE ENDED ------------------------------------------------------------------------------

    if F == 'p': # If phone
      i = input("Enter data: ")# Ask for input
      res = find_PhoneNumbers(i) # find numbers
      
      if res: 
        # Format all phone numbers with commas using list comprehension, join them into a string and remove the first redundant comma and space using [2:]
        numbers = ''.join([f", {p}" for p in res])[2:]
        print(f"Phone number(s) found: {numbers}") # Print numbers
        
        cp = input("Do you wish to copy the detected phone numbers to your clipboard?(y/n)").lower().strip() # Ask if the user wants to copy results
        if cp == "y": 
          pyperclip.copy(numbers) # Copy results to user's clipboard
          print("Result Copied!") # Inform user that the results have been copied
      else: 
        print("No phone numbers found.") # In case nothing is found
    elif F == 'e':
      i = input("Enter data: ")# Ask for input
      res = find_Email(i) # find emails
      
      if res: 
        # Format all emails with commas using list comprehension, join them into a string and remove the first redundant comma and space using [2:]
        emails = ''.join([f", {p}" for p in res])[2:] 

        print(f"Email(s) found: {emails}") # Print emails

        cp = input("Do you wish to copy the detected emails to your clipboard?(y/n)").lower().strip() # Ask if the user wants to copy results
        if cp == "y": 
          pyperclip.copy(emails) # Copy results to user's clipboard
          print("Result Copied!") # Inform user that the results have been copied
      else: 
        print("No emails found.") # In case nothing is found