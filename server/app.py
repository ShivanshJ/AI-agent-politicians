import json
import spacy
from openai import OpenAI
import requests
import re as regex
from bs4 import BeautifulSoup


openaiClient = OpenAI(api_key=OPENAI_API_KEY)


def get_answer_gpt(text, question):
    response = openaiClient.chat.completions.create(
        model="gpt-4o",
        messages=[
            # {"role": "system", "content": "You give exact text based- answers, from the html and also understand tabular html in code."},
            {"role": "system", "content": question},
            {"role": "user", "content": text}
        ],
        # max_tokens=200,
        # n=1,
        # stop=None,
        # temperature=0.7,
        # frequency_penalty=0,
        # presence_penalty=0.6
    )

    answer = response.choices[0].message.content
    return answer


if __name__ == '__main__':
    pass