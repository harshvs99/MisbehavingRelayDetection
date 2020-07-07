import math
import numpy as np
import matplotlib.pyplot as plt

# Set pameters for the model
d_i = 1  # Distance b/w source and relay
E_s = 1  # Normalised SNR measure - Source
d_r = 1  # Distance between relay and reciever
E_r = 1  # Normalised SNR measure - Relay
m = 3  # Path loss exponent
N_o = 0.5  # Variance


def y_calculate(h, E, x):
    n = 0
    y = h * x * pow(pow(d_i, -m) * E, 0.5) + n
    return y


def z_estimation_calculate(h, y):
    L_r = ((4 * pow(pow(d_r, -m) * E_r, 0.5)) / N_o) * (np.conj(h[0]) * y[0]).real
    L_1 = ((4 * pow(pow(d_i, -m) * E_s, 0.5)) / N_o) * (np.conj(h[1]) * y[1]).real
    L_2 = ((4 * pow(pow(d_i, -m) * E_s, 0.5)) / N_o) * (np.conj(h[2]) * y[2]).real

    if L_r * L_1 * L_2 < 0:
        L_z = -1 * min(abs(L_r), abs(L_1), abs(L_2))
    elif L_r * L_1 * L_2 >= 0:
        L_z = min(abs(L_r), abs(L_1), abs(L_2))
    print(f"L_r: {L_r}\nL_1: {L_1}\nL_2: {L_2}")
    print(f"LLR value of z is: {L_z}")
    return L_z


def z_estimation(x1, x2, p, ):
    h_r = complex(1, 0.5)
    h_1 = complex(1, 0.5)
    h_2 = complex(1, 0.5)
    y_r = complex(y_calculate(h_r, E_r, p))
    y_1 = complex(y_calculate(h_1, E_s, x1))
    y_2 = complex(y_calculate(h_2, E_s, x2))
    h = [h_r, h_1, h_2]
    y = [y_r, y_1, y_2]
    return z_estimation_calculate(h, y)


def BER_estimation_calculate(h, y, SNR_b, a, no):
    SNR_r = 2 * SNR_b * (1 - a)
    SNR_s = a * SNR_b

    L_r = round(((4 * pow(SNR_r, 0.5)) / pow(N_o,0.5)) * abs((np.conj(h[0]) * y[0]).real), 2)
    L_1 = round(((4 * pow(SNR_s, 0.5)) / pow(N_o,0.5)) * abs((np.conj(h[1]) * y[1]).real), 2)
    L_2 = round(((4 * pow(SNR_s, 0.5)) / pow(N_o,0.5)) * abs((np.conj(h[2]) * y[2]).real), 2)
    print(L_r,L_1,L_2)
    P_fa = 0.5 * (1 - (pow(SNR_r / (1 + SNR_r), 0.5) * (SNR_s / (1 + SNR_s))))
    P_md = P_fa
    j = math.log((math.exp(L_r) + math.exp(L_2)) / 1 + math.exp(L_r + L_2))  # to find BER for x1
    pf, p1, p2 = 1, 1e-2, 1e-2
    Pz_1 = pf * (1 + 2*p1 + 2*p2 + 3*p1*p2) + (p1 + p2 + 2 * p1*p2)
    Pz1 = 1 - Pz_1
    if no == 1:
        ans = 1 / (1 + math.exp(abs(L_1 + j)))
        return ans
    elif no == 2:
        ans = (((1 - P_md) * Pz_1 + (1 - P_fa) * Pz1) / (1 + math.exp(abs(L_1 + j)))) + ((P_md * Pz_1 + P_fa * Pz1) / (1 + math.exp(abs(L_1 - j))))
        return ans
    elif no == 3:
        ans = (Pz1 / (1 + math.exp(abs(L_1 + j)))) + (Pz_1 / (1 + math.exp(abs(L_1 - j))))
        return ans


def BER_estimation(SNR_b, a, no): #Print Graph for 𝛼 = 2/3, 𝑃(𝑧 = −1) = 10−2.
    x1, x2, p = -1, -1, -1
    h_r = complex(1, 0.5)
    h_1 = complex(1, 0.5)
    h_2 = complex(1, 0.5)
    y_r = complex(y_calculate(h_r, E_r, p))
    y_1 = complex(y_calculate(h_1, E_s, x1))
    y_2 = complex(y_calculate(h_2, E_s, x2))
    h = [h_r, h_1, h_2]
    y = [y_r, y_1, y_2]
    return BER_estimation_calculate(h, y, SNR_b, a, no)