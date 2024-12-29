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

#-----------------------------------------------------------------------------

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




#---------------------------------------------------------------
# import requests
# import re
# import json
# import csv

# # URL страницы
# url = "https://www.christies.com/en/auction/fine-chinese-modern-and-contemporary-ink-paintings-30363?page=3&sortby=lotnumber"

# # Заголовки для запроса
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
# }

# # Отправляем запрос
# response = requests.get(url, headers=headers)

# # Проверяем статус ответа
# if response.status_code != 200:
#     print(f"Ошибка: сервер вернул статус {response.status_code}")
#     exit()

# # Ищем JSON в HTML-коде
# match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", response.text, re.DOTALL)
# if match:
#     json_str = match.group(1)
#     lots_data = json.loads(json_str).get("data", {}).get("lots", [])
# else:
#     print("Не удалось найти JSON-данные в HTML.")
#     exit()

# # Обрабатываем данные
# results = []
# for lot in lots_data:
#     title = lot.get("title_secondary_txt", "")
#     artist = lot.get("title_primary_txt", "")
#     price = lot.get("price_realised_txt", "")
#     estimate = lot.get("estimate_txt", "")
#     description = lot.get("description_txt", "")

#     # Извлечение периода из имени художника
#     period = ""
#     artist_clean = artist
#     artist_match = re.search(r"\(([^)]+)\)", artist)
#     if artist_match:
#         artist_clean = artist[:artist_match.start()].strip()
#         period = artist_match.group(1).strip()


#     # Парсинг размера
#     dimensions = ""
#     dimension_match = re.search(r"(\d+\.?\d*)\s*x\s*(\d+\.?\d*)\s*cm", description, re.IGNORECASE)
#     if dimension_match:
#         dimensions = f"{dimension_match.group(1)} x {dimension_match.group(2)} cm"

#     results.append({
#         "название": title,
#         "имя_художника": artist_clean,
#         "стоимость": price,
#         "примерная_оценка": estimate,
#         "материал": "",  # Можно доработать для извлечения материала
#         "размер": dimensions,
#         "страна": "Китай",  # Страна фиксированная
#         "период": period,
#         "стиль": "Traditional Chinese Art"  # Фиксированный стиль
#     })

# # Записываем в CSV
# csv_file = "Fine_Chinese_Modern_and_Contemporary_Ink_Paintings.csv"
# fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writeheader()
#     writer.writerows(results)

# print(f"Данные сохранены в {csv_file}")





#------------------------------------------------------------------------

# import requests
# import re
# import json
# import csv

# # URL страницы
# url = "https://onlineonly.christies.com/s/exquisite-eye-chinese-paintings-online/lots/3828?page=2&sortby=LotNumber"

# # Заголовки для HTTP-запроса
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
# }

# # Отправляем запрос к странице
# response = requests.get(url, headers=headers)

# if response.status_code != 200:
#     print(f"Ошибка загрузки страницы: {response.status_code}")
#     exit()

# # Ищем скрипт с JSON-данными на странице
# page_content = response.text
# match = re.search(r"window\.chrComponents\s*=\s*(\{.*?\});", page_content, re.DOTALL)

# if not match:
#     print("Не удалось найти данные о лотах на странице.")
#     exit()

# # Извлекаем JSON-данные
# json_str = match.group(1)
# chr_components = json.loads(json_str)

# # Проверяем наличие данных о лотах
# lots_data = chr_components.get("lots", {}).get("data", {}).get("lots", [])
# if not lots_data:
#     print("Данные о лотах отсутствуют в JSON.")
#     exit()

# # Обрабатываем данные
# results = []
# for lot in lots_data:
#     title = lot.get("title_secondary_txt", "")
#     artist = lot.get("title_primary_txt", "")
#     price = lot.get("price_realised_txt", "")
#     estimate = lot.get("estimate_txt", "")
#     description = lot.get("description_txt", "")

#     # Удаление HTML-тегов из описания
#     description_clean = re.sub(r"<.*?>", " ", description)

#     # Извлечение размера
#     size_match = re.search(r"([\d.,]+ x [\d.,]+ cm)", description_clean)
#     size = size_match.group(1) if size_match else ""

#     # Извлечение страны и периода из имени художника
#     country = "CHINA"
#     period = ""
#     artist_clean = re.sub(r"<.*?>", " ", artist)
#     artist_name = artist_clean.strip()
#     artist_match = re.search(r"(.*?)\(([^,]+)\)", artist_clean)
#     if artist_match:
#         artist_name = artist_match.group(1).strip()  # Имя автора
#         period = artist_match.group(2).strip()  # Период
    

#     results.append({
#         "Название": title,
#         "Имя художника": artist_name,
#         "Стоимость": price,
#         "Примерная оценка": estimate,
#         "Размер": size,
#         "Страна": country,
#         "Период": period,
#         "Стиль": "Traditional Chinese Art"
#     })

# # Записываем в CSV
# csv_file = "Exquisite_Eye_hinese_Paintings.csv"
# fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Размер", "Страна", "Период","Стиль"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writeheader()
#     writer.writerows(results)

# print(f"Данные сохранены в {csv_file}")


#-----------------------------------------------------------------------------------------


# import requests
# import re
# import json
# import csv

# # URL страницы
# url = "https://www.christies.com/en/auction/vivre-la-couleur-hommage-jean-fournier-30660/"

# # Заголовки для HTTP-запроса
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
# }

# # Отправляем запрос к странице
# response = requests.get(url, headers=headers)

# if response.status_code != 200:
#     print(f"Ошибка загрузки страницы: {response.status_code}")
#     exit()

# # Ищем скрипт с JSON-данными на странице
# page_content = response.text
# match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", page_content, re.DOTALL)

# if not match:
#     print("Не удалось найти данные о лотах на странице.")
#     exit()

# # Извлекаем JSON-данные
# json_str = match.group(1)
# chr_components = json.loads(json_str)

# # Проверяем наличие данных о лотах
# lots_data = chr_components.get("data", {}).get("lots", [])
# if not lots_data:
#     print("Данные о лотах отсутствуют в JSON.")
#     exit()

# # Обрабатываем данные
# results = []
# for lot in lots_data:
#     title = lot.get("title_secondary_txt", "").strip()  # Название произведения
#     artist = lot.get("title_primary_txt", "").strip()   # Имя художника
#     price = lot.get("price_realised_txt", "").strip()   # Стоимость
#     estimate = lot.get("estimate_txt", "").strip()      # Примерная оценка
#     description = lot.get("description_txt", "").strip()  # Описание

#     # Извлечение периода из имени художника
#     period = ""
#     artist_clean = artist
#     artist_match = re.search(r"\(([^)]+)\)", artist)
#     if artist_match:
#         artist_clean = artist[:artist_match.start()].strip()
#         period = artist_match.group(1).strip()
#     # Удаляем фразы "né en" и другие ненужные выражения
#         period = re.sub(r"né en\s*", "", period, flags=re.IGNORECASE)
#         period = period.strip()

    
#      # Извлечение размера
#     dimensions = ""
#     description_match = re.search(r"(\d+\s*x\s*\d+\s*cm)", description, re.IGNORECASE)
#     if not description_match:
#         description_match = re.search(r"\((\d+\s*x\s*\d+\s*cm)\)", description, re.IGNORECASE)
#         if not description_match:
#             description_match = re.search(r"(\d+\s*x\s*\d+\s*in)", description, re.IGNORECASE)
#     if description_match:
#         dimensions = description_match.group(1)

#     # Извлечение материала
#     material = ""
#     material_match = re.search(r"(oil on canvas|acrylic|mixed media|gouache|watercolor|bronze)", description, re.IGNORECASE)
#     if material_match:
#         material = material_match.group(1).capitalize()

#     results.append({
#         "название": title,
#         "имя_художника": artist_clean,
#         "стоимость": price,
#         "примерная_оценка": estimate,
#         "материал": material,
#         "размер": dimensions,
#         "страна": "FRENCH",  # Можно добавить логику извлечения
#         "период": period,
#         "стиль": "Abstractus"
#     })

# # Записываем в CSV
# csv_file = "Vivre_la_couleur.csv"
# fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writeheader()
#     writer.writerows(results)

# print(f"Данные сохранены в {csv_file}")

#-----------------------------------------------------------------------------------

import requests
import re
import json
import csv

# URL страницы
url = "https://www.christies.com/en/auction/old-masters-part-i-30289/"

# Заголовки для HTTP-запроса
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

# Отправляем запрос к странице
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Ошибка загрузки страницы: {response.status_code}")
    exit()

# Ищем скрипт с JSON-данными на странице
page_content = response.text
match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", page_content, re.DOTALL)

if not match:
    print("Не удалось найти данные о лотах на странице.")
    exit()

# Извлекаем JSON-данные
json_str = match.group(1)
chr_components = json.loads(json_str)

# Проверяем наличие данных о лотах
lots_data = chr_components.get("data", {}).get("lots", [])
if not lots_data:
    print("Данные о лотах отсутствуют в JSON.")
    exit()

# Обрабатываем данные
results = []
for lot in lots_data:
    title = lot.get("title_secondary_txt", "").strip()  # Название произведения
    artist = lot.get("title_primary_txt", "").strip()   # Имя художника
    price = lot.get("price_realised_txt", "").strip()   # Стоимость
    estimate = lot.get("estimate_txt", "").strip()      # Примерная оценка
    description = lot.get("description_txt", "").strip()  # Описание

    # Извлечение периода из имени художника
    period = ""
    artist_clean = artist
    artist_match = re.search(r"\(([^)]+)\)", artist)
    if artist_match:
        artist_clean = artist[:artist_match.start()].strip()
        period = artist_match.group(1).strip()
    # Удаляем фразы "né en" и другие ненужные выражения
        period = re.sub(r"né en\s*", "", period, flags=re.IGNORECASE)
        period = period.strip()

    
     # Извлечение размера
    dimensions = ""
    description_match = re.search(r"(\d+\s*x\s*\d+\s*cm)", description, re.IGNORECASE)
    if not description_match:
        description_match = re.search(r"\((\d+\s*x\s*\d+\s*cm)\)", description, re.IGNORECASE)
        if not description_match:
            description_match = re.search(r"(\d+\s*x\s*\d+\s*in)", description, re.IGNORECASE)
    if description_match:
        dimensions = description_match.group(1)

    # Извлечение материала
    material = ""
    material_match = re.search(r"(oil on canvas|acrylic|mixed media|gouache|watercolor|bronze)", description, re.IGNORECASE)
    if material_match:
        material = material_match.group(1).capitalize()

    results.append({
        "название": title,
        "имя_художника": artist_clean,
        "стоимость": price,
        "примерная_оценка": estimate,
        "материал": material,
        "размер": dimensions,
        "страна": "",  # Можно добавить логику извлечения
        "период": period,
        "стиль": "Abstractus"
    })

# Записываем в CSV
csv_file = "Old_Masters_Part_I.csv"
fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль"]

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
    writer.writeheader()
    writer.writerows(results)

print(f"Данные сохранены в {csv_file}")
