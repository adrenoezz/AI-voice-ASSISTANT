from openai import OpenAI
client=OpenAI(
    api_key="",

)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Virtual assistant named JARVIS, skilled in explaining complex programming."},
        {"role": "user", "content": "explain python and java"}
    ]
)

print(completion.choices[0].message.content)


