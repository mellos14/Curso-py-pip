import utils
import read_csv
import charts


# Dualidad de los modulos
# Ejecutarse como Script desde la terminal
# Ser llamados con import a otro archivo
# IF COMUN --> if __name__ == "__main__" --> ejecuta el script



def run():

    data = read_csv.read_csv("./data.csv")

    country = input("type country --> ")
    data = list(filter(lambda item: item['Continent']== 'South America',data))
    
    countries = list(map(lambda item: item["Country/Territory"], data))
    population = list(map(lambda item: float(item["World Population Percentage"]), data))
    new_list = list(zip(countries,population))
    charts.generate_pie_chart(countries,population)
    # countrys_v1 = []
    # population_v1 = []
    # for x,y in new_list:
    #     if y >= 1 :
    #         countrys_v1.append(x)
    #         population_v1.append(y)
    #     print(countrys_v1)
    #     print(population_v1)
    # charts.generate_pie_chart(countrys_v1,population_v1)
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'],labels, values)

        


if __name__ == "__main__":
    run()
