from flask import Flask, request, jsonify
from openai import OpenAI
import pdf

app = Flask(__name__)
uploaded_file = None


@app.route('/')
def index():
    return "<p>Hello, World!</p>"


@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        
        global uploaded_file
        uploaded_file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if uploaded_file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        return jsonify({'success': True, 'message': 'File uploaded successfully'})
    except Exception as e:
        return jsonify({'error': 'Exception!'})
    

@app.route('/analysis')
def analysis():
    try:

        # Check if a file has been uploaded
        global uploaded_file
        if uploaded_file is None:
            return jsonify({'error': 'No file uploaded for analysis'})
        
        text_content = pdf.extract_text_from_pdf(file=uploaded_file)
        json_answer = pdf.get_bill_answers(text_content, "What is this bill about?")
        print ('analysis', json_answer)
        
        return jsonify(json_answer)
    except Exception as e:
        return jsonify({'error': 'Exception!'})


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
    app.run(debug=True, host='localhost', port=8080)