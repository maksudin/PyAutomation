#SberBank
from selenium import webdriver

#optional

baseurl = "https://online.sberbank.ru"
name = "l"
passwd = "p"
xpath = {
	'login' : '//*[@id="login"]',
	'passwd' : '//*[@id="password"]',
	'btn' : '//*[@id="buttonSubmit"]/div[1]/button'
}

mydriver = webdriver.Chrome()
mydriver.get(baseurl)
mydriver.find_element_by_xpath(xpath["login"]).send_keys(name)
mydriver.find_element_by_xpath(xpath["passwd"]).send_keys(passwd)
mydriver.find_element_by_xpath(xpath["btn"]).click()
