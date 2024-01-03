import openai
from config import apikey

openai.api_key = apikey

# Make an API request using openai.Completion.create
response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt="write a story in cow\n\n",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)
