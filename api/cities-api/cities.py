import csv
import json
import unicodedata

cities = {
    'cities': []
}


# Opens csv file
def open_csv():
    with open('cities.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Convert to unicode format
            unicode_city = unicode(row[0], 'utf-8')
            # print(unicode_city)

            # Convert to normal characters
            normalised_cities = unicodedata.normalize('NFKD', unicode_city).encode('ascii', 'ignore')
            cities['cities'].append(normalised_cities)
        return cities


def write_to_file():
    with open('cities.json', 'w') as csvjsonfile:
        json.dump(str(open_csv()), csvjsonfile)
        print('Written to cities file')


def read_from_json():
    with open('cities.json') as json_data:
        data = json.load(json_data)
        print(data)

write_to_file()
