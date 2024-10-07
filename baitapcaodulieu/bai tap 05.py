import re

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import requests

#tao ra noi data frame vaf data farm rong
d = pd.DataFrame({'name': [], 'birth' : [], 'death' : [], 'nationality' : []})


#########################################################################
driver = webdriver.Chrome()
for i in range(65, 68 ):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"

