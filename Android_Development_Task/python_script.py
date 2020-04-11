from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://smallseotools.com/plagiarism-checker/")
searchbox = driver.find_element_by_xpath('//*[@id="textBox"]')
x = input("Enter the string:")
searchbox.send_keys(x)
searchbutton = driver.find_element_by_xpath('//*[@id="checkPlag"]')
searchbutton.click()

y = driver.find_element_by_css_selector('#dialog-message')
print(y)
print('It was copied from : https://smallseotools.com/plagiarism-checker/')