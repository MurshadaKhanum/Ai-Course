AI Agent


Overview:

1.This project sets up a LangChain-powered research assistant that:

2.Uses DuckDuckGo Search and Wikipedia tools to gather information.

3.Structures the output into a Pydantic model for consistency.

4.Saves results into a file (research_output.txt) using a custom save tool.

5.Runs on Google Generative AI (Gemini) via LangChain integration.

The agent follows the ReAct (Reasoning + Acting) framework, meaning it thinks step-by-step, calls tools, and saves the final structured response.

Project Explanation:
1.This project builds a LangChain-based AI research assistant that:

2.Accepts a user’s query (e.g., “History of AI”).

3.Uses DuckDuckGo Search and Wikipedia tools to gather information.

4.Structures the findings into a Pydantic model (ResearchResponse) with fields for topic, summary, sources, and tools used.

5.Saves the structured output into a file (research_output.txt) using a custom save_tool.

6.Runs on Google Generative AI (Gemini) via LangChain integration.

7.The agent follows the ReAct framework (Reason + Act), meaning it:

8.Thinks step by step.

Calls tools when needed.

Produces a final structured JSON.

Saves the result automatically.


Requirements:

requirements.txt includes:

1.langchain → Core framework for building agents, prompts, and tool integrations.

2.wikipedia → Provides access to Wikipedia summaries.

3.langchain-community → Community-contributed tools/utilities (e.g., WikipediaQueryRun, DuckDuckGoSearchRun).

4.langchain-google-genai → Integration with Google’s Gemini models.

5.langchain-anthropic → Optional integration with Anthropic models (Claude).

6.python-dotenv → Loads environment variables (e.g., GOOGLE_API_KEY) from a .env file.

7.pydantic → Defines structured output schemas for consistent parsing.

8.duckduckgo-search → Enables DuckDuckGo search queries for real-time information.

Installation:

place your code in a source-code editor like VS code.
use terminal to create venv (virtual environment) in project folder for the code to run safely.
Create a virtual environment (recommended).

1.python -m venv venv
2.venv\Scripts\activate      # On Windows

Install dependencies from requirements.txt.

bash
pip install -r requirements.txt
Set up environment variables.

Create a .env file in your project root.

Add your Google API key:

GOOGLE_API_KEY=your_api_key_here

How to Run:

Run the agent script:

bash
main.py
You’ll be prompted:

Code
--- Agent is Ready ---
What can i help you research?
Type a query (e.g., “History of the Silk Road”). The agent will:

Search DuckDuckGo and Wikipedia.

Summarize findings into a structured JSON.

Save results to research_output.txt.

Output Example:

History of the Silk Road:
