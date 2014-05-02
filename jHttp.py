import requests

def get_url_content(site_url):
    r = requests.get(site_url)
    print r.status_code
    content = r.text.encode('utf-8', 'ignore')
    return content