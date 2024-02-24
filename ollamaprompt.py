import ollama
from ollama import generate
from ollama import chat
from halo import Halo
import thehackernews_com


@Halo(text='Loading', spinner='dots')
def runResponse(promptText):
    print(promptText)
    response = chat(model='tinyllama', messages=[
    {
        'role': 'user',
        'content': promptText,
    },
    ])
    return response

article = thehackernews_com.get()[0]
prompt = f"Make a summary of the following: {article.text}"
print(prompt)

@Halo(text='Loading', spinner='dots')
def run():
    response = generate('tinyllama',prompt)
    print(response['response'])
#run()