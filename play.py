import os
import image2txt


def getTxt(imagePath, txtPath):
    img_count = 1
    while img_count <= len(os.listdir(imagePath)):
        imageFile = imagePath + str(img_count) + '.png'
        txtFile = txtPath + str(img_count) + '.txt'
        image2txt.image2txt(imageFile, txtFile)
        print('制作舞蹈中: ' + str(img_count) + '%')
        img_count += 1


def play(txtPath):
    txt_count = 1
    while txt_count <= len(os.listdir(txtPath)):
        os.system('type ' + txtPath + str(txt_count) + '.txt')
        txt_count += 1
        os.system('cls')


txt_dir_path = r'D:\Code\testPython\transcoder\txt' + '\\'
img_dir_path = r'D:\Code\testPython\transcoder\images' + '\\'
getTxt(img_dir_path, txt_dir_path)
play(txt_dir_path)
