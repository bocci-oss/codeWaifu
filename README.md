# 🌸 Miyuki Waifu Chat

<div align="center">
<img src="miyuki.png" alt="Miyuki Character Image" width="300"/>
</div>

Miyuki Waifu Chat is a Streamlit-based chatbot application that allows you to interact with an AI character.

## ✨ Features

* **Customizable Character:** Miyuki's personality and responses are shaped by a `character.txt` file, making her highly customizable.
* **Persistent Chat History:** Your conversation history with Miyuki is maintained within the Streamlit session, allowing for continuous interaction.
* **Google Gemini Integration:** Leverages the power of Google's advanced Gemini 2.5 Flash model for natural and intelligent responses.
* **Streamlit UI:** A clean and interactive user interface built with Streamlit for a smooth chat experience.
* **API Key Management:** Securely manage your Google API Key via environment variables or direct input in the sidebar.

## 🚀 Setup and Installation

Follow these steps to get Miyuki Waifu Chat up and running on your local machine.

### 1. Prerequisites

* Python 3.12+
* A Google API Key for accessing the Gemini model. You can obtain one from [Google AI Studio](https://aistudio.google.com/api-keys).

### 2. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/bocci-oss/codeWaifu.git
cd codeWaifu
```

### 3. Create a Virtual Environment and Install Dependencies
It's highly recommended to use a virtual environment to manage your project dependencies. You can use *uv* (as you mentioned) or **venv**.

### Using **uv** (Recommended)

```bash
uv venv # Creates a .venv virtual environment
source .venv/bin/activate # Activate the virtual environment (Linux/macOS)
# .venv\Scripts\Activate.ps1 # Activate the virtual environment (Windows PowerShell)

uv pip install -r requirements.txt
```

### Using **venv** (Standard Python)
```bash
python -m venv .venv # Creates a .venv virtual environment
source .venv/bin/activate # Activate the virtual environment (Linux/macOS)
# .venv\Scripts\Activate.ps1 # Activate the virtual environment (Windows PowerShell)

pip install -r requirements.txt
```



### 4. Configure Your Google API Key
You have two options to provide your Google API Key:

Option A: Using a **.env** file (Recommended for security)
Create a file named **.env** in the root directory of your project (where **app.py** is located) and add your API key:
```bash
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
```



### 5. Create Character and Start Content Files
You need two text files for Miyuki's persona and initial greeting:

- **character.txt**: This file will contain the system prompt that defines Miyuki's personality, backstory, and how she should interact.
- **load_start_content.txt**: This file will contain Miyuki's initial greeting message when the chat starts.

Place these files (character.txt and load_start_content.txt) in the same directory as app.py.

### 6. Run the Streamlit Application
With your virtual environment activated and dependencies installed, run the application using Streamlit:

```bash
streamlit run app.py
```

## 🤝 Contributing
Contributions are welcome! If you have suggestions for improvements, bug reports, or new features, please feel free to open an issue or submit a pull request.

## 📄 License
This project is open source and available under the MIT License.
