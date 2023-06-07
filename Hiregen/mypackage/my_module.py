import streamlit as st
import requests
from streamlit_lottie import st_lottie
# import time
from bs4 import BeautifulSoup
import openai
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from docx import Document
import gradio as gr
import re
import json
def my_function():
    # description = st.text_area("Enter the description:", value=st.session_state.get("description", ""))
    description = """ The candidate should have 5+ Years of experience and should be responsible for software test automation design, planning, scripting and execution for a variety of key customer-facing and other mobile apps.

        The individual should be self-motivated, creative and proactive, to work successfully in a fast-paced environment including multiple platforms and architectures, diverse technologies and lab environments. The individual will work closely with developers, test engineers, project manager, Testing Head, client and other stakeholders throughout the SDLC, executing automated test iterations, tracking & reporting test results, troubleshooting and coordinating the bug fixes. The individual should have a strong understanding of agile processes and the related QA lifecycle and automation methodology. 

        Major Responsibilities: 

        Interact with product management, project management and development teams to develop a strong understanding of the project and testing objectives

        Should co-ordinate between onshore & offshore teams

        Participate in troubleshooting and triaging of issues with different teams to drive towards root cause identification and resolution

        Design and create test conditions, test data and test scripts to address business and technical use cases

        Use existing tools and techniques to execute test cases and build/script new tools for performing testing/validation function

        Develop and lead the automation strategy/effort and generate scripts to perform automated testing cycles using Selenium , Appium and Any of the performance testing tool.

        Design, Execute and analyze automation test scripts & test results for Web applications, iOS, Android & Windows Phone apps

        Document, track and escalate issues as appropriate, using JIRA

        Support during production deployment of applications and perform “validation testing” during the off-hours maintenance windows 

        Experience/Skills:

        Relevant work experience in development and/or testing role.

        Excellent verbal and written communication skills to co-ordinate efficiently with client, products, offshore & onshore teams and bridge the communication gaps

        Technical background and an understanding of the mobile apps & eco-system

        Good development/scripting skills in common languages which are Web-driver compatible language such as Java, Objective-C, JavaScript with Node.js, PHP, Python, Ruby, C#, or Perl with the Selenium WebDriver API and language-specific client libraries.

        Good experience with different Mobile Operating Systems (iOS, Android, Windows Phone)

        Expertise practical knowledge of automated testing tools Selenium & Appium

        Knowledge & Experience on JIRA tool is a must

        Knowledge on Selenium and Open STA or any other performance tools is a plus

        Must demonstrate an understanding of test automation frameworks

        Proven ability to manage and prioritize multiple, diverse projects simultaneously

        Must be flexible with working hours, independent and self-motivated

        Punctual, Regular and consistent attendance

        

        Education: 

        Bachelor’s degree ior higher.
    
    """
   
    job_tech =[]
    job1=[]
    job2=[]
    type_value = " "
  

    openai.api_key = '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'

    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Get the Job Role , Education , Place , Technologies & Skills , Experience , Job Type from Description:\n{description}\n",
    
    temperature=0.5,
    max_tokens=100,
    n=1,
    stop=None,
    timeout=10,
    
    )

    main_summary = response.choices[0].text.strip()

    print(main_summary)

    if main_summary != " ":       
        # Extract specific information using regular expressions
        job_role = re.search(r'Job Role:(.*)', main_summary).group(1).strip()
        education = re.search(r'Education:(.*)', main_summary).group(1).strip()
        place = re.search(r'Place:(.*)', main_summary).group(1).strip()
        technologies = re.search(r'Technologies & Skills:(.*)', main_summary).group(1).strip()
        experience = re.search(r'Experience:(.*)', main_summary).group(1).strip()
        # job_type = re.search(r'Job Type:(.*)', main_summary).group(1).strip()

        match = re.search(r'Job Type:(.*)', main_summary)
        if match:
            job_type = match.group(1).strip()
        else:
            job_type = "N/A"

        # Create a dictionary for the summary
        summary_dict = {
            'Job_Role': job_role,
            'Education': education,
            'Place': place,
            'Technologies': technologies,
            'Experience': experience,
            'Job_Type': job_type,
        }

        # Print the summary dictionary
        print(summary_dict)

        value1 = summary_dict.get("Job_Role")
        value2 = summary_dict.get("Education")
        value3 = summary_dict.get("Place")
        value4 = summary_dict.get("Technologies")
        value5 = summary_dict.get("Experience")
        value6 = summary_dict.get("Job_Type")



        if value1 != "N/A" and value1 !="Not Specified" and value1 != "None" and value1 != " ":
            role_values = word_tokenize(value1)
            stop_words =stopwords.words("english")
            stop_words.extend(['.',",",":",")",","])

            filtered_words = []
            for token in role_values:
                if token not in stop_words:
                    filtered_words.append(token)
            
            old_char = '/'
            new_char = '-'

            updated_list = []

            for string in filtered_words:
                updated_string = string.replace(old_char, new_char)
                updated_list.append(updated_string)
            job_tech.append(updated_list)
        else:
            pass


        # if value2 != "N/A" and value2 !="Not Specified" and value2 != "None" and value2 != " ":
        #     job.append(value2)
        # else:
        #     pass


        if value3 != "N/A" and value3 !="Not Specified" and value3 != "None" and value3 != " " and value3 != "undefined" and value3 != "Unknown ":
            place_values = word_tokenize(value3.lower())
            stop_words =stopwords.words("english")
            stop_words.extend(['.',",",":",")",",","any"])

            filtered_words1 = []
            for token in place_values:
                if token not in stop_words:
                    filtered_words1.append(token)
            
            old_char = '/'
            new_char = '-'
            updated_list1 = []

            for string in filtered_words1:
                updated_string = string.replace(old_char, new_char)
                updated_list1.append(updated_string)
            job1.append(updated_list1)
        else:
            pass


        if value4 != "N/A" and value4 !="Not Specified" and value4 != "None" and value4 != " ":
            tech_values = word_tokenize(value4)
            stop_words =stopwords.words("english")
            stop_words.extend(['.',",",":",")",",","("])

            filtered_words2 = []
            for token in tech_values:
                if token not in stop_words:
                    filtered_words2.append(token)

            old_char = '/'
            new_char = '-'

            updated_list2 =[]
            for string in filtered_words2:
                updated_string1 = string.replace(old_char, new_char)
                updated_list2.append(updated_string1)
            job_tech.append(updated_list2)
        else:
            pass

        if value5 != "N/A" and value5 !="Not Specified" and value5 != "None" and value5 != " " and value5 !="0":

            pattern = r"(?i)(?:(\d+(?:\.\d+)?|\d+\+?)\s*(?:years|yrs|yr.|years of experience))|(?:\b(\w+)\s+years\s+of\s+experience\b)"
        
            matches = re.findall(pattern, value5)
            
            numeric_matches = [match[0] for match in matches if match[0]]
            word_matches = [match[1] for match in matches if match[1]]
            
            totals = numeric_matches + word_matches

            print("lalitha")
            print(totals)
            print("lalitha")

            flattened3 = []
            for item in totals:
                if isinstance(item, list):
                    flattened3.extend(item)
                else:
                    flattened3.append(item)
            print(flattened3)
            string_result = str(flattened3)
            print(string_result)
            if string_result != " ":
                if string_result != "0" and string_result < "3.1":
                    string_result = float(string_result)
                    string_result = string_result*12
                    exp=int(string_result)
                    print(exp)
                else:
                    exp=500
        else:
            pass


        if value6 != "N/A" and value6 != "Not Specified" and value6 != "None" and value6 != " "and value6 != "None Specified":
            value6 = value6.lower()
            if value6 == "full time" or value6 == "Full-time":
                type_value = 1
            elif value6 == "part time":
                type_value = 2
            elif value6 == "internship":
                type_value = 3
            elif value6 == "apprenticeship":
                type_value = 6
            else:
                type_value = 0
        else:
            pass
        # print(job)

        flattened = []
        for item in job_tech:
            if isinstance(item, list):
                flattened.extend(item)
            else:
                flattened.append(item)
        print(flattened)
        joined_string = '-'.join(str(element) for element in flattened)
        joined_string = joined_string.lower()
        print(joined_string)

        flattened1 = []
        for item in job1:
            if isinstance(item, list):
                flattened1.extend(item)
            else:
                flattened1.append(item)


        print(flattened1)
        joined_string1 = '-'.join(str(element) for element in flattened1)
        joined_string1 = joined_string1.lower()
        print(joined_string1)

        # if joined_string and joined_string1 and exp and type_value :
        #     url = "\n".join([f"https://www.freshersworld.com/jobs/jobsearch/{joined_string}-jobs-in-{joined_string1}?experience={exp}&job_type={type_value}".format(joined_string,joined_string1,string_result,type_value)])
        # if joined_string and joined_string1 and exp :
        #     url = "\n".join([f"https://www.freshersworld.com/jobs/jobsearch/{joined_string}-jobs-in-{joined_string1}?experience={exp}".format(joined_string,joined_string1,string_result)])
        if joined_string and joined_string1 :
            url = "\n".join([f"https://www.freshersworld.com/jobs/jobsearch/{joined_string}-jobs-in-{joined_string1}".format(joined_string,joined_string1)])
        elif joined_string :
            url = "\n".join([f"https://www.freshersworld.com/jobs/jobsearch/{joined_string}-jobs".format(joined_string)])
        else:
            print("Give some detailed information")
        print(url)
    else:
        print("Give some detailed information")  
        


    # url = "https://www.freshersworld.com/jobs/jobsearch/"+a[0]+"-"+a[1]+"-jobs-for-"+a[2]+"-in-"+a[3]+"?course=16"

    print(url)
    response = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(response.content, 'html.parser')
    job_listings = soup.find_all('div', class_='job-container')

    for job in job_listings:
        job_title = job.find('span', class_='wrap-title').text
        company_name = job.find('h3', class_='latest-jobs-title font-16 margin-none inline-block company-name').text
        job_location = job.find('span', class_='job-location display-block modal-open job-details-span').text
        qualifications = job.find('span', class_='qualifications display-block modal-open pull-left job-details-span').text

        view_apply_button = job.find('span', class_='view-apply-button')
        view_apply_link = ''
        if view_apply_button:
            parent_div = view_apply_button.find_parent('div', class_='job-container')
            if parent_div:
                view_apply_link = parent_div.get('job_display_url', '')

            print(job_title[:-4].rstrip())
            results = [job_title[:-4].rstrip(),company_name,job_location,qualifications,view_apply_link]
            print(results)
            return results 