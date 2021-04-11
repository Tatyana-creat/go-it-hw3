import os

  

def sort():
    files = os.listdir("xlam") 
    doc_ext =["doc", "docx", "txt", "pdf", "xlsx", "pptx"]
    video_ext=["avi", "mp4", "mov", "mkv"]
    imeg_ext = ["jpeg", "png", "jpg", "svg"]
    music_ext = ["mp3", "ogg", "wav", "amr"]
    arch_ext = ["zip", "gz", "tar"]

    for file in files: 
        x = str(file).split(".")[-1]
        if x in doc_ext:
            print(file + " is doc")
        elif x in video_ext:
            print(file + " is vidio")
        elif x in imeg_ext:
            print(file + " is imig")
        elif x in music_ext:
            print(file + " is music")
        elif x in arch_ext:
            print(file + " is arch")
        else:
            print(file + " is unknon")    
                 
        
sort()

    
