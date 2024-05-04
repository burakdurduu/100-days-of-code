from question_model import Question
from quiz_brain import QuizBrain
import requests, json
import html

url = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
text = url.text
quiz_api_data = json.loads(text)
question_data = quiz_api_data["results"]


question_bank = []
for i in question_data:
    question_text = html.unescape(i["question"])
    question_answer = i["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've complated he quiz.")
print(f"Your final score was: {quiz.score}/ {quiz.question_number}")
