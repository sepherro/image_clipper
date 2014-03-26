import tkinter
from PIL import Image, ImageTk
from sys import argv

snap_xsize = 15
snap_ysize = 15

x = 0
y = 0

#Tkinter stuff window creation
window = tkinter.Tk()
#open image
image = Image.open("cat.png")
#create canvas of given size
canvas = tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
#convert to a class that can be displayed on the canvas; display the image
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)
canvas.configure(cursor="crosshair")

def lmb_callback(event):
    print("clicked at: ", event.x, event.y)
    global x                    # need to find a more 'pythoney' way to do it
    global y
    x = event.x
    y = event.y
    canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)
    canvas.create_line(x-snap_xsize, y-snap_ysize, x+snap_xsize, y-snap_ysize, x+snap_xsize, y+snap_ysize,
                       x-snap_xsize, y+snap_ysize, x-snap_xsize, y-snap_ysize)
    return x, y


def rmb_callback(event):
    print("rmb pressed! x=", x, "y=", y)
    box = (x-snap_xsize, y-snap_ysize, x+snap_xsize, y+snap_ysize)
    region = image.crop(box)
    region.save("samples/cutout.png", "PNG")


def key_callback(event):
    print("Pressed", event.char)
    global snap_xsize           # need to find a more 'pythoney' way to do it
    global snap_ysize
    if event.char == 'a' and snap_xsize < 30:
        snap_xsize += 5
        snap_ysize += 5
    if event.char == 's' and snap_xsize > 5:
        snap_xsize -= 5
        snap_ysize -= 5
    print ("window size is now ", snap_xsize, " by ", snap_ysize, " pixels")


#the line below is necessary for the keypress callback to work
canvas.focus_set()



canvas.bind("<Button-1>", lmb_callback)
canvas.bind("<Button-3>", rmb_callback)
canvas.bind("<Key>", key_callback)

tkinter.mainloop()