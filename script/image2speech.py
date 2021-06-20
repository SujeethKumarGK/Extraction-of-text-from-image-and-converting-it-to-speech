# importing modules for image extraction
from googletrans import Translator
import easyocr # ocr = optical character recognition
from gtts import gTTS # gtts = google text to translate
from IPython.display import Audio #to save & play the audio

lang = "kn" #to specify what langauge is present in the image
reader = easyocr.Reader([lang])  #for recognizing the language in the image
import PIL  # PIL is Python Imaging Language used for image processing techniques
from PIL import ImageDraw #used to draw the bounding boxes around the text
#***********************************************************************************************#

img1 = "pic" + str('.jpeg') #to get the image 
im=PIL.Image.open(img1)   # for reading the image
bounds=reader.readtext(img1, add_margin=0.3,width_ths=2.0,link_threshold=0.8,decoder='beamsearch',blocklist='=-')  # for reading the text in the image
print(bounds) #printing the values of recongnized OCR language

#***********************************************************************************************#
# for making the boundung bozes around the texts
def draw_boxes(image, bounds, color='yellow',width=2): # function to draw bounding boxes around the text
    draw=ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image
draw_boxes(im,bounds)
im.show() #shows the image with bounding box around the featured text
#***********************************************************************************************#
# to extract and  print the text from the image
text_list=reader.readtext(img1 ,link_threshold=0.8,add_margin=0.55,width_ths=0.7,decoder='beamsearch',blocklist='=-',detail=0)
print(text_list) #printing the text present in the image without displaying OCR values

text_comb=' '.join(text_list)     #to join and print the text as a single string
print(text_comb)
#***********************************************************************************************#
#to print the text as a single string
translator = Translator()
print(translator.detect(text_comb))    #calling the method in class Translator to detect the language in the text
#***********************************************************************************************#
text_en=translator.translate(text_comb,src=lang,dest='en')     # to convert the text from given language to english
print(text_en.text)
# to translate the text to audio file
ta_tts=gTTS(text_en.text) #usesd to change text to destination language
ta_tts.save('english.mp3')
Audio('english.mp3',autoplay=True)  # with us accent

#with indian accent
ta_tts=gTTS(text_en.text,lang='hi')    #with the change in  dest location(lang=hi here we used indian accent)  we can get that that location accent
ta_tts.save('hi_english.mp3')
Audio('hi_english.mp3',autoplay=True)   #with indian accent
#***********************************************************************************************#
#to change the text to indian language(hindi)
text_hi=translator.translate(text_comb, src=lang, dest='hi')
print(text_hi.text)
ta_tts_hi=gTTS(text_hi.text, lang='hi')
ta_tts_hi.save('hindi.mp3')
Audio('hindi.mp3',autoplay=True)
#***********************************************************************************************#
#to change the language to telugu
text_te=translator.translate(text_comb,src=lang,dest='te')
print(text_te.text)
ta_tts_te=gTTS(text_te.text,lang='te')
ta_tts_te.save('telugu.mp3')
Audio('telugu.mp3',autoplay=True)
#************************************************************************************************#
#to change the language to french
text_fr=translator.translate(text_comb,src=lang,dest='fr')
print(text_fr.text)
ta_tts_fr=gTTS(text_fr.text,lang='fr')
ta_tts_fr.save('french.mp3')
Audio('french.mp3',autoplay=True)




