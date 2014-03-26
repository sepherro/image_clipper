import tkinter
from PIL import Image, ImageTk
from sys import argv

snap_xsize = 15
snap_ysize = 15

x = 0
y = 0

window = tkinter.Tk()

image = Image.open("cat.png")
canvas = tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)


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
    region.save("cutout.png", "PNG")


canvas.bind("<Button-1>", lmb_callback)
canvas.bind("<Button-3>", rmb_callback)

tkinter.mainloop()