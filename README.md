# jobsdb-scraper
This is a Python script project that allows you to scrape job listings from hk.jobsdb.com based on a search keyword and store the data in a structured format using Pandas.

## Getting Started 

### Prerequisites 
Before running the script, ensure you have the following libraries installed:

* BeautifulSoup4
* Requests
* Pandas

You can install these libraries using pip:

```bash
pip install beautifulsoup4 requests pandas
```

## How to Use 
1- Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/hk-jobsdb-scraper.git
cd hk-jobsdb-scraper
```
2- Run the script:
```bash
python jobsdb_scraper.py
```
3- The script will prompt you to enter a search keyword for the job listings. Enter the keyword and press Enter.
4- The script will start scraping the job listings from hk.jobsdb.com based on the provided keyword.
5- Once the scraping process is complete, the data will be saved to a CSV file named job_listings.csv in the project directory.
6- You can open the job_listings.csv file with any spreadsheet software like Microsoft Excel or Google Sheets to view the scraped data.

## Notes 
* The script may take some time to scrape all the job listings, depending on the number of results and the website's response time.
* Please be considerate while scraping data from websites and avoid making too many requests in a short period to prevent overloading the server.
* This script is provided for educational purposes and personal use. Be sure to review the terms of service of hk.jobsdb.com or any website you intend to scrape to ensure compliance with their policies

## License 
This project is licensed under the MIT License - see the LICENSE file for details.

