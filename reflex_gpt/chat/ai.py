from decouple import config
from openai import OpenAI

OPENAI_API_KEY = config("OPENAI_API_KEY", cast=str, default=None)
OPENAI_MODEL = "gpt-4o-mini"

client = OpenAI()


def get_client():
    return OpenAI(api_key=OPENAI_API_KEY)


def get_lim_response(gpt_messages):
    client = get_client()
    completion = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=gpt_messages,
    )
    return completion.choices[0].message.content


completion = client.chat.completions.create(
    model=OPENAI_MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about recursion in programming."},
    ],
)

print(completion.choices[0].message)
