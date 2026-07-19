from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float)-> str:
    """Useful for performing basic arithmetic calculation """
    return f"Ther sum of {a} and {b} is {a+b}"

def main():
    model = ChatGroq(model="llama-3.1-8b-instant",temperature=0)

    tools = [calculator]
    agent_executor = create_agent(model = model ,tools = tools)

    print("Hi welcome! I am your chat assistant.Type 'quit' to exit the propgram.....")
    print("You can ask me to perform calculation or you can chat with me!!!")

    while True:
        user_input = input("\nYou : ").strip()

        if user_input == "quit":
            break

        print("\nAssistant : " , end="")

        respone = agent_executor.invoke(
            {"messages" : [HumanMessage(content=user_input)]}
        )

        print(respone["messages"][-1].content)

if __name__ == "__main__":
    main()