from tkinter import *
import tkinter
import tkinter.messagebox
import webbrowser
import os




def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

#website definition i need
def rev():
    webbrowser.open_new("https://revanced.io/manager/#download-apk")
def open_g(): 
    webbrowser.open_new("https://microg.org/download.html")
def open_fildo():
    webbrowser.open_new("https://fildo.net/Android#downloadSection")
def open_xmanager():
    webbrowser.open_new("https://github.com/xManager-App/xManager/releases")
def honeygain():
    webbrowser.open_new("https://www.honeygain.com/download/")
def Earn():
    webbrowser.open_new("https://earnapp.com/bandwidth")


def shutdown():
    return os.system("shutdown /s /t 1")
 
def restart():
    return os.system("shutdown /r /t 1")
 
def logout():
    return os.system("shutdown -l")



#app icons













root=tkinter.Tk()
root.configure(bg=rgb_hack((61, 220, 132))) 
root.title('L-Updater manually')  
root.geometry('500x500')  

#icon for work




#part for all apps ioriginal use on android  
reva = Button(root, text="Revanced Manager", font=("helvetica", 14), width="40", fg=rgb_hack((0, 0, 0)) ,bg=rgb_hack((152, 251, 152)), command=rev)
reva.pack(pady=8)

microg = Button(root, text="MicroG", font=("helvetica", 14),  width="40", fg=rgb_hack((0, 0, 0)) ,bg=rgb_hack((152, 251, 152)), command=open_g)
microg.pack(pady=8)


fildo = Button(root, text="Fildo", font=("helvetica", 14),  width="40", fg=rgb_hack((0, 0, 0)) ,bg=rgb_hack((152, 251, 152)), command=open_fildo)
fildo.pack(pady=8)

x = Button(root, text="XManager", font=("helvetica", 14),  width="40", fg=rgb_hack((0, 0, 0)) ,bg=rgb_hack((152, 251, 152)), command=open_xmanager)
x.pack(pady=8)

Honney = Button(root, text="Honeygain", font=("helvetica", 14),  width="40", fg=rgb_hack((0, 0, 0)) ,bg=rgb_hack((152, 251, 152)), command=honeygain)
Honney.pack(pady=8)

earnapp = Button(root, text="Earnapp", font=("helvetica", 14),  width="40", fg=rgb_hack((0, 0, 0)) ,bg=rgb_hack((152, 251, 152)), command=Earn)
earnapp.pack(pady=8)




#exit PC methodes
log = Button(root, text="Log Out", font=("helvetica", 14),  width="40", fg=rgb_hack((0, 0, 0)) , bg=rgb_hack((109, 127, 0)) , command=logout)
log.pack(pady=8)

res = Button(root, text="Restart", font=("helvetica", 14),  width="40", fg=rgb_hack((0, 0, 0)) , bg=rgb_hack((204, 153, 0)) ,command=restart)
res.pack(pady=8)

shut = Button(root, text="Shutdown", font=("helvetica", 14),  width="40", fg=rgb_hack((255, 255, 255)) ,bg=rgb_hack((166, 16, 37)), command=shutdown)
shut.pack(pady=8)







#part for my apps





root.mainloop()