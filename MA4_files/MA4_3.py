from time import perf_counter as pc
from time import sleep as pause
import multiprocessing as mp
import concurrent.futures as future
import functools
import random 
import math
import numpy as np



def estimate_volume(n,d):
	random_numbers = [random.uniform(-1,1) for i in range(n*d)]
	arr = np.array(random_numbers).reshape(n,d)
	a = np.array(list(map(lambda x: x**2, arr)))
	distance_1= np.sum(a,axis=1)
	print(len(distance_1))
	print (a)
	distance = np.sum(arr**2,axis=1)
	print(distance)
	n_c_1= np.sum(distance_1<=1)
	# z=0
	# for i in range(len(distance)):
	# 	if distance[i]<=1:
	# 		z+=1
	# print(f'z',z)
	n_c = np.sum(distance<=1)
	print(n_c, n_c_1)
	fraction = n_c/n
	volume_estimate = (2**d)*fraction
	volume = (math.pi**(d/2))/math.gamma((d/2)+1)
	print (f'True volume of spehere:',volume)
	return volume_estimate

def runner(p):
    estimation = estimate_volume(100000,11)
    return estimation

def parallel(n,d):
    with future.ProcessPoolExecutor() as ex: 
        p = list(range(0,10))
        results = ex.map(runner,p)
        return results

def main():
    start = pc()
    estimation = parallel(10000000, 10)
    
    print(f'Volume estimated: ',estimation)
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")

if __name__ == "__main__":
    main()
   
    