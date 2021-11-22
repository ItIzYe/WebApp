import random
import json
import os
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
import time

class account(QWidget):
    def __init__(self):
        super(account, self).__init__()

        file = open("current_user.json", "r")
        data = json.load(file)

        if os.path.exists(f"user/account/{data['user']}.txt"):
            self.decrypt_account(f"user/account/{data['user']}.txt.key")
            file = open(f"user/account/{data['user']}.txt", "r")
            liste = file.read()
            balance = liste[0]
            file.close()

            biglabel = QLabel(self)
            biglabel.setText("ACCOUNT")
            biglabel.setFont(QtGui.QFont('Poppins', 20, QtGui.QFont.Bold))
            biglabel.move(825, 0)

            translabel = QLabel(self)
            translabel.setText("Kontostand: " + balance + "€")
            translabel.setFont(QtGui.QFont('Poppins', 14))
            translabel.move(800, 100)

            menuebutton = QPushButton('Menü', self)
            menuebutton.move(900, 700)
            menuebutton.setFont(QtGui.QFont('Poppins', 16))
            menuebutton.clicked.connect(self.menuein)

            self.encrypt_account()
            self.setGeometry(50, 50, 1920, 1080)
            self.setWindowTitle("Buchhalter")
            self.setWindowIcon(QIcon("Book.jpg"))
            self.showMaximized()

        else:
            t = QLabel(self)
            t.setText("Kontostand: 0€")
            t.setFont(QtGui.QFont('Poppins', 20, QtGui.QFont.Bold))
            t.move(700, 0)

            menuebutton = QPushButton('Menü', self)
            menuebutton.move(900, 700)
            menuebutton.setFont(QtGui.QFont('Poppins', 16))
            menuebutton.clicked.connect(self.menuein)

            file = open(f"user/account/{data['user']}.txt", "w")
            a = "0"
            file.write(a)
            file.close()

            file = open(f"user/account/{data['user']}.txt", "r")
            balance = file.read()
            file.close()

            #print("TRANSAKTIONEN\n\n")
            #print(transaction_list)
            #print("OPTIONEN\n\n1] Zurück")

            self.encrypt_account()

            #m = input("Gebe bitte die Zahl des Reiters an, auf den du Zugreifen möchtest\n")

            self.setGeometry(50, 50, 1920, 1080)
            self.setWindowTitle("Buchhalter")
            self.setWindowIcon(QIcon("Book.jpg"))
            self.showMaximized()

    def encrypt_account(self):

        file = open("current_user.json", "r")
        data = json.load(file)

        filename = ("user/account/%s" % data["user"] + ".txt")
        to_encrypt = open(filename, "rb").read()
        size = len(to_encrypt)
        key = os.urandom(size)

        with open(filename + ".key", "wb") as key_out:
            key_out.write(key)
        encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))

        with open(filename, "wb") as encrypted_out:
            encrypted_out.write(encrypted)

    def decrypt_account(self, key):

        file = open("current_user.json", "r")
        data = json.load(file)
        file = open("user/account/%s" % data["user"] + ".txt", "rb").read()
        key = open(key, "rb").read()
        decrypted = bytes(a ^ b for (a, b) in zip(file, key))

        with open("user/account/%s" % data["user"] + ".txt", "wb") as decrypted_out:
            decrypted_out.write(decrypted)

class trans(QWidget):
    def __init__(self):
        super(trans, self).__init__()

        file = open("current_user.json", "r")
        data = json.load(file)

        if os.path.exists(f"user/transactions/{data['user']}.txt"):
            self.decrypt_transactions(f"user/transactions/{data['user']}.txt.key")
            file = open(f"user/transactions/{data['user']}.txt", "r")
            transactions = file.read()
            file.close()

            biglabel = QLabel(self)
            biglabel.setText("TRANSAKTIONEN")
            biglabel.setFont(QtGui.QFont('Poppins', 20, QtGui.QFont.Bold))
            biglabel.move(825, 0)

            translabel = QLabel(self)
            translabel.setText(transactions)
            translabel.setFont(QtGui.QFont('Poppins', 14))
            translabel.move(800, 100)

            menuebutton = QPushButton('Menü', self)
            menuebutton.move(900, 700)
            menuebutton.setFont(QtGui.QFont('Poppins', 16))
            menuebutton.clicked.connect(self.menuein)

            #print("OPTIONEN\n\n1] Zurück")
            #m = input("Gebe bitte die Zahl des Reiters an, auf den du Zugreifen möchtest\n")
            self.encrypt_transactions()
            self.setGeometry(50, 50, 1920, 1080)
            self.setWindowTitle("Buchhalter")
            self.setWindowIcon(QIcon("Book.jpg"))
            self.showMaximized()

        else:
            t = QLabel(self)
            t.setText("Transaktionsdatei wurde erstellt")
            t.setFont(QtGui.QFont('Poppins', 20, QtGui.QFont.Bold))
            t.move(700, 0)

            menuebutton = QPushButton('Menü', self)
            menuebutton.move(900, 700)
            menuebutton.setFont(QtGui.QFont('Poppins', 16))
            menuebutton.clicked.connect(self.menuein)

            file = open(f"user/transactions/{data['user']}.txt", "w")
            a = "Transaktionsdatei wurde erstellt"
            file.write(a)
            file.close()

            file = open(f"user/transactions/{data['user']}.txt", "r")
            transaction_list = file.read()
            file.close()

            #print("TRANSAKTIONEN\n\n")
            #print(transaction_list)
            #print("OPTIONEN\n\n1] Zurück")

            self.encrypt_transactions()

            #m = input("Gebe bitte die Zahl des Reiters an, auf den du Zugreifen möchtest\n")

            self.setGeometry(50, 50, 1920, 1080)
            self.setWindowTitle("Buchhalter")
            self.setWindowIcon(QIcon("Book.jpg"))
            self.showMaximized()

    def menuein(self):

        self.hide()
        self.w = menue()

    def encrypt_transactions(self):

        file = open("current_user.json", "r")
        data = json.load(file)

        filename = ("user/transactions/%s" % data["user"] + ".txt")
        to_encrypt = open(filename, "rb").read()
        size = len(to_encrypt)
        key = os.urandom(size)

        with open(filename + ".key", "wb") as key_out:
            key_out.write(key)
        encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))

        with open(filename, "wb") as encrypted_out:
            encrypted_out.write(encrypted)

    def decrypt_transactions(self, key):

        file = open("current_user.json", "r")
        data = json.load(file)
        file = open("user/transactions/%s" % data["user"] + ".txt", "rb").read()
        key = open(key, "rb").read()
        decrypted = bytes(a ^ b for (a, b) in zip(file, key))

        with open("user/transactions/%s" % data["user"] + ".txt", "wb") as decrypted_out:
            decrypted_out.write(decrypted)

class logout(QWidget):
    def __init__(self):
        super(logout, self).__init__()

        self.encrypt_user()

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)

        btn = QPushButton("Logout", self)
        btn.move(40,80)
        btn.clicked.connect(self.doaction)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Daten werden verschlüsselt")
        self.show()

    def encrypt_user(self):

        file = open('current_user.json', "r")
        data = json.load(file)

        filename = (f"user/{data['user']}.txt")
        to_encrypt = open(filename, "rb").read()
        size = len(to_encrypt)
        key = os.urandom(size)

        with open(filename + ".key", "wb") as key_out:
            key_out.write(key)
        encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))

        with open(filename, "wb") as encrypted_out:
            encrypted_out.write(encrypted)

    def doaction(self):

        for i in range(101):
            time.sleep(0.05)
            self.pbar.setValue(i)

        sys.exit(app.exec())

           #QtCore.QCoreApplication.instance().quit





class menue(QWidget):
    def __init__(self):
        super(menue, self).__init__()

        biglabel = QLabel(self)
        biglabel.setText("Menü")
        biglabel.setFont(QtGui.QFont('Poppins', 20, QtGui.QFont.Bold))
        biglabel.move(900, 0)

        button1 = QPushButton("Account", self)
        button2 = QPushButton("Transaktionen", self)
        button3 = QPushButton("Logout", self)

        button1.setFont(QtGui.QFont('Poppins', 20))
        button2.setFont(QtGui.QFont('Poppins', 20))
        button3.setFont(QtGui.QFont('Poppins', 20))

        button1.move(450, 400)
        button2.move(850, 400)
        button3.move(1300, 400)

        button1.clicked.connect(self.acc_in)
        button2.clicked.connect(self.trans_in)
        button3.clicked.connect(self.logout_in)

        self.setGeometry(50, 50, 1920, 1080)
        self.setWindowTitle("Buchhalter")
        self.setWindowIcon(QIcon("Book.jpg"))
        self.showMaximized()

    def acc_in(self):

        self.hide()
        self.w = account()

    def trans_in(self):

        self.hide()
        self.w = trans()

    def logout_in(self):

        self.w = logout()

class login2(QWidget):
    def __init__(self):
        super(login2, self).__init__()

        pas, done1 = QtWidgets.QInputDialog.getText(self, 'Login', 'Please repeat your password:')

        file = open("current_user.json", "r")
        data = json.load(file)

        file = open(f"user/{data['user']}.txt", "r")
        liste = file.readlines()
        rps = liste[0]

        if int(pas) == int(rps):

            print("Logging...")
            print("Eingeloggt")

            file = open(f"user/{data['user']}.txt", "r")
            liste = file.readlines()
            file.close()

            self.logged()

        else:

            file = open(f"user/{data['user']}.txt", "r")
            liste = file.readlines()
            file.close()

            file = open(f"user/{data['user']}.txt", "w")
            tries = liste[2]
            ntries = int(tries) - 1
            liste[2] = str(ntries) + "\n"
            file.writelines(liste)
            file.close()

            pas, done1 = QtWidgets.QInputDialog.getText(self, 'Login', f'Falsches passwort! Sie haben noch {ntries} Versuche')

            if int(pas) == int(rps):

                print("Logging...")
                print("Eingeloggt")

                file = open(f"user/{data['user']}.txt", "r")
                liste = file.readlines()
                file.close()

                self.logged()

            else:

                file = open(f"user/{data['user']}.txt", "w")
                tries = liste[2]
                ntries = int(tries) - 1
                liste[2] = str(ntries) + "\n"
                file.writelines(liste)
                file.close()

                pas, done1 = QtWidgets.QInputDialog.getText(self, 'Login', f'Falsches passwort! Sie haben noch {ntries} Versuche')

                if int(pas) == int(rps):

                    print("Logging...")
                    print("Eingeloggt")

                    file = open(f"user/{data['user']}.txt", "r")
                    liste = file.readlines()
                    file.close()

                    self.logged()

                else:

                    title = QLabel(self)
                    title.setText('Sie haben ihr Passwort zu oft falsch eingegeben. Das Programm wird nun geschlossen')
                    title.move(0, 10)

                    self.setGeometry(500, 700,  450, 100)
                    self.setWindowTitle("Programm Shutdown")
                    self.setWindowIcon(QIcon("Book.jpg"))
                    self.show()


    def logged(self):

        print("Eingeloggt1")

        self.w = menue()





class tutorial(QWidget):
    def __init__(self):
        super(tutorial, self).__init__()

        text1 = QLabel(self)
        text1.setText(f"Willkommen bei TransWare von ItIzYe Development Inc.!\n ")
        text1.move(575, 0)
        text1.setFont(QFont('Poppins', 20, QtGui.QFont.Bold))
        text2 = QLabel(self)
        text2.setText("Hier finden sie eine Anleitung zu dem Programm:\n")
        text2.move(725, 50)
        text2.setFont(QFont('Poppins', 17))
        text3 = QLabel(self)
        text3.setText("Um ihre Anmeldung zu vervollständigen werden sie gleich gebeten, ihr Passwort einzugeben. Im Menü können sie auf drei Reiter zugreifen:\n\n")
        text3.move(300, 150)
        text3.setFont(QFont('Poppins', 16))
        text4 = QLabel(self)
        text4.setText("-Account\n   -> Dieser Reiter zeigt ihnen ihren Kontostand an. Mit dem ausführen von im Account gennanten Reitern können sie entweder\n Geld zum Konto hinzufügen oder entfernen\n")
        text4.move(350, 250)
        text4.setFont(QFont('Poppins', 14))
        text5 = QLabel(self)
        text5.setText("-Transaktionen\n   -> In diesem Reiter können sie sich ihre vergangenen Transaktionen anschauen\n")
        text5.move(350, 375)
        text5.setFont(QFont('Poppins', 14))
        text6 = QLabel(self)
        text6.setText("-Log Out\n   -> Durch diesen Reiter loggen sie sich vom Programm aus\n\n")
        text6.move(350, 450)
        text6.setFont(QFont('Poppins', 14))
        text7 = QLabel(self)
        text7.setText("Auf die jeweiligen Reiter erhalten sie Zugriff wenn sie die Zahl des Reiters in die Konsole eingeben")
        text7.move(350, 550)
        text7.setFont(QFont('Poppins', 14))
        text8 = QLabel(self)
        text8.setText("ACHTUNG:")
        text8.move(900, 600)
        text8.setFont(QFont('Poppins', 17, QtGui.QFont.Bold))
        text9 = QLabel(self)
        text9.setText("Ihre Daten werden nach ihrem Log Out verschlüsselt. Und beim nächsten Log In wieder entschlüsselt.\n")
        text9.move(500, 650)
        text9.setFont(QFont('Poppins', 14))
        text10 = QLabel(self)
        text10.setText("Jedoch können sie nur verlässlich verschlüsselt werden, wenn sie sich ordnungsgemäß vom Gerät abmelden.\n Ansonsten verschlüsselt der Alghorithmus ihre Daten doppelt, und sie gehen für immer verloren!!!")
        text10.move(500, 700)
        text10.setFont(QFont('Poppins', 14))

        button = QPushButton('Weiter', self)
        button.move(960, 900)
        button.setFont(QFont('Poppins', 14))
        button.setToolTip('Kommen si in ihr menü')
        button.clicked.connect(self.tutorial_end)


        self.setGeometry(50, 50, 1920, 1080)
        self.setWindowTitle("Buchhalter")
        self.setWindowIcon(QIcon("Book.jpg"))
        self.showMaximized()

    def tutorial_end(self):

        self.hide()
        self.w = login2()


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.initMe()

    def initMe(self):

        name, done1 = QtWidgets.QInputDialog.getText(self, 'Login', 'Bitte gebe deinen Namen ein:')

        d = {"user": f"{name}"}
        file = open("current_user.json", "r+")
        data = json.load(file)
        data.update(d)
        file.seek(0)
        json.dump(data, file)
        file.close()

        if os.path.exists("user/%s" % name + ".txt"):

            self.decrypt_user(f"user/{data['user']}.txt.key")

            file = open("user/%s" % name + ".txt", "r")
            liste = file.readlines()
            rps = liste[0]
            file.close()

            self.w = login2()

        elif not os.path.exists("user/%s" % name + ".txt"):

            d = {f"{name}": "User"}
            file = open("debug.json", "r+")
            data = json.load(file)
            data["user"].update(d)
            file.seek(0)
            json.dump(data, file)
            file.close()

            file = open("user/%s" % name + ".txt", "w")
            file.write("0\n0\n3")
            file = open("user/%s" % name + ".txt", "r")
            liste = file.readlines()
            file.close()

            file = open("user/%s" % name + ".txt", "w")
            password = liste[0]

            npassword, done2 = QtWidgets.QInputDialog.getText(self, 'Login', 'Bitte erstelle ein Passwort bestehend aus Zahlen')

            liste[0] = str(npassword) + "\n"
            file.writelines(liste)
            #rps = liste[0]
            file.close()

            self.w = tutorial()

    def decrypt_user(self, key):

        file = open("current_user.json", "r")
        data = json.load(file)
        file = open(f"user/{data['user']}.txt", "rb").read()
        key = open(key, "rb").read()
        decrypted = bytes(a ^ b for (a, b) in zip(file, key))

        with open(f"user/{data['user']}.txt", "wb") as decrypted_out:
            decrypted_out.write(decrypted)

"""
 ___     ___    ___       ___
|   |   |   |   \  \     /  /
|   |   |   |    \  \   /  /
|   |   |   |     \  \ /  /
|   |   |   |      \     /
|   |   |   |       \   /
|   |   |   |       |   |
|   |   |   |       |   |
|   |   |   |       |   |
|___|   |___|       |___|

@IIY Development INC.
"""


app = QApplication(sys.argv)

w = Login()

sys.exit(app.exec())