# SETUp BLOCK
with open("sample.txt", "w") as f:
    f.write("Hello world\n\nThis is a Python test.\nWe are searching for the keyword Python.\n\nPython is fun! 123")

with open("scores.txt", "w") as f:
    f.write("Alice,85\nBob,90\nCharlie,78\n")


#task 1: Count non-blank lines
def count_non_blank_lines(filename):
    total_lines = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() != "":
                total_lines = total_lines + 1
                
    return total_lines


#task 2: Find keyword line numbers
def find_keyword_lines(filename, keyword):
    line_numbers = []
    current_line_number = 1
    
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                line_numbers.append(current_line_number)
            current_line_number = current_line_number + 1
            
    return line_numbers

# tAsk 3: Calculate average score
def calculate_average_score(filename):
    total_score = 0
    student_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            clean_line = line.strip()
            if clean_line != "":
                parts = clean_line.split(',')
                
                score = int(parts[1])
                
                total_score = total_score + score
                student_count = student_count + 1
    if student_count == 0:
        return 0
        
    average = total_score / student_count
    return average


# task 4: Caesar Cipher
def caesar_cipher(filename, shift, direction):
    with open(filename, 'r') as file:
        original_text = file.read()
        
    encrypted_text = ""
    
    for char in original_text:
        if char.isdigit():
            encrypted_text = encrypted_text + char
            
        elif char.isupper():
            x = ord(char) 
            
            if direction == "right":
                y = (x + shift - 65) % 26 + 65
            elif direction == "left":
                y = (x - shift - 65) % 26 + 65
                
            encrypted_text = encrypted_text + chr(y)

        elif char.islower():
            x = ord(char)
            
            if direction == "right":
                y = (x + shift - 97) % 26 + 97
            elif direction == "left":
                y = (x - shift - 97) % 26 + 97
                
            encrypted_text = encrypted_text + chr(y)

        else:
            encrypted_text = encrypted_text + char

    new_filename = "encrypted_" + filename
    with open(new_filename, 'w') as out_file:
        out_file.write(encrypted_text)
        
    print(f"Success! Encrypted text saved to: {new_filename}")
# test the functions
if __name__ == "__main__":
    print("- Testing question 1 -")
    lines = count_non_blank_lines("sample.txt")
    print(f"Total non-blank lines: {lines}")

    print("\n--- Testing question 2-")
    keyword_lines = find_keyword_lines("sample.txt", "Python")
    print(f"The word 'Python' appears on lines: {keyword_lines}")

    print("\n-- Testing quétion 3 -")
    average = calculate_average_score("scores.txt")
    print(f"The average student score is: {average}")

    print("\n--- Testing question 4 ---")
    print("Shifting 'sample.txt' right by 3 positions...")
    caesar_cipher("sample.txt", 3, "right")
