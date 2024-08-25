import pandas as pd
import re
from typing import Match

# Load the resume dataset from a CSV file into a DataFrame
resumes: pd.DataFrame = pd.read_csv('resumes.csv')

# Define regex
jobs_regex = r"^([A-Z\s\.\,\-]+)\b" 
skills_regex = r"\b(python|sql|r|excel)\b"
edu_regex = r"\b(PhD|Master|Bachelor)\b"

# Lists to store extracted data
job_titles: list[str] = []
tech_skills: list[str] = []
education: list[str] = []

# functions to extract data
def get_job_title(resume: str) -> Match[str] | None:
    """Extract job titles from a string column."""

    return re.search(jobs_regex, resume)
    

def get_skills(resume: str) -> list[str]:
    """Get a list of skills from a string."""

    return re.findall(skills_regex, resume, flags=re.IGNORECASE)


def get_education(resume: str) -> list[str]:
    """Get a list of education history."""
    
    return re.findall(edu_regex, resume, flags=re.IGNORECASE)

# Extract data and add to lists
for resume in resumes['Resume_str']:

    # extract job titles
    jobs_match = get_job_title(resume)
    
    # if a job title is found, add to the list
    if jobs_match is not None:
        job_titles.append(jobs_match.group(0).strip())
    else:
        job_titles.append("")
   
    # extract tech skills
    skills = set([skill.title() for skill in get_skills(resume)])
    tech_skills.append(", ".join(skills))
    
    # extract education history
    education_history = set([education.title() for education in get_education(resume)])
    education.append(", ".join(education_history))

# Add extracted data as columns to resumes df
resumes['job_titles'] = job_titles
resumes['tech_skills'] = tech_skills
resumes['education'] = education

# Filter a copy of the df
filtered_df = resumes[(resumes['job_titles'] != "") & (resumes['tech_skills'] != "") & (resumes['education'] != "")]

# Create a new df w/ only the columns required
candidates_df = filtered_df[['ID', 'job_titles', 'tech_skills', 'education']]

# ensure column names are lower case
candidates_df.columns = candidates_df.columns.str.lower()

# drop Null values
candidates_df.dropna()

# display the df
print(candidates_df.head())
