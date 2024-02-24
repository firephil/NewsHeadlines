import ollama
from halo import Halo
import thehackernews_com

@Halo(text='Loading', spinner='dots')
def run(text):
    response = ollama.chat(model='llama2-uncensored', messages=[
    {
        'role': 'user',
        'content': f'{text}',
    },
    ])
    return response

article = thehackernews_com.get()[0]
print(article.title)

prompt = "write the following article in a different style : " + "f{article.title}"

print(run(prompt))