import math
from relay_detect import z_estimation
import matplotlib.pyplot as plt


    for SNR_b in [1, 10, 100, 1000]:
        x = []
        y = []
        for i in range(0, 100001):
            a = i / 100000
            x.append([a])
            SNR_r = 2 * (1 - a) * SNR_b
            SNR_s = a * SNR_b
            P_fa = 0.5 * (1 - (pow(SNR_r / (1 + SNR_r), 0.5) * (SNR_s / (1 + SNR_s))))
            y.append([P_fa])
        plt.plot(x, y, label=f"Y_b={int(round(10 * math.log(SNR_b, 10), 0))}dB")
    plt.xlabel('Fraction of Energy per Source, a')
    plt.ylabel('P_FA and P_MD')
    plt.yscale('log')
    plt.legend(loc="lower left")
    plt.grid(True, which="both", ls="dotted")
    plt.show()


def test_z_estimator():
    print("Enter '+1' for binary 1 and '-1' for binary 0")
    x1 = input("Enter source 1 output: ")
    x2 = input("Enter source 2 output: ")
    p = input("Enter relay output: ")
    predict = z_estimation(-1, 1, 1)
    if predict >= 0:
        print("Decoded output is +1")
    elif predict < 0:
        print("Decoded output is -1")
    else:
        print("Incorrect operation")


if __name__ == '__main__':
    # Setup: Set parameter models (or check default values in relay_detect.py
    while 1:
        print("Given functions to compute")
        print("1. Probability of mis-detection as function of a (Fraction of energy per source)")
        print("2. z Estimator for given values at source")
        choice = int(input("Enter the choice number to view functions: "))
        if choice == 1:
            P_Graph()
        elif choice == 2:
            test_z_estimator()
        else:
            print("Please enter only integer values for choice")
            pass
        new = input("Choose another operation (y/n)? ").lower()
        if new == 'n':
            break
        elif new == 'y':
            pass
        else:
            print("Please input valid input choice")
