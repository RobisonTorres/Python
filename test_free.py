from selenium import webdriver
import sys, subprocess
subprocess.run('cls', shell=True)
print('Test Free')
print()
# crt + D / alt + mouse / alt + up or down / shift + alt + up or down / crt + l
# crt + N .. crt + k, m .. crt + s

#path = r"C:\Users\rcssi\Downloads\geckodriver"
#drive = webdriver.Firefox

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/")
