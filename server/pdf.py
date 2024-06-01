from openai import OpenAI
from secrets import OPENAI_API_KEY
import PyPDF2

openaiClient = OpenAI(api_key=OPENAI_API_KEY)

file_path = 'BILLS-118s1444is.pdf'

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def get_bill_answers(text, question):
    response = openaiClient.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": question},
            {"role": "user", "content": text}
        ]
    )
    
    answer = response.choices[0].message.content
    return answer


pdf_content = extract_text_from_pdf(file_path=file_path)
answer = get_bill_answers(pdf_content, "What is this bill about?")
print(answer)