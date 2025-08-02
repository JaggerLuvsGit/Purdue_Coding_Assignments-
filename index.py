import phonephinder
import csv
from pathlib import Path

def present_menu():
    while True:
        print("Menu:")
        print("F: Search for full phone number")
        print("A: Search for area code")
        print("E: Search for exchange")
        print("X: Exit the program")
        
        userchoice = input("Please choose from the following options: ").strip().upper()
        
        if userchoice in ['F', 'A', 'E', 'X']:
            return userchoice
        else:
            print("Invalid selection, please try again.")

def main():
    # Import CSV file as a Python list
    phonenumberlist = []
    with open(Path(__file__).with_name('phone_numbers.csv'), newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            phonenumberlist.extend(row) 
        f.close()
    # Report the number of phone numbers in the original list
    print(f"\nThere were {len(phonenumberlist)} phone numbers in the CSV file orgianly.")
    
    # Clean the phone numbers using phonephinder
    clean_numbers = phonephinder.clean_phone_numbers(phonenumberlist)
  
    # Report the number of cleaned phone numbers
    print(f"\nThere are now {len(clean_numbers)} phone numbers after cleaning.\n")
    
    while True:
        # Present the menu and get the user's selection
        userchoice = present_menu()
        if userchoice == 'X':
            print("Goodbye!")
            break
        
        search_term = input("Please enter the search term: ").strip()
        
        if userchoice == 'F':
            results = phonephinder.find_number(clean_numbers, search_term)
        elif userchoice == 'A':
            results = phonephinder.find_area(clean_numbers, search_term)
        elif userchoice == 'E':
            results = phonephinder.find_exchange(clean_numbers, search_term)
        
        # Report the search results
        if results:
            print(f"\nFound {len(results)} result(s) for that search:")
            for result in results:
                print(result)
        else:
            print("No results found.")
    
if __name__ == "__main__":
    main()
