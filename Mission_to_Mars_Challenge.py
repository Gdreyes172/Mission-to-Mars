#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=2)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)


# In[4]:


#Setting up the HTML parser
# Parse the resulting html with soup
html = browser.html
item_soup = soup(html, 'html.parser')
slide_elem = item_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')


# In[5]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[6]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
item_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
img_url_rel = item_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[ ]:


# Visit URL
url = 'https://galaxyfacts-mars.com'
browser.visit(url)

# Using.read_html() to create a DataFrame using pandas
marspp_df = pd.read_html('https://galaxyfacts-mars.com')[0]
marspp_df.columns=['description', 'Mars', 'Earth']
marspp_df.set_index('description', inplace=True)
marspp_df

marspp_df.to_html()


# In[ ]:


browser.quit()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[14]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Use the parent element to find the paragraph text
for x in range(4):
    mars_dict = {}
    browser.find_by_css('a.product-item h3')[x].click()
    attr = browser.find_link_by_text('Sample').first
    img_url = attr['href']
    title = browser.find_by_css("h2.title").text
    mars_dict["img_url"] = img_url
    mars_dict["title"] = title
    hemisphere_image_urls.append(mars_dict)
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# 5. Quit the browser
browser.quit()

