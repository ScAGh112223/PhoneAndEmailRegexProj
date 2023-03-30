## Basic Usage

### Input modes
This supports 3 input modes:

* Terminal - Input directly from the terminal(does not work well with multiple lines)
* File - Reads data from a file, must be plain text file(reccomended for multi line inputs)
* Website - Uses website's source code for input(often includes html tags in emails or dates and variable values in phone numbers. Most likely will require human refinement).  
  Some webistes use bytes along with a decode function to display contact data, this does not detect that.  
  If you need to extract emails/phone numbers form such websites, it is reccomended to copy and paste user-visible text and using input mode 2.

### Saving to file

When Ctrl+C is pressed to exit the program, you will be asked if you want to save your data to a spreadsheet.
This option will save all phone numbers and emails detected during the session to a xslx file.
The file path will be shown, these files can be opened with software such as excel or google sheets.

### Usage as a module

This program can be used as a python module by simply import the main.py file, note that you will need the __init__.py file to use this program in any way.

### Compatible formats

All usable inputs are in the test_main.py file

Install pytest with _*pip install pytest*_ and enter "pytest" in shell to test file
