# Web Scraping Russian Coin Data from livecoin.net Using the Wayback Machine

This project utilizes web scraping techniques to extract Russian coin data from the livecoin.net website using the Wayback Machine. The website's content is rendered using JavaScript, requiring the use of Selenium's ChromeDriver to obtain the dynamic page source. The Scrapy framework is then employed to parse the HTML and extract the necessary data.

## Prerequisites
- Python
- Scrapy
- Selenium
- ChromeDriver
- Wayback Machine API (optional)

## Installation
1. Install Python (if not already installed): Python Official Website
2. Install Scrapy: pip install scrapy
3. Install Selenium: pip install selenium
4. Download and install ChromeDriver: ChromeDriver Official Website

## Usage
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the Scrapy spider to scrape data: scrapy crawl russian_coin_spider
4. The scraped data will be saved as a JSON file in the output directory.

## How It Works
1. Selenium with ChromeDriver: Selenium is used to automate the web browser and access the livecoin.net website. ChromeDriver is utilized to interact with Google Chrome and retrieve the dynamically generated content of the website.

2. Scrapy for HTML Parsing: Once the page source is obtained, Scrapy's Selector is used to parse the HTML and extract the required data. XPath expressions are employed to locate specific elements containing the Russian coin data.

3. Saving Scraped Data: The extracted data is then saved as a JSON file for further analysis or usage.

## About the Project
This project aims to provide a method for retrieving Russian coin data from the livecoin.net website, even when the original site is unavailable. By utilizing the Wayback Machine, historical snapshots of the website are accessed, ensuring the availability of the required data.

## Future Improvements
- Implement error handling for potential issues during web scraping.
- Enhance data extraction techniques for improved accuracy and efficiency.
- Integrate the Wayback Machine API for streamlined access to archived web pages.

## Acknowledgments
Special thanks to the developers of Scrapy and Selenium for providing powerful tools for web scraping and automation. Appreciation also goes to the Wayback Machine team for archiving internet content and making it accessible for historical analysis.

### website view

![image](https://github.com/FaeyO/webscrapping-livecoin.com/assets/118575325/bbcf6a66-4026-492b-9a4e-8aa9c1fee19c)
