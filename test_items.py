# Тест для нахождения на странице корзины для добавления товара
import pytest
from time import sleep


    
def test_guest_should_see_basket(browser,request):
    link = f"https://selenium1py.pythonanywhere.com/{request.config.getoption('language')}/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_elements_by_css_selector("#add_to_basket_form button[type='submit']")
    assert len(button) != 0, 'Your Majesty, The Button for basket was not found. May be your need to change selector' 
    sleep(30)
    