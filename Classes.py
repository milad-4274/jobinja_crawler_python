

class BriefJob():
    def __init__(self, title : str, company_name: str, location: str, type: str, link: str):
        self.title = title
        self.company_name = company_name
        self.location = location
        self.type = type
        self.link = link
    
    def get_title(self):
        return self.title

    def get_compony_name(self):
        return self.company_name

    def get_location(self):
        return self.location
    
    def get_type(self):
        return self.type

    def get_link(self):
        return self.link
    

class Job():
    def __init__(self,brief: BriefJob, category: str, minimum_years: str, salary: str, description, compony_summary, skills, sex, military_status, minimum_license) -> None:
        self.brief = brief
        self.category = category
        self.minimum_years = minimum_years
        self.salary = salary
        self.description = description
        self.compony_summary = compony_summary
        self.skills = skills
        self.sex = sex
        self.military_status = military_status
        self.license = minimum_license
    

