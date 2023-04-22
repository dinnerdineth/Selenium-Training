# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 20:28:23 2022

@author: Dineth
"""
import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def web_scrape():
  url = 'http://quotes.toscrape.com/'
  response = requests.get(url)
  soup = BeautifulSoup(response.text,'lxml')
  quotes = soup.find_all("span",class_="text")
  authors = soup.find_all("small",class_="author")
  #print(quotes) #Prints entire text
  for i in range(0,len(quotes)):
    print(quotes[i].text + " - " + authors[i].text)
    

def paginated_scraping1():
  url = 'https://scrapingclub.com/exercise/detail_basic/?page=1'
  response = requests.get(url)
  soup = BeautifulSoup(response.text,'lxml')
  items = soup.find_all("div",class_="col-lg-8")
  for i in items:
    itemName = i.find('h3',class_='card-title').text
    itemPrice = i.find('h4').text
    print('Price: %s - Item Name: %s' %(itemPrice,itemName))
    
def auto_web_browsing_one():
  driver = webdriver.Chrome()
  driver.maximize_window()
  url = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'
  driver.get(url)
  
  #kill popup
  closeButton = driver.find_elements("xpath",'//*[@id="at-cv-lightbox-close"]')
  if closeButton:
      closeButton.click()
  
  #First input field
  messageField = driver.find_element("xpath",'//*[@id="user-message"]')
  messageField.send_keys("Hello world")
  show_message_button = driver.find_element("xpath",'//*[@id="get-input"]/button')
  show_message_button.click()
  
  #Second input field
  aField = driver.find_element("xpath",'//*[@id="sum1"]')
  aField.send_keys(234)
  bField = driver.find_element("xpath",'//*[@id="sum2"]')
  bField.send_keys(456)
  addButton = driver.find_element("xpath",'//*[@id="gettotal"]/button')
  addButton.click()
  
  time.sleep(15)

def drag_drop():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
    driver.get(url)
    actions = ActionChains(driver)
    
    washingtonBox = driver.find_element("xpath",'//*[@id="box3"]')
    USBox = driver.find_element("xpath",'//*[@id="box103"]')
    actions.drag_and_drop(washingtonBox,USBox).perform()
    
    time.sleep(15)
    
def api_call():
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
    parameters = {'upc':'012993441012'}
    response = requests.get(baseUrl,params=parameters)
    print(response.url)
    
    content = response.content
    #print(content)
    info = json.loads(content)
    print(type(info))
    print(info)
    item = info['items']
    itemInfo = item[0]
    title = itemInfo['title']
    print(title)
    brand = itemInfo['brand']
    print(brand)
    
def page_interaction():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("http://python.org")
  
  search = driver.find_element("name","q")
  search.clear()
  search.send_keys("pycon")
  search.send_keys(Keys.RETURN)
  
  time.sleep(15)
  
  driver.close()
    
def filling_forms():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("file:///home/dineth/Documents/Python/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH03/03_02/html_code_03_02.html")
  time.sleep(2)
  
  select = Select(driver.find_element("name","numReturnSelect"))
  select.select_by_index(4)
  time.sleep(2)
  
  select.select_by_visible_text("200")
  time.sleep(2)
  
  select.select_by_value("250")
  time.sleep(2) 
  
  #options = select.options
  #print(options)
  
  submit_button = driver.find_element("name","continue")
  #submit_button.click()
  submit_button.submit()
  
  time.sleep(15)
  driver.close()
  
  
def drag_drop_two():
  driver = webdriver.Chrome()
  driver.maximize_window()
  url = "http://jqueryui.com/droppable"
  driver.get(url)
  driver.switch_to.frame(0)
  
  action_chains = ActionChains(driver)
  
  source = driver.find_element("id","draggable")
  target = driver.find_element("id","droppable")
  
  action_chains.drag_and_drop(source,target).perform()
  
  time.sleep(10)
  
def challenge():
  driver = webdriver.Chrome()
  driver.maximize_window()
  url = "https://wiki.python.org/moin/FrontPage"
  driver.get(url)
  time.sleep(2)
  
  search = driver.find_element("id","searchinput")
  search.clear()
  search.send_keys("Beginner")
  search.send_keys(Keys.RETURN)
  
  # search_button = driver.find_element("id","fullsearch")
  # search_button.click()
  
  #change menu option
  actions_menu = Select(driver.find_element("xpath",'//*[@id="sidebar"]/div[3]/ul/li[5]/form/div/select'))
  actions_menu.select_by_visible_text("Raw Text")
  
  
  
  time.sleep(15)
  driver.close()
  
def explicit_wait():
  driver = webdriver.Chrome()
  driver.maximize_window()
  url = 'http://python.org'
  driver.get(url)
  
  try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'start-shell')))
    
  finally:
    driver.quit()
    
    
def implicit_wait():
  driver = webdriver.Chrome()
  driver.maximize_window()
  url = 'http://python.org'
  driver.get(url)
  
  driver.implicitly_wait(10)
  