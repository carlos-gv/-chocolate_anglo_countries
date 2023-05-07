import csv
chocolates = {'Milk Bars': 0, 'Peanut Butter Cubes': 0, 'Manuka Honey Choco': 0, 'Orange Choco': 0, 'Choco Coated Almonds': 0, 'Almond Choco': 0, 'White Choc': 0, "Baker's Choco Chips": 0, '99% Dark & Pure': 0, 'Drinking Coco': 0, '85% Dark Bars': 0, 'Fruit & Nut Bars': 0, 'Eclairs': 0, 'After Nines': 0, '50% Dark Bites': 0, 'Caramel Stuffed Bars': 0, 'Raspberry Choco': 0, 'Mint Chip Choco': 0, 'Smooth Sliky Salty': 0, '70% Dark Bites': 0, 'Organic Choco Syrup': 0, 'Spicy Special Slims': 0}
countries = set()

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      chocolates[country_dict['Product']] += 1 
      countries.add(country_dict['Geography'])
      data.append(country_dict)
    return data,header

if __name__ == '__main__':
  data, header = read_csv('./chocolate-data.csv')
  print(header)
  print(data[0])
  print()
  print(chocolates)
