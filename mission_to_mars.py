# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
import requests
import pandas as pd

def title_scrape():
    
    data = {}
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)  # Retrieve page with the requests module
    soup = bs(response.text, 'html.parser') # Create BeautifulSoup object; parse with 'html.parser'
    
    #collect the latest News Title and Paragragh Text.
    data['title'] = soup.find('div',class_='content_title').find('a').text

    data['paragraph'] = soup.find('div',class_='rollover_description_inner').text

    
    return (data)



#JPL Mars Space Images - Featured Image

def image_link():

    path = {}
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.find_link_by_partial_text('FULL').first.click()
    html = browser.html
    
    soup = bs(html, 'html.parser')


    image =  soup.find('a',class_='button')


    link = image['data-link']

    image_url = 'https://www.jpl.nasa.gov' + str(link)

    browser.visit(image_url)

    html2 = browser.html
    soup2 = bs(html2, 'html.parser')

    jpeg_image = soup2.find('figure',class_='lede')
    
    final_jpeg = jpeg_image.a['href']

    featured_image_url = 'https://www.jpl.nasa.gov' + str(final_jpeg)

    path["src"] = featured_image_url

    return (path)

#Mars Weather Data from Twitter

def tweet_response():
    weather = {}
    weather_response = requests.get('https://twitter.com/marswxreport?lang=en')
    soup3 = bs(weather_response.text, 'html.parser')

    weather_result = soup3.find(class_="content")

    weather['today'] = weather_result.find('p', class_="TweetTextSize").text

    return(weather)



#Mars Facts

def table_data():
    url = 'http://space-facts.com/mars/'
    table = pd.read_html(url)
    table_df = table[0]
    table_df.columns = ['Parameters' , 'Values']
    table_df.set_index('Parameters', inplace = True)
    html_table = table_df.to_html()

    return (html_table)

