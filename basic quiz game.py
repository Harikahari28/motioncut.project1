import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_number):
        question = self.questions[question_number]['question']
        options = self.questions[question_number]['options']

        print(f"\nQuestion {question_number + 1}: {question}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_answer = self.get_user_input(len(options))
        self.check_answer(question_number, user_answer)

    def get_user_input(self, num_options):
        while True:
            try:
                user_input = int(input(f"Enter your choice (1-{num_options}): "))
                if 1 <= user_input <= num_options:
                    return user_input
                else:
                    print("Invalid choice. Please enter a number within the given range.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_answer(self, question_number, user_answer):
        correct_answer = self.questions[question_number]['correct_answer']

        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}: {self.questions[question_number]['options'][correct_answer-1]}\n")

    def start_quiz(self):
        for i in range(len(self.questions)):
            self.display_question(i)

        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")


# Define your quiz questions, options, and correct answers
quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'correct_answer': 3
    },
    {
        'question': 'Which programming language is known for its readability and ease of use?',
        'options': ['Java', 'Python', 'C++', 'Ruby'],
        'correct_answer': 2
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['Earth', 'Jupiter', 'Mars', 'Saturn'],
        'correct_answer': 2
    }
]

# Shuffle the questions to randomize the order
random.shuffle(quiz_questions)

# Create and start the quiz game
quiz = QuizGame(quiz_questions)
quiz.start_quiz()
