import utils
import read_csv
import charts

def run():
  data, header = read_csv.read_csv('./chocolate-data.csv')
  newZeland = list(filter(lambda x: x['Geography'] == 'UK', data))
  print(len(newZeland))
  print(read_csv.countries)
  #Pie chart of total units of chocolate per country
  chocolateCountry = chocolate_per_country(data,read_csv.countries)
  x = list(chocolateCountry.keys())
  y = list(chocolateCountry.values())
  charts.generate_pie_chart(x,y,'chocolate-pie-per-country.png')
  
def chocolate_per_country(data, countries):
  chocolatePerCountry = {key: 0 for key in countries}
  for line in data:
    chocolatePerCountry[line['Geography']] += int(line['Units'])
  return chocolatePerCountry
  #x = list(read_csv.chocolates.keys())
  #y = list(read_csv.chocolates.values())
  #charts.generate_bar_chart(x,y)
  '''
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  '''
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  '''

if __name__ == '__main__':
  run()