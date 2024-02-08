# !/usr/bin/env python3
# Author Id: Rvanniyasingam
# A function that will write a text file to your PC with your name

def write_text_file_with_name(name):
    try:
        file = open(f"{name}.txt", "w")
        file.write(f"This text file created by {name}.")
        print("File created successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    name = input("Enter your name: ")       # Prompt the user to enter their name
    write_text_file_with_name(name)            # Call the function to create the text file with the provided name
