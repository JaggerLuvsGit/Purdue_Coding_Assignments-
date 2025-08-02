import re

def clean_phone_numbers(numbers):
    valid_numbers = []
    for number in numbers:
        # Remove any non-digit characters
        cleaned_number = re.sub(r'\D', '', number)
        # Check if the cleaned number is exactly 10 digits long
        if len(cleaned_number) == 10:
            valid_numbers.append(cleaned_number)
    x=0
    for number in valid_numbers:
        print(number,end= ' ')
        x=x+1
        if x == 5:
            break
        
    return valid_numbers
    


def find_number(numbers, search_term):
    matches = [number for number in numbers if search_term in number]
    return matches

def find_area(numbers, search_term):
    matches = [number for number in numbers if number.startswith(search_term)]
    return matches

def find_exchange(numbers, search_term):
    matches = [number for number in numbers if number[3:6] == search_term]
    return matches
