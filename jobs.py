from bs4 import BeautifulSoup
import requests 
import pandas as pd 
import re 


def info_extractor(keyword:str,page_number:int,container:dict):
    search_template = 'https://hk.jobsdb.com/hk/search-jobs/{}/{}'
    url = search_template.format(keyword,page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    jobs = soup.find_all('article')
    for job_id,job in enumerate(jobs) :
        print('the job id is : {}'.format(job_id))
        title = job.find('div',attrs={"class":"FYwKg _2j8fZ_0 sIMFL_0 _1JtWu_0"}).get_text()
        try:
            salary = job.find_all('span',attrs={"class":'FYwKg _2Bz3E C6ZIU_0 _1_nER_0 _2DNlq_0 sQuda_0'})[1].get_text()
        except:
            salary = 'not available'
        print('the job title is : {}'.format(title))
        try:
            company = job.find('span',attrs={'class':'FYwKg _2Bz3E C6ZIU_0 _6ufcS_0 _2DNlq_0 _29m7__0'}).get_text()
        except:
            company= 'Company Confidential'
        description = [ point.get_text() for point in job.find_all('li',attrs={'class':'FYwKg zoxBO_0'})]
        container.append({
             'title':title,
             'salary':salary,
             'company':company, 
             'description':description
        })


def get_page_count(keyword:str) -> int:
    url = 'https://hk.jobsdb.com/hk/search-jobs/{}/1'.format(keyword)
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    jobs_count = soup.find('span',attrs={'class':'FYwKg _2Bz3E C6ZIU_0 _1_nER_0 _2DNlq_0 _29m7__0 _1PM5y_0'}).get_text()
    jobs_count = re.findall(r'\d+',jobs_count)[-1]
    if (int(jobs_count)/30).is_integer():
        page_count = int(jobs_count)/30
    else:
        page_count = int(jobs_count)//30 + 1
    return page_count 


def main():
    jobs_details = list() 
    keyword = input('Enter the keyword : ')
    page_count = get_page_count(keyword)
    for page_id in range(1,page_count+1):
        print('page number : {}'.format(page_id))
        info_extractor(keyword,page_id,jobs_details)
    jobs = pd.DataFrame(jobs_details)
    jobs.to_csv('jobs.csv')


if __name__ == '__main__':
    main()
