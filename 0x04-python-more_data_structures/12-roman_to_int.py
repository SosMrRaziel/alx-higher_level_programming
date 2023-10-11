#!/usr/bin/python3
# Define a dictionary of Roman symbols and their values
roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Define a function that converts a Roman numeral to an integer
def roman_to_int(roman_string):
    # Check if the input is a valid string
    if not isinstance(roman_string, str) or roman_string == "":
        return 0
    
    # Initialize the result as zero
    result = 0
    
    # Loop through the characters of the string from left to right
    for i in range(len(roman_string)):
        # Get the value of the current symbol
        current_value = roman_values.get(roman_string[i], 0)
        
        # If the current symbol is the last one, add its value to the result
        if i == len(roman_string) - 1:
            result += current_value
        
        # Otherwise, compare the current symbol with the next one
        else:
            # Get the value of the next symbol
            next_value = roman_values.get(roman_string[i + 1], 0)
            
            # If the current symbol is smaller than the next one, subtract its value from the result
            if current_value < next_value:
                result -= current_value
            
            # Otherwise, add its value to the result
            else:
                result += current_value
    
    # Return the final result
    return result
