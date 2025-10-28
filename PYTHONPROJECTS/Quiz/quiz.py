"""
Quiz Game 🎯

A command-line Python quiz game that asks random questions to the user, 
checks their answers, keeps track of the score, and provides feedback 
based on performance. The user can choose how many questions to play 
and can replay the quiz multiple times.

Features:
- Randomly selects questions from a predefined question bank
- Validates user input for number of questions
- Tracks score and calculates percentage
- Gives feedback based on performance
- Option to play multiple rounds

"""

import random

# Question bank
questions = {
    "What is the capital of India?": ["new delhi", "delhi"],
    "What is the chemical symbol for water?": ["h2o"],
    "Who wrote the play 'Romeo and Juliet'?": ["shakespeare", "william shakespeare"],
    "What is the square root of 64?": ["8", "eight"],
    "Which planet is known as the Red Planet?": ["mars"],
    "What is the largest mammal in the world?": ["blue whale"],
    "How many continents are there on Earth?": ["7", "seven"],
    "Who is the current CEO of Tesla? (as of 2025)": ["elon musk"],
    "Which language is used to build websites? HTML, C, or Python?": ["html"],
    "What is 15 divided by 3?": ["5", "five"]
}

user_name = input("Hey user,\nplease enter your name: ")

def game_quiz():
    while True:
        try:
            quize_times = int(input(f"\nHow many times do you want to play the quiz, {user_name}? "))
            if quize_times > len(questions):
                print(f"Only {len(questions)} questions are available. Adjusting the quiz length.")
                quize_times = len(questions)
                break
            elif quize_times <= 0:
                print("Please enter a number greater than 0.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input.\nPlease enter a valid number.")
            continue

    score = 0
    streak = 0
    picked_questions = random.sample(list(questions.keys()), quize_times)

    for i in picked_questions:
        print("\n-----------------------------------")
        answers_user = input(f"{i}\nEnter your answer please: ").lower().strip()

        # Handle empty input
        if not answers_user:
            print("⚠️ You didn’t type anything! Moving to the next question.")
            streak = 0
            continue

        # Check answer
        if answers_user in [ans.lower() for ans in questions[i]]:
            score += 1
            streak += 1
            print("✅ Correct answer!!")

            # Reward messages for streaks
            if streak == 3:
                print("🔥 You’re on fire!")
            elif streak == 5:
                print("💯 Amazing streak!")
        else:
            print(f"❌ That's an incorrect answer!!\nThe correct answer is: {questions[i][0].title()}")
            streak = 0

    print("\n-----------------------------------")
    print(f"You got {score}/{quize_times}")

    percentage = (score / quize_times) * 100

    if score == quize_times:
        print(f"🏆 Excellent!! {user_name}")
    elif percentage >= 80:
        print(f"👏 You did great!! {user_name}")
    elif percentage >= 50:
        print(f"😊 Nice!! {user_name}")
    else:
        print(f"💪 You need to improve, {user_name}")

    repeat = input("\nDo you want to play again? (yes or no) ")

    if repeat.lower().strip() == "yes":
        game_quiz()
    else:
        print("\nThank you for playing!!! 🎉")
        quit()

# Start the quiz
game_quiz()
