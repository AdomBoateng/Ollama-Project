# Import
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the questions below

Here is the conversational chat history: {context}

Question: {question}

Answer:
"""

# Access the model
model = OllamaLLM(model="llama3.1", stream=True)

# Create prompt from template
prompt = ChatPromptTemplate.from_template(template)

# Chain the model and template using langchain
chain = prompt | model

# Create a function to handle conversation
def handle_conversation():
    context = ""
    print("Hello welcome to Giddy's Chatbot, Please type 'exit' to end the application")
    while True:
        user_input = input("You:")
        if user_input == "exit":
            break
        result = chain.stream({"context":"", "question":user_input})
        for chunk in result:
            print(chunk['message']['question'], end='', flush=True)
        context += f"\nUser:{user_input}\nAI:{result}"
        
if __name__ == "__main__":
    handle_conversation()