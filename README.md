Command-Line Chatbot
Chatbot built using gemini-api, it can remember converstaions,show iput tokens and output tokens in addition to the input and output price, it is also made in a way to act like a friendly coworker.It enforces max_token_limit to stop the conversation when the token limit is reached.

Features
Multi-turn conversation (previous messages are sent with each new prompt)
Prints input tokens, output tokens, and the cost of each turn
Ends the conversation once it reaches 1000 tokens in total
Requirements
Python 3.11+
A Gemini API key
Packages: google-genai, python-dotenv
Setup
Clone the repo and open the project folder.
Install the packages: pip install google-genai python-dotenv
Create a .env file in the same folder: GEMINI_API_KEY=your_key_here
Make sure .env is listed in .gitignore (never commit your key).
Run
python main.py Type a prompt and press Enter. The chat ends when the token limit is hit.

Known limitations
The limit is checked after a reply, so the last turn can go slightly over.
until now the prices of input and output tokens have to be manually adjusted according to the market.
