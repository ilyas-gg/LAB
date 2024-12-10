import pickle


phones = {
    "iPhone 16": {"USA": 1000, "UK": 769, "Germany": 899, "France": 879, "China": 799, "India": 1200, "Brazil": 1300, "Japan": 850},
    "Samsung Galaxy S24": {"USA": 699, "UK": 679, "Germany": 719, "France": 739, "China": 680, "India": 900, "Brazil": 1000, "Japan": 720},
    "Google Pixel 9": {"USA": 599, "UK": 569, "Germany": 629, "France": 649, "China": 610, "India": 800, "Brazil": 900, "Japan": 630},
    "Infinix note 30 vip": {"USA": 729, "UK": 699, "Germany": 749, "France": 769, "China": 700, "India": 950, "Brazil": 1100, "Japan": 740},
    "Xiaomi Mi 15": {"USA": 699, "UK": 679, "Germany": 699, "France": 719, "China": 640, "India": 800, "Brazil": 950, "Japan": 680},
    "Poco f6 pro": {"USA": 1299, "UK": 1249, "Germany": 1299, "France": 1349, "China": 1200, "India": 1500, "Brazil": 1800, "Japan": 1250},
    "Huawei P90": {"USA": 0, "UK": 0, "Germany": 1100, "France": 1150, "China": 1050, "India": 1300, "Brazil": 1500, "Japan": 1100},
}

print("Телефон и их средняя стоимость")
avgprice={}
for phones , price in phones.items():
    avgprice=sum(price.values()) / len([v for in price.values() if v>0])
    avgprice[phone]=avg_price
    print(f"{phone}:{avg_price}:.2f")
    min_phone=min(avgprice, key=avgprice.get)
    phones.pop(min_phone)
    print(f"Телефон с самой маленькой ценой удален{min_phone}")
    maxavgprice=max(avgprice.Values())
    free=maxavgprice*0.3
    print("мобильные телефоны, отличающиеся по стоимости менее чем на 30% от максимальной.")
    for phone , avgprice in avgprice.items():
        if maxavgprice - avgprice >= free:
            print("",phone)
            for phone, prices in phones.items():
                if price.get("USA">0) > price.get("UK">0):
                    print("телефоны, стоимость которых в США превышает их стоимость в Великобритании:", phone)
                    
with open("data.pickle", "wb") as f:
 pickle.dump(phones, f)
print("\nСловарь сохранён в файл data.pickle.")
with open("data.pickle", "rb") as f:
    loaded_phones = pickle.load(f)
print("\nСловарь из файла data.pickle:")
print(loaded_phones)