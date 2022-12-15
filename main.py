from bs4 import BeautifulSoup as bs
import requests
from Models import *

page_number = 1
base_url = "https://jobinja.ir/jobs/latest-job-post-%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85%DB%8C-%D8%AC%D8%AF%DB%8C%D8%AF?&page={str(page_number)}&preferred_before=1670790452&sort_by=published_at_desc"


page = requests.get(base_url)

mapper = {"skill": "مهارت", "sex": "جنسیت", "license": "مدرک", "military": "وظیفه"}


soup = bs(page.content, "html.parser")

job_div = soup.find_all("div", class_="o-listView__itemInfo")


jobs = []

# check if job exist with url
check_if_job_exist = lambda url: Job.select().where(Job.link == url).exists()

for job_element in job_div:
    # print(job.prettify())
    title_element = job_element.find(
        "h3", class_="o-listView__itemTitle c-jobListView__title"
    )
    link_element = title_element.find("a")
    relative_date = title_element.span.text.replace("(", "").replace(")", "").strip()
    # print(relative_date)
    detail_element = job_element.find(
        "ul", class_="o-listView__itemComplementInfo c-jobListView__meta"
    )
    details = detail_element.find_all("li")

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




class htmlTags ():
    def __init__(self,name,class_) -> None:
        self.name = name
        self.class_ = class_

    def find_with_class(self, bs):
        tags = bs.find(self.name, class_=self.class_)


HTML_TAGS={
    "tag":"c-jobView__firstInfoBox c-infoBox"
}




for job in jobs:
    url = job.get_link()

    if check_if_job_exist(url):
        continue

    # print(url)
    job_page = requests.get(url)
    job_soup = bs(job_page.content, "html.parser")
    # a = "true" if "c-jobView__firstInfoBox" in job_page.content else "false"
    # print(a)
    # print(job_soup.contents)

    tags = job_soup.find("ul", class_=HTML_TAGS["tag"])
    # print(tags.text)
    tags = tags.find_all("li")

    category = tags[0].div.text.strip()
    minimum_years = tags[3].div.text.strip()
    salary = tags[4].div.text.strip()

    description = job_soup.find(
        "div", class_="o-box__text s-jobDesc c-pr40p"
    ).text.strip()

    compony_summary = job_soup.find_all("div", class_="o-box__text")[-1].text.strip()

    tags = job_soup.find_all("ul", class_="c-infoBox")[-1]
    tags = tags.find_all("li")

    military, skills, sex, license = "", "", "", ""

    for tag in tags:
        tag_text = tag.h4.text.strip()

        if mapper["skill"] in tag_text:
            skills = tag.div.text.strip()

        elif mapper["sex"] in tag_text:
            sex = tag.div.text.strip()

        elif mapper["military"] in tag_text:
            military = tag.div.text.strip()

        elif mapper["license"] in tag_text:
            license = tag.div.text.strip()

    complete_job = Job(
        title=job.get_title(),
        compony_name=job.get_compony_name(),
        location=job.get_location(),
        j_type=job.get_type(),
        link=job.get_link(),
        category=category,
        years=minimum_years,
        salary=salary,
        description=description,
        compony_summary=compony_summary,
        sex=sex,
        military=military,
        license=license,
    )
    complete_job.save()

    # print(url, category, minimum_years, salary, description, compony_summary, skills, sex, military, license, sep="\n\n")
    # print(job.title, job.get_compony_name(), job.get_location(), job.get_type(),sep="\n*")
