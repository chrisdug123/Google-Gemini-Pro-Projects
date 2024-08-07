import google.generativeai as palm
from Markdown2docx import Markdown2docx
# capture user input

#product_idea=input('What would you like to build?: ')


def generate( api_key,product_idea):
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
    prompt = f"""Act as a senior project manager with vast experience in software development. Write a brief Project Charter documentfor our product idea, The Project Charter should include the following sections:

    1) Project Title and Description
    2) Project urpose or Justification
    3) Objectives and COntraints
    4) Scope Description
    5) Project Deliverables
    6) Project BUdget
    7) Stakeholder Identification
    8) High - Level Risks and Assumptions 

    Our product idea is: {product_idea}

    Now please write the Project Charter with the 8 sections mentioned above: """


    response = palm.generate_text(
        **defaults,
        prompt=prompt )

    # save that as a Word document
    my_file = open('project_charter.md', 'w')
    my_file.write(response.result)
    my_file.close()

    word_file=Markdown2docx('project_charter')
    word_file.eat_soup()
    word_file.save()

    return response.result


#generate project charter
