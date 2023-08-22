def display_question(question, options):r
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print()

def get_user_choice(num_options):
    while True:
        try:
            choice = int(input("Enter the number of your answer: "))
            if 1 <= choice <= num_options:
                return choice
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_quiz(questions):
    score = 0
    total_questions = len(questions)

    for question, options, correct_choice in questions:
        display_question(question, options)
        user_choice = get_user_choice(len(options))

        if user_choice == correct_choice:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")

    print(f"You scored {score} out of {total_questions} questions.")

if __name__ == "__main__":
    quiz_questions = [
        ("What is the capital of France?", ["Paris", "Berlin", "London"], 1),
        ("Which planet is known as the 'Red Planet'?", ["Venus", "Mars", "Jupiter"], 2),
        ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe"], 2),
        ("What is the chemical symbol for water?", ["H2O", "CO2", "O2"], 1),
        ("Who wrote the play 'Romeo and Juliet'?", ["William Shakespeare", "Jane Austen", "Charles Dickens"], 1),
    ]

    print("Welcome to the Quiz Game!")
    play_quiz(quiz_questions)
1