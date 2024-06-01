from openai import OpenAI
from secrets import OPENAI_API_KEY
import PyPDF2

openaiClient = OpenAI(api_key=OPENAI_API_KEY)

file_path = 'BILLS-118s1444is.pdf'

def extract_text_from_pdf(file_path):
    file = openaiClient.files.create(
        file=open(file_path, "rb"),
        purpose="fine-tune"
    )

    file_id = file.id
    content = openaiClient.files.content(file_id)

    with open(file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text()
    return text_content


def get_bill_answers(text, question):
    response = openaiClient.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": question},
            {"role": "user", "content": text}
        ]
    )
    answer = response.choices[0].message.content
    return answer


text_content = extract_text_from_pdf(file_path=file_path)
answer = get_bill_answers(text_content, "What is this bill about?")
print(answer)