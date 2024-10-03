import os
import logging
from groq import AsyncGroq

logging.basicConfig(level=logging.INFO)

model = "llama3-groq-70b-8192-tool-use-preview"
client = AsyncGroq(api_key=os.environ.get("Groq_API_KEY"))

class ChatBot:
    def __init__(self, system, tools, tool_functions):
        self.system = system
        self.tools = tools
        self.tool_functions = tool_functions

    async def generate_response(self, user_message):
        try:
            logging.info(f"User message: {user_message}")
            response = await client.chat(model=model, 
                                          messages=[{"role": "user", "content": user_message}],
                                          system=self.system, 
                                          tools=self.tools)
            logging.info(f"Model response: {response}")
            return response['choices'][0]['message']['content']
        except Exception as e:
            logging.error(f"Error during response generation: {str(e)}")
            return "Sorry, I couldn't process your request."

# Example tool function
async def example_tool_function(parameters):
    # Your tool logic here
    return f"Tool executed with parameters: {parameters}"

# Instantiate the bot with your system message and tools
system_message = "You are a helpful assistant."
tools = [
    {"name": "Example Tool", "function": example_tool_function}
]
tool_functions = {"Example Tool": example_tool_function}

chatbot = ChatBot(system=system_message, tools=tools, tool_functions=tool_functions)
