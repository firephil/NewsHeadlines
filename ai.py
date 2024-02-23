import ollama
from halo import Halo

@Halo(text='Loading', spinner='dots')
def run():
    response = ollama.chat(model='deepseek-coder', messages=[
    {
        'role': 'user',
        'content': 'the date today',
    },
    ])
    return response


res = run()

print(res)
