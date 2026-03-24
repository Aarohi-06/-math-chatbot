# Math Chat Bot

A conversational mathematical assistant built with Python, LangChain, and Groq. The agent uses a LLaMA 3.1 8B model and can converse normally, greet users, and solve complex mathematical expressions using a dedicated reasoning tool.

## Features

- **Conversational AI**: Powered by Groq's fast inference and the `llama-3.1-8b-instant` model.
- **Math Solver Tool**: Leverages the `sympy` library to evaluate mathematical expressions accurately (e.g., `2+6/2`, `sqrt(16)`, `sin(pi/2)`).
- **Agentic Workflow**: The assistant is formulated as a LangChain agent that intelligently decides when to use its specialized tools (`solve_math`, `say_hello`) based on user input.

## Prerequisites

- Python 3.12+
- A [Groq API Key](https://console.groq.com/keys)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd "Math chat bot"
   ```

2. **Environment Setup:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Install dependencies:**
   This project uses `uv` for dependency management. You can install dependencies using:
   ```bash
   # If you use uv (recommended)
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

## Usage

Start the interactive chat assistant by running:

```bash
python main.py
```

### Example Interaction

```text
Math Assistant Ready! Type 'quit' to exit.

You: Hello!
Assistant: Hello! Nice to meet you.

You: What is (5 + 3) / 2?
Assistant: The answer is 4.00000000000000

You: quit
```

## Technologies Used

- [LangChain](https://www.langchain.com/) - Application framework for LLMs
- [Groq](https://groq.com/) - Ultra-fast AI inference platform
- [SymPy](https://www.sympy.org/) - Python library for symbolic mathematics
