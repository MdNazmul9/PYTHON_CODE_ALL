import cv2
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Tesseract-OCR\tesseract.exe'

img = cv2.imread('./BreakingNews.png')
text = pytesseract.image_to_string(img)
print(text)

img = cv2.imread('./BitCoin.jpeg')
text = pytesseract.image_to_string(img)
print(text)