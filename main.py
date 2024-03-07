import pyttsx3
import PyPDF2

speaker = pyttsx3.init()

with open("book.pdf", "rb") as book:
    pdfreader = PyPDF2.PdfReader(book)
    full_text = ""

    for page_num in range(len(pdfreader.pages)):
        page = pdfreader.pages[page_num]
        text = page.extract_text()
        if text:
            clean_text = text.strip().replace("\n", " ")
            print(clean_text)
            full_text += clean_text + " "

speaker.save_to_file(full_text, "audio.mp3")

speaker.runAndWait()

speaker.say(full_text)

speaker.runAndWait()

speaker.stop()
