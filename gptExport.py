from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

print("Running script!")
# Set up the WebDriver (make sure you have ChromeDriver installed and in your PATH)
browserOptions  = FirefoxOptions()
browserOptions.add_argument("--headless")

driver = webdriver.Firefox(options=browserOptions)

# Open the ChatGPT webpage (replace with the actual URL)
driver.get("https://www.openai.com/chatgpt")

# Allow time for the page to load
time.sleep(5)

while(True):
    # Locate the input field (replace with the actual element identifier)
    input_field = driver.find_element_by_xpath('//textarea[@name="prompt-textarea"]')
    inputChoice = input("Enter your input: ")
    if (inputChoice == "end"):
        break
    input_field.send_keys(inputChoice)
    send_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Send prompt"]')
    send_button.click()

    #input_field.send_keys(Keys.RETURN)

    # Allow time for the response to be generated
    time.sleep(5)

    # Read the response (replace with the actual element identifier)
    paragraph = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="markdown prose w-full break-words dark:prose-invert light"]/p'))
    )
    response = paragraph.text

    print("ChatGPT response:", response)

    # Close the WebDriver

driver.quit()
