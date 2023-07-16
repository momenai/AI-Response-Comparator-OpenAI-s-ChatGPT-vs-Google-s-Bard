import openai
from bardapi import Bard
from config import os
def generate_answer(text):
    prompt = f"  {text} and generate the answer long to be written in Markdown style. \n"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.0,
    )

    reply = response.choices[0].text.strip()

    return reply

def get_bard_answer(text):
    return Bard().get_answer(str(text))["content"]
