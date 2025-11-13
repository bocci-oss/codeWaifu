import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

# 1. Load .env file
# (The file must contain GOOGLE_API_KEY="YOUR_API_KEY")
load_dotenv()

# If you are not using a .env file, uncomment the line below and enter your key directly.
# os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"

# 2. Initialize the model
# gemini-2.5-flash is currently in preview or is the latest lightweight model.
# (Using the model specified in your code.)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 3. Initialize prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "{character_prompt}",
        ),
        MessagesPlaceholder(variable_name="chat_history"), # For conversation context
        ("human", "{input}"),
    ]
)

# 4. Chaining
output_parser = StrOutputParser()
chain = prompt | model | output_parser

# Load character prompt
file_path = "character.txt"
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        character_text_file = f.read()
except FileNotFoundError:
    print(f"Error: Can't found '{file_path}'")


chat_history = []

chatbot_name = "Miyuki"
print(f"{chatbot_name}: start a conversation. (Type 'exit' to end.)")

# *** ADDED: while loop for continuous chat ***
while True:
    try:
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == "exit":
            print(f"{chatbot_name}: Good bye!")
            break

        # Invoke the chain with history and new input
        response = chain.invoke(
            {
                "character_prompt": character_text_file,
                "chat_history": chat_history,
                "input": user_input,
            }
        )
        
        print(f"{chatbot_name}: {response}")

        # Update chat history
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=response))

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print(f"\n{chatbot_name}: End the conversation.")
        break
    except Exception as e:
        print(f"\n!!! Error occurred: {e} !!!")