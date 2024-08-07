import google.generativeai as palm

# configure palm, passing an API key

palm.configure(api_key="AIzaSyDt5k8lt-guTy39a-okCbxOOoUyxG3ErVQ")

defaults = {
    'temperature' : 0.7,
    'candidate_count':1,
    'top_k':40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences':[],
    #'safety_settings':[{"category":"HARM_CATEGORY_HARASSMENT","threshold":1},{"category":"HARM_CATEGORY_HATE_SPEECH","threshold":1},{"category":"HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold":1},{"category":"HARM_CATEGORY_DANEROUS_CONTENT","threshold":2}]
}
#concept="cells"
#age='10'
#num_sentences='2'
#prompt=f"""Explain {concept} as if I'm {age}, in {num_sentences}"""

input='tea'
prompt=f"""I will say a word and you tell me the color that describes your emotional state"""




response = palm.generate_text(
    **defaults,
    prompt=prompt
)
print(response.result)

