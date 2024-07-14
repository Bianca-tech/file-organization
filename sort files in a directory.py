import os
import shutil

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

def isimg(file):
    return os.path.splitext(file)[1] in img
def isaudio(file):
    return os.path.splitext(file)[1] in video
def isvideo(file):
    return os.path.splitext(file)[1] in audio
def isUniversityFile(file):
    return "university" in os.path.splitext(file)[0].lower()

def checkFiles(path: str):
    os.chdir(rf"{path}")
    for file in os.listdir():
        if isimg(file):
            if not os.path.exists("Image"):
                os.makedirs("Images")
                print("A directory was made with the name - Images.")
            shutil.move(file,path+r"\Images") 
        if isaudio(file):
            if not os.path.exists("Audio"):
                os.makedirs("Audio")
                print("A directory was made with the name - Audio.")
            shutil.move(file,path+r"\Audio") 
        if isvideo(file):   
            if not os.path.exists("Video"):
                os.makedirs("Video")
                print("A directory was made with the name - Video.")
            shutil.move(file,path+r"\Video") 
        if isUniversityFile(file):
            if not os.path.exists("Univeristy"):
                os.makedirs("University")
                print("A directory was made with the name - University.")
            shutil.move(file,path+r"\University")

if __name__ == "__main__":
    dir = input("The directory where you want to sort: ")
    checkFiles(dir)