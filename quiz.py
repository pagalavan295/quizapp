from questions import questions

def show_instructions():
    print("\n===== QUIZ INSTRUCTIONS =====")
    print("1. Each question has four options: A, B, C, D.")
    print("2. Enter the letter of your answer.")
    print("3. Each correct answer gives 1 point.")
    print("4. Incorrect answers get 0 points.")
    print("5. Your final score will be displayed at the end.")

def start_quiz():
    score = 0
    correct = 0
    incorrect = 0

    print("\n===== QUIZ STARTED =====")

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")

        for j, option in enumerate(q["options"]):
            print(f"{chr(65 + j)}. {option}")

        while True:
            answer = input("Enter your answer (A/B/C/D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid choice! Please enter A, B, C, or D.")

        if answer == q["answer"]:
            print("Correct answer!")
            score += 1
            correct += 1
        else:
            print("Incorrect answer!")
            print("Correct answer:", q["answer"])
            incorrect += 1

    total = len(questions)
    percentage = (score / total) * 100

    print("\n===== QUIZ RESULTS =====")
    print("Total Questions:", total)
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    print("Final Score:", percentage, "%")

    if percentage >= 80:
        print("Performance: Excellent!")
    elif percentage >= 60:
        print("Performance: Good job!")
    elif percentage >= 40:
        print("Performance: Keep practicing!")
    else:
        print("Performance: Try again!")

def play_quiz():
    while True:
        start_quiz()

        while True:
            replay = input("\nWould you like to play again? (yes/no): ").strip().lower()

            if replay == "yes":
                break
            elif replay == "no":
                print("Thank you for playing!")
                return
            else:
                print("Invalid choice! Enter yes or no.")