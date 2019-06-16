import pandas as pd
import keystroke_verifier as kv
from time import time

def main():
    path = r"C:\Users\irfak\Documents\GitHub\Notebooks"
    file = r"\DSL-StrongPasswordData.xls"
    filepath = path + file
    df = pd.read_excel(filepath)
    df.drop(df.iloc[:, 1:3], axis=1, inplace=True)
    thresholds = list(map(float,input("Enter the Threshold values: ").split()))
    print("Threshold entered is : "+ str(thresholds))
    #print(len(thresholds))
    #print(type(thresholds))
    train = int(input("Enter the training sample size : "))
    test = int(input("Enter the testing sample size : "))
    users = df["subject"].unique()
    false_accept_rate, false_reject_rate = kv.keystroke_verifier(df,thresholds, train, test).split_data(users)
    print("False Accept Rate : " + str(false_accept_rate))
    print("False Reject Rate : " + str(false_reject_rate))

if __name__ == "__main__":

    print(" ")
    start_time = time()
    main()
    stop_time = time()
    print(" ")
    print("Program Execution Time(seconds) : " + str(stop_time - start_time))