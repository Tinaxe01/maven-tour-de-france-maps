**Tour de France Wikipedia Routes Scraper**  

This Python script is designed to scrape Tour de France Wikipedia routes and extract the necessary information for use in Power BI. It utilizes the Beautiful Soup, CSV, and Requests libraries to perform the scraping and data extraction tasks.

The script fetches the route details from the relevant Tour de France Wikipedia pages using the requests library to make HTTP requests. The HTML content of the pages is then parsed and navigated using the Beautiful Soup library, allowing the script to extract specific data points such as start and finish locations, distances, and notable landmarks.

The scraped data is then processed and saved in a CSV (Comma-Separated Values) format. The CSV file can be easily imported into Power BI for further analysis and visualization.

**Installation**
Before running the script, ensure that you have the required libraries installed. You can install them using pip, the Python package manager, by running the following command:
pip install beautifulsoup4 csv requests

**Usage**
To run the script, follow these steps:

Open a terminal or command prompt.
Navigate to the directory where the script is located.
Execute the script by running the following command:
python tour_de_france_scraper.py


The script will start scraping the Tour de France Wikipedia routes and output the extracted data into a CSV file.

**Output**
The script saves the scraped data into a CSV file named "tour_de_france_routes.csv". Each row in the CSV represents a route and includes details such as the start and finish locations, distances, and notable landmarks along the route.

**Credits**
This script utilizes the following libraries:

Beautiful Soup:[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
CSV: Python's built-in CSV module
Requests: [Requests](https://requests.readthedocs.io/)
**License**
This project is licensed under the MIT License. See the LICENSE file for more information.

**Contact**
If you have any questions, suggestions, or feedback, feel free to contact [email](chinyatitb1@gmail.com).
