

# List all Models first
from groq import  Groq
from groq import Groq
#import ListenV3
from openai import OpenAI
global_permission = True
apiKey="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"
client = Groq(api_key=apiKey,)
messages=[
            {"role": "system", "content": "you are a helpful personal assistant who has sarcastic and humorous behaviour in talking"},

        ]
while True:
    a =str(input("Enter your"))
    b = {"role": "user", "content": a}
    messages.append(b)
    resource = client.chat.completions.create(
        model="mixtral-8x7b-32768",  # mixtral-8x7b-32768
        messages=messages,
        temperature=0.5,
    )
    text = resource.choices[0].message.content
    res = {"role": "system", "content": text}
    messages.append(res)
    print(text)