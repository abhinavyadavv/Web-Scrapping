from bs4 import BeautifulSoup
import requests
import pandas as pd  # Import pandas library
import time
# Request library is used to request information from a specific website

print('Put Some Skill That You Are Not Familiar With')
unfamiliar_skill = input('>')
print(f'Filtering Out {unfamiliar_skill}')

# Create a list to store scraped data
job_data = [] 

def find_jobs():
    html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

    # print(html_text),we will get reponse 200 which means request is done successfully,in order to get html text,and avoid status code we will write .text in the end of the url
    # print(html_text)

    soup= BeautifulSoup(html_text,'lxml')

    jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    # print(job)
# The enumerate() function in Python is used to iterate over elements of an iterable (such as a list, tuple, or 
# string) while keeping track of the index of the current element. It's a convenient way to access both the index 
# and value of each item in the iterable during a loop. The primary purpose of enumerate() is to simplify tasks 
# where you need to associate each element with its position in the iterable.

    for index, job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date: #This line will allow us to get the posts with few days ago
            company_name=job.find('h3',class_="joblist-comp-name").text.replace(' ','')
            skills= job.find('span',class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open('posts/{index.txt}','w') as f:
                # print(skills)
                # print(company_name)
                    job_data.append({
                    'Company Name': company_name.strip(),
                    'Skills Required': skills.strip(),
                    'More Info': more_info,
                })
                print(f"Data Added for Job {index}: {company_name.strip()}")
                    
    # Create a DataFrame from the job data
    df = pd.DataFrame(job_data)   
    
    # Export the DataFrame to an Excel file
    df.to_excel('job_data.xlsx', index=False)
    print("Data saved to job_data.xlsx")
        
if __name__ == '__main__':
    find_jobs()

            


