# menyortir data dictionary di dalam list berdasarkan key tertentu


def sortDataListOfDict(self, data, key):
    result = [dict(t) for t in {tuple(d.items()) for d in data}]
    result = sorted(result, key=lambda x: x[key], reverse=True)
    return result

# inisialisasi chrome driver selenium


def startChromeDriver(self, lokasi_driver):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=D:\\MASTER\\userdata")
    # options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path=lokasi_driver, options=options)
    driver.maximize_window()
    return driver
