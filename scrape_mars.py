#!/usr/bin/env python
# coding: utf-8

from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_info():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # variables = {}

    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)


    html=browser.html
    soup=bs(html, 'html.parser')

    element=soup.select_one('div.list_text')
    news_title=element.find("div", class_="content_title")
    soup.find_all("div", class_="content_title")
    news_intro_paragraph=element.find("div", class_="article_teaser_body")
    featured_image_url = "https://spaceimages-mars.com/"
    browser.visit(featured_image_url)
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()
    html=browser.html
    img_soup = bs(html, 'html.parser')
    img_url_rel = img_soup.find("img", class_="fancybox-image").get('src')
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)
    tables = pd.read_html(facts_url)
    type(tables)
    df = tables[1]
    hemispheres_url="https://marshemispheres.com/"
    browser.visit(hemispheres_url)
    html=browser.html
    soup=bs(html, 'html.parser')
    element_a=soup.select_one('h3.list_text')
    cerberus=soup.find_all("h3")[0]
    schiaparelli=soup.find_all("h3")[1]
    syrtis_major=soup.find_all("h3")[2]
    valles_marineris=soup.find_all("h3")[3]
    cerberus_url="https://marshemispheres.com/cerberus.html"
    browser.visit(cerberus_url)
    cerberus_elem = browser.find_by_tag('a')[3]
    cerberus_elem.click()\

    html=browser.html
    img_soup = bs(html, 'html.parser')
    img_url_rel_a = img_soup.find("img", class_="wide-image").get('src')
    schiaparelli_url="https://marshemispheres.com/schiaparelli.html"
    browser.visit(schiaparelli_url)
    schiaparelli_elem = browser.find_by_tag('a')[3]
    schiaparelli_elem.click()

    html=browser.html
    img_soup = bs(html, 'html.parser')
    img_url_rel_b = img_soup.find("img", class_="wide-image").get('src')
    syrtis_major_url="https://marshemispheres.com/syrtis.html"
    browser.visit(syrtis_major_url)
    syrtis_major_elem = browser.find_by_tag('a')[3]
    syrtis_major_elem.click()

    html=browser.html
    img_soup = bs(html, 'html.parser')
    img_url_rel_c = img_soup.find("img", class_="wide-image").get('src')
    valles_marineris_url="https://marshemispheres.com/valles.html"
    browser.visit(valles_marineris_url)
    valles_marineris_elem = browser.find_by_tag('a')[3]
    valles_marineris_elem.click()
    
    html=browser.html
    img_soup = bs(html, 'html.parser')
    img_url_rel_d = img_soup.find("img", class_="wide-image").get('src')


    mars_dict = [
    {"title": soup.find_all("h3")[0],"img_url": img_url_rel_a},
    {"title": soup.find_all("h3")[1],"img_url": img_url_rel_b},
    {"title": soup.find_all("h3")[2],"img_url": img_url_rel_c},
    {"title": soup.find_all("h3")[3],"img_url": img_url_rel_d}
    ]

    variables_dict = [
        {"Latest News Title": news_title, 
        "Latest News Paragraph": news_intro_paragraph,
        "Featured Image URL": img_url_rel,
        "Hemisphere 1": cerberus,
        "Hemisphere 2": schiaparelli,
        "Hemisphere 3": syrtis_major,
        "Hemisphere 4": valles_marineris,
        "Hemisphere Images": mars_dict}
    ]
    # variables["Latest News Title"]=soup.find("div", class_="content_title").get_text
    # variables["Latest News Paragraph"]=soup.find("div", class_="article_teaser_body").get_text
    # variables["Featured Image URL"]=soup.find("img", class_="fancybox-image").get_text
    # variables["Hemisphere 1"]=soup.find_by_tag(browser.find_by_tag('a')[3]).get_text
    # variables["Hemisphere 2"]=soup.find_by_tag(browser.find_by_tag('a')[3]).get_text
    # variables["Hemisphere 3"]=soup.find(browser.find_by_tag('a')[3]).get_text
    # variables["Hemisphere 4"]=soup.find(browser.find_by_tag('a')[3]).get_text

    
    
    browser.quit()

    return variables_dict








