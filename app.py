import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Miyuki Chat", page_icon="🌸")
st.title("🌸 Miyuki Waifu")


with st.sidebar:
    user_api_key = st.text_input(
        "Google API Key",
        value=os.getenv("GOOGLE_API_KEY", ""), 
        type="password"
    )
    st.info("The API key is automatically loaded from your .env file. You can enter it directly here.")

if not user_api_key:
    st.error("Please enter your Google API key in the sidebar or set up your .env file.")
    st.stop()


# --- 2. load chacracter prompt (use cache) ---

# @st.cache_data: Cache files without rereading them each time.
@st.cache_data
def load_character_prompt(file_path="character.txt"):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"'{file_path}' File not found. Make sure it is in the same directory as app.py.")
        st.stop()
    except Exception as e:
        st.error(e)
        st.stop()
def load_start_content(file_path="start_content.txt"):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"'{file_path}' File not found. Make sure it is in the same directory as app.py.")
        st.stop()
    except Exception as e:
        st.error(e)
        st.stop()

character_text_file = load_character_prompt()
start_text_file = load_start_content()



# --- 3. Initialize Chain ---
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "{character_prompt}",
        ),
        MessagesPlaceholder(variable_name="chat_history"), 
        ("human", "{input}"),
    ]
)

output_parser = StrOutputParser()

try:
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=user_api_key  
    )
    chain = prompt | model | output_parser
except Exception as e:
    st.error(f"Error initializing Gemini: {e}")
    st.stop()


# --- 4. Streamlit Session State ---
chatbot_name = "Miyuki"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content= start_text_file )
    ]

# --- 5. Chat UI ---

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        role = "assistant"
        avatar = "🌸"
    elif isinstance(message, HumanMessage):
        role = "user"
        avatar = "🧑"
    
    with st.chat_message(role, avatar=avatar):
        st.markdown(message.content)


if user_input := st.chat_input("Please enter your message..."):
    
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    with st.spinner(f"{chatbot_name}is thinking..."):
        try:
            response = chain.invoke(
                {
                    "character_prompt": character_text_file,
                    "chat_history": st.session_state.chat_history, 
                    "input": user_input,
                }
            )
            
            st.session_state.chat_history.append(AIMessage(content=response))
            with st.chat_message("assistant", avatar="🌸"):
                st.markdown(response)

        except Exception as e:
            st.error(f"An error occurred while generating the response:{e}")