import os
import openai
import requests
import dotenv
import bs4

openai.api_key = 'API_KEY'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

h = input("Input: ")

f = f"""
Answer only True or False, Not anything else, because this will go \
back to my code as an api request, will you be able to answer this \
question in a precise manner or should the user specify more for \
a more precise answer, here is the question: {h}
"""

f = get_completion(f)

print(f)