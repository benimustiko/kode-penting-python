# menyortir data dictionary di dalam list berdasarkan key tertentu


def sort_data_list_of_dict(data, key):
    result = [dict(t) for t in {tuple(d.items()) for d in data}]
    result = sorted(result, key=lambda x: x[key], reverse=True)
    return result

# inisialisasi chrome driver selenium
# butuh import library
# from selenium import webdriver


def start_chrome_driver(self, lokasi_driver):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=D:\\MASTER\\userdata")
    # options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path=lokasi_driver, options=options)
    driver.maximize_window()
    return driver

# membaca file csv pada lokasi tertentu
# butuh import library
# import csv


def read_csv(lokasi_file):
    with open(lokasi_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        # get the nims and data_row_0s
        for row in csv_reader:
            data_row_0 = row[0]
            data_row_1 = row[1]

            if line_count == 0:
                print('')
                line_count += 1
            else:
                print(data_row_0)
                print(data_row_1)
                line_count += 1
