
# functions 

# This is a simple calculator app that performs basic arithmetic operations.
# 1.Calculation 
def calculation(num1, num2, operator):
    if(operator == "+"):
        return num1 + num2
    elif(operator == "-"):
        return num1 - num2
    elif(operator == "*"):
        return num1 * num2
    elif(operator == "/"):
        return num1 / num2
    else:
        return "Invalid operator"


# 2. Temperature Conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 3. Vower Counter
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# 4.sum, average and maximum of a list
def list_operations(option):
    if option == 1:
        data = list(map(int, input("Enter numbers separated by space: ").split()))
        if not data:
            return 0, 0, None
        total = sum(data)
        average = total / len(data)
        maximum = max(data)
        return total, average, maximum
    elif option == 2:
        data = input("Enter a string to reverse:")
        return data[::-1]

# main code
if __name__ == "__main__":
    print("Welcome to the calculator app!")
    # num1 = float(input("Enter first number: "))
    # num2 = float(input("Enter second number: "))
    # operator = input("Enter operator (+, -, *, /): ")

    # result = calculation(num1, num2, operator)
    # print(f"The result of {num1} {operator} {num2} is: {result}")

    # celsius = float(input("Enter temperature in Celsius: "))
    # fahrenheit = celsius_to_fahrenheit(celsius)
    # print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")

    # text = input("Enter a string to count vowels: ")
    # vowel_count = count_vowels(text)
    # print(f"The number of vowels in '{text}' is: {vowel_count}")

    option = int(input("Choose an option (1: sum, average, max) or (2: reverse list): "))
    data = list_operations(option)
    print(f"Result: {data}")
