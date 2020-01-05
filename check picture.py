import imghdr
from PIL import Image
import pathlib
import os
import glob
import shutil
from datetime import datetime as dt

#to_dir = pathlib.Path('C:\\Users\\よーちゃん\\Pictures\\')

tdatetime = dt.now()
today = tdatetime.strftime('%Y%m%d')

filename=[]

filename=glob.glob("C:\\Users\\よーちゃん\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\*")
j=0
for i in range(len(filename)):
    width, height = Image.open(filename[i]).size
    if (width == 1920) & (height == 1080):
        print("OK file:",filename[i])
        j+=1
        shutil.copy(filename[i], 'C:\\Users\\よーちゃん\\Pictures\\新しいフォルダー\\'+today+str(j).zfill(2)+'.jpg')
    else:
        continue

print("number of OK files=",j)
