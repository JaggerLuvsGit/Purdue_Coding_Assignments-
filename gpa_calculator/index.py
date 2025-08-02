# TODO: Write a function that asks the user for a letter grade. If the letter grade is in the grade_dict, return it. Otherwise, ask the user again for a valid letter grade.

def get_grade_input(grade_dict):
    """Asks the user for a valid letter grade and returns it."""
    while True:
        grade = input("Please enter the letter grade, or 'done' to finish: ").strip().upper()
        if grade == "DONE":
            return None  # Exit the function if "done" is entered
        if grade in grade_dict:
            return grade
        print("Invalid grade. Please enter a valid letter grade.")

    
# TODO: Write a function that calculates the GPA from a list of GPA values

def calculate_gpa(grade_value_list):
    if not grade_value_list:
        return 0.0
    return sum(grade_value_list) / len(grade_value_list)
   


def main():
  # Dictionary that converts letter values to numeric equivalents
  grade_dict = {'A+':4.2, 'A':4, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'F':0} 
  # List of all letter grades entered
  grade_list = []
  # List of all grade values based on letter grades entered
  grade_value_list = []
   
  # TODO: Write the primary logic of your program here

  while True:
        grade = get_grade_input(grade_dict)
        if grade is None:
            break  # Exit the main loop if "done" is entered

        grade_list.append(grade)
        grade_value_list.append(grade_dict[grade])

        gpa = calculate_gpa(grade_value_list)

        print("Your grades are:", ', '.join(grade_list))
        print(f"Your GPA is: {gpa}")

        while True:
            user_input = input("Would you like to (C) continue or (X) exit? ").strip().upper()
            if user_input == "C":
                break  # Continue the loop
            elif user_input == "X":
                print("Exiting the program, goodbye")
                exit()  # kill program
            else:
                print("Invalid input. Please enter C or X.")
  
     

if __name__== "__main__":
  main()