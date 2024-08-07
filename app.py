import project_charter
import risk_management
import project_plan
import os
# configure palm, passing an API key
api_key=os.environ.get('PALM_API_KEY')

#user input
product_idea=input('What would you like to build?: ')

#generate project charter
project_charter_text=project_charter.generate(api_key,product_idea)

project_plan_text =project_plan.generate(api_key,project_charter)
#print(project_charter_text)

risk_management_text = risk_management.generate(api_key,project_charter)



#print(project_plan_text)

