import openai
while True:
    content = input ("User: ")
    messages.append({"role": "user", "content": content})
    
    completion = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = messages
    )
    
    chat_response = completion.choices[0].message.content
    print(f'ChatGPT response: {chat_response}')
