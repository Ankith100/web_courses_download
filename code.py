from selenium import webdriver
import pickle
from time import sleep
import json


browser = webdriver.Chrome("chromedriver")

with open("links.txt") as f:
    links = f.readlines()

cookies = pickle.load(open("cookies.pkl", "rb"))

browser.get(links[0])
browser.delete_all_cookies()
for cookie in cookies:
    browser.add_cookie(cookie)

di = {}
i = 1

# print(browser.execute_script('s="";x = document.querySelector("#tl-navbar-progress");for(var i=0;i<x.childElementCount;i++){if(x.children[i].querySelector("a"))s += x.children[i].querySelector("a").href + "\n";}console.log(s);'))

for link in links:
    browser.get(link)
    browser.execute_script("x = document.querySelector('iframe.video-frame')")
    browser.execute_script("if (x) { vi = x.contentWindow.document.querySelector('video') }else {vi = ''}")
    key = browser.execute_script('return document.querySelector("#tl-dropdown-progress > a > span[title]").title')
    url = browser.execute_script("if(vi){ return vi.src }else{ return '' }")
    di[key] = url
    print(i)
    i += 1
    sleep(2)

with open("data.json", "w") as f:
    json.dump(di, f)

browser.quit()