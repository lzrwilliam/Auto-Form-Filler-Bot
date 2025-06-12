from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Încarcă datele din fișierul JSON
with open("raspunsuri_fashion.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

# Setează driverul
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

def click_option_by_text(text):
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[normalize-space(text())='{text}']")))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(0.5)
        element.click()
    except:
        print(f"⚠️ Nu s-a găsit opțiunea: {text} ➡️ Selectez prima opțiune disponibilă...")
        try:
            first = wait.until(EC.element_to_be_clickable((By.XPATH, '(//div[@role="radiogroup" or @role="list"]//label)[1]')))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", first)
            time.sleep(0.4)
            first.click()
        except:
            print("❌ Nu s-a putut selecta nici prima opțiune.")

def fill_form(response):
    for value in response.values():
        if isinstance(value, list):
            for item in value:
                click_option_by_text(item)
        else:
            click_option_by_text(value)

# Parcurge toate răspunsurile din JSON
for idx, response in enumerate(responses):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc9HqACY7vc9q_fM9dCIiea6IyYbOJ6Z487S5SJUE_AHTJfcw/viewform")
    time.sleep(3)
    
    fill_form(response)

    # Dă submit
    try:
        submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Trimite")]')))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", submit_btn)
        time.sleep(0.5)
        submit_btn.click()
        print(f"[{idx + 1}/{len(responses)}] Formular trimis.")
    except:
        print(f"❌ Eroare la trimitere pentru răspunsul {idx + 1}")
    
    time.sleep(2)

driver.quit()
