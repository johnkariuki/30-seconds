import csv
import json
import unicodedata

countries = {
    'countries': []
}


# Opens csv file
def open_csv():
    with open('countries.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Convert to unicode format
            unicode_country = unicode(row[1], 'utf-8')
            # print(unicode_country)

            # Convert to normal characters
            normalised_countries = unicodedata.normalize('NFKD', unicode_country).encode('ascii', 'ignore')
            if normalised_countries not in countries['countries']:
                countries['countries'].append(normalised_countries)
            else:
                countries['countries'] = countries['countries']
        return countries


def write_to_file():
    with open('countries.json', 'w') as csvjsonfile:
        json.dump(str(open_csv()), csvjsonfile)
        print('Written to countries file')


def read_from_json():
    with open('countries.json') as json_data:
        data = json.load(json_data)
        print(data)

write_to_file()
