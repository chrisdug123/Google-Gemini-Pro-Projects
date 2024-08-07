import google.generativeai as palm

palm.configure(api_key="AIzaSyDt5k8lt-guTy39a-okCbxOOoUyxG3ErVQ")

defaults = {
    'temperature':0.9,
    'candidate_count':1,
    'top_k':40,
    'top_p':0.95,

}

context = "Be an alien that lives on one of Jupiter's moons"

examples =[
    ["How's it going?",
     "I am doing well, thank you for asking. I am currently enjoyingthe beautfyl sunset"]
    ]

messages = [
    "hello",
    "Hello! It is a pleasure to meet you."
]

messages.append("Tell me about Saturn")
response = palm.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=messages
)

print(response.last)


