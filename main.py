# -*- coding: utf-8 -*-
import json
from bs4 import BeautifulSoup
from selenium import webdriver

naver_url = 'https://dict.naver.com/enendict/'
search_url = '#/search?query='

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)

if __name__=='__main__':
    f = open('./word_list.txt', 'r')
    word_list = [x.strip() for x in f.readlines()]
    f.close()

    for i, word in enumerate(word_list):
        driver.get(naver_url + search_url + word)
        driver.find_element_by_class_name('txt_origin').find_element_by_tag_name('a').click()
        html = BeautifulSoup(driver.page_source, 'lxml')

        def_list = []
        ex_list = []
        for _def in html.find_all('p', {'class': 'cont'}):
            elem = _def.find('m')
            if elem:
                def_list.append(elem.text)

        for _ex in html.find_all('p', {'class': 'origin'}):
            elem = _ex.find('span', {'class': 'text'})
            if elem:
                ex_list.append(elem.text)

        num = i + 2297

        with open('./data/' + str(num) + '_' + word + '.json', 'w') as f:
            json.dump([def_list, ex_list], f)
