# agents.py

from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
from typing import TypedDict
import os

# Set Groq API key
os.environ["GROQ_API_KEY"] = "your-groq-api-key-here"

# Load Groq Llama-3 model
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.2,
)

# Define conversation state
class AgentState(TypedDict):
    question: str
    answer: str
    memory: list[str]

# Define agent function
def answer_agent(state: AgentState):
    question = state["question"]
    memory = state.get("memory", [])

    # Combine memory into context
    if memory:
        context = "\n".join(memory) + "\n\n" + question
    else:
        context = question

    response = llm.invoke(context)

    updated_memory = memory + [f"User: {question}", f"Assistant: {response.content}"]

    return {
        "answer": response.content,
        "memory": updated_memory
    }

# Create workflow
workflow = StateGraph(AgentState)
workflow.add_node("agent", RunnableLambda(answer_agent))
workflow.set_entry_point("agent")
workflow.add_edge("agent", END)
workflow = workflow.compile()

