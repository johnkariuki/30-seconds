import csv
import json
import unicodedata

continents = {
    'continents': []
}


# Opens csv file
def open_csv():
    with open('continents.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Convert to unicode format
            unicode_continent = unicode(row[1], 'utf-8')
            # print(unicode_continent)

            # Convert to normal characters
            normalised_continents = unicodedata.normalize('NFKD', unicode_continent).encode('ascii', 'ignore')
            continents['continents'].append(normalised_continents)
        return continents


def write_to_file():
    with open('continents.json', 'w') as csvjsonfile:
        json.dump(str(open_csv()), csvjsonfile)
        print('Written to continents file')


def read_from_json():
    with open('continents.json') as json_data:
        data = json.load(json_data)
        print(data)

write_to_file()
