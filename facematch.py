# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:24:54 2020

@author: Lenovo
"""
#%%
import streamlit as st 
import face_recognition 
from PIL import Image, ImageDraw, ImageOps, ImageFont
#import imagehash

#%%
language = st.checkbox("Thai Language")
st.title("*Face Match* :dart:")


#%%
if language:
    t = ["**:one: อัพโหลดรูปภาพบุคคลที่คุณต้องการเช็คความเหมือน**", #0
         "อัพโหลดรูปภาพที่หนึ่ง...",    #1
         "รูปภาพที่อัพโหลด",         #2
         "**:two: อัพโหลดรูปภาพที่ต้องการเปรียบเทียบ**",  #3
         "อัพโหลดรูปภาพที่สอง...",   #4
         "รูปภาพที่อัพโหลด",        #5
         "**:mag_right: ถึงเวลาเปรียบเทียบรูปภาพแล้ว**", #6
         "วิธีที่ใช้ในการเปรียบเทียบ:" ,  #7
         "ดูคำอธิบายเพิ่มเติมของวิธีนี้",     #8
         "ในที่นี้ 'Image hash' คือวิธีที่ถูกนำมาใช้ดูความเหมือนในภาพรวมของรูปภาพเท่านั้นว่าเหมือนหรือต่างกันมากน้อยเพียงใด\
         โดยคำนวณค่าของรูปภาพด้วยฟังก์ชั่น average_hash แล้วเปรียบเทียบค่าที่ได้ของทั้งสองรูปภาพ \
         ดังนั้นจึงได้ผลลัพธ์เพียงค่าความเหมือนของภาพ ซึ่งหากต้องการเปรียบเทียบความเหมือนของใบหน้าในแต่ละรูปภาพสามารถเลือกวิธี 'Face distance' ได้", #9
         "คะแนนความหมือนของภาพอยู่ที่ {}%",    #10
         "ในที่นี้ 'Face distance' คือวิธีที่ใช้คำนวณเปอร์เซ็นต์ความคล้ายของใบหน้าระหว่างใบหน้าจากภาพทั้ง 2 ภาพ ซึ่งจะให้ค่าความคล้ายของใบหน้าของคนในรูปภาพที่สองเมื่อเทียบกับรูปภาพแรก\
         ดังนั้นลองอัพโหลดรูปภาพที่สองใหม่โดยนำภาพที่มีคนมากกว่า 1 คน แล้วดูค่าความเหมือนที่ได้ว่ามีใครในภาพเหมือนที่สุด",  #11
         "เราพบใบหน้าของ {} คนในรูปภาพของคุณ" ,  #12
         "**ใบหน้าของคนที่ {} มีความคล้ายกับใบหน้าของคนในภาพแรก {}**" #13
         ]

else:
     t= ["**:one: Upload a person image you would like to check for similarity.**",  #0
        "Upload the 1st image...",      #1
        "Uploaded Image.",      #2
        "**:two: Upload an image to compare.**", #3
        "Upload the 2nd image...",  #4
        "Uploaded Image.",  #5
        "**:mag_right: Now, it's time to compare.**",   #6
        "Method of comparison:", #7
        "See more about method explanation.", #8
        "In this area, 'Image hash' is the method used to find the similarity \
        between 2 images and measure the similarity score of the images using average_hash function. \
        So, there wil let you know only the overall similarity score between the images.\
        If you would like to know more about the Face matching score of the images, please try the method of 'Face distance'.", #9
        "Similarity Score is {}%.", #10
        "In this area, 'Face distance' is the method which lets you know \
        the matching score between faces from the above 2 images. So, there will provide you the matching score of faces in image 2 compared to the first one.\
        Please try uploading the picture of several people in the second image and see the result.",    #11
        "{} Face(s) detected in your image." ,     #12
        "**Matching Score of Face {} is {}**" #13
        ]

st.write(t[0])  
uploaded_file = st.file_uploader(t[1] , type=("png", "jpg","jpeg"))

#video_file = open 
#%%

def findface(file):
    img = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(img, number_of_times_to_upsample=2)
    face_encodings = face_recognition.face_encodings(img, known_face_locations=face_locations,num_jitters=100)
    return img, face_locations, face_encodings
#%%
if uploaded_file is not None:

    #Img1 
    image = Image.open(uploaded_file)
    image = ImageOps.exif_transpose(image) #rotate
    #image.thumbnail((700,1200))
    image.save('rotated.png')
    st.image(image, caption=t[2], use_column_width=True)  
    img1, known_locat ,known_encodings = findface('rotated.png')

        
#%%    
st.write(t[3])  
uploaded_file2 = st.file_uploader(t[4],  type=("png", "jpg","jpeg"))
#%%
if uploaded_file2 is not None:
    #Img2
    unknown_image = Image.open(uploaded_file2)
    unknown_image = ImageOps.exif_transpose(unknown_image) #rotate
    #unknown_image.thumbnail((2400,1600), Image.ANTIALIAS)
    unknown_image.save('rotated2.png')
    st.image(unknown_image, caption=t[5], use_column_width=True)
    img2, unknown_locat, unknown_encodings = findface('rotated2.png')
    
if uploaded_file is not None and uploaded_file2 is not None:
    #img2
    #try:
        
        #unknown_image = Image.open(uploaded_file2)
        #unknown_image = ImageOps.exif_transpose(unknown_image) #rotate
        #unknown_image.thumbnail((2400,1600), Image.ANTIALIAS)
        #unknown_image.save('rotated2.png')
        #st.image(unknown_image, caption=t[5], use_column_width=True)
        #img2, unknown_locat, unknown_encodings = findface('rotated2.png')
            
        
    pill_image = Image.fromarray(img2)
    font = ImageFont.truetype(".\ARLRDBD.TTF", 16)
    draw = ImageDraw.Draw(pill_image)
    
    #choose method to compare
    #method = ['Image hash', 'Face distance'] 
    st.write(t[6])
    st.text(t[7] + "'Face Distance'")
    #select = st.selectbox(t[7], method)
    agree = st.checkbox(t[8])
    #Method 1
    #if select == 'Image hash':
        #if agree:
        #    st.write(f'<div style="color: grey; font-size: small">{t[9]} </div>', unsafe_allow_html=True)                     
     
        
        #hash = imagehash.average_hash(image) 
        #otherhash = imagehash.average_hash(unknown_image) 
        #st.markdown(f'<div style="color: red; font-size: large-bold">{t[10].format(100-(hash-otherhash))} </div>', unsafe_allow_html=True)
    
        #method 2 :
        #else:
    if agree:
        st.write(f'<div style="color: grey; font-size: small">{t[11]} </div>', unsafe_allow_html=True)   
            
    st.markdown(f'<div style="color: red; font-size: large-bold">{t[12].format(len(unknown_locat))} </div>', unsafe_allow_html=True)
        
    i = 1
    for (top, right, bottom, left), unknown_encodings in zip(unknown_locat,unknown_encodings):
        draw.rectangle(((left, top), (right, bottom )), outline = (0,0,0))
   
        result = face_recognition.compare_faces(known_encodings, unknown_encodings)
        distance = face_recognition.face_distance(known_encodings, unknown_encodings)
        text_width, text_height = draw.textsize("{:.2%}".format(1-distance[0])) #"{:.2%}".format(1-distance[0])
        draw.rectangle(((left, bottom- text_height-10),(right, bottom+3)), fill = (0,0,0), outline = (0,0,0))
        draw.text((left+ 5, bottom - text_height-5), "{:.2%}".format(1-distance[0]), font = font,fill = (255,255,255,255))
        st.write(t[13].format(i, "{:.2%}".format(1-distance[0])))
        i+=1         
   
    del draw
    st.image(pill_image, use_column_width= True)
    #except IndexError:
     #   st.write("Try again")
#%%             
st.text("Creator: Innovation lab | Kawisara N.")


