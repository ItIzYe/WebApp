#Zuerst die Libs importieren
#ACHTUNG: Das hier gehört nicht primär zum Projekt. Das sind nur ein paar Templates falls jemand anderes daran arbeitet!



upvote = QPushButton("Upvote me")
abo = QPushButton('Subscribe me')
h = QHBoxLayout()
h.addStretch(1)
h.addWidget(upvote)
h.addWidget(abo)

v = QVBoxLayout()
v.addStretch(1)
v.addLayout(h)

a = QLabel(self)
a.setText('<a href= "https://www.google.com"> Zu Google</a>')
a.setOpenExternalLinks(True)
a.linkActivated.connect(self.gedrueckt)

self.statusBar().showMessage('test')

# menubar = self.menuBar()
# file = menubar.addMenu('Log In')

# gedrueckt = QAction(QIcon('Book.jpg'), '&Exit', self)
# gedrueckt.setShortcut('Ctrl+E')
# gedrueckt.triggered.connect(self.close)
# gedrueckt.setStatusTip('Exit')
# file.addAction(gedrueckt)

label = QLabel('Bitte melden sie sich an', self)
label.move(10, 10)

button = QPushButton('Log Out', self)
button.move(50, 50)
button.setFont(QFont('Poppins', 14))
button.setToolTip('Log In to your Account')
button.clicked.connect(QtCore.QCoreApplication.instance().quit)

button1 = QPushButton('Print', self)
button1.move(50, 100)
button1.setFont(QFont('Poppins', 14))
button1.setToolTip('Print Message')
button1.clicked.connect(self.gedrueckt)

self.setGeometry(50, 50, 500, 500)
self.setWindowTitle("Buchhalter")
self.setWindowIcon(QIcon("Book.jpg"))
self.show()


def gedrueckt(self, text):
    print('Yay')


def keyPressEvent(self, QKeyEvent):
    if QKeyEvent.key() == Qt.Key_W:
        self.close()
    if QKeyEvent.key() == Qt.Key_Enter:
        # print(text)
        return
    else:
        return
