import csv
from map_link_scraper import get_tour_de_france_map_link

tour_de_france_map_data = []
for year in range(2020, 2024):
    map_data = {
        'Year': year,
        'Map URL': get_tour_de_france_map_link(year)
    }
    tour_de_france_map_data.append(map_data)

# Define path to csv file
csv_file = 'tour_de_france_map_data.csv'

# Write the data to the csv file
with open(csv_file, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=['Year', 'Map URL'])
    writer.writeheader()
    writer.writerows(tour_de_france_map_data)

print(f'Data saved to {csv_file}')
