from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service('path_to_chromedriver'))
driver.get("https://petfriends.skillfactory.ru/all_pets")

wait = WebDriverWait(driver, 10)

table = wait.until(EC.visibility_of_element_located((By.XPATH, '//table')))

pets = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//table/tbody/tr')))

for pet in pets:
    name = pet.find_element(By.XPATH, './/td[1]').text
    age = pet.find_element(By.XPATH, './/td[2]').text
    breed = pet.find_element(By.XPATH, './/td[3]').text

    print(f"Имя: {name}, Возраст: {age}, Порода: {breed}")

driver.quit()