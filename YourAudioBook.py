import pyttsx3
import PyPDF2

book = open('book_name.pdf', 'rb')  # reading the book in read binary mode
PDFReader = PyPDF2.PdfFileReader(book)
pageCount = PDFReader.getNumPages()
talk = pyttsx3.init()

for num in range(0, pageCount):  # loop to read the content of the book upTo pageCount of the book
    page = PDFReader.getPage(num)
    text = page.extractText()
    talk.say(text)
    talk.runAndWait()
