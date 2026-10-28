# 24 Quiz Game Program

questions = ["What is the capital of France?",
            "Which planet is known as the Red Planet?",
            "How many sides does a hexagon have?"]
options = [["A. London", "B. Paris", "C. Rome", "D. Madrid"],
          ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
          ["A. 3", "B. 4", "C. 5", "D. 6"]]
answers = ["B", "B", "D"]
guesses = []

score = 0
question_number = 0

for question in questions:
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_number]:
        print("CORRECT")
        score += 1
    else:
        print("INCORRECT")
        print(f"The correct answer is {answers[question_number]}")

    question_number += 1

print("Results")
print("-------")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
print(f"Your score is {score}")

