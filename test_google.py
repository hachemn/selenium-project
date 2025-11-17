from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless=new")  # Chrome sans interface graphique
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com")

if "Google" in driver.title:
    print("TEST OK : Google s'affiche correctement.")
else:
    print("TEST FAILED : Page non trouvée.")

driver.quit()
