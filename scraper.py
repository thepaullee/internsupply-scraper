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
        
    
def is_good_response(rep):
    #Returns true if reponse is HTML, false otherwise
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 && content_type is not None && content_type.find('html') > -1 )


def log_error(e):
    #Prints errors
    print(e)