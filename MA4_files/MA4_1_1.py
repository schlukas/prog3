import random 
import math
import matplotlib.pyplot as plt

def estimate_pi(intervall):
    n_c = 0
    n = 0
    colour = []
    random_x = []
    random_y = []
    for i in range(intervall):
        random_x.append(random.uniform(-1,1))
        random_y.append(random.uniform(-1,1))
        if random_x[i]**2 + random_y[i]**2 <=1:
            n_c +=1
            colour.append('red')
        else:
            colour.append('black') 
        n += 1
    estimation_pi = (4*n_c)/n
    plt.scatter(random_x,random_y,s=5, c=colour)
    plt.show()
    print(f'n_c: ', n_c)
    return estimation_pi

def main():
    estimation = estimate_pi(1000)
    pi = math.pi
    print(f'estimation of pi: ', estimation)
    print(f'pi: ', pi)

if __name__ == '__main__':
	main()