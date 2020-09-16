from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    button = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.send_keys(y)

    # Ваш код, который заполняет обязательные поля

    che = browser.find_element_by_id("robotCheckbox")
    che.click()
    rad = browser.find_element_by_id("robotsRule")
    rad.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()