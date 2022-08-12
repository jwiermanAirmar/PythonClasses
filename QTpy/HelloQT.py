# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:14:36 2022

@author: jwierman


https://realpython.com/python-pyqt-gui-calculator/#anaconda-installation

"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('BreakerBox')

"""

window.setGeometry(100, 100, 500, 400) # (?, ?, width, height)
window.move(60, 15)
breakMessage = QLabel('<h1>BREAKER?</h1>', parent=window)
breakMessage.move(180, 50)

"""


breakerButton = QPushButton("Break")



layout = QHBoxLayout()

layout.addWidget(QPushButton('BREAKER!'))
window.setLayout(layout)

window.show()

if (breakerButton.clicked == True):#FIXME
    
    print("CLICKED")


sys.exit(app.exec_())