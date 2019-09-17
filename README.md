# Scrape Real Estate Website and House Prices Prediction Using KNN and SVM Algorithm

Scrape all houses information for sale in Toronto from <link>https://www.rew.ca/properties/areas/toronto-on</link> with Scrapy Framework, then built KNN and SVM models to predicting house price.

## Set Up
Create a virtual environment</br>
Install Scrapy Framework, PyMySQL, Scikit-learn, NumPy, Pandas, Jupyter and other dependencies from requirement.txt file

## Writing Scrapy Spider
<code>scrapy startproject rewhouse</code> <br>
<code>scrapy genspider -t basic rew www.rew.ca</code>

## Data Collection 
Getting data using PyMySQL and save in MySQL database <br>
Exporting scraped data as a json: <code>scrapy crawl rew -o rew_data.json</code>

## Data Preparation 
Transform raw data into to NumPy ndarray data, then clean independent variables and dependent variables

## Data Processing
Splitting the dataset into the Training and Test set <br>
Feature Scaling <br>
Fitting KNN and SVM model <br>
Predicting the test set <br>

## Output
Evaluating model <br>
Getting accuracy score for KNN model: 0.66666666666666667 <br>
Getting accuracy score for SVM model: 0.93333333333333334 <br>
