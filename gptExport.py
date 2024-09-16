from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import time

loadTime = 3            #seconds
responseWaitTime = 8 

chatGPT = "https://www.openai.com/chatgpt"
HTMLinputID = "prompt-textarea"

debug = 1
def d(message):
    if debug == 1:
        print(message)

def checkLogin():
    #if exists:
    <div role="dialog" id="radix-:r0:" aria-describedby="radix-:r2:" aria-labelledby="radix-:r1:" 
    data-state="open" class="popover relative start-1/2 col-auto col-start-2 row-auto row-start-2 h-full w-full bg-token-main-surface-primary text-start shadow-xl ltr:-translate-x-1/2 rtl:translate-x-1/2 rounded-2xl flex flex-col focus:outline-none max-w-[373px] sm:max-w-[400px]" 
    tabindex="-1" style="pointer-events: auto;"><div class="flex-grow overflow-y-auto"><div class="flex flex-col items-center justify-center px-6 py-8 sm:px-10 sm:pb-10 sm:pt-12">
    <p class="mb-1 text-center text-2xl font-semibold">Thanks for trying ChatGPT</p><p class="mb-6 text-center text-token-text-secondary">Log in or sign up to get smarter responses, upload files and images, and more.
    </p><div class="flex w-full flex-col gap-2 sm:gap-2.5">
    <button class="btn relative btn-primary btn-large w-full" as="button"><div class="flex items-center justify-center">
    Log in</div></button><button class="btn relative btn-secondary btn-large w-full" as="button"><div class="flex items-center justify-center">Sign up</div></button></div><a href="#" 
    class="mt-5 cursor-pointer text-sm font-semibold text-token-text-secondary underline">Stay logged out</a></div></div></div>

    #click: <a href="#" class="mt-5 cursor-pointer text-sm font-semibold text-token-text-secondary underline">Stay logged out</a>

d("Starting program!")

browserOptions  = FirefoxOptions()
#browserOptions.add_argument("--headless")
driver = webdriver.Firefox(options=browserOptions)
d("Firefox initialized...")

driver.get(chatGPT)
time.sleep(loadTime) #use WebDriverWaitt

d("GPT Loaded.\n")

#checkLogin()
time.sleep(loadTime)

while(True):
    inputField = driver.find_element(By.ID, HTMLinputID)
    d("Entry field identified.")
    inputChoice = input("/nEnter your input: ")
    if (inputChoice == "end"):
        break
    # input_field.send_keys(inputChoice)
    # send_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Send prompt"]')
    # send_button.click()

    # time.sleep(responseWaitTime)

    # # Read the response (replace with the actual element identifier)
    # paragraph = WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located((By.XPATH, '//div[@class="markdown prose w-full break-words dark:prose-invert light"]/p'))
    # )
    # response = paragraph.text

    # print(response)

    

driver.quit()