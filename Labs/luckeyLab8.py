''' 
-----------------------------------------------------------------------------
Solution:       luckeyLab8.py
-----------------------------------------------------------------------------
Developer:      Victoria Luckey
Course:         Intro to Programming & Logic - CITC-1301
Creation Date:  11/3/2025
Last Mod Date:  11/06/20025
E-mail Address: vlluckey@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - Student Web Page Generator
-----------------------------------------------------------------------------
Description of input:
Student's name, major, college, graduation date, hobbies and intrest
Description of output: prints confirmtaion, writes to a file and generates a web page

-----------------------------------------------------------------------------
'''


 # Get Information about the student
def main():
    print("Student Web Page Generator")
    print("This program generates a web page based on entered information.\n")

    # Get Student name and makes sure it's not empty
    name = input("Name: ")
    while len(name) == 0:
        print("Error: Can Not be blank.  Enter your name: ")
        name = input("Name: ")

    # Get the students major and makes sure it's not empty
    major = input("Major: ")
    while len(major) == 0:
        print("Error: Can Not be blank. Enter you major: ")
        major = input("Major: ")

    # Get the College the student is attending and makes sure it's not empty
    college = input("College: ")
    while len(college) == 0:
        print("Error: Can Not be blank. Enter your college: ")
        college = input("College: ")

    # Get students Graduation Year and makes sure it's not empty
    grad_year = input("Graduaton Year: ")
    while len(grad_year) == 0 :
        print("Error: Can Not be blank. Enter your graduation year: ")
        grad_year = input("Graduation Year: ")

    # Students hobbies and intrest
    hobbies = input("Hobbies and interests: ")

    # Generate filename for webpage
    filename = "biography.html"
    # Call the function 'writeBiography' to write the HTML File
    writeBiography(filename, name, major, college, grad_year, hobbies)

def writeBiography(filename, name, major, college, grad_year, hobbies):
    # Need a variable before try to make sure "finally" closes the file
    file = None

    try:
        # Trys to open file to write
        file = open(filename, "w") 

        # Opens the html 
        file.write("<html>\n")
        # The title for browser
        file.write(f"<head><title>{college} student: {name}</title></head>\n")
        # Starts the body
        file.write("<body>\n")
         # Center student name on page
        file.write(f"<center><h1>{name}</h1></center>\n")
        file.write("<h1>\n")
        # Students biograpy
        file.write(f"My name is {name}. I am a {major} major at {college}. ")
        file.write(f"I expect to graduate in {grad_year}. <br><br>\n")
        # Students hobbies
        file.write(f"{hobbies}\n")
        file.write("<hr>\n")
        # Close HTML
        file.write("<body>\n")
        file.write("</html>\n")
        # Confirms the file was written
        print(f'\nWriting web page to "{filename}". ')
        print("Done!")
    
    except Exception:
        # Prints Error if file cannot open or written
        print("Error: A problem has occured writing the file")
    finally: 
      # Makes sure file closes even if an error happens  
      if file:
        file.close()

main ()