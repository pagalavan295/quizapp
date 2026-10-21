from quiz import start_quiz, show_instructions, play_quiz

def main():
    while True:
        print("\n===== QUIZ APPLICATION =====")
        print("1. Start Quiz")
        print("2. View Quiz Instructions")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                play_quiz()
            elif choice == 2:
                show_instructions()
            elif choice == 3:
                print("Thank you for using Quiz Application!")
                break
            else:
                print("Invalid choice! Please select 1, 2, or 3.")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()