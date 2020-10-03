import os
import time

import numpy as np
import pickle
from xy_interact import root, c_size, point

# Parameters
pmin, pmax = -3, 2
qmin, qmax = -2.5, 2.5
ppoints, qpoints = c_size
repeats = 300
limit = 4

# Color settings
contrast = 6  # (0; 10)
palette = 5  # 0 - 5


# Checking parameters
assert 0 < contrast < 10, "Contrast is out of range"
assert 0 <= palette <= 5, "Palette is out of range"
assert type(palette) is int, "Palette must be integer"

contrast = 20 - contrast * 2


# Calculating
if os.path.isfile(f"seminar_2.cache/{c_size}"):
    with open(rf"seminar_2.cache/{c_size}", 'rb') as file:
        data = pickle.load(file)
    print(f"Calculations for canvas {c_size} was found in cache")
else:
    print("Calculating...")
    start_time = time.time()
    data = np.zeros(c_size, dtype=np.int16)

    for ip, p in enumerate(np.linspace(pmin, pmax, ppoints)):
        for iq, q in enumerate(np.linspace(qmin, qmax, qpoints)):
            c = p + 1j * q
            z = 0
            for k in range(repeats):
                z = z ** 2 + c
                if abs(z) < limit:
                    data[ip, iq] += 1
                else:
                    break
    print(f"Calculating time: {time.time() - start_time:.1f} sec")

    # Caching
    with open(rf"seminar_2.cache/{c_size}", 'wb') as file:
        pickle.dump(data, file)


# Rendering
print("Rendering...")
start_time = time.time()
max_color = data.max()
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        value = int((abs(cell) / max_color) ** (1 / contrast) * 255)
        channel = {
            0: value,
            1: value,
            2: 100
        }
        palette_dict = {
            0: (0, 1, 2),
            1: (0, 2, 1),
            2: (1, 0, 2),
            3: (1, 2, 0),
            4: (2, 1, 0),
            5: (2, 0, 1)
        }
        rgb = tuple(map(lambda x: channel[x], palette_dict[palette]))
        clr = "#" + '%02x%02x%02x' % rgb
        point(i, j, True, clr)
print(f"Rendering time: {time.time() - start_time:.1f} sec")


# Start
root.mainloop()
