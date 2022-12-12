from Models import *


jobs = list(Job.select())
for job in jobs:
    # print(job)
    print(job.title)
    print(job.compony_name)
    print(job.location)
    print(job.j_type)
    print(job.link)
    print(job.category)
    print(job.years)
    print(job.salary)
    print(job.description)
    print(job.compony_summary)
    print(job.sex)
    print(job.military)
    print(job.license)
    print("_______________________________")