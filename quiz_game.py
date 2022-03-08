print("Welcome to the Game!")

player = input("Do you want to play? ").lower()

if player[0] == "y":
    print("Okay!")

score = 0

answer = input("What is the capital of the Germany? ").lower()
if answer == "berlin":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the PM of India? ").lower()
if answer == "modi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the currency of USA? ").lower()
if answer == "dollar":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the name of our Galaxy? ").lower()
if answer == "milkyway":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " of them correct!")
print("You got " + str((score / 4) * 100) + "%")