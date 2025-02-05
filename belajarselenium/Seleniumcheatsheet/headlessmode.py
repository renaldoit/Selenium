from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)