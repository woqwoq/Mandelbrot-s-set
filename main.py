#start with Google Colab or Jupyter
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(Re, Im, max_iter):
    c = complex(Re, Im)
    z = 0.0j
    
    for i in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
        
    return max_iter

columns = 3000
rows = 3000

result = np.zeros([rows, columns])
for row_index, Re in enumerate(np.linspace(-2, 1, num=rows)):
    for column_index, Im in enumerate(np.linspace(-1, 1, num=columns)):
        result[row_index, column_index] = mandelbrot(Re, Im, 100)
plt.figure(dpi=200)
plt.imshow(result.T, cmap='hot', interpolation='bilinear', extent=[-2, 1, -1, 1])
plt.xlabel('Re')
plt.ylabel('Im')
plt.show
