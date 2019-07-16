from itertools import chain

from pyknow import *


class Medic(Fact):
    pass


class tuber(Fact):
    pass


class plantDiagnosis(KnowledgeEngine):

    @Rule(AND(Fact(tempreture='h'), Fact(humidty='n'),
              tuber(color='r'), tuber(apperance='s')))
    def black_heart(self):
        print("The plant has black heart\n")

    @Rule(AND(Fact(tempreture='l'), Fact(humidty='h'),
              tuber(color='n'), tuber(apperance='s')))
    def late_blight(self):
        print("The plant has late blight\n")

    @Rule(AND(Fact(tempreture='h'), Fact(humidty='n'),
              tuber(dry='y'), tuber(apperance='c')))
    def dry_rot(self):
        print("The plant has dry rot\n")

    @Rule(AND(Fact(tempreture='n'), Fact(humidty='n'),
              tuber(color='b'), tuber(apperance='w')))
    def early_blight(self):
        print("The plant has early blight\n")


class Engine (KnowledgeEngine):
    @Rule(Medic(age=MATCH.age_1, sympotetes=MATCH.Low))
    def function_low_sugar(self, age_1, Low):
        var = Low["shakiness"]+Low["hunger"]+Low["sweating"]+Low["headache"]+Low["pale"]
        if var > 2 and age_1 <= 5:
            print("The patient in risk of Low Sugar")
            while True:
                check_parents = str(input("Is anyone of your parents has diabetes Enter Y/N : "))
                if check_parents == "Y" or check_parents == "y" or check_parents == "N" or check_parents == "n":
                    break
                else:
                    print("Invalid Input Please Try Again")
            if check_parents == 'Y' or check_parents == 'y':
                print("you could be diabetic\n")
            else:
                print("That is Ok , Darling\n")
        elif age_1 > 5:
            print("You Are Not Child Don't Worry\n")
        else:
            print("You Don't Have Low Sugar")

    @Rule(Medic(age=MATCH.age_2, sympotetes=MATCH.High))
    def function_high_sugar(self, age_2, High):
        var = High["thirst"] + High["blurred vision"] + High["headache"] + High["dry mouth"] + High["smelling breath"] + High["shortness of breath"]
        if var > 2 and age_2 <= 5:
            print("The patient in risk of High Sugar\n")
        elif age_2 > 5:
            print("You Are Not Child There is No Problem\n")
        else:
            print("You Don't Have High Sugar\n")

    @Rule(Medic(coldsigns=MATCH.cold))
    def function_cold(self, cold):
        var = cold["runny nose"] + cold["harsh cough"]
        if var == 2:
            print("You Have Signs of Cold Please Visit the Doctor\n")
        else:
            print("you don't Have Cold\n")

    @Rule(Medic(Mumpssign=MATCH.M, mumpsage=MATCH.age))
    def function_mumps(self, M, age):
        var = M["mouth dry"] + M["swollen lymph nodes in neck"] + M["saliva is not normal"] + M["moderate temperature"]
        if age <= 5:
            if var == 4:
                print("You Already Have Mumps please Visit the Doctor Immediately\n")
            else:
                print("You Don't Have all the symptotes of mumps Mumps\n")
        else:
            print("No Problem You are Not A child please See the doctor for more information\n")

    @Rule(Medic(measles=MATCH.dic, mes_age=MATCH.age_mesales))
    def function_measles(self, dic, age_mesales):
        if age_mesales > 5:
            print("No Dangerous Your Age is More than five you are not child\n")
        else:
            var = sum(dic.values())
            if var == 4:
                print("You must See the doctor you suffer from measles\n")
            else:
                print("it's OK you don't Have all the symptotes of measles ")

    @Rule(Medic(Flu_list=MATCH.fl, Fluage=MATCH.flage))
    def function_flu(self, fl, flage):
        var = sum(fl.values())
        if var == 6:
            if flage <= 5:
                print("You Have Child Flu Please See the doctor\n")
            elif flage > 5:
                print("You Have Adult Flu please See the doctor\n")
        else:
            print("You Do not Have All the sympotetes of FLU That's OK\n")


def sugar_checking():
    dictionary_vlaues = {"shakiness": 0, "hunger": 0, "sweating": 0,
                         "headache": 0, "pale": 0,
                         "thirst": 0, "blurred vision": 0, "dry mouth": 0,
                         "smelling breath": 0, "shortness of breath": 0}
    for i in dictionary_vlaues:
        print("Does the patient suffer from " + i)
        while True:
            value = input("Enter Y/N : ")
            if value == "Y" or value == "y" or value == "N" or value == "n":
                break
            else:
                print("Invalid Input Please Try Again")
        if value == 'Y' or value == 'y':
            dictionary_vlaues[i] = 1
        else:
            dictionary_vlaues[i] = 0
    while True:
        print("The Child age is less Than or Equal to 5 and adult is More Than this \n\n")

        age = input("Enter the age of the patient : ")
        if age.isdigit():
            age_integer = int(age)
            if age_integer > 0:
                break
            else:
                print("Invalid input please Try Again")
        else:
            print("Invalid input please Try Again")
    var_engine = Engine()
    var_engine.reset()
    var_engine.declare(Medic(age=age_integer, sympotetes=dictionary_vlaues))
    var_engine.run()


def cold_checking():
    dictionary_values = {"runny nose": 0, "harsh cough": 0}
    for i in dictionary_values:
        while True:
            print("Do You Suffer From " + i)
            c = input("Enter Your Choice Y/N : ")
            if c != "Y" and c != "y" and c != "N" and c != 'n':
                print("Invalid Input Please Try Again\n")
            else:
                break
        if c == "Y" or c == "y":
            dictionary_values[i] = 1
    var = sum(dictionary_values.values())
    var_engine = Engine()
    var_engine.reset()
    var_engine.declare(Medic(coldsigns=dictionary_values))
    var_engine.run()
    if var == 2:
        return True
    else:
        return False


def mumps_checking():
    dictionary_values = {"moderate temperature": 0, "saliva is not normal": 0,
                         "swollen lymph nodes in neck": 0, "mouth dry": 0}
    for i in dictionary_values:
        while True:
            print("Does the patient  suffer from " + i)
            choice = input("Enter Your Choice Y/N : ")
            if choice != "Y" and choice != "y" and choice != "N" and choice != "n":
                print("Invalid Input Please Try Again\n")
            else:
                break
        if choice == "Y" or choice == "y":
            dictionary_values[i] = 1
    print("Please Enter Your Age Childerns are less than or equal to 5\n")
    while True:
        string_age = input("Enter Your Age : ")
        if not(string_age.isdigit()):
            print("Invalid Input Please Try Again\n")
        else:
            age = int(string_age)
            if age <= 0:
                print("Invalid Input Please Try Again\n")
            else:
                break

    var_engine = Engine()
    var_engine.reset()
    var_engine.declare(Medic(Mumpssign=dictionary_values, mumpsage=age))
    var_engine.run()


def measles_checking():
    print("We Must First Check if there is Cold\n")
    bool_var = cold_checking()
    if not bool_var:
        print("There is No Cold So There is No Measles\n")
    else:
        dictinory_vlaues = {"brownish-pink rash": 0, "high and fast temprature": 0, "bloodshot eyes": 0,
                            "white spots inside cheek": 0}
        for i in dictinory_vlaues:
            while True:
                print("Do you Suffer From " + i)
                c = input("Enter you Choice Y/N : ")
                if c != "Y" and c != "y" and c != "N" and c != "n":
                    print("Invalid Input Please Try Again\n")
                else:
                    break
            if c == "Y" or c == "y":
                dictinory_vlaues[i] = 1
        print("Please Enter the Age Childrens are less than or Equal to 5")
        while True:
            string_age = input("Enter Your Age : ")
            if not(string_age.isdigit()):
                print("Invalid Input Please Try Again\n")
            else:
                age_int = int(string_age)
                if age_int <= 0:
                    print("Invalid Input Please Try Again\n")
                else:
                    break
        var_engine = Engine()
        var_engine.reset()
        var_engine.declare(Medic(measles=dictinory_vlaues, mes_age=age_int))
        var_engine.run()


def Flu_checking():
    print("Before We heck it we must Check Cold Signs\n")
    var_bool = cold_checking()
    if not var_bool:
        print("You Do not Have Cold My dear No FLU\n")
    else:
        dictionary_values = {"conjunctives": 0, "strong body aches": 0, "weakness": 0,
                             "vomiting": 0, "sore throat": 0, "sneezing":0}
        for i in dictionary_values:
            print("Do You Suffer From " + i)
            while True:
                c = input("Enter Your Choice Y/N : ")
                if c != "y" and c != "y" and c != "N" and c != "n":
                    print("Invalid Input Please Try Again\n")
                else:
                    break
            if c == "Y" or c == "y":
                dictionary_values[i] = 1
        print("We Need To Know Your Age \n")
        while True:
            string_age = input("Enter Your Age please : ")
            if not(string_age.isdigit()):
                print("Invalid Input please Try Again\n")
            else:
                age_int = int(string_age)
                if age_int <= 0:
                    print("Invalid Input please Try Again\n")
                else:
                    break
    var_engine = Engine()
    var_engine.reset()
    var_engine.declare(Medic(Flu_list=dictionary_values, Fluage=age_int))
    var_engine.run()


def medical_expert_system():
    print("Welcome To the medical system\n")
    c = "y"
    while c == "y" or c == "Y":
        while True:
            print("1. Sugar Checking\n2. Cold Checking\n3. Mumps\n4. measles\n5. Flu\n")
            choice = input("Enter Your Choice : ")
            if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
                print("Invalid Input please Try Again\n")
            else:
                break
        if choice == "1":
            sugar_checking()
        elif choice == "2":
            cold_checking()
        elif choice == "3":
            mumps_checking()
        elif choice == "4":
            measles_checking()
        elif choice == "5":
            Flu_checking()

        while True:
            print("Do You Want Another Check : Y/N ")
            c = input("You Choice is : ")
            if c != "Y" and c != "y" and c != "n" and c != "N":
                print("Invalid Input Please Try again\n")
            else:
                break


def start():
    c = "Y"
    while c == 'Y' or c == 'y':
        temp = input("What's the temperature?\n h:high\n l:low\n n:normal\n ")
        hum = input("What's the humidity?\n h:high\n l:low\n n:normal\n ")
        d = input("is the tuber dry? y/n \n")
        tubercolor = input("What's the tuber's color?\n r:reddish brown\n b:brown\n n:normal\n")
        tuberapp = input("What does the tuber look like ?"
                         "\n c:has circles\n s:has spots\n w:has wrinkles\n")
        p = plantDiagnosis()
        p.reset()
        p.declare(Fact(tempreture=temp))
        p.declare(Fact(humidty=hum))
        p.declare(tuber(dry=d))
        p.declare(tuber(color=tubercolor))
        p.declare(tuber(apperance=tuberapp))
        p.run()
        print("Do You Want To check antother Plant Press Y/N\n")
        while True:
            c = input("Enter You Choice : ")
            if c == 'y' or c == 'Y' or c == 'N' or c == 'n':
                break
            else:
                print("InValid Input Please Try Again\n")


def plants_expert_system():
    start()


print("Welcome To Our Expert Systems\n")

while 1:
    print("1. Medical expert System \n2. The plants Expert System\n3. To Exit\n")
    n = input("Your Choice : ")
    if n == "1":
        medical_expert_system()
    elif n == "2":
        plants_expert_system()
    elif n == "3":
        print("Thanks For Using Our Service Wish you All OK\nGood Bye\n")
        break
    else:
        print("Enter Invalid input please Try Again\n\n")

