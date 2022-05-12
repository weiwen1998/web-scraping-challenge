#!/usr/bin/env python
# coding: utf-8

# In[1]:

def scrape_info():
        from splinter import Browser
        from bs4 import BeautifulSoup as bs
        import time
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        import pandas as pd


        # In[2]:


        # In[3]:


        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)


        # In[4]:


        url = "https://redplanetscience.com/"
        browser.visit(url)


        # In[5]:


        time.sleep(1)


        # In[6]:


        html=browser.html
        soup=bs(html, 'html.parser')
        element=soup.select_one('div.list_text')


        # In[7]:


        news_title=element.find("div", class_="content_title").text


        # In[10]:


        soup.find_all("div", class_="content_title")[0].text


        # In[9]:


        news_intro_paragraph=element.find("div", class_="article_teaser_body").text


        # In[11]:


        featured_image_url = "https://spaceimages-mars.com/"
        browser.visit(featured_image_url)


        # In[12]:


        full_image_elem = browser.find_by_tag('button')[1]
        full_image_elem.click()


        # In[13]:


        html=browser.html
        img_soup = bs(html, 'html.parser')


        # In[14]:


        img_url_rel = img_soup.find("img", class_="fancybox-image").get('src')


        # In[15]:


        facts_url = "https://galaxyfacts-mars.com/"
        browser.visit(facts_url)


        # In[16]:


        tables = pd.read_html(facts_url)


        # In[17]:


        type(tables)


        # In[18]:

        df = pd.read_html('https://galaxyfacts-mars.com')[0]

        df.columns = ['Description', 'Mars', 'Earth']
        df.set_index('Description', inplace=True)
        df = df.to_html(classes="table table-striped")
 


        # In[19]:


        hemispheres_url="https://marshemispheres.com/"
        browser.visit(hemispheres_url)


        # In[21]:


        html=browser.html
        soup=bs(html, 'html.parser')
        element_a=soup.select_one('h3.list_text')


        # In[23]:


        cerberus=soup.find_all("h3")[0].text


        # In[24]:


        schiaparelli=soup.find_all("h3")[1].text


        # In[25]:


        syrtis_major=soup.find_all("h3")[2].text


        # In[26]:


        valles_marineris=soup.find_all("h3")[3].text


        # In[27]:


        cerberus_url="https://marshemispheres.com/cerberus.html"
        browser.visit(cerberus_url)


        # In[28]:


        cerberus_elem = browser.find_by_tag('a')[3]
        cerberus_elem.click()


        # In[29]:


        html=browser.html
        img_soup = bs(html, 'html.parser')


        # In[30]:


        img_url_rel_a = img_soup.find("img", class_="wide-image").get('src')


        # In[31]:


        schiaparelli_url="https://marshemispheres.com/schiaparelli.html"
        browser.visit(schiaparelli_url)


        # In[32]:


        schiaparelli_elem = browser.find_by_tag('a')[3]
        schiaparelli_elem.click()


        # In[33]:


        html=browser.html
        img_soup = bs(html, 'html.parser')


        # In[34]:


        img_url_rel_b = img_soup.find("img", class_="wide-image").get('src')


        # In[35]:


        syrtis_major_url="https://marshemispheres.com/syrtis.html"
        browser.visit(syrtis_major_url)


        # In[36]:


        syrtis_major_elem = browser.find_by_tag('a')[3]
        syrtis_major_elem.click()


        # In[37]:


        html=browser.html
        img_soup = bs(html, 'html.parser')


        # In[38]:


        img_url_rel_c = img_soup.find("img", class_="wide-image").get('src')


        # In[39]:


        valles_marineris_url="https://marshemispheres.com/valles.html"
        browser.visit(valles_marineris_url)


        # In[40]:


        valles_marineris_elem = browser.find_by_tag('a')[3]
        valles_marineris_elem.click()


        # In[41]:


        html=browser.html
        img_soup = bs(html, 'html.parser')


        # In[42]:


        img_url_rel_d = img_soup.find("img", class_="wide-image").get('src')


        # In[45]:


        mars_dict = [
        {"title": cerberus,"img_url": img_url_rel_a},
        {"title": schiaparelli,"img_url": img_url_rel_b},
        {"title": syrtis_major,"img_url": img_url_rel_c},
        {"title": valles_marineris,"img_url": img_url_rel_d}
        ]


        featured_image_url = featured_image_url + img_url_rel

        # In[47]:


        browser.quit()


        # In[50]:


        mars = {"Latest_News_Title": news_title, 
                "Latest_News_Paragraph": news_intro_paragraph,
                "Featured_Image": featured_image_url,
                "Featured_Image_URL": img_url_rel,
                "Facts_Table": df,
                "Hemispheres": mars_dict}
                

        return mars