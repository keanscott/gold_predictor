## Gold - An analysis of the macroeconomic effects on the price of gold

### Intro
This project will follow a typical data science life cycle in order to explore and analyse data relating to the price of the commodity gold. I will collect data from numerous souces, employing web scraping techniques where possible over directly downloading the data in tabular format.

Below is a rough plan:

#### 1. Project Planning and Design (Completed)

##### Scope and Key Goals:
    
- Identify key economic factors that influence gold price trends.
- Create a predictive model to forecast the price of gold in the future (1 month)

##### Identify Data Sources
    
- Explore options for collecting data, APIs and web scraping

#### 2. Data Scraping (In Progress)
    
- Use Python to query and scrape data
    - Code contained in `data_collection/scrape_data.py` scrapes web for CPI and S&P500 data, outputting to a CSV.
    - Did not scrape the rest of the data in `data` folder as sources did not allow for such methods, rather downloaded as CSV. 

#### 3. Data Cleaning & Preprocessing (In Progress)

- Handle missing values + outliers
- Merge and align the various data sources
- Feature engineering?

#### 4. Exploratory Data Analysis (**EDA**)

- Statistical summaries
- Time series analysis
- Visualise relationships
- Identify key events

#### 5. Data Visualisation

- Create an interactive dashboard using Tableau

#### 6. Model Building & Forecasting

- Explore a variety of techniques, including classical statistical models and machine learning
- Feature selection
- Model evaluation: make a training testing split to test performance agaisnt real outcomes
- Visualise the forecast

