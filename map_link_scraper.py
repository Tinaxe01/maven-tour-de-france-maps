import requests
from bs4 import BeautifulSoup


def get_tour_de_france_map_link(year):
    # Construct the URL for the Wikipedia page of the specific year
    url = f"https://en.wikipedia.org/wiki/{year}_Tour_de_France"
    # Send a request to the webpage
    response = requests.get(url)
    if response.status_code == 200:
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the map image element using CSS selector or other suitable method
        for data in soup.find_all('td', class_='infobox-image'):
            for url in data.find_all('img'):
                return 'https:' + url.get('src')
        return None


# Example usage:
year = 2018
map_link = get_tour_de_france_map_link(year)
print(map_link)


if __name__ == '__main__':
    get_tour_de_france_map_link(year)