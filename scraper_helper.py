from selenium import webdriver
import os

class Driver:

	def __init__(self, driver_path : str, download_path : str):
		
		"""Initialize chrome browser with given download path"""

		# Preferences
		ops = webdriver.ChromeOptions()
		preferences = {'download.default_directory' : download_path, "plugins.always_open_pdf_externally": True}
		ops.add_experimental_option('prefs', preferences)

		self.download_path = download_path
		self.browser = webdriver.Chrome(executable_path= driver_path, options = ops)
	
	def do_func_on_list_containing_text(self, text : str, function):

		"""Does passed function on each item in the list containing given text
		function call: function(obj = list_item)"""

		item_count = len(self.browser.find_elements_by_partial_link_text(text))

		for i in range(item_count):
			items = self.browser.find_element_by_partial_link_text(text)
			function(obj = items[i])

	def click_do_func_back(self, obj : webdriver.Chrome._web_element_cls, function):

		"""Calls click on given web element, does function, and goes to previous page"""

		obj.click()
		function()
		self.browser.back()
	

	def is_downloading(self) -> bool:
		"""Checks to see if any files are currently downloading"""
	
		doc_names = os.listdir(self.download_path)
		for name in doc_names:
			if ".crdownload" in name:
				return True
		return False
	
	@staticmethod
	def clean_string(s:str):

		"""Clean file names for downloads to windows"""

		windows_naughty_char = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]

		s = s.strip()
		clean = ""

		for c in s:
			if c in windows_naughty_char:
				clean += " "
			else:
				clean += c

		clean = clean.strip()
			
		return clean

	@staticmethod
	def is_image(s: str):

		"""Checks if given file is an image"""

		types = [".jpg", ".jpeg", ".png", ".img", ".txt"]
		for t in types:
			if t in s.lower():
				return True
		return False
		
	