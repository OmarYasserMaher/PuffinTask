from bs4 import BeautifulSoup
import requests

def scrape_yahoo_finance():
    """
    Scrapes yahoo finance for crypto data
    """
    count = 250
    offset = 0

    url = "https://finance.yahoo.com/crypto/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    #get number of results
    num_results = soup.find('span', attrs={'class':'Mstart(15px) Fw(500) Fz(s)'}).text
    num_results = int(num_results.split(' ')[-2])
    headers = []
    for header in soup.find_all('th'):
        headers.append(header.text)

    
    #loop through pages
    while offset < num_results:
        data = []
        url = f"https://finance.yahoo.com/crypto/?count={count}&offset={offset}"
        yahoo_headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
        html = requests.get(url,headers=yahoo_headers,allow_redirects=False).text
        soup = BeautifulSoup(html, 'html.parser')

        for row in soup.find_all('tr', attrs={'class':'simpTblRow'}):
            row_data = {}
            for i, td in enumerate(row.find_all('td')):
                #ignoring chart data
                if td.text:
                    row_data[headers[i]] = td.text 
            data.append(row_data)
        offset += count
        yield data
