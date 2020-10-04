import numpy as np
import io
import os
import pickle
import time

import tkinter as tk
from PIL import Image, EpsImagePlugin, ImageGrab


class Mandelbrott(tk.Frame):
    def __init__(self, root, size):
        tk.Frame.__init__(self, root)
        self.root = root
        self.canvas = tk.Canvas(self, width=size, height=size, background="bisque")
        self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0, 0, size, size))

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Parameters
        self.c_size = [size, size]
        self.pmin, self.pmax = -3, 2
        self.qmin, self.qmax = -2.5, 2.5
        self.ppoints, self.qpoints = self.c_size
        self.repeats = 300
        self.limit = 4  # >= 4
        self.contrast = 5  # (0; 10)

        assert 0 < self.contrast < 10, "Contrast is out of range"
        self.contrast = 1 / (10 - self.contrast)

        self.render(self.calculate())

        # Buttons:
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_end)
        self.canvas.bind("<MouseWheel>", self.zoom)

    def calculate(self):
        if os.path.isfile(f"seminar_2.cache/{self.c_size}"):
            print(f"Calculations for canvas {self.c_size} was found in cache")
            with open(rf"seminar_2.cache/{self.c_size}", 'rb') as file:
                return pickle.load(file)
        else:
            print("Calculating...")
            start_time = time.time()
            data = np.zeros(self.c_size, dtype=np.int16)

            for ip, p in enumerate(np.linspace(self.pmin, self.pmax, self.ppoints)):
                for iq, q in enumerate(np.linspace(self.qmin, self.qmax, self.qpoints)):
                    c = p + 1j * q
                    z = 0
                    for k in range(self.repeats):
                        z = z ** 2 + c
                        if abs(z) < self.limit:
                            data[ip, iq] += 1
                        else:
                            break
            print(f"Calculating time: {time.time() - start_time:.1f} sec")

            # Caching
            with open(rf"seminar_2.cache/{self.c_size}", 'wb') as file:
                pickle.dump(data, file)

            return data

    def render(self, data):
        print("Rendering...")
        start_time = time.time()
        max_color = data.max()
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                value = int((cell / max_color) ** self.contrast * 255)
                clr = "#" + '%02x%02x%02x' % (255 - value, value, value)
                self.canvas.create_rectangle(i, j, i + 1, j+1, fill=clr, outline=clr)
        print(f"Rendering time: {time.time() - start_time:.1f} sec")

    # move
    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def move_end(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    # windows zoom
    def zoom(self, event):
        if event.delta > 0:
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif event.delta < 0:
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def recache(self, *args):
        folder = "seminar_2.cache"
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                os.unlink(file_path)
            except Exception as e:
                print(e)
        for size in args:
            self.c_size = size
            self.calculate()

    # def save_png(self):
    #     x = self.canvas.winfo_rootx() + self.canvas.winfo_x()
    #     y = self.canvas.winfo_rooty() + self.canvas.winfo_y()
    #     x1 = x+self.canvas.winfo_width()
    #     y1 = y+self.canvas.winfo_height()
    #     box = (x, y, x1, y1)
    #     ImageGrab.grab(bbox=box).save("out.png")
    #     # ImageGrab.grab_to_file("out_grabtofile.png", ImageGrab.grab(bbox=box))
    #
    #
    #
    #     # EpsImagePlugin.gs_windows_binary = r'C:\Program Files\gs\gs9.53.3\bin\gswin64c'
    #     # ps = self.canvas.postscript(colormode='color')
    #     # img = Image.open(io.BytesIO(ps.encode('utf-8')))
    #     # img.save('filename.png', 'png')
    #     # file_name = "temp"
    #     # self.canvas.postscript(file=file_name + '.eps')
    #     # img = Image.open(file_name + '.eps')
    #     # img.save(file_name + '.png', 'png')
    #     # img.close()


if __name__ == "__main__":
    root = tk.Tk()
    Mandelbrott(root, 500).pack(fill="both", expand=True)
    root.mainloop()
