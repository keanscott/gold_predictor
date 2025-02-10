import pandas as pd
import requests
from bs4 import BeautifulSoup, SoupStrainer

cpi_url = "https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/"
sp500_url = "https://finance.yahoo.com/quote/%5EGSPC/history/?frequency=1mo&period1=631152000&period2=1738454400"
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


def get_sp500_data(url):
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        try:
            tr_tags = SoupStrainer("tr") # Table rows
            th_tags = SoupStrainer("th") # Table head for column names

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
            
            # Find table column names
            table_head = BeautifulSoup(r.text, "html.parser", parse_only=th_tags)

            heads = table_head.find_all("th")
            col_names = [head.get_text(strip=True) for head in heads]
        
            # Convert data to pandas DataFrame
            df = pd.DataFrame(clean_data, columns=col_names)
            return df
        except:
            ValueError("incorrect url")


def main():
    cpi_data = get_cpi_data(url=cpi_url)
    cpi_data.to_csv("./data/cpi_data.csv", index=False)

    sp500_data = get_sp500_data(url=sp500_url)
    sp500_data.to_csv("./data/sp500_data.csv", index=False)


if __name__ == '__main__':
    main()