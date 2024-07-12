import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

file = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/train.csv")

i = True
while i == True:
    def survived():
        file.Survived.value_counts().plot(kind="barh")
        plt.title("Titanic")
        plt.xlabel("Number of Passengers")
        plt.ylabel("Dead: 0 and Alive: 1")
        plt.show()
        return survived

    def gender():
        file.Gender.value_counts().plot(kind='pie')
        plt.title("Gender")
        plt.ylabel("")
        plt.show()
        return gender

    def pclass():
        file.Pclass.value_counts().plot(kind='density')
        plt.title("Pclass")
        plt.ylabel("")
        plt.show()
        return pclass

    inp = input("1: Survived\n2: Gender\n3: Pclass\n4: Quit\nEnter the value: ")

    if inp == "1":
        print(survived())

    elif inp == "2":
        print(gender())

    elif inp == "3":
        print(pclass())

    elif inp == "4":
        break

    else:
        print("Choose the Number (1 to 4)")