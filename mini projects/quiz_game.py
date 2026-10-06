score = 0

print("Welcome to the Quiz Game")

answer = input("1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("2. Which language are you learning? ")

if answer.lower() == "python":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("3. What is 5 + 5? ")

if answer == "10":
    print("Correct")
    score += 1
else:
    print("Wrong")

print("\nFinal Score:", score)