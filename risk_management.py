import google.generativeai as palm
from Markdown2docx import Markdown2docx



def generate( api_key,project_charter):
    palm.configure(api_key= api_key)
    defaults = {
        'temperature' : 0.7,
        'candidate_count':1,
        'top_k':40,
        'top_p': 0.95,
        'max_output_tokens': 1024,
        'stop_sequences':[],
        #'safety_settings':[{"category":"HARM_CATEGORY_HARASSMENT","threshold":1},{"category":"HARM_CATEGORY_HATE_SPEECH","threshold":1},{"category":"HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold":1},{"category":"HARM_CATEGORY_DANEROUS_CONTENT","threshold":2}]
    }
    # prompting!

    #product_idea=input()
    prompt = f"""Act as a senior project manager with experience in software project. Write a Risk Management Plan that identifies, assesses, and outlines strategies to manage risks in the project, based on the following Project Charter:
    {project_charter}
    """
   
    response = palm.generate_text(
        **defaults,
        prompt=prompt )
    
    # save that as a Word document
    my_file = open('risk_management.md', 'w')
    my_file.write(response.result)
    my_file.close()

    word_file=Markdown2docx('risk_management')
    word_file.eat_soup()
    word_file.write_html()
    word_file.save()
    return response.result




