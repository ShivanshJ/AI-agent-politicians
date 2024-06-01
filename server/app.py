from flask import Flask
from openai import OpenAI

app = Flask(__name__)

# openaiClient = OpenAI(api_key=OPENAI_API_KEY)

@app.route('/')
def index():
    return "<p>Hello, World!</p>"


# def get_answer_gpt(text, question):
#     response = openaiClient.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             # {"role": "system", "content": "You give exact text based- answers, from the html and also understand tabular html in code."},
#             {"role": "system", "content": question},
#             {"role": "user", "content": text}
#         ],
#         # max_tokens=200,
#         # n=1,
#         # stop=None,
#         # temperature=0.7,
#         # frequency_penalty=0,
#         # presence_penalty=0.6
#     )

#     answer = response.choices[0].message.content
#     return answer


if __name__ == '__main__':
    app.run(debug=True)