import pandas as pd
import requests
import urllib
from bs4 import BeautifulSoup, SoupStrainer

cpi_url = "https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/"

# Define header to tell website we're a genuine user
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

def get_cpi_data(url):
    """ 
    * Scrapes html from usinflationcalculator.com and parses table to get data.
    * Output: pandas dataframe of scraped CPI data
    """
    r = requests.get(url=url, headers=headers)
    print(r)
    if r.status_code == 200:
        try:
            tr_tags = SoupStrainer("tr")
            # Parse html to find table             
            table = BeautifulSoup(r.text, "html.parser", parse_only=tr_tags)
            rows = table.find_all("tr")

            # Process table data
            clean_data = []
            for row in rows:
                cols = row.find_all("td")
                cols = [col.get_text(strip=True) for col in cols]
                if cols:
                    clean_data.append(cols)
            col_names = clean_data[1]
            clean_data = clean_data[2:]

            # Convert data to pandas DataFrame
            df = pd.DataFrame(clean_data, columns=col_names)

            return df
        
        except:
            ValueError("incorrect url")