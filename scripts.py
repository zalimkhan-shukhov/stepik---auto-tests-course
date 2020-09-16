'''
import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
'''
'''
from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

'''
'''
from selenium import webdriver
import math
import time


url = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
try:
    
    browser.get(url)
    link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
'''
'''
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_css_selector('input[type="text"]')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_xpath('//button[text() = "Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
'''
'''
from selenium import webdriver
import math
from time import sleep

url = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))




browser = webdriver.Chrome()

try:
    browser.get(url)
    x_elem = browser.find_element_by_css_selector("#treasure")
    val = x_elem.get_attribute('valuex')


    y = calc(val)

    elem = browser.find_element_by_css_selector("#answer")
    elem.send_keys(y)

    ch_box = browser.find_element_by_css_selector("#robotCheckbox")
    ch_box.click()

    r_btn = browser.find_element_by_css_selector("#robotsRule")
    r_btn.click()

    s = browser.find_element_by_css_selector('.btn.btn-default')
    s.click()

finally:
    sleep(10)
    browser.quit()
'''
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time


url = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
try:
    browser.get(url)
    elem = browser.find_element_by_css_selector('#num1')
    n1 = int(elem.text)
    elem = browser.find_element_by_css_selector('#num2')
    n2 = int(elem.text)

    select = Select(browser.find_element_by_css_selector('#dropdown'))
    select.select_by_visible_text(str(n1+n2))
    elem = browser.find_element_by_css_selector('.btn.btn-default')
    elem.click()
finally:
    time.sleep(5)
    browser.quit()

'''
'''
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/execute_script.html'
try:
    browser.get(url)
    val = browser.find_element_by_css_selector('#input_value').text
    x = calc(val)

    txt_elem = browser.find_element_by_css_selector('#answer')
    txt_elem.send_keys(x)
    button = browser.find_element_by_css_selector('.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    elem = browser.find_element_by_css_selector('#robotCheckbox')    
    elem.click()
    r_btn = browser.find_element_by_css_selector('#robotsRule')
    r_btn.click()
    button.click()

finally:
    time.sleep(7)
    browser.quit()

'''
'''
from selenium import webdriver
import time

my_path = globals()['__file__'] #получаем полное имя исполняемого файла
my_path = my_path[:my_path.rfind('/')] # отделяем путь к исполняеммому файлу от его полного имени
url = 'http://suninjuly.github.io/file_input.html'
print(my_path)

browser = webdriver.Chrome()
try:
    browser.get(url)
    elem = browser.find_element_by_css_selector('input[name = "firstname"]')
    elem.send_keys('firstname')
    elem = browser.find_element_by_css_selector('input[name = "lastname"]')
    elem.send_keys('lastname')
    elem = browser.find_element_by_css_selector('input[name = "email"]')
    elem.send_keys('email')
    elem = browser.find_element_by_css_selector('#file')
    elem.send_keys(my_path+'/1.txt')
    elem = browser.find_element_by_css_selector('.btn.btn-primary')
    elem.click()
finally:
    time.sleep(7)
    browser.quit()
'''
'''
from selenium import webdriver
import time
import math

url = 'http://suninjuly.github.io/alert_accept.html'



def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get(url)
    btn_submit = browser.find_element_by_css_selector('.btn.btn-primary')
    btn_submit.click()
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)
    x = browser.find_element_by_css_selector('#input_value').text
    elem = browser.find_element_by_css_selector('#answer')
    elem.send_keys(calc(x))
    btn_submit = browser.find_element_by_css_selector('.btn.btn-primary')
    btn_submit.click()

finally:
    time.sleep(7)
    browser.quit()
    '''

'''
from selenium import webdriver
import time
import math

url = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get(url)
    btn_submit = browser.find_element_by_css_selector('.trollface.btn.btn-primary')
    btn_submit.click()
    new_wnd = browser.window_handles[1]
    browser.switch_to.window(new_wnd)
    x = browser.find_element_by_css_selector('#input_value').text
    elem = browser.find_element_by_css_selector('#answer')
    elem.send_keys(calc(x))
    btn_submit = browser.find_element_by_css_selector('.btn.btn-primary')
    btn_submit.click()


finally:
    time.sleep(7)
    browser.quit()
'''
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math

url = 'http://suninjuly.github.io/explicit_wait2.html'



def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get(url)
    button = browser.find_element_by_css_selector('#book')
    elem = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,'price'),'100'))
    button.click()

    x = browser.find_element_by_css_selector('#input_value').text
    elem = browser.find_element_by_css_selector('#answer')
    elem.send_keys(calc(x))
    btn_submit = browser.find_element_by_css_selector('#solve')
    btn_submit.click()

finally:
    sleep(7)
    browser.quit()