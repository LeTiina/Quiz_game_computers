import json

import requests

response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean').json()
question_data = []

for a in response['results']:
    question = a['question']
    answer = a['correct_answer']
    question_data.append({"text": question, "answer": answer})



