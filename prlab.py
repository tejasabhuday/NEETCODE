import numpy as np
import pandas as pd
import re 

iris = pd.read_csv(r'C:\Users\Dr Poonam Pandey\Desktop\NEETCODE\Iris.csv')
def match_pattern(data, column, pattern):
    matched_result = [value for value in data[column] if re.match(pattern, str(value))]
    return matched_result

def get_user_input():
    print("\nEnter the name of the column you wish to search in the IRIS dataset")
    col = input("Enter name of the column: ").strip() 
    valid_columns = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
    if col not in valid_columns:
        print("Invalid column name! Please enter a valid column name.")
        return  
    pattern = input("Enter the pattern to match in the column: ").strip()
    matched_results = match_pattern(iris, col, pattern)

    if matched_results:
        print(f"Found {len(matched_results)} matches for the pattern '{pattern}' in '{col}':")
        for result in matched_results:
            print(result)
    else:
        print("No matches found.")

def main():
    print("Welcome to the IRIS Dataset Pattern Search Program using Regular Expressions")
    while True:
        get_user_input()
        again = input("\nDo you want to search again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the search program!")
            break
if __name__ == "__main__":
    main()
