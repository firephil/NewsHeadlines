import ollama
from halo import Halo
import thehackernews_com

@Halo(text='Loading', spinner='dots')
def run(text):
    response = ollama.chat(model='tinyllama', messages=[
    {
        'role': 'assistant',
        'content': f'{text}',
    },
    ])
    return response

article = thehackernews_com.get()[0].getText()
print(article)

text = "write it in a different style, the following article: " + "f{article}"

#res = run(text)

#print(res)