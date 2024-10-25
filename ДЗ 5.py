import zipfile
import csv

# Шаг 1: Создаём словарь для хранения данных о покупках
purchase_dict = {}

try:
    # Разархивируем файл и читаем данные о покупках
    with zipfile.ZipFile('purchase_log.zip', 'r') as zip_ref:
        with zip_ref.open('purchase_log.csv') as purchase_file:
            reader = csv.reader(purchase_file)
            next(reader)  # Пропускаем заголовок
            for row in reader:
                user_id, category = row
                purchase_dict[user_id] = category
except FileNotFoundError:
    print("Файл purchase_log.zip не найден. Проверьте, что он находится в той же папке, что и скрипт.")
except Exception as e:
    print(f"Произошла ошибка при обработке файла purchase_log.zip: {e}")

# Шаг 2 и 3: Обрабатываем файл visit_log и создаём funnel.csv
try:
    with open('visit_log__1_.csv', 'r') as visit_file, \
         open('funnel.csv', 'w', newline='') as funnel_file:

        visit_reader = csv.reader(visit_file)
        funnel_writer = csv.writer(funnel_file)

        # Записываем заголовок в funnel.csv
        funnel_writer.writerow(['user_id', 'source', 'category'])

        # Пропускаем заголовок исходного файла
        next(visit_reader)

        # Шаг 4: Построчно проверяем визиты
        for row in visit_reader:
            user_id, source = row
            # Проверяем, есть ли покупка для данного user_id
            if user_id in purchase_dict:
                # Записываем строку с категорией в funnel.csv
                funnel_writer.writerow([user_id, source, purchase_dict[user_id]])

    print("Файл funnel.csv успешно создан.")
except FileNotFoundError:
    print("Файл visit_log__1_.csv не найден. Проверьте, что он находится в той же папке, что и скрипт.")
except Exception as e:
    print(f"Произошла ошибка при обработке файла visit_log__1_.csv: {e}")
