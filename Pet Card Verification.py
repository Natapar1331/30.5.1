from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(service=Service('path_to_chromedriver'))
driver.implicitly_wait(10)

driver.get("https://petfriends.skillfactory.ru/")

pets = driver.find_elements(By.CLASS_NAME, 'card-deck')

for pet in pets:
    pet_photo = pet.find_element(By.TAG_NAME, 'img')
    pet_name = pet.find_element(By.XPATH, './/h5')
    pet_age = pet.find_element(By.XPATH, './/p')

    print(f"Фото: {pet_photo.get_attribute('src')}, Имя: {pet_name.text}, Возраст: {pet_age.text}")

driver.quit()