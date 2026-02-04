


# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print("Result:", result)

elif operation == "-":
    result = num1 - num2
    print("Result:", result)

elif operation == "*":
    result = num1 * num2
    print("Result:", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operation")



# Simple Quiz Program

score = 0

# # Question 1
answer1 = input("What is the capital of France? ").lower()
if answer1 == "paris":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Wrong! The answer is Paris.")

# # Question 2
answer2 = input("What is 5 + 3? ")
if answer2 == "8":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Wrong! The answer is 8.")

# # Question 3
answer3 = input("Which programming language are we using? ").lower()
if answer3 == "python":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Wrong! The answer is Python.")

print("Final score:", score)

