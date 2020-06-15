import math
import numpy as np

#Set pameters for the model
d_i = 1 # Distance b/w source and relay
E_s = 1 # Normalised SNR measure - Source
d_r = 1 # Distance between relay and reviever
E_r = 1 # Normalised SNR measure - Relay
m = 0.7 # Path loss exponent
N_o = 0.25 # Variance

def y_calculate(h,E,x):
    n=0
    y = h*x*pow(pow(d_i,-m)*E,0.5)+n
    return y

def z_estimation_calculate(h,y):
    L_r = ((4*pow(pow(d_r,-m)*E_r,0.5))/N_o)*((np.conj(h[0])*y[0]).real)
    L_1 = ((4*pow(pow(d_i,-m)*E_s,0.5))/N_o)*((np.conj(h[1])*y[1]).real)
    L_2 = ((4*pow(pow(d_i,-m)*E_s,0.5))/N_o)*((np.conj(h[2])*y[2]).real)

    if L_r*L_1*L_2<0:
        L_z = -1*min(abs(L_r),abs(L_1),abs(L_2))
    elif L_r*L_1*L_2>=0:
        L_z  = min(abs(L_r),abs(L_1),abs(L_2))
    print(f"L_r: {L_r}\nL_1: {L_1}\nL_2: {L_2}")
    print(f"LLR value of z is: {L_z}")
    return L_z

def z_estimation(x1,x2,p):
    h_r = complex(1,0.5)
    h_1 = complex(1,0.5)
    h_2 = complex(1,0.5)
    y_r = complex(y_calculate(h_r,E_r,p))
    y_1 = complex(y_calculate(h_1,E_s,x1))
    y_2 = complex(y_calculate(h_2,E_s,x2))
    h=[h_r,h_1,h_2]
    y=[y_r,y_1,y_2]
    return z_estimation_calculate(h,y)
