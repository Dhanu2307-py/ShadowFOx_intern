from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchName=recentSearches&from=submit&luceneResultSize=25&txtKeywords=Python&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=Python&searchBy=0&rdoOperator=OR&gadLink=Python')
soup = BeautifulSoup(html_text.content, 'lxml')


def scrap():
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = soup.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            com_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_about_job = job.header.h2.a['href']
            print(
                f"Company Name: {com_name.strip()} \nSkills Required: {skills.strip()} \nMore about the job: {more_about_job.strip()}")

            print(' ')


if __name__ == '__main__':
    scrap()
