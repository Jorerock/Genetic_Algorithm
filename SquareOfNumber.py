#Test code to learn how does plt work
import numpy as np
import matplotlib.pyplot as plt

def SquareShow():
    x = np.linspace(-10, 10, 400)
    y = x**2
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='$f(x)=x^2$', color='b', linestyle='-')
    plt.title('$f(x)=x^2$')
    plt.xlabel('$x$')
    plt.ylabel('$y=x^2$')
    plt.legend()
    plt.grid(True)
    plt.show()
    print("stop")

    
SquareShow()