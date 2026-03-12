from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
import sympy as sp

load_dotenv()


# -------- MATH TOOL --------

@tool
def solve_math(problem: str) -> str:
    """
    Solve mathematical expressions or problems.
    Examples:
    2+6/2
    (5+3)/2
    sqrt(16)
    sin(pi/2)
    """

    print("Math tool called")

    try:
        result = sp.sympify(problem).evalf()
        return f"The answer is {result}"
    except Exception:
        return "I couldn't solve that math problem."


# -------- HELLO TOOL --------

@tool
def say_hello(name: str) -> str:
    """Greet the user."""
    print("Hello tool called")
    return f"Hello {name}! Nice to meet you."


# -------- MAIN PROGRAM --------

def main():

    model = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    tools = [solve_math, say_hello]

    agent_executor = create_agent(
        model,
        tools,
        system_prompt="""
You are a helpful math assistant.

Whenever the user asks a math question,
use the solve_math tool.

Examples of math:
2+6/2
(5+3)/2
sqrt(16)
sin(pi/2)

For greetings use the say_hello tool.
For normal conversation respond normally.
"""
    )

    print("Math Assistant Ready! Type 'quit' to exit.")

    while True:

        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            break

        print("\nAssistant:", end=" ")

        response = agent_executor.invoke(
            {"messages": [HumanMessage(content=user_input)]}
        )

        print(response["messages"][-1].content)


if __name__ == "__main__":
    main()