import math
from relay_detect import z_estimation, BER_estimation
import matplotlib.pyplot as plt


def P_Graph():  # To print Graph1
    for SNR_b in [1, 10, 100, 1000]:
        x = []
        y = []
        for i in range(0, 1001):
            a = i / 1000
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
    x1 = int(input("Enter source 1 output: "))
    x2 = int(input("Enter source 2 output: "))
    p = int(input("Enter relay output: "))
    predict = z_estimation(x1, x2, p)
    if predict >= 0:
        print("Decoded output is +1")
        print(f"Valid code-word: ({x1}, {x2}, +1)")
    elif predict < 0:
        print("Decoded output is -1")
        print(f"Valid code-word: ({x1}, {x2}, -1)")
    else:
        print("Incorrect operation")


def BER_Graph():  # To print Graph1
    x = []
    y1 = []
    y2 = []
    y3 = []
    a = 2 / 3
    for i in range(0, 161):
        x_no = i/10
        SNR_b = pow(10, x_no)
        x.append([x_no])
        P_E1 = BER_estimation(SNR_b, a, 1)
        y1.append([P_E1])
        P_E1 = BER_estimation(SNR_b, a, 2)
        y2.append([P_E1])
        P_E1 = BER_estimation(SNR_b, a, 3)
        y3.append([P_E1])

    plt.plot(x, y1, label="Conventional")
    plt.plot(x, y2, label="Proposed")
    plt.plot(x, y3, label="Genie-aided")
    plt.xlabel('Received SNR per information bit (in dB)')
    plt.ylabel('Probability of Bit Error (P_E1)')
    plt.yscale('log')
    plt.legend(loc="lower left")
    plt.grid(True, which="both", ls="dotted")
    plt.show()


if __name__ == '__main__':
    # Setup: Set parameter models (or check default values in relay_detect.py
    while 1:
        print("Given functions to compute")
        print("1. Probability of mis-detection as function of a (Fraction of energy per source)")
        print("2. z Estimator for given values at source")
        print("3. Probability of bit error versus received SNR per information bit (in dB)")
        choice = int(input("Enter the choice number to view functions: "))
        if choice == 1:
            P_Graph()
        elif choice == 2:
            test_z_estimator()
        elif choice == 3:
            BER_Graph()
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