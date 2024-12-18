import requests
from bs4 import BeautifulSoup
import csv


toplists_url = "https://worldathletics.org/records/toplists"


disciplines = {
    "high_jump": "high-jump",  
    "pole_vault": "pole-vault",
    "long_jump": "long-jump",  
    "triple_jump": "triple-jump" 
}


genders = {
    "men": "M",
    "women": "W"
}


years = range(2001, 2025)


output_file = "top_result.csv"


def extract_top_result(soup):
    table = soup.find("table", class_="records-table")
    if not table:
        return None

 
    first_row = table.find("tbody").find("tr")
    if not first_row:
        return None

  
    columns = first_row.find_all("td")
    if len(columns) < 6:
        return None

    athlete_name = columns[1].text.strip()
    country = columns[2].find("span", class_="country-name").text.strip()
    result = columns[3].text.strip()
    competition_date = columns[4].text.strip()

    return {
        "name": athlete_name,
        "country": country,
        "result": result,
        "date": competition_date
    }


data = []

for discipline, discipline_url in disciplines.items():
    for gender, gender_code in genders.items():
        for year in years:

            url = f"{toplists_url}/{discipline_url}/{gender_code}/{year}"

   
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Ошибка при загрузке {url}")
                continue
            soup = BeautifulSoup(response.content, "html.parser")


            top_result = extract_top_result(soup)
            if top_result:
                data.append({
                    "year": year,
                    "discipline": discipline,
                    "gender": gender,
                    **top_result
                })


with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["year", "discipline", "gender", "name", "country", "result", "date"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

print(f"Данные сохранены в этот крутой файл {output_file}")
