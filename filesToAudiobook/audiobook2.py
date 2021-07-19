import pyttsx3
import pdfplumber
import PyPDF2
import os


folder = "/home/colton/Documents/Readings/filesToAudiobook"
files = os.listdir(folder)

for file in files:
	pdfFileObj = open(file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdFileobj)
	pages = pdfReader.numPages
	with pdfplumber.open(file) as pdf:
		#Loop through the number of pages
		page = pdf.pages[i]
		text = page.extract_text()
		print(text)
		speaker = pyttsx3.init
		speaker.say(text)
		speaker.runAndWait()