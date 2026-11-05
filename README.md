
# AI Personal Assistant 🤖

A locally running AI Personal Assistant built using Python, Ollama, Llama 3.2, and the OpenAI Agents SDK.

The assistant can answer general questions, perform calculations, provide date and time information, and retrieve simulated weather information through custom Python tools.

## 🚀 Features

- Local AI model using Ollama and Llama 3.2.
- Addition and multiplication using custom tools.
- Current date and time using a timezone-aware tool.
- Weather information using a custom weather tool.
- Conversation history using SQLiteSession.
- Interactive command-line interface.

## 🛠️ Technologies Used

- Python
- Ollama
- Llama 3.2
- OpenAI Agents SDK
- SQLite

## 📁 Project Structure

## 📁 Project Structure

```text
AI-Personal-Assistant/
├── main.py
├── calculator.py
├── dateTimeTool.py
├── weatherTool.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/AI-Personal-Assistant.git

cd AI-Personal-Assistant

### 2. Create a virtual environment

python -m venv venv

### 3. Activate the environment

Windows:

venv\Scripts\activate

### 4. Install dependencies

python -m pip install -r requirements.txt

### 5. Install and run Ollama

Download Ollama from https://ollama.com/

Pull the model:

ollama pull llama3.2:3b

Make sure Ollama is running.

### 6. Run the application

python main.py

## 💬 Example Usage

User: 10 + 20
Assistant: The result is 30.

User: What's the weather in Mumbai?
Assistant: 31°C, humid, light rain.

User: What time is it in India?
Assistant: Returns the current Indian date and time.

## 📌 Future Improvements

- Live weather API integration.
- Web-based user interface.
- Voice interaction.
- More intelligent personal assistant capabilities.

## 👨‍💻 Author

Kalpesh Nivilkar

GitHub: https://github.com/KalpeshNivilkar
