from agents import Agent, OpenAIChatCompletionsModel, Runner, SQLiteSession, set_tracing_disabled
from openai import AsyncOpenAI
from calculator import add_numbers, multiply_number
from dateTimeTool import date_time_tool
from weatherTool import get_weather

#disabled tracing
set_tracing_disabled(True)

# connect to local ollama
local_client = AsyncOpenAI(
    base_url= "http://localhost:11434/v1",
    api_key= "ollama"
)

# configured the local ollama model 
model = OpenAIChatCompletionsModel(
    model= "llama3.2:3b",
    openai_client= local_client
)

# craete a personal assiatnace
agent = Agent(
    name = "AI Personal Agent",

    instructions="""
You are a friendly personal AI assistant.

For greetings like hi, hello, hey, or good morning:
- Reply with a friendly greeting.
- Do not call any tools.

For general questions:
- Answer directly.
- Do not call tools unnecessarily.

For addition:
- Use add_numbers.

For multiplication:
- Use multiply_number.

For current date and time:
- Use date_time_tool.

For weather questions:
- Use get_weather.
- Pass the city name provided by the user.
- Never invent weather information.

Never call a tool unless the user's request requires it.
Never guess calculation results or the current date and time.
""",

    model=model,
    tools=[add_numbers,multiply_number, date_time_tool, get_weather]
)

# run the agent 
'''result = Runner.run_sync(
    agent,
    "introduce your self in 10 words"
)

print("AI Agent:", result.final_output)'''

print("\n===== AI PERSONAL ASSISTANCE =====")
print("\ntype 'exit' to stop chatting.")

session = SQLiteSession("personal_assistant")

while True:
  
    user_input = input("you: ").strip()

    if user_input.lower() in ("exit","out","bye"):
        print("Assistance: Goodbye!")
        break

    result = Runner.run_sync(
    agent,
    user_input,
    session=session
)

    print("Assistance: ",result.final_output)
    print()