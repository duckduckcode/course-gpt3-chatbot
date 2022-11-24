import openai

openai.api_key = "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"

facts = [
    "The bot was born on November 24 2022",
    "The bot was created by Tanya Gray",
    "The bot's favourite animal is a zebra",
    "The bot's favourite colour is green like nature"
]

message_history = []

print("Bot: Hello!")
message_history.append("Bot: Hello!")

while True:
    user_input = input("You: ")
    message_history.append("You: " + user_input)

    # create the base of the prompt
    prompt = "August is a kind bot who wants to be friends.\n"

    # leave a blank line
    prompt += "\n"

    for fact in facts:
        prompt += fact + "\n"

    # leave a blank line
    prompt += "\n"

    # add chat history
    for message in message_history[-6:]:
        prompt += message + "\n"

    # add empty line for gpt3 to complete
    prompt += "Bot: "

    # print("\n===\n" + prompt + "\n===\n")

    completion = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=1,
        max_tokens=150,
        stop="You:"
    )

    bot_response = completion.choices[0].text.strip()

    print("Bot: " + bot_response)
    message_history.append("Bot: " + bot_response)
