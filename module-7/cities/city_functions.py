def main():
    #test data
    print(format_city("Jakarta", "Indonesia"))#Order changed from initial test data because several languages are commonly spoken in Indonesia
    print(format_city("Buffalo", "United States", 275000))#Rounded approximate population
    print(format_city("Sendai", "Japan", 1000000, "Japanese"))#Rounded approximate population

def format_city(city_name, country_name, population = "", language = ""):
    formatted_city = f"{city_name.title()}, {country_name.title()}"

    if population:# Optional population information
        formatted_city += f" - population {population}"

    if language:# Optional language information
        formatted_city += f", {language}"

    return  formatted_city

if __name__ == '__main__':
    main()