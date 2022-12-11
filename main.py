from bs4 import BeautifulSoup as bs
import requests
from Models import *

page_number = 1
base_url = "https://jobinja.ir/jobs/latest-job-post-%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85%DB%8C-%D8%AC%D8%AF%DB%8C%D8%AF?&page={str(page_number)}&preferred_before=1670790452&sort_by=published_at_desc"


page = requests.get(base_url)


soup  = bs(page.content, "html.parser")

job_div = soup.find_all("div",class_="o-listView__itemInfo")


jobs = []
for job_element in job_div:
    # print(job.prettify())
    title_element = job_element.find("h3", class_="o-listView__itemTitle c-jobListView__title")
    link_element = title_element.find("a")
    detail_element = job_element.find("ul",class_="o-listView__itemComplementInfo c-jobListView__meta")
    details =  detail_element.find_all("li")
   
    title = link_element.text.strip()
    compony_name = details[0].text.strip()
    location = details[1].text.strip()
    type = details[2].span.span.text.strip()
    link = link_element["href"]

    job = BriefJob(title, compony_name, location, type, link)
    jobs.append(job)

    # print(link_element.prettify(), end="\n\n")

# print(soup)
print(len(jobs))

for job in jobs[:1]:
    url = job.get_link()
    print(url)
    job_page = requests.get(base_url)
    job_soup = bs(job_page.content, "html.parser")
    # a = "true" if "c-jobView__firstInfoBox" in job_page.content else "false"
    # print(a)
    tags = job_soup.find("ul",class_="c-jobView__firstInfoBox c-infoBox")
    print(tags.text)
    tags = tags.find_all("li")
    
    category = tags[0].div.text
    minimum_years = tags[3].div.text
    salary = tags[4].div.text
    
    description = job_soup.find("div",class_="o-box__text s-jobDesc c-pr40p").text

    compony_summary = job_soup.find("div",class_="o-box__text")

    tags = job_soup.find("ul",class_="c-infoBox")
    tags = tags.find_all("li")

    skills = tags[0].div.text
    sex = tags[1].div.text
    military = tags[2].div.text
    license = tags[3].div.text

    print(url, category, minimum_years, salary, description, compony_summary, skills, sex, military, license, sep="\n\n")



