from __init__ import *# Custom script that installs pip packages

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

# Function that saved requested data to xlsx file
def save_To_Sheet(email_data: list = [], phone_data: list = []):
  '''Writes given data to a uniquely named file.

  @params:
      email_data - data to write to file with all emails(must be enumerable)
      phone_data - data to write to file with all phone numbers(also must be enumerable)
  @returns:
      Tuple - (name of file, full path to file)
  '''
  uName = f"PaED-{uuid.uuid4()}.xlsx" # Make unique filename (PaED stands for Phone and Email detector)
  book = xlsxwriter.Workbook(uName) # Initiate xlsx workbook with unique filename.
  sheet = book.add_worksheet() # Make worksheet(spreadsheet) in workbook
  
  for r, val in enumerate(email_data): # Loop through data and get indeces with enumerate()
    sheet.write(r+1, 0, r) # Index each data entry  
    sheet.write(r+1, 1, val) # Add value for each entry
 
  # Same thing but for phones
  for r, val in enumerate(phone_data):
    sheet.write(r+1, 3, r)
    sheet.write(r+1, 4, val)

  sheet.write(0, 0, f"{len(email_data)} emails in total") # Add Index column title and total number of entries
  sheet.write(0, 1, "Email address") # Add title for value column

  sheet.write(0, 3, f"{len(phone_data)} phones in total") # Add title for phones
  sheet.write(0, 4, "Phone numbers") # Add second title for phones

  book.close() # Close filestream
  
  return (uName, f"{pathlib.Path().resolve()}\{uName}")

# SIGINT(Ctrl+C) handler function to ask user if they want to save data collected in session
def exit_interface(data: tuple):
  '''Provides an interface for the user to optionally save all data extracted within session to a xlsx file.

  @params:
    data - Tuple ([List with all emails], [List with all phones])
  @returns:
    nothing.
  '''
  # Need to use end = "" to prevent the cursor from going to the next line. Can't use input() in a SIGINT handler.
  # Flush to remove buffer as it messes up code sequence when in SIGINT handler function.
  print("\nDo you wish to save all extracted phones and emails of this session as a spreadsheet?(y/n)? ", end="", flush=True)
  sv = readchar.readkey().strip().lower() # Read using readchar.readkey() as input() does not work.

  if (sv == "y"): # If the user wants to, save data to file
      filePath = save_To_Sheet(data[0], data[1])[1] # Write file and get filePath
      print(f"\nPath to file: {filePath}\nDo you wish to copy this path?(y/n) ", end="") # Tell user file path and ask them if they want to copy it
      cp = readchar.readkey().strip().lower() # Take input
      if(cp == "y"): # If user wants to copy file path
          pyperclip.copy(filePath) # Copy filePath
          print("Path copied!") # Inform user that the path has been copied
  sys.exit(0) # End program

# Function that nicely prints detected emails and phone numbers
# Made into a function to avoid repeating it 3 times
def output_Interface(i: str):
    '''Prints results with a nice interface.

    @parameters:
        i - input data.

    @returns:
        Tuple - ([detected phones/emails], [if user wanted emails(1) or phones(0)])
    '''
    if(F == "p"):
        res = find_PhoneNumbers(i) # find numbers
      
        if res: 
          # Format all phone numbers with commas using list comprehension, join them into a string and remove the first redundant comma and space using [2:]
          numbers = ''.join([f", {p}" for p in res])[2:]

          print("Phone number(s) found: ")
          pprint.pprint(numbers) # Print numbers
          
          cp = input("Do you wish to copy the detected phone numbers to your clipboard?(y/n)").lower().strip() # Ask if the user wants to copy results
          if cp == "y": 
            pyperclip.copy(numbers) # Copy results to user's clipboard
            print("Result Copied!") # Inform user that the results have been copied
          return (res, 0)
        else:
          print("No phone numbers found.") # In case nothing is found
          return ([], 0) # Return empty list if nothin is found
    elif F == 'e':
        res = find_Email(i) # find emails
        
        if res: 
          # Format all emails with commas using list comprehension, join them into a string and remove the first redundant comma and space using [2:]
          emails = ''.join([f", {p}" for p in res])[2:] 

          print("Email(s) found: ")
          pprint.pprint(emails) # Print emails

          cp = input("Do you wish to copy the detected emails to your clipboard?(y/n)").lower().strip() # Ask if the user wants to copy results
          if cp == "y": 
            pyperclip.copy(emails) # Copy results to user's clipboard
            print("Result Copied!") # Inform user that the results have been copied
          return (res, 1)
        else: 
          print("No emails found.") # In case nothing is found
          return ([], 1) # Return empty list in case nothing is found
    else:
        return ([], -1) # Return error code if function not provided

# Only ask for input if file is being ran directly so that it can be used as a module
if (__name__ == "__main__"):
  # Supported countries and instructions
  print("Supported coutnries: Canada, India, Mexico, USA, Antigua and Barbuda, Jamaica, Bermuda, Dominican Republic. Ctrl+C to exit.\nUse Ctrl+Shift+V to paste.")
  print("Options for input type: \n1.Terminal\n2.File\n3.Website")

  totalEmailData = [] # List for all email data
  totalPhoneData = [] # List for all phone data
  signal.signal(signal.SIGINT, lambda x,y : exec("exit_interface(data=(totalEmailData, totalPhoneData))")) # Execute exit handler with data

  while True:
    FT = input("\nEnter your input type of choice: ").strip().lower() # Ask for input type
    F = input("Do you wish to find [p]hone numbers or [e]mails? ").lower().strip() # Ask for which functions to use

    ### INPUT TYPE ONE
    if (FT == "1"):
        i = input("Enter data: ").strip().lower()

        # Show output interface, detect if the user extracted email or phone and sort into appropriate list.
        (res, ep) = output_Interface(i)
        if (ep == 0):
            totalPhoneData.extend(res)
        elif (ep == 1):
            totalEmailData.extend(res)

    ### INPUT TYPE TWO
    if (FT == "2"):
      filename = input("Enter the name/path of your file: ").strip().lower() # Ask for filename
      try: # Try except in case file does not exist
        with open(filename, "r") as file: # Open file
          i = file.read() # Read file data

          # Show output interface, detect if the user extracted email or phone and sort into appropriate list.
          (res, ep) = output_Interface(i)
          if (ep == 0):
              totalPhoneData.extend(res)
          elif (ep == 1):
              totalEmailData.extend(res)

      except FileNotFoundError:
          print("File not found, try again.") # Inform user that thier file could not be found

    ### INPUT TYPE THREE
    if (FT == "3"):
      url = input("Enter the url to your website: ").strip().lower() # Ask for URL
      try: # Try except in case an error occurs with reading url source
        # Send a get request to the url, which returns the a http response with the contents of the website.
        # Then access the http response's content with .content and after that, decode the bytes into a string for processing.
        i = requests.get(url).content.decode("utf-8")

        # Show output interface, detect if the user extracted email or phone and sort into appropriate list.
        (res, ep) = output_Interface(i)
        if (ep == 0):
            totalPhoneData.extend(res)
        elif (ep == 1):
            totalEmailData.extend(res)

      except requests.RequestException:
        print("Invalid URL") # Inform user that the URL is invalid
