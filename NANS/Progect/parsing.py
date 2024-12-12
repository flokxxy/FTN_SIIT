# import json
# import re
# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.edge.service import Service

# edge_options = Options()
# # edge_options.add_argument("--headless")

# driver_path = "D:\\project on python\\msedgedriver.exe"
# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=edge_options)

# url = "https://www.christies.com/en/auction/british-and-european-art-29994/browse-lots"
# driver.get(url)

# driver.implicitly_wait(10)

# scripts = driver.find_elements(By.TAG_NAME, "script")
# lots_json = None

# for script in scripts:
#     text = script.get_attribute("innerHTML")
#     if "window.chrComponents.lots" in text:
#         match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", text, re.DOTALL)
#         if match:
#             json_str = match.group(1)
#             lots_data = json.loads(json_str)
#             lots_json = lots_data["data"]["lots"]
#         break

# if not lots_json:
#     print("Не удалось найти данные о лотах.")
#     driver.quit()
#     exit()

# results = []
# for lot in lots_json:
#     artist = lot.get("title_primary_txt", "")
#     title = lot.get("title_secondary_txt", "")
#     price = lot.get("price_realised_txt", "")
#     estimate = lot.get("estimate_txt", "")
#     description = lot.get("description_txt", "")

#     # Удаляем все содержимое в скобках из имени художника
#     # Например, было: "GUSTAVE COURBET (FRENCH, 1819-1877)"
#     # Станет: "GUSTAVE COURBET"
#     artist_clean = re.sub(r"\([^)]*\)", "", artist).strip()

#     # Парсинг страны и периода из имени художника.
#     # Формат ожидается: ARTIST NAME (COUNTRY, YYYY-YYYY)
#     country = ""
#     period = ""
#     artist_match = re.search(r"\(([^,]+),\s*([^)]+)\)", artist)
#     if artist_match:
#         country = artist_match.group(1).strip()
#         period = artist_match.group(2).strip()

#     lines = description.split("<br>")
#     material = ""
#     dimensions = ""
#     for l in lines:
#         line = l.strip()
#         # Ищем материал
#         if "oil on" in line.lower() or "watercolor" in line.lower() or "bronze" in line.lower():
#             material = line

#         # Ищем размеры в см
#         cm_match = re.search(r"\(([\d.,]+)\s*x\s*([\d.,]+)\s*cm\.\)", line)
#         if cm_match:
#             width_cm = cm_match.group(1)
#             height_cm = cm_match.group(2)
#             dimensions = f"{width_cm} x {height_cm} cm"

#     results.append({
#         "название": title,
#         "имя_художника": artist_clean ,
#         "стоимость": price,
#         "примерная_оценка": estimate,
#         "материал": material,
#         "размер": dimensions,
#         "страна": country,    
#         "период": period,    
#         "стиль": ""      
#     })

# driver.quit()

# # Записываем в CSV
# csv_file = "British and European Art_14dec.csv"
# fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     # Используем точку с запятой как разделитель полей
#     # Отключаем кавычки вовсе
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writeheader()
#     writer.writerows(results)


# print(f"Данные сохранены в {csv_file}")


# import json
# import re
# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.edge.service import Service

# edge_options = Options()
# # edge_options.add_argument("--headless")

# driver_path = "D:\\project on python\\msedgedriver.exe"
# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=edge_options)

# url = "https://www.christies.com/en/auction/the-sam-josefowitz-collection-graphic-masterpieces-by-rembrandt-van-rijn-part-ii-30288/?page=2&sortby=lotnumber"
# driver.get(url)

# driver.implicitly_wait(10)

# scripts = driver.find_elements(By.TAG_NAME, "script")
# lots_json = None

# for script in scripts:
#     text = script.get_attribute("innerHTML")
#     if "window.chrComponents.lots" in text:
#         match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", text, re.DOTALL)
#         if match:
#             json_str = match.group(1)
#             lots_data = json.loads(json_str)
#             lots_json = lots_data["data"]["lots"]
#         break

# if not lots_json:
#     print("Не удалось найти данные о лотах.")
#     driver.quit()
#     exit()


# results = []
# for lot in lots_json:
#     artist = lot.get("title_primary_txt", "")
#     title = lot.get("title_secondary_txt", "")
#     price = lot.get("price_realised_txt", "")
#     estimate = lot.get("estimate_txt", "")
#     description = lot.get("description_txt", "")

#     # Извлекаем период из скобок
#     period = ""
#     period_match = re.search(r"\(([^)]+)\)", artist)
#     if period_match:
#         period = period_match.group(1).strip()

#     # Удаляем скобки с периодом из имени художника
#     artist_clean = re.sub(r"\([^)]*\)", "", artist).strip()

#     # Страна отсутсвует
#     country = ""
#     dimensions = ""

#     lines = description.split("<br>")


#     for l in lines:
#         line = l.strip()
#          # Ищем материал
#         if "oil on" in line.lower() or "watercolor" in line.lower() or "bronze" in line.lower():
#              material = line
#     # Ищем размеры в см
#         if re.search(r"\d+\s*x\s*\d+", l):
#             dimensions = l.strip()

    

#     results.append({
#         "название": title,
#         "имя_художника": artist_clean,
#         "стоимость": price,
#         "примерная_оценка": estimate,
#         "материал": "",   # Если нужно, добавьте логику определения материала
#         "размер": dimensions,
#         "страна": "",
#         "период": period,
#         "стиль": "Graphic"
#     })

# driver.quit()

# # Записываем в CSV без кавычек
# csv_file = "Graphic Masterpieces by Rembrandt van Rijn - Part II.csv"
# fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     # Используем точку с запятой как разделитель полей, без кавычек
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writeheader()
#     writer.writerows(results)

# print(f"Данные сохранены в {csv_file}")

import json
import re
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

# Настройка Microsoft Edge 
edge_options = Options()
# edge_options.add_argument("--headless")  # Если нужно, можно раскомментировать для headless

# Путь к вашему msedgedriver
driver_path = "D:\\project on python\\msedgedriver.exe"

service = Service(driver_path)
driver = webdriver.Edge(service=service, options=edge_options)

url = "https://www.christies.com/en/auction/fine-chinese-modern-and-contemporary-ink-paintings-30363/"
driver.get(url)

driver.implicitly_wait(10)

scripts = driver.find_elements(By.TAG_NAME, "script")
lots_json = None

for script in scripts:
    text = script.get_attribute("innerHTML")
    if "window.chrComponents.lots" in text:
        match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", text, re.DOTALL)
        if match:
            json_str = match.group(1)
            lots_data = json.loads(json_str)
            lots_json = lots_data["data"]["lots"]
        break

if not lots_json:
    print("Не удалось найти данные о лотах.")
    driver.quit()
    exit()

results = []
for lot in lots_json:
    title = lot.get("title_primary_txt", "")
    artist = lot.get("title_secondary_txt", "")
    price = lot.get("price_realised_txt", "")
    estimate = lot.get("estimate_txt", "")
    description = lot.get("description_txt", "")

    lines = description.split("<br>")
    material = ""
    dimensions = ""
    for l in lines:
        if "oil on" in l.lower() or "watercolor" in l.lower() or "bronze" in l.lower():
            material = l.strip()
        if re.search(r"\d+\s*x\s*\d+", l):
            dimensions = l.strip()

    results.append({
        "название": title,
        "имя_художника": artist,
        "стоимость": price,
        "примерная_оценка": estimate,
        "материал": material,
        "размер": dimensions,
        "страна": "",    
        "период": "",    
        "стиль": ""      
    })

driver.quit()

# Записываем в CSV
csv_file = "lots_data.csv"
fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль"]

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"Данные сохранены в {csv_file}")
