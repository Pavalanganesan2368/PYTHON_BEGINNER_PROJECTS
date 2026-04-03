import random
import math

class RandomPassword :
    def __init__ (self) :
        self.passwords = []
        self.passwordResult = ""
        self.password = ""
        self.SLetter = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        self.CLetter = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        self.Number = "1 2 3 4 5 6 7 8 9 0"
        self.Symbols = "! @ # $ % ^ & * ( ) [ ] { ? / } , ."

    def createPassword (self) :
        smallLetters = self.SLetter.split()
        capitalLetters = self.CLetter.split()
        numbersLetters = self.Number.split()
        symbolsLetters = self.Symbols.split()

        self.passwords = [*smallLetters, *capitalLetters, *numbersLetters, *symbolsLetters]

    def generatePassword (self, passwordLength) :
        for _ in range(passwordLength) :
            getPassword = math.floor(random.random() * len(self.passwords))
            self.passwordResult += self.passwords[getPassword]

        print(f"Your Password is : {self.passwordResult}")


try :
    passwordLength = int(input("ENTER THE PASSWORD LENGTH : "))
    randomPassword = RandomPassword()
    randomPassword.createPassword()
    randomPassword.generatePassword(passwordLength)
except :
    print("YOU DIDN'T ENTER THE VALID VALUE")