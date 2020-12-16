from selenium import webdriver
import time
from datetime import datetime
import os

def scrapeTradingview(d):
    # go to tradingview silver
    print("scraping tradingview")
    d.get("https://www.tradingview.com/symbols/COMEX-SI1%21/technicals/")
    time.sleep(5)

    #find signal
    signal = d.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[2]/div[2]/span[2]')
    print("finished scraping tradingview")
    return signal.text

def logInTwitter(d, user, pw):
    # go to twitter login
    print("logging into twitter")
    d.get("https://twitter.com/login")
    time.sleep(2)

    #find user/pass box and fill in credentials
    userBox = d.find_element_by_xpath('//input[@name="session[username_or_email]"]')
    userBox.send_keys(user)
    passBox = d.find_element_by_xpath('//input[@name="session[password]"]')
    passBox.send_keys(pw)
    time.sleep(2)

    #click login button
    d.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div/span/span').click()
    time.sleep(1)

    print("logged in")
    return

def makeTweet(d, tweet_text):
    #go to compose tweet
    print("composing tweet")
    d.get("https://twitter.com/compose/tweet")
    time.sleep(2)
    #enter in tweet text
    tweetBody = d.find_element_by_xpath('//div[@aria-label="Tweet text"]')
    tweetBody.send_keys(tweetText)
    time.sleep(2)

    #tweet message
    tweetButton = d.find_element_by_xpath('//span[text()="Tweet"]')
    tweetButton.click()
    print("tweet sent")
    return

### main ###
#if os.path.isdir("/home/ubuntu"):
 #   from pyvirtualdisplay import Display
  #  display = Display(visible=0, size=(800,600))
   # display.start()

driver = webdriver.Chrome()

silverRecommend = scrapeTradingview(driver)

logInTwitter(driver, "eb11697317", "autoeb()")

# dd/mm/YY H:M:S
dateTimeString = datetime.now().strftime ("%m/%d/%Y %H:%M:%S")
#str(dateTimeString)
tweetText = "It is recommended to " + silverRecommend + " silver futures at " + dateTimeString

makeTweet(driver, tweetText)
