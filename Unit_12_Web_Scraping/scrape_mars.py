from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #news title
    newsTitle = soup.find("div", {"class" : "content_title"})
    newsTitle.text

    titleLink = newsTitle.find("a").text
    titleLink

    # News description
    body = soup.find_all("div", class_="article_teaser_body")[0].text
    body

    #images mars
    url_img = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_img)

    html_1 = browser.html
    soup_1 = BeautifulSoup(html_1, 'lxml')

    featImage = soup_1.find_all("article", class_= "carousel_item")
    featImage

    link_1 = soup_1.find_all("a", class_="fancybox")[1]["data-fancybox-href"]

    frontBit = "https://www.jpl.nasa.gov"

    fullLink_featImage = frontBit + link_1
    fullLink_featImage

    #tweets
    url_twitter = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_twitter)

    html_twitter = browser.html
    soup_twitter = BeautifulSoup(html_twitter, 'lxml')

    tweet = soup_twitter.find('p', {"class": "tweet-text"})
    tweet

    weather = tweet.text
    weather

    #Mars Facts

    url_fact = "https://space-facts.com/mars/"
    tables = pd.read_html(url_fact)
    df = tables [0]
    df.columns = ['Variables', 'Values']
    df.set_index('Variables', inplace=True)
    df

    mars_table = df.to_html()

    #Mars Hemispheres
    url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser = Browser('chrome', headless=True)
    browser.visit(url_hemisphere)
    html_hemisphere = browser.html
    soup_hemisphere = BeautifulSoup(html_hemisphere, 'html.parser')
    browser.quit()

    links = []
    a = soup_hemisphere.find_all("a", class_="itemLink product-item")
    for x in range(len(a)):
        link = "https://astrogeology.usgs.gov" + a[x]["href"]
        if link not in links:
            links.append(link)
    links

    hemisphere_image_urls = []
    for x in range(len(links)):
        browser = Browser('chrome', headless=True)
        browser.visit(links[x])
        html_hemisphere = browser.html
        soup_hemisphere = BeautifulSoup(html_hemisphere, 'html.parser')
        url_astro = 'https://astrogeology.usgs.gov' + soup_hemisphere.find("img", class_="wide-image")["src"]
        title = soup_hemisphere.find("h2", class_="title").text
        dic = {"title": title, "img_url": url_astro}
        hemisphere_image_urls.append(dic)
    hemisphere_image_urls

    # Close the browser after scraping
    browser.quit()

    # Return results
    data = {
        'head': titleLink,
        'body': body,
        'image': fullLink_featImage,
        'weather': weather,
        'table': mars_table,
        'hems': hemisphere_image_urls
    }

    return data
