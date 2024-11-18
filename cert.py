from PIL import Image, ImageDraw, ImageFont #these modules used to write on a IMAGE
import pandas as pd #to analyze CSV files
import os

#paths to template certificate
template_path = "template/certificate.png"
output_folder = "output/" #where should the finished certificates be.
#you can change the font according to your needs its not nesscary you should use only this font 
#to get fonts visit https://fonts.google.com/
font_path = "font/cert_font.ttf"  #ensure you include path for readable font

#load data (CSV with Name, Email columns)
data = pd.read_csv("participants.csv")

#generate certificates
for index, row in data.iterrows():
    name = row['Name'] #if your name row has diff name please replace the "Name" to the respective words
    cert = Image.open(template_path)
    draw = ImageDraw.Draw(cert)
    
    #customize font and placement
    font = ImageFont.truetype(font_path, 60)  #adjust font size
    text_x, text_y = 800, 710  #please check out my repo video of how to set values
    draw.text((text_x, text_y), name, fill="white", font=font)
    output_folder = "output/"  # Folder where certificates will be saved
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Automatically create the folder if missing

    output_path = f"{output_folder}{name}_certificate.png"#the o/p file 
    cert.save(output_path)
    print(f"Certificate saved for {name}")
#dev@127.4.7.8
