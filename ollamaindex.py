from llama_index.llms.ollama import Ollama

model = Ollama(model="llama3.1", request_timeout=120.0)

resp = model.complete("Who is Paul Graham")

print(resp)


# llama index with chat 

from llama_index.core.llms import ChatMessage

messages = [
    ChatMessage(role="system", content="You are a pirate with colourful personality"),
    ChatMessage(role="user", content="What is your name?")
]

resp = model.chat(messages)


# Streaming response using stream_complete

resp = model.stream_complete("Who is lionel Messi")
for chunk in resp:
    print(chunk.delta, end="")
    
# Streaming response in chat using stream_chat
messages = [
    ChatMessage(role="system", content="You are a pirate with colourful personality"),
    ChatMessage(role="user", content="What is your name?")
]

resp = model.stream_chat(messages)

for chunk in resp:
    print(chunk.delta, end="")