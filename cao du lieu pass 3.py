
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#### khoi tao Weddriver
driver = webdriver.Chrome()
# mo trang
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name"
driver.get(url)

#doikhoang2giay
time.sleep(2)
#lay tat ca cac the
tags = driver.find_elements(By .XPATH, "//a[contains(@title, 'List of painters')]")
#tao ra danh cac the <a>
links = [ tag.get_attribute("href") for tag in tags ]
#xuatthongtin
for link in links:
    print(link)
###dong wwed
driver.quit()