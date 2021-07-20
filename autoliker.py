#!/usr/bin/python
# -*- coding: utf8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *



oshibka = ['','Похоже с вашим логином или паролем что-то не так.'+ "\n" +' Перепроверьте всё и попробуйте снова.','всё прекрасно сработало','У вас кончился лимит лайков в инстаграмме' + "\n" + "через некоторое время можете продолжить", "Ошибка: проверьте своё подключение к интернету", "Упс, на сайте произошла ошибка"  + "\n" + "У Instaram есть защита от автолайкеров, из-за этого программа может работать ни с первого раза"  + "\n" + "Попробуйте ещё разок"]


def Instagram_registr(username, password, hech, num):
    chrome_options = webdriver.ChromeOptions()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)
    num = int(num)
    try:
        driver.get("https://www.instagram.com/")
    except:
        driver.close()
        return 4
    driver.implicitly_wait(3)
    try:
        name = driver.find_element_by_xpath(r"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    except:
        driver.close()
        return 5
    name.send_keys(username)
    passwords = driver.find_element_by_name("password")
    passwords.send_keys(password)
    time.sleep(1)
    passwords.send_keys(u'\ue007')
    time.sleep(5)
    driver.get(f"https://www.instagram.com/explore/tags/{hech}/")
    time.sleep(5)
    cart = driver.find_elements_by_class_name("_9AhH0")
    i = 0
    likecost = 0
    while likecost < num:
        try:
            time.sleep(0.5)
            cart[i].click()
            time.sleep(1.5)
            likee = driver.find_element_by_css_selector('span[class*="fr66n"]')
            time.sleep(0.5)
            like = likee.find_element_by_css_selector('button[type*="button"]')
            time.sleep(0.5)
            likein = like.find_element_by_class_name("_8-yf5 ")
            doit = likein.get_attribute("aria-label")
            time.sleep(1)
            if doit == "Нравится":
                like.click()
                likecost+=1
            try:
                element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div/div[2]/button[2]")))
                time.sleep(0.5)
                element.click()
                driver.close()
                return 3
            except:
                esc_button = driver.find_element_by_xpath("/html/body/div[5]/div[3]")
                time.sleep(0.5)
                esc_button.click()
                cart = driver.find_elements_by_class_name("_9AhH0")
                i+=1
        except:
            try:
                time.sleep(1)
                esc_button = driver.find_element_by_xpath("/html/body/div[5]/div[3]")
                time.sleep(1)
                esc_button.click()
                i += 1
            except:
                driver.close()
                return 1
    driver.close()
    return 2


def clicked():
    soob.configure(text = '', fg = 'red')
    lbl4.configure( text="Сколько постов нужно лайкнуть?", fg='black')
    btn.configure(state='disabled', text = 'подождём')
    if txt1.get() == "" or txt2.get() == "" or txt3.get() == "" or txt4.get() == "":
        btn.configure(text = "не все поля введены", state='normal')
        return 0
    try:
        test = int(txt4.get())
    except:
        lbl4.configure(text="цифрами пожалуйста", fg='red')
        btn.configure(text = "поехали", state='normal')
        return 0
    txt1.configure(state='disabled')
    txt2.configure(state='disabled')
    txt3.configure(state='disabled')
    txt4.configure(state='disabled')
    tyt1 = str(txt1.get())
    tyt2 = str(txt2.get())
    tyt3 = str(txt3.get())
    time.sleep(1)
    otvet = int(Instagram_registr(tyt1, tyt2, tyt3, test))
    if otvet == 2:
        soob.configure(fg='green')
    soob.configure(text=oshibka[otvet])
    soob.grid(column=2, row=9)
    txt1.configure(state='normal')
    txt2.configure(state='normal')
    txt3.configure(state='normal')
    txt4.configure(state='normal')
    btn.configure(state='normal', text = 'Поехали')

window = Tk()
window.title("Добро пожаловать в автолайкер для instaram. Разработчик Кирилл Давиденко")
window.geometry('400x640')
lbl1 = Label(window, text="Введите ваш логин в instagram", padx=50)
lbl1.grid(column=2, row=0)
txt1 = Entry(window, width=10)
txt1.grid(column=2, row=1)
lbl2 = Label(window, text="Введите пароль")
lbl2.grid(column=2, row=2)
txt2 = Entry(window, width=10)
txt2.grid(column=2, row=3)
lbl3 = Label(window, text="Введите хэштег")
lbl3.grid(column=2, row=4)
txt3 = Entry(window, width=10)
txt3.grid(column=2, row=5)
lbl4 = Label(window, text="Сколько постов нужно лайкнуть?")
lbl4.grid(column=2, row=6)
txt4 = Entry(window, width=10)
txt4.grid(column=2, row=7)
btn = Button(window, text="Start", command=clicked)
btn.grid(column=2, row=8)
soob = Label(window, text='', fg = 'red')
soob.grid(column=2, row=9)
window.mainloop()

#Instagram_registr('Alonas345','f1a2t3h4e5r','музыка', 36)
# options.add_argument("--headless")
#r'C:\Users\Кирилл\PycharmProjects\chromedriver'
#C:\Users\Кирилл\PycharmProjects\pythonProject\autolikerApp\venv\Scripts\activate
#py2applet --make-setup autoliker.py