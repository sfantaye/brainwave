from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
from typing import TypedDict
from dotenv import load_dotenv  
import os

# Load environment variables from .env file
load_dotenv()

# Set Groq API key from .env file
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Load Groq Llama-3 model
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.2,
    groq_api_key=GROQ_API_KEY,  
)

# Define conversation state
class AgentState(TypedDict):
    question: str
    answer: str
    memory: list[str]

# Define agent function
# Define agent function
# Define agent function
def answer_agent(state: AgentState):
    question = state["question"]
    memory = state.get("memory", [])

    # Combine memory into context
    if memory:
        context = "\n".join(memory) + "\n\n" + question
    else:
        context = question

    # Get response from the model
    response = llm.invoke(context)

    # Split the response into sentences and add newlines between them
    sentences = response.content.split(". ")
    formatted_response = ".\n".join(sentences)  # Add a newline after each sentence

    # Update memory with the formatted response
    updated_memory = memory + [f"User: {question}", f"BrainWave: {formatted_response}"]

    return {
        "answer": formatted_response,  # Return the formatted response
        "memory": updated_memory
    }

    
# Create workflow
workflow = StateGraph(AgentState)
workflow.add_node("agent", RunnableLambda(answer_agent))
workflow.set_entry_point("agent")
workflow.add_edge("agent", END)
workflow = workflow.compile()