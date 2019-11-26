# Author:	Duan Le
# Date:		26th Nov, 2019
# python3

"""
What: Get text and remove newline in lines and then copy to clipboard
Why: I usually copy text in paper research and I get problems -> I resolve it.
How: I replace \n\r with space, and then use "Tk" module to create clipboard and addpend.
When: Remove newline in paragraph message
Where: Copy from pdf
"""

try:
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk

def remove_newline(text, *args, **kwargs):
	
	""" remove \n\r in text and then replace it with space"""

	if type(text) is str:
	
		return text.replace('\r', '').replace('\n', ' ')
	
	else:
		print("get error input")
		return text

if __name__ == "__main__":

	r = Tk()
    
	r.withdraw()

	exit_text = ""
	while not exit_text == "q": # because my keyboard is broken, You can alter logical
		
		exit_text = input()

		input_text = r.clipboard_get()

		r.clipboard_clear()
		r.clipboard_append(remove_newline(input_text))

	r.destroy()