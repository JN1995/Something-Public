# Author:	Duan Le
# Date:		26th Nov, 2019
# python3
# requirement: install xcip or xsel (sudo apt-get install xsel) to system

"""
What: Get text and remove newline in lines and then copy to clipboard
Why: I usually copy text in paper research and I get problems -> I resolve it.
How: I replace \n\r with space, and then use "Tk" module to create clipboard and addpend.
When: Remove newline in paragraph message
Where: Copy from pdf
"""


import time
# from tomorrow import threads
from threading import Thread
import pyperclip
import clipboard

def remove_newline(text, *args, **kwargs):
	
	""" remove \n\r in text and then replace it with space"""

	if type(text) is str:
		
		return text.replace('\r', '').replace('\n', ' ')
	
	else:
		print("get error input")
		return text

# @threads(1)
def listen_to_clipboard():

	
	pass


if __name__ == "__main__":


	try:
		input_text = clipboard.paste()
	except Exception as e:
		print(e)
		input_text = ""

	old_input_text = ""

	while True: # because my keyboard is broken, You can alter logical

		try:
			input_text = clipboard.paste()
		except Exception as e:
			print(e)
			input_text = ""
		
		if not input_text == old_input_text:
			
			old_input_text = remove_newline(input_text)
			# input_text = r.clipboard_get()
			
			
			clipboard.copy(old_input_text)
			

			print(input_text)
			
			time.sleep(2)

		print(old_input_text)
		print(input_text == old_input_text)
		time.sleep(5)