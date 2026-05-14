# Chapter 8 Project - Pig Latin Translator

def main():
    print("Pig Latin Translator\n")
    print("This program translates the contents of a text file to Pig Latin.\n")

    while True:      
        try:
            # Get file path from user
            filePath = input("File path: ")

            # Attempt to open and read contents of specified file and 
            # Split the text into a list based on newline character (each line of text becomes an element in list)
            linesList = readFile(filePath).split("\n")
        except Exception as ex:
            # If there is an error opening file
            print(ex)
        else:
            break       # Exit loop if there are no problems
        # end try        
    # end while

    # Translate and add each line to translated list
    translatedLinesList = []
    for line in linesList:
        translatedLinesList.append(translateLineToPigLatin(line))
    # end for

    try:
        # Determine name for translated file
        periodIndex = filePath.rfind(".")
        translatedFilePath = filePath[:periodIndex] + "PigLatin" + filePath[periodIndex:]

        # Write translation to file
        print("\nTranslating...")
        writeFile(translatedFilePath, translatedLinesList)
        print("Translated file written to", translatedFilePath)
    except Exception as ex:
        # If there is an error writing file
        print(ex)
    # end try    
# end function

def readFile(filePath):
    try:
        # Open file path for reading
        fileObject = open(filePath, "r")

        # Read all lines from file
        fileContents = fileObject.read()
    except FileNotFoundError:
        raise FileNotFoundError("Unable to open file: the specified file does not exist.")
    except:
        raise Exception("An unexpected problem occurred whilst opening the file.")
    else:
        fileObject.close()

        return fileContents
    # end try
# end function

def writeFile(filePath, linesList):
    try:
        # Open file path for writing
        fileObject = open(filePath, "w")

        # Ensure there is at least 1 item in list
        if len(linesList) > 0:
            # Process each line of text in list
            for line in linesList:
                # Write each translated line to file
                fileObject.write(line)
            # end for
        else:
            raise Exception("Unable to translate: the file does not contain any text.")
        # end if
    except:
        raise Exception("An unexpected problem occurred whilst writing the file.")
    else:
        fileObject.close()
    # end try
# end function

def translateLineToPigLatin(line):
    translatedLine = ""
    
    # If line has one or more character
    if len(line) > 0:
        # If line ends with a newline character, remove it
        if line.endswith("\n"):
            line = line.rstrip("\n")
        # end if
        
        # Split line into a words list based on a space
        wordList = line.split(" ")

        # Concatenate each translated word with a trailing space to translatedLine
        for word in wordList:
            translatedLine += translateWordToPigLatin(word) + " "
        # end for
    # end if

    return translatedLine + "\n"    # Return translated line with trailing newline character
# end function

def translateWordToPigLatin(word):
   # Empty string that stores the end punctuation
    symbol = ""
    
    # Checks if a ',' or '.' is at the end 
    if word.endswith(",") or word.endswith("."):
       # Stores the punctuation 
       symbol = word[-1]
       # Takes the punctuation out
       word = word[:-1]
    # If it is a number leaves it as is
    if word.isdigit():
       # Puts the number and punctuation back
       return word + symbol
    
    # Checks if the first letter of the word is Capitalized 
    upper_Case = word[0].isupper()
    # Makes the entire word lower case
    w = word.lower()
    
    # Checks if the first letter is a vowel
    vowels = "aeiou"
    # If the word starts with a vowel adds "yay" to the end
    if w[0] in vowels:
            pigword = w + "yay"
    else: 
        # If fist letter isn't a vowel it moves it to the end and adds "ay"
        pigword = w[1:] + w[0] + "ay" 
        # If the original first letter was Capitalized then   
        if upper_Case:
         # Makes the new first letter Capitalized
         pigword = pigword[0].upper() + pigword[1:]
    # Returns the piglatin word with punctation added back     
    return pigword + symbol
# end function

# DO NOT MODIFY CODE BELOW THIS LINE
if __name__ == "__main__":
    main()
# end if
