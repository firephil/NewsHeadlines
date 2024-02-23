import ollama
from halo import Halo
import thehackernews_com

@Halo(text='Loading', spinner='dots')
def run(text):
    response = ollama.chat(model='mistral', messages=[
    {
        'role': 'assistant',
        'content': f'{text}',
    },
    ])
    return response

article = thehackernews_com.get()[0].getText

text = "write it in a different style: " + "f{article}"

res = run(text)

print(res)