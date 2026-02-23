#1 Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000
num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1
#2 Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
inches = float(input("Enter inches (negative value to stop): "))
while inches >= 0:
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters.")
    inches = float(input("Enter inches (negative value to stop): "))
#3 Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Invalid input. Please enter a number.")
if numbers:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
else:
    print("No numbers were entered.")
#4 Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.
import random
number_to_guess = random.randint(1, 10)
guess = 0
while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > number_to_guess:
        print("Too highhh!")
    elif guess < number_to_guess:
        print("Too loww!")
    else:
        print("Correctt!")
#5 Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.
correct_username = "python"
correct_password = "rules"
attempts = 0
while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        attempts -= 1
        print(f"Incorrect credentials. You have {attempts} attempts left.")
if attempts == 5:
    print("Access denied.")
#6 Write a function that extracts the middle character of a given string. If the string length is even, extract the middle two characters.
def extract_middle_characters(s):
    length = len(s)
    if length % 2 == 0:
        middle_characters = s[length // 2 - 1:length // 2 + 1]
    else:
        middle_characters = s[length // 2]
    return middle_characters
#7 Write a function that takes a phrase and returns an acronym using the first letter of each word, capitalized. For example: Input: "unidentified foreign object" Output: "UFO"
def get_acronym(phrase):
    words = phrase.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym