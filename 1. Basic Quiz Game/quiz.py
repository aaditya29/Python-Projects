print("Welcome To Computer Quiz Game!!!")

playing = input("Do you want to participate? ")

if playing.lower() != "yes":
    quit()

print("Let's start the game!")
marks = 0

answer = input("What is time complexity of binary search? ")
if answer.lower() == "ologn":
    print('Correct!')
    marks += 1
else:
    print("Incorrect!")
    marks -= 0.33

answer = input("The IA-32 system follows which of the following design?")
if answer.lower() == "cisc":
    print('Correct!')
    marks += 1
else:
    print("Incorrect!")
    marks -= 0.33

answer = input(
    "Which forms have a relation that contains information about a single entity?")
if answer.lower() == "4nf":
    print('Correct!')
    marks += 1
else:
    print("Incorrect!")
    marks -= 0.33

answer = input(
    "What is the best case runtime of linear search(recursive) algorithm on an ordered set of elements?")
if answer.lower() == "o(1)":
    print('Correct!')
    marks += 1
else:
    print("Incorrect!")
    marks -= 0.33

print("You marked " + str(marks) + " questions correct!")
print("Your score is: " + str((marks / 4) * 100) + "%.")
