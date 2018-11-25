from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('chromedriver.exe') 

driver.maximize_window()

driver.get("http://www.khitguntur.com/jntuk-results/") 
wait = WebDriverWait(driver, 600) 

x_arg = '//a[@href="results/jntuk-bt-1-2-r16-results-may-2018.html"]'
R16_12_Results = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 
R16_12_Results.click()

string='178x1a0585'

inp_xpath = '//input[@id="ht"]'
input_box = wait.until(EC.presence_of_element_located(( 
	By.XPATH, inp_xpath))) 
input_box.send_keys(string + Keys.ENTER) 

results = wait.until(EC.presence_of_element_located(( 
	By.XPATH, "//div[@id='rs']/table/tbody/tr[2]/td[2]"))) 

resultstext = driver.find_element_by_xpath("//div[@id='rs']/table").text

print(resultstext)

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600)




target = 'Techgigs'

# Replace the below string with your own message 


x_arg = '//span[@title="'+ target + '"]'
print(x_arg)
group_title = wait.until(EC.presence_of_element_located(( 
	By.XPATH, x_arg))) 
group_title.click() 
inp_xpath = '//div[text()="Type a message"]/following::div'
input_box = wait.until(EC.presence_of_element_located(( 
	By.XPATH, inp_xpath))) 
input_box.send_keys(resultstext+ Keys.ENTER) 
