import google.generativeai as palm

palm.configure(api_key="AIzaSyDt5k8lt-guTy39a-okCbxOOoUyxG3ErVQ")

defaults = {
    'temperature':0.9,
    'candidate_count':1,
    'top_k':40,
    'top_p':0.95,

}

context = "Keep responses very, very short"
examples =[]
messages = []

while True:
    #capturing user input
    user_input = input("You: ")

    #add input to the message list
    messages.append(user_input)

    #send that to the AI
    response = palm.chat(
        **defaults,
        context=context,
        examples=examples,
            messages=messages
)

    #show response to the user
    print("AI: ", response.last)

    #update the message list
    messages.append(response.last)



