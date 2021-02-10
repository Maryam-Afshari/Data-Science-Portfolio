


# - One line of code for each method


def add_comma(a_string):
    """returns a copy of the string 
        with every word separated by
        a comma"""
    return a_string.replace(' ',', ') 


def belongs_to(a_string, a_word):
    """returns true if a_string
       contains a_word """
    if a_word in a_string:
        return True
    return False


def count_repetition(a_string, a_substring):
    """returns how many times a_substring 
       occurs in a_string """
    return a_string.count(a_substring)
  
    

def is_a_question(a_string):
    """returns true if a_string
       ends with a "?" """
    if "?" in a_string:
        return True
    return False
    
    

def remove_surrounding_whitespaces(a_string):
    """returns a copy of the string with leading 
        and trailing whitespaces removed"""
    return a_string.strip()


def replace(initial_string, old_letter, new_letter):
    """returns a copy of the string with the
       new letter replacing the old one""" 
    return initial_string.replace(old_letter,new_letter)


def full_description_concatenation(first_name, last_name, age):
    """returns a sentence with the first_name and the last_name
       capitalized and the age using concatination"""
    return first_name.capitalize()+" "+last_name.capitalize()+" is "+str(age)


def full_description_formatting(first_name, last_name, age):
    """returns a sentence with the first_name and the last_name
       capitalized and the age using formatting""" 
    return f"{first_name.capitalize()} {last_name.capitalize()} is {age}"

