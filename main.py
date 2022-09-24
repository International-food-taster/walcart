import time
from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome("/home/maruf/PycharmProjects/o_o/chromedriver_linux64/chromedriver")

webdriver.get('https://www.walcart.com/')

webdriver.find_element(By.ID, 'search').send_keys('walton fan')
webdriver.maximize_window()

webdriver.find_element(By.XPATH, '//*[@id="search_mini_form"]/div[2]/button').click()
webdriver.find_element(By.XPATH,
                       '//*[@id="maincontent"]/div[1]/div[2]/div[1]/div/div[4]/ol/li[1]/div/div[2]/h2/a').click()
webdriver.find_element(By.ID, 'qty').clear()
webdriver.find_element(By.ID, 'qty').send_keys('2')
webdriver.find_element(By.ID, 'product-addtocart-button').click()
time.sleep(1)
webdriver.find_element(By.ID, 'top-cart-btn-checkout').click()
time.sleep(1)
webdriver.find_element(By.ID, 'mobile').send_keys('01676386249')
webdriver.find_element(By.XPATH, '//*[@id="tab-login"]/div[3]/div[1]/button').click()
time.sleep(1)
webdriver.find_element(By.ID, 'pass').send_keys('QWEr!@#4')
webdriver.find_element(By.XPATH, '//*[@id="tab-login"]/div[3]/div[2]/button').click()
time.sleep(1)
webdriver.find_element(By.ID, 'product-addtocart-button').click()
time.sleep(1)
webdriver.find_element(By.ID, 'top-cart-btn-checkout').click()
time.sleep(1)

webdriver.find_element(By.XPATH, '//*[@id="shipping-method-buttons-container"]/div/button').click()
time.sleep(2)
webdriver.find_element(By.XPATH, '//*[@id="checkout-payment-method-load"]/div/div/div[7]/div[1]/label/img').click()
time.sleep(4)

Catch_Text = webdriver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/div/div[2]/div[4]/ol/li[3]/div/form/fieldset/div[2]/div/div/div[7]/div[2]/div[4]/div/button/span').text

if Catch_Text == 'Place Order':
    print("______Order Process test PASS ______")
else:
    print("______Order Process test fail------")

webdriver.close()
