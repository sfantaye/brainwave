# BrainWave

**BrainWave** is an AI-powered chat application built using FastAPI and Groq. It leverages the power of the Groq API for conversational AI and includes a dynamic frontend with real-time typing effects. The app offers users the ability to interact with an AI assistant in an engaging and conversational way.


## Features
- **Real-Time Typing Effect**: The assistant responds with a smooth typing animation, simulating a live conversation.
- **Memory**: The assistant remembers previous interactions, creating a more context-aware experience.
- **FastAPI Backend**: A lightweight, fast backend for handling chat requests.
- **Groq API Integration**: Utilizes Groq's powerful LLMs (Large Language Models) for processing and responding to user queries.

## Technologies Used
- **FastAPI**: A modern web framework for building APIs.
- **Groq API**: For handling natural language processing tasks.
- **HTML/JS**: For the frontend interface.
- **LangGraph**: To manage agent workflows and memory.

## Installation

To run BrainWave locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/sfantaye/brainwave.git
    cd brainwave
    ```

2. **Install dependencies**:

    Create a virtual environment (optional but recommended):
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

    Install the required packages:
    
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the Groq API**:

    - Obtain a Groq API key from [Groq](https://groq.ai).
    - Set the API key as an environment variable:
    
    ```bash
    export GROQ_API_KEY="your-groq-api-key"
    ```

4. **Run the server**:

    To start the FastAPI server, run:

    ```bash
    uvicorn main:app --reload
    ```

    The app will be available at [http://localhost:8000](http://localhost:8000).

## Usage

- Visit the main page at [http://localhost:8000](http://localhost:8000).
- Type your question in the input field and click **Send**.
- The assistant will respond with a real-time typing effect.


