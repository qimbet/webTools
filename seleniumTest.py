from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

browserOptions  = FirefoxOptions()
browserOptions.add_argument("--headless")

driver = webdriver.Firefox(options=browserOptions)
startupPage = "https://en.wikipedia.org/wiki/Main_Page"
contentTarget = "Today's featured article: "

driver.get(startupPage)
print(f"Firefox initialized, {startupPage} initalized\n")

#<h2 id="From_today's_featured_article" class="mp-h2"><span id="From_today.27s_featured_article"></span>From today's featured article</h2>
#ID: mp-tfa
searchParameter = "mp-tfa"

featuredArticle = driver.find_element(By.ID, searchParameter)
#print("Featured Article", featuredArticle)

y = input("Press enter to continue")

mainTitle = featuredArticle.find_element(By.TAG_NAME, "b")
#print("Main title: ", mainTitle)

print(contentTarget + str(mainTitle.text))

while(True):
    x = input("Press enter on a blank line to end the program, or enter a value to try again:\n")
    if(x == ""):
        break
    