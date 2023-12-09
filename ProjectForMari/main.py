import zipfile, os, json, csv


def main(*args) -> None:
    file_name = 'students.zip'
    json_file_name = 'students.json'
    out_put_file = 'studentsCSV.csv'
    zip_file_name = 'zippedCSVfile.zip'

    # проверка на действительность файла
    if os.path.exists(file_name) and file_name.endswith('.zip'):
        try:
            # разархирование файла
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall()
        except FileNotFoundError:
            print('File not found!')
    else:
        print('File name is not correct or does not exist.')

    if os.path.exists(json_file_name) and json_file_name.endswith('.json'):
        try:
            # считываем данные с Джейсон
            with open(json_file_name, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            print('File name is not correct or does not exist.')

    entries = data[0]
    fieldnames = ["lastname", "firstname"]

    # запись данных в цсв файл
    with open(out_put_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for entry in entries:
            writer.writerow({"lastname": entry["lastname"], "firstname": entry["firstname"]})

    # заархирование цсв файла
    with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
        zip_file.write(out_put_file, os.path.basename(out_put_file))


if __name__ == '__main__':
    main()