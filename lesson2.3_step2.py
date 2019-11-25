from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку
    button1 = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
    button1.click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    # Отправляем заполненную форму
    button2 = browser.find_element_by_css_selector("button.btn.btn-primary")
    button2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
