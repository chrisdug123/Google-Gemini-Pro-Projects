import google.generativeai as palm

# configure palm, passing an API key

palm.configure(api_key="AIzaSyDt5k8lt-guTy39a-okCbxOOoUyxG3ErVQ")

# prompting!
my_promt="how many planets are there in our solar system"

response = palm.generate_text(prompt=my_promt)

# display response

print(response.result)