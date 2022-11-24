import openai

GPT3_API_KEY = "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"

PROMPT = "Charlie is a digital human created by a company called Soul Machines. He is friendly, charming, clever and he wants to learn about you.\n\n"

history = []

openai.api_key = GPT3_API_KEY

while True:
    # capture user input
    user_input = input("You: ")

    # add user input to the history
    history.append("You:" + user_input)

    # create the prompt
    prompt = PROMPT

    # add conversation history
    for message in history:
        prompt += message + "\n"

    # add the response prompt
    prompt += "Bot:"

    print("\n===\n" + prompt + "\n===\n")

    # create the GPT3 request
    completion = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        stop="You:"
    )

    # print(completion)

    # extract the result
    bot_response = completion.choices[0].text.strip()

    # save it to the chat history
    history.append("Bot: " + bot_response)

    # show it to the user
    print("Bot: " + bot_response)
