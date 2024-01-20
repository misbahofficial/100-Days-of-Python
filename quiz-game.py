# This is a Quiz Game.
import random

questions = [
    ('What is the full form of CPU?', 'Central Processing Unit'),
    ('What is RAM?', 'Random Access Memory'),
    ('What is an SSD?', 'Solid State Drive'),
    ('What is the capital of Bangladesh?', 'Dhaka'),
    ('Who is the founder of Apple?', 'Steve Jobs'),
]

random.shuffle(questions)

score = 0
correct_answer = 0

for question, answer in questions:
    user_answer = input(f'{question}\nType your answer: ').lower()

    if user_answer == answer.lower():
        score += 1
        correct_answer += 1

print(f'''
********** Thank You for taking the Quiz *********
---------- Here is your summary -----------

You answered -> {len(questions)}
Correct answers -> {correct_answer}
Wrong answers -> {len(questions) - correct_answer}
Score -> {score}
''')
