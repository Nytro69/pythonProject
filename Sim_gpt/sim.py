import openai
import dotenv
import os
import sys

def separate(string: str) -> str:
    i = 0
    h = 0
    new = []
    while i < len(string):
        if i % 80 == 0 and i != 0:
            h = 1

        if string[i].isspace() and h == 1:
            new.append("\n")
            h = 0
            i += 1
            continue
        else:
            new.append(string[i])
            i += 1

    return ''.join(new)


dotenv.load_dotenv()

z = os.getenv("API_KEY")

openai.api_key = z

chat_history = [{"role": "system", "content": "you feel strong affection towards the one talking to you, answer max in 3 sentances"},
                {"role": "user", "content": "hi *smiles*"}]
chat_history_options = [{"role": "system", "content": "you are going to generate an option to the prompt as if you were in a date and is trying to charm the other person, try to steer the conversation to something non-romantic, answer max in 2 sentances"}]

while True:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    chat_history_options.append({"role": "user", "content": response['choices'][0]['message']['content']})

    print(f"\n{separate(f"{response['choices'][0]['message']['content']}")}\n\n")

    one = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history_options
    )

    two = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history_options
    )

    three = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history_options
    )
    one_s = separate(f"{one['choices'][0]['message']['content']}")
    two_s = separate(f"{two['choices'][0]['message']['content']}")
    three_s = separate(f"{three['choices'][0]['message']['content']}")

    user = int(input(f"1: {one_s}\n\n2: {two_s}\n\n3: {three_s}\nYour choice: ").strip())


    if user == 1:
        chat_history.append({"role": "user", "content": one['choices'][0]['message']['content']})
    elif user == 2:
        chat_history.append({"role": "user", "content": two['choices'][0]['message']['content']})
    elif user == 3:
        chat_history.append({"role": "user", "content": three['choices'][0]['message']['content']})
    else:
        sys.exit("Invalid int")