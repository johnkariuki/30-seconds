import csv
import json
import unicodedata

currency = {
    'currency': []
}


# Opens csv file
def open_csv():
    with open('currency.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Convert to unicode format
            unicode_city = unicode(row[1], 'utf-8')
            # print(unicode_city)

            # Convert to normal characters
            normalised_currency = unicodedata.normalize('NFKD', unicode_city).encode('ascii', 'ignore')
            currency['currency'].append(normalised_currency)
        return currency


def write_to_file():
    with open('currency.json', 'w') as csvjsonfile:
        json.dump(str(open_csv()), csvjsonfile)
        print('Written to currency file')


def read_from_json():
    with open('currency.json') as json_data:
        data = json.load(json_data)
        print(data)

write_to_file()
