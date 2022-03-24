In [1]: from selenium import webdriver



In [2]: driver = webdriver.Chrome('./chromedriver.exe')



In [3]: driver.get('https://www.linkedin.com')



In [4]: username = driver.find_element(by='id', value='session_key')



In [5]: username.send_keys('MAIL-COMES-HERE')



In [6]: password = driver.find_element(by='id', value='session_password')



In [7]: password.send_keys('PASSWORD-COMES-HERE')



In [8]: from selenium.webdriver.common.by import By



In [9]: log_in_button = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")



In [10]: log_in_button.click()



In [12]: driver.get('https://www.google.com')



In [13]: search_query = driver.find_element(By.NAME, "q")



==> site:linkedin.com/in/ AND "React.js" AND "Paris" ==> Will return 10 Linkedin Profile in Paris with React.js knowledge.



In [14]: search_query.send_keys('site:linkedin.com/in/ AND "React.js" AND "Paris"')



In [15]: from selenium.webdriver.common.keys import Keys



In [16]: search_query.send_keys(Keys.RETURN)





````````````````````````````````````````````````````````````````````````````````````

// checking the length of the scrapped websites ==> Should be 10, but here some advertisement are being called by the cite class. We must search for a unique identifier for jsut the links needed. 



In [17]: linkedin_urls = driver.find_elements(By.TAG_NAME, "cite")



In [18]: len(linkedin_urls)

Out[18]: 18





After many retries, I ended up finding this class



In [19]: linkedin_urls = driver.find_elements(By.CLASS_NAME, "yuRUbf")



In [20]: len(linkedin_urls)

Out[20]: 10



OR 



In [236]: linkedin_urls = driver.find_elements(By.CLASS_NAME, "tF2Cxc")



In [237]: linkedin_urls = [url.text for url in linkedin_urls]



In [238]: linkedin_urls





OR 



In [242]: linkedin_urls = driver.find_elements(By.CLASS_NAME, "NJo7tc ")



In [243]: linkedin_urls = [url.text for url in linkedin_urls]



In [244]: linkedin_urls



==========================================================================

{{{[ ONLY FOR INFORMATION WITHOUT LINK]}}}} 

In [254]: linkedin_urls = driver.find_elements(By.CLASS_NAME, "LC20lb ")



In [255]: linkedin_urls = [url.text for url in linkedin_urls]



In [256]: linkedin_urls

===========================================================================



To avoid extracting unwanted advertisements, we will only specify the "yuRUbf" class to ensure we only extract LinkedIn profile URL's.



````````````````````````````````````````````````````````````````````````````````````



In order to work with the new classes please use this one:  YESS

In [265]: linkedin_urls = driver.find_elements(By.CLASS_NAME, "yuRUbf")

In [266]: links = [url.find_element(By.CSS_SELECTOR, 'a').text for url in linkedin_urls]



In [269]: profile = [url.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for url in linkedin_urls]



In [270]: profile

Out[270]:


 'https://fr.linkedin.com/in/dXXXXXXXX',
 'https://fr.linkedin.com/in/dXXXXXXXX',
 'https://fr.linkedin.com/in/dXXXXXXXX',
 'https://fr.linkedin.com/in/dXXXXXXXX',
 'https://fr.linkedin.com/in/dXXXXXXXX',
 'https://fr.linkedin.com/in/dXXXXXXXX',
 'https://fr.linkedin.com/in/dXXXXXXXX',
 'https://fr.linkedin.com/in/dXXXXXXXX',
 'https://fr.linkedin.com/in/dXXXXXXXX']





In [21]: linkedin_urls = [url.text for url in linkedin_urls]





