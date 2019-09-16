# Scrape Real Estate Website with 

Scrape all houses inforamtion for sale in Toronto from <link>https://www.rew.ca/properties/areas/toronto-on</link> with Scrapy Framework.

## Set Up
Create a virtual environment</br>
Install Scrapy Framework, PyMySQL, Scikit-learn, NumPy, Pandas and other dependencies from requirement.txt file

## Writing Scrapy Spider
<code>scrapy startproject rewhouse</code> <br>
<code>scrapy genspider -t basic rew www.rew.ca</code>

## Data Collection 
Getting data using PyMySQL and save in MySQL database <br>
Exporting scraped data as a json: <code>scrapy crawl rew -o rew_data.json</code>

## Data Preparation 
Transform raw data into to pandas series data, then clean it

## Data Processing

## Output
