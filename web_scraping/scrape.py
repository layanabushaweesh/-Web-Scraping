from bs4 import BeautifulSoup
import requests

URL='https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(URL):

    """
    this function takes in 
    a url and returns an integer
    that represent to how many citations needed

    """
    pages=requests.get(URL)
    soup=BeautifulSoup(pages.content,'html.parser')
    data=soup.find_all('a' , href="/wiki/Wikipedia:Citation_needed" )
    
    print(f"{len(data)}  number of citations needed")
    
    return len(data)

get_citations_needed_count(URL)

def get_citations_needed_report(URL):

    """
    this function  takes in a url and returns a string
    the string should be formatted with each citation 
    needed on own line, in order found

    """
    pages=requests.get(URL)
    soup=BeautifulSoup(pages.content,'html.parser')
    datas=soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
   
    need_data = ''
    for data  in datas:
        need_data = need_data + f'{data.parent.text.strip()}'
    return need_data
print(get_citations_needed_report(URL))


    
