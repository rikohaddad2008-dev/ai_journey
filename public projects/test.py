from google import genai
import os
from google.genai import types #ADDED
from dotenv import load_dotenv

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MAX_CONVERSATION_TOKENS=1000  # ADDED
history=''
while True:
    print('-'*20)
    prompt=input('enter prompt:')
    print('-'*20)
    prompt=prompt+history
    response=client.models.generate_content(model='gemini-3.8-flash',contents=prompt,config=types.GenerateContentConfig(system_instruction='You are a friendly co-worker,Keep answers short.')) 
    token_input=client.models.count_tokens(model='gemini-3.8-flash',contents=prompt)
    token_output=client.models.count_tokens(model='gemini-3.8-flash',contents=response.text)
    history=history+f'user:{prompt}'
    history=history+f'ai:{response.text}'
    print(response.text)
    print('token input:',token_input.total_tokens)
    print('token_output:',token_output.total_tokens)
    input_price=0.75
    output_price=3.75
    input_cost=token_input.total_tokens*input_price/1000000
    output_cost=token_output.total_tokens*output_price/1000000
    print(f'input cost:{input_cost}$  output cost:{output_cost}$')
    if token_input.total_tokens+token_output.total_tokens>=MAX_CONVERSATION_TOKENS:  # ADDED
        print('Token limit reached. Ending chat.')  # ADDED
        break  # ADDED
