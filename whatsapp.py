from selenium import webdriver

# driver=webdriver.Chrome() 
driver = webdriver.Chrome(executable_path='E:\coding\personal\python work\whatsapp\drivers\chromedriver.exe')
# driver = webdriver.Chrome('path/to/chromedriver')
driver.get('https://web.whatsapp.com/')

name=input('Enter the name of user group: ')
msg=input('Enter your message: ')
count=int(input('Enter the count'))

input('Enter anything after scanning qr code')

user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
# user=driver.find_element_by_xpath('//span[@title="Harsh CoE10"]')
# WebDriverWait(driver, 10).until(expected_conditions.invisibility_of_element_locate‌​d((By.XPATH, "//input[@id='message']")))
user.click()

msg_box=driver.find_element_by_class_name('_1Plpp')

for i in range(count):
    msg_box.send_keys(msg)
    button=driver.find_element_by_class_name('_35EW6')
    button.click()
    print(i+1)
