from PIL import Image
import pytesseract
import datetime
import mysql.connector

im = Image.open("sample1.jpg")

text = pytesseract.image_to_string(im, lang='eng')

cnx = mysql.connector.connect(user='vishal', password='vishal',
                              host='127.0.0.1',
                              database='GDG')
cursor = cnx.cursor()

query = ("SELECT NumberPlate FROM Central")

cursor.execute(query)
flag=1
for name in cursor:
	if(text == name[0]):
		print("Car Found")
		flag=0
if(flag==1):
	print("Car not Found")
cursor.close()
cnx.close()
