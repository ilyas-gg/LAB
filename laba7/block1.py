import pickle


mobile_prices = {
    "iPhone 16": {"USA": 999, "UK": 879, "Germany": 949, "France": 970, "Japan": 950, "India": 1150, "China": 899, "Canada": 1000},
    "Samsung Galaxy S24 ultra": {"USA": 899, "UK": 799, "Germany": 869, "France": 880, "Japan": 870, "India": 920, "China": 850, "Canada": 900},
    "Google Pixel 9": {"USA": 599, "UK": 649, "Germany": 630, "France": 640, "Japan": 610, "India": 680, "China": 600, "Canada": 620},
    "OnePlus": {"USA": 699, "UK": 729, "Germany": 710, "France": 720, "Japan": 700, "India": 750, "China": 680, "Canada": 710},
    "Xiaomi 14": {"USA": 599, "UK": 619, "Germany": 600, "France": 610, "Japan": 620, "India": 650, "China": 570, "Canada": 590},
    "Sony Xperia 1 IV": {"USA": 1299, "UK": 1199, "Germany": 1250, "France": 1270, "Japan": 1280, "India": 1350, "China": 1200, "Canada": 1300},
    "Huawei P60 pro": {"USA": 899, "UK": 850, "Germany": 870, "France": 880, "Japan": 890, "India": 950, "China": 820, "Canada": 870}
}

print("\nСредние стоимости телефонов:")
for model, prices in mobile_prices.items():
    avg_price = sum(prices.values()) / len(prices)
    print(f"{model}: {avg_price:.2f}")


model_to_remove = min(mobile_prices, key=lambda model: sum(mobile_prices[model].values()) / len(mobile_prices[model]))
print(f"\nУдаляем телефон с минимальной средней стоимостью: {model_to_remove}")
del mobile_prices[model_to_remove]


max_avg_price = max(sum(prices.values()) / len(prices) for prices in mobile_prices.values())
threshold = max_avg_price * 0.7
print("\nТелефоны с ценой менее чем на 30% ниже максимальной:")
for model, prices in mobile_prices.items():
    avg_price = sum(prices.values()) / len(prices)
    if avg_price >= threshold:
        print(model)


print("\nТелефоны, стоимость которых в США превышает стоимость в Великобритании:")
us_vs_uk = {model: prices for model, prices in mobile_prices.items() if prices["USA"] > prices["UK"]}
for model in us_vs_uk:
    print(model)


with open("data.pickle", "wb") as f:
    pickle.dump(mobile_prices, f)
print("\nСловарь сохранен в файл data.pickle.")


with open("data.pickle", "rb") as f:
    loaded_data = pickle.load(f)
print("\nСловарь загружен из файла data.pickle:")
print(loaded_data)


try:
    with open("input.txt", "r", encoding="utf-8") as infile, open("output.txt", "w", encoding="utf-8") as outfile:
        for line in infile:
            words = line.split()
            if words:
                longest_word = max(words, key=len)
                outfile.write(longest_word + "\n")
    print("\nСлова максимальной длины записаны в файл output.txt.")
except FileNotFoundError:
    print("\nФайл input.txt не найден.")