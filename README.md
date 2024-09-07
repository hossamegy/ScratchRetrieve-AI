# Simple Agent with LangChain and Google Generative AI

## Overview

This project implements a conversational agent using the LangChain library and Google Generative AI. The agent can retrieve information from various documents and respond to user queries based on that information. The system uses embeddings, document loaders, and vector stores to manage and query information efficiently.

## Components

### Retriever

The `Retriever` class is responsible for loading and indexing documents using embeddings and vector databases. It supports loading documents from PDFs and creating retrievers for different types of information.

### SimpleAgent

The `SimpleAgent` class interacts with the Google Generative AI model to generate responses. It processes user queries, executes actions based on retrieved information, and handles conversation loops.

### reActPrompt

The `reActPrompt` function defines a prompt template for guiding the agent's actions, including how to handle user queries and manage context.



3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory of the project and add your Google API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

1. **Configure Retrievers**

    Update the `course_info_path`, `agent_info_path`, and `user_info_path` in the `Retriver` initialization with paths to your PDF documents.

    ```python
    course_info_retriever, agent_info_retriever, user_info_retriever = Retriver(
        'path/to/course_info.pdf',
        'path/to/agent_info.pdf',
        'path/to/user_info.pdf'
    ).create()
    ```

2. **Run the Agent**
   

## Jupyter Notebook

A Jupyter Notebook containing the complete code and examples is also available in the repository. You can use it to interactively explore and run the code.

1. **Launch Jupyter Notebook**

    ```bash
    Agent_from_scratch.ipynb
    ```

2. **Open the Notebook**

    Navigate to the notebook file (`your_notebook.ipynb`) in the Jupyter interface.

## Example

Here's how to query the agent:

```python
agent.query("What is your name?", max_turns=10)
