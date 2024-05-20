from selenium import webdriver
from selenium.webdriver.chrome.service import Service

web = "https://leetcode.com/problemset/?page=20"
path = "C:\Program Files (x86)\chromedriver.exe"

file = open("leetcode-scraper-2.txt", "w")

service = Service(executable_path = path)
driver = webdriver.Chrome(service = service)

driver.get(web)

problems = driver.find_elements(by = "xpath", value = "//div[contains(@class, 'odd:bg-layer-1')]")

for problem in problems:
    file.write("{\n")
    file.write("\tproblemName: " + "\"" + problem.find_element(by = "xpath", value = ".//a[contains(@class, 'h-5')]").text + "\",\n")
    file.write("\tdifficulty: " + "\"" + problem.find_element(by = "xpath", value = ".//div[contains(@style, 'flex: 84 0 auto')]").text + "\",\n")
    file.write("\tleetCodeLink: " + "\"" + problem.find_element(by = "xpath", value = ".//a[contains(@class, 'h-5')]").get_attribute("href") + "\",\n")
    file.write("\tsolutionLink: \"#\"\n")
    file.write("},\n")

file.close()
driver.quit()

