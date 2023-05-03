#names = ["a1.png", "a2.png", "a3.png", "a4.png", "a5.png", "a6.png", "a7.png", "a8.png", "a9.png", "a10.png", "a11.png", "a12.png", "a13.png", "a14.png", "a15.png", "a16.png", "a17.png", "a18.png", "a19.png", "a20.png", "a21.png", "a22.png", "a23.png", "a24.png", "a25.png", "a26.png", "a27.png", "a28.png", "a29.png"]
#from pygoogle_image import image as downloader
#for i in range(10):
#   s=input()
#downloader.download("Dragon City Mobile", limit=15)
def nameFormatter(name):
    s=""
    for i in name:
        if i.isalnum() or i==".":
            s+=i
        else:
            s+="_"
    s+="_gameplay_screenshots"
    return s
print(nameFormatter("Transmute: Galaxy Battle"))