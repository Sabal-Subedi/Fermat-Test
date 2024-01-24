import random
import math

# Generates Random positive integer between 2 and N-1
def random_integer(n:int):
    return random.randint(2,n-1) # generating random value between 2 and N-1

def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    # You will need to implement this function and change the return value.
    if y == 0: 
        return 1
    
    # Make recursive call    
    z = mod_exp(x, math.floor(y/2), N)
    
    z_square = z*z
    if y % 2 == 0:
        return z_square % N
    else:
        return (x*z_square) % N
	

def fprobability(k):
    # You will need to implement this function and change the return value.   
    prob_success= 1-math.pow(0.5,k)
    return prob_success


def mprobability(k):
    # You will need to implement this function and change the return value.   
    prob_success= 1-math.pow(0.25,k)
    return prob_success


def fermat(N,k):
    result_modular=0
    while(k>0):
        a = random_integer(N) # getting value of a; a<N
        result_modular = mod_exp(a,N-1,N) # calling the modular exponential 
        k-=1 # decreasing the counter
        
    if result_modular == 1:
        return "prime"
    return "composite"
   


def miller_rabin(N,k):
    if N<=1:
        return 'composite'
    
    if N==2 or N==3:
        return 'prime'
    
    # _epoch and _N to determine number of iteration for Miller-Rabin test
    # flag:bool ; True indicates Prime and False indicate Composite
    _epoch, _N = 0, N-1 
    flag = False
    
    while _N %2 ==0:
        _epoch+=1
        _N = _N/2
        
    for _ in range(k): # loop for k different values of a
        x= random_integer(N)
        _power = N-1 
        result_modular = mod_exp(x,N-1,N) # to check whether it passes the fermet test or not
        if result_modular == 1 or result_modular == N-1: # test value of modular to proceed into Miller-Rabin test
            flag=True
            for _ in range(_epoch-1): # loops until (N-1)%2=0 
                _power = int(_power/2) # used to get square root
                result = mod_exp(x,_power,N) # computes exponentail                
                if result == N-1 or result == 1: # tests if exponential value is 1 or -1
                    flag=True # indicates the number N is Prime
                    if result == N-1:
                        break # satisfies N-1; Breaks out of the loop
                else:
                    flag=False # indicates the number N is Composite
        else:
            flag=False          
    return "prime" if flag else "composite" # Return Prime or Composite based on Flag
