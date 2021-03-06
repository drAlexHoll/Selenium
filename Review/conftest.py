import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption('--browser_name', action='store', default = None, help = "Choose browser: chrome or firefox")
	parser.addoption('--language', action='store', default = None, help = "Choose language ru, eng, fr, etc...")


@pytest.fixture(scope="function")
def browser(request):
	browser_name = request.config.getoption("browser_name")
	browser = None
	user_language = request.config.getoption("language")

	if browser_name == "chrome":
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		print("\nstart CHROME browser for test")
		browser = webdriver.Chrome(options=options)
		
	elif browser_name == "firefox":
		print("\nstart FIREFOX browser for test")
		browser = webdriver.Firefox(executable_path='C:\\firefoxdriver\\geckodriver.exe')

	else:
		raise pytest.UsageError("--browser_name should be chrome or firefox")

	yield browser
	time.sleep(10)
	print("\nquit browser")
	browser.quit()