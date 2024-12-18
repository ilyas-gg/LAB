import requests
import json


API_URL = "https://restcountries.com/v3.1"


languages = ["spanish", "portuguese", "german"]


output_file = "results.json"


countries_data = {}


for language in languages:
    response = requests.get(f"{API_URL}/lang/{language}")
    if response.status_code != 200:
        print(f"Не удалось загрузить язык: {language}")
        continue
    
    
    countries = [
        {
            "name": country.get("name", {}).get("common", "Unknown"),
            "capital": country.get("capital", ["Unknown"])[0],
            "area": country.get("area", 0),
            "population": country.get("population", 0),
            "flag_url": country.get("flags", {}).get("png", None),
        }
        for country in response.json()
        if country.get("area", 0) > 100000
    ]

   
    largest_country = max(countries, key=lambda x: x["area"], default=None)
    if largest_country:
        print(f"Наибольше говорящая на  {language}: {largest_country['name']} с площадью {largest_country['area']} км^2")

        
        if largest_country["flag_url"]:
            flag_response = requests.get(largest_country["flag_url"])
            if flag_response.status_code == 200:
                flag_file = f"flag_{language}.png"
                with open(flag_file, "wb") as f:
                    f.write(flag_response.content)
                print(f"Сохранён флаг {largest_country['name']} как {flag_file}")

    
    countries_data[language] = countries


with open(output_file, "w", encoding="utf-8") as f:
    json.dump(countries_data, f, ensure_ascii=False, indent=4)

print(f"Results saved to {output_file}")