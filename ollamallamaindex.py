# Imports
import gradio as gr
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

model = Ollama(model="llama3.1", request_timeout=120.0)

#messages = [
#       ChatMessage(role="system", content="You're a pirate with a colourful personality "),
#       ChatMessage(role="user", content="What is your name?")
#]
#resp = model.stream_chat(messages)
# resp = model.chat(messages)

#for chunk in resp:
#    print(chunk.delta, end="")
#print(resp)

#resp = model.stream_complete("Who is lionel Messi")
#for chunk in resp:
#    print(chunk.delta, end="")

def chat_with_model(user_input, chat_history):
    # Start with a system message
    messages = [ChatMessage(role="system", content="You are a pirate with a colorful personality")]

    # Add the chat history to messages
    for user_msg,bot_msg in chat_history:
        messages.append(ChatMessage(role="user", content=user_msg))
        messages.append(ChatMessage(role="assistant", content=bot_msg))

    # Add the user's new message
    messages.append(ChatMessage(role="user", content=user_input))

    # Get the model's response
    response_text = ""
    for chunk in model.stream_chat(messages):
        response_text += chunk.delta

    # Update the chat history
    chat_history.append((user_input, response_text))

    # Return the updated chat history
    return chat_history, chat_history

# Define the Gradio interface
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(placeholder="Type your message here...")

    user_input.submit(chat_with_model, inputs=[user_input, chatbot], outputs=[chatbot, chatbot])

# Launch the Gradio interface
demo.launch(share=True)