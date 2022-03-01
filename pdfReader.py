from gtts import gTTS
import pdfplumber, time
import os

language = 'en'
pathToFile = 'path/to/your/pdf/file.pdf' # Change this variable to your desired path

file = pdfplumber.open(pathToFile)
pages = file.pages

for i,pg in enumerate(pages):
    print("Converting page_{}...".format(i))
    text = pages[i].extract_text()
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("page_{}.mp3".format(i))
    print("Page_{} saved successfully!".format(i))

# Uncomment this section to play audio from terminal
# Make sure mpg321 is installed to use this feature.

# ask = input("Do you want to read PDF page by page?(Y/n): ")
# if ask == "Y" or ask == 'y':
#     # os.system("mpg321 page_0.mp3".format(i))
#     for j in range(i):
#         os.system("mpg321 page_{}.mp3".format(j))
