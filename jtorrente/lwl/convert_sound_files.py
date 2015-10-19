__author__ = 'jtorrente'
import os
INPUT_DIR = r"D:/Dropbox/UCL/LISTEN WITH LEMUR/Sounds-Converted/Input"
INPUT_DIR = r"D:\Dropbox\UCL\LISTEN WITH LEMUR\Sounds-Converted\Output"
def convert():
    savepath = os.getcwd()
    os.chdir(INPUT_DIR)
    results = os.listdir('.')
    for file in os.listdir(INPUT_DIR):
        os.execlp('sox',file,"-b", "16","converted_"+file)

    os.chdir(savepath)

convert()