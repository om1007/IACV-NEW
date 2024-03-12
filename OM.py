!pip install easyocr deep_translator matplotlib

import cv2
import matplotlib.pyplot as plt
import easyocr
from deep_translator import GoogleTranslator

# Read the image (ensure correct format)
img = cv2.imread(r"/content/bul.PNG", cv2.IMREAD_COLOR)

# Initial variables for successful translation
translated_text = []
target_language_detected = False

# Iterate through language groups until a translation is found
for languages in [
  #  ['en', 'hi', 'mr', 'ne'],
  #  ['en', 'ar', 'fa', 'ur'],
  #  ['en', 'fr', 'es', 'ga', 'de'],
  #  ['ch_tra', 'en'],
  #  ['ch_sim', 'en'],
  ['en', 'ru', 'rs_cyrillic', 'bg', 'uk', 'mn', 'be'],
  #  ['te', 'en'],
  #  ['ta', 'en'],
   # ... other language groups ...
]:
   reader = easyocr.Reader(languages, gpu=False)
   text_ = reader.readtext(img)

   translator = GoogleTranslator(source='auto', target='en')
   for t in text_:
       bbox, text, score = t
       translated = translator.translate(text)
       translated_text.append((bbox, translated, score))

       # Indicate successful translation and break the loop
       target_language_detected = True
       break

   if target_language_detected:
       break

# Only draw bounding boxes and text if translation was successful
if translated_text:
   for bbox, text_to_display, score in translated_text:
       x1, y1 = int(bbox[0][0]), int(bbox[0][1])  # Top-left corner
       x2, y2 = int(bbox[2][0]), int(bbox[2][1])  # Bottom-right corner
       text_origin = (x1, y1)
       cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
       cv2.putText(img, text_to_display, text_origin, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

   plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
   plt.show()
else:
   print("Translation unsuccessful. Language not found in supported groups.")
