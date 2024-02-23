import ollama

def send():
    response = ollama.chat(model='tinylama', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
    ])
    ollama.list()