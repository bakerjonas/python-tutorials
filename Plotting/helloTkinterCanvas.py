from Tkinter import *

# Setup Tkinter
root = Tk()

# Create canvas with a vertical scrollbar
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 1000
FRAME_WIDTH = 525 # leave some room for scrollbar
FRAME_HEIGHT = 500
# Create frame
frame = Frame(root, width=FRAME_WIDTH, height=FRAME_HEIGHT)
frame.place(x=0, y=0)
frame.pack(fill=BOTH, expand=1)
# Create canvas in frame
canvas = Canvas(frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, scrollregion=(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))
# Add scrollbar
vbar = Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT, fill=Y)
vbar.config(command=canvas.yview)
canvas.place(x=0, y=0)
canvas.config(yscrollcommand=vbar.set)
canvas.pack(fill=BOTH, expand=True)

# Set window position and size
root.geometry('%dx%d+%d+%d' % (FRAME_WIDTH, FRAME_HEIGHT, 200, 100))

# Add a few rectangles
canvas.create_rectangle(100, 200, 150, 300, fill="red")
canvas.create_rectangle(100, 700, 200, 750, fill="green")
canvas.create_rectangle(400, 100, 450, 800, fill="blue")

# Add some text
canvas.create_text(10, 10, text="Hello world!", anchor=NW)

# Enter GUI loop
mainloop() # block until user closes window
