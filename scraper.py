from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    #Makes HTTP GET request to passed url, returns raw content
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during request to {0} : {1}'.format(url, str(e)))
        return None

def get_companies():
    #Extracts company info from website and returns a list

    url="https://intern.supply"
    response = simple_get(url)
    companies = set()

    if response is not None: 
        html = BeautifulSoup(response, 'html.parser')
        #Adds sub title text as well, need to clean up select
        for p in html.select('p'):
            if 'title' in p['class']:
                companies.add(p.text)
    return list(companies)
    
def is_good_response(resp):
    #Returns true if reponse is HTML, false otherwise
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1 )


def log_error(e):
    #Prints errors
    print(e)

if __name__ == '__main__':
    print(get_companies())
