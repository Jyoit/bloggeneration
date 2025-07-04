
from dotenv import load_dotenv
import os

from openai import OpenAI
import time

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENAI_API_KEY"),
)


# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = "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"

# system_message = "Write a blog post that explains an advanced concept in simple terms, using at least 3 real-life examples and a conclusion with actionable advice"
def get_response(user_input: str, task: str = "all") -> str:
    # task = input("What do you want? (grammar/expand/hashtags/all): ")
    if task == "grammar":
        system_message = "You are an expert editor. Correct all grammar and spelling mistakes in the given text. Output only the corrected text."
    elif task == "expand":
        system_message = "You are an expert writer. Rewrite and expand the given text into a longer, more detailed and engaging version. Output only the improved text."
    elif task == "hashtags":
        system_message = "You are a social media specialist. Read the given text and output exactly {n} relevant and popular hashtags "
        "related to the topic, in lower case, separated by spaces. Do not include explanations."
    else:
        system_message = '''You are an expert social media content editor.  
Given a piece of text, you will:
1. Correct all grammar and spelling mistakes in the text.
2. Rewrite and expand the text to make it more engaging and detailed.
3. At the end of the response, add **exactly 5 relevant and popular hashtags** on a new line.  
The hashtags should be related to the topic of the text, concise, and written in lower case.  
Output only the improved text followed by the hashtags.  
Do not include explanations or anything '''
    # try: 
    #     while True:    
    #         user_input = input("You: ")
    #         if user_input.lower() in ["exit", "quit"]:
    #             print("Exiting the chat. Goodbye!")
    #             break   

    #         print("Thinking...")

    try:


        completion = client.chat.completions.create(
        #   extra_headers={
        #     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        #     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        #   },
        extra_body={},
        model="deepseek/deepseek-r1-0528:free",
        messages=[
            {"role": "system", "content": system_message},
            {
            "role": "user",
            "content": user_input
            }
        ],
        # max_tokens=400,
        temperature=0.7
            
        )
        # print (completion.choices[0].message.content)


        # Extract & print reply
        if (
            completion.choices
            and completion.choices[0].message
            and completion.choices[0].message.content
        ):
            return completion.choices[0].message.content.strip()
            # print(f"\nBot: {reply}\n")
        else:
            return "⚠️ No valid response returned from the model. Raw response:"
            # print(completion)



    except Exception as e:
        return f"An error occurred: {e}"
        # time.sleep(1)




            # def get_answer_from_llm(user_input):
            # response = openai.ChatCompletion.create(
            #     model="gpt-3.5-turbo",

            #     messages=[
            #         {"role": "system", "content": system_message},      
            #         {"role": "user", "content": user_input}
            #     ],
            #     max_tokens=400,
            #     temperature=0.7
            # )

            # answer= response['choices'][0]['message']['content'].strip()
            # # return answer
            # print(f"Mentor: {answer}")
            

    # except KeyboardInterrupt:
    #     print("\nInterrupted by user. Goodbye!")