def main():
  # Creates 2 dictionaries
  state_to_abbrev = {
   "Tennessee": "TN" ,
   "Florida": "FL",
   "Georgia": "GA"

 }

  abbrev_to_state = {
   "TN": "Tennessee",
   "FL": "Florida",
   "GA": "Georgia"
 }
 # pass dictionaries to function
  lookup_state(state_to_abbrev, abbrev_to_state)

def lookup_state(state_dict, abbrev_dict):
   print("Type a full state name (like Tennessee) OR an abbreviation (like TN). ")
   print("Type 'quit' to stop")

   entry= input("Enter state or abbrevaiton (or 'quit'): ")
   while entry != "quit":
     try:
       #check if entry is a full state name
       if entry in state_dict:
         abbrev = state_dict[entry]
         print(f"{entry} is abbreviated as {abbrev}. \n ")
       elif entry in abbrev_dict:
         state = abbrev_dict[entry]
         print(f"{entry} stands for {state}.\n ")
       else:
          #force KeyError to trigger your except block
          raise KeyError
     except KeyError:
       print("That state or abbreviation is not in the system.\n") 
     entry = input("Enter state or abbrevation (or 'quit): ")
     print("Done looking up states.\n")

main()