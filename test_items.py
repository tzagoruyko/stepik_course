import time
from selenium.webdriver.common.by import By

def test_add_to_basket_button_is_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button.is_displayed(), "Кнопка не отображается на странице"

