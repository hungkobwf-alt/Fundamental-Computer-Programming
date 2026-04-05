#1 

numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    
    if user_input == "":
        break  

    number = int(user_input)
    numbers.append(number)

numbers.sort(reverse=True)


top_five = numbers[:5]

print("The five greatest numbers are:", top_five)
#2 

num = int(input("Enter an integer: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
#3
cities = []
for _ in range(5):
    city = input("Enter the name of a city: ")
    cities.append(city)
print("The cities you entered are:")
for city in cities:
    print(cities)
#4

def get_list_sum(number_list):
    """This function takes a list of integers and returns their total sum."""
    total = 0
    
    for number in number_list:
        total = total + number  
        
    return total

def main():

    test_list = [10, 25, 5, 50, 10]
    
    final_sum = get_list_sum(test_list)
    
    print("The numbers in the list are:", test_list)
    print("The total sum of the numbers is:", final_sum)

if __name__ == "__main__":
    main()
#5
# --- Function Definition ---def remove_uneven_numbers(number_list):
    """Takes a list of integers and returns a new list with only the even numbers."""
    even_list = []
    
    for number in number_list:
        if number % 2 == 0:
            even_list.append(number)
            
    return even_list


def main():

    original = [1, 2, 3, 4, 5, 6, 7, 10, 15, 22]
    cut_down = remove_uneven_numbers(original)
    
    print("Original list:", original)
    print("Cut-down list:", cut_down)

if __name__ == "__main__":
    main()