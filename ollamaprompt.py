import ollama
from halo import Halo
import thehackernews_com

@Halo(text='Loading', spinner='dots')
def run(promptText):
    print(promptText)
    response = ollama.chat(model='tinyllama', messages=[
    {
        'role': 'user',
        'content': promptText,
    },
    ])
    return response

article = thehackernews_com.get()[0]

prompt = f"Make a summary of the following: {article.text}"

print(run(prompt))