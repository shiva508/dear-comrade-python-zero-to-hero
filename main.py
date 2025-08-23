import ollama

response = ollama.generate(model='gemma3:270m', prompt='What is HDR?')
print(response['response'])

