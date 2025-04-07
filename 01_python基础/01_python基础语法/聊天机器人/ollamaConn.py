import ollama

client = ollama.Client(
    host='http://localhost:11434',
    # headers={'x-some-header': 'some-value'}
)