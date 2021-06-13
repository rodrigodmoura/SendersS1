# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:35:14 2021

@author: Admin
"""
from Email import Email
import configparser
from BackLog import BackLog
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import threading
import time
class Main(QtCore.QThread):
    str_signal = QtCore.pyqtSignal(str)
    def __init__(self, BackLog, QListWidget, QProgressBar):
        QtCore.QThread.__init__(self)
        self.progresBar = QProgressBar
        self.backlog = BackLog
        self.data = self.backlog.getConfiguration()
        self.qlistWidget = QListWidget
        self.loadConfig()
        self.isExit = True
        self.load = 0

    def loadConfig(self):
        config = configparser.ConfigParser()
        config.readfp(open(self.data['config']))
        self.senderEmail = config.get('Config', 'Sender')
        self.password = config.get('Config', 'Password')
        
    def run(self):
        self.df = pd.read_excel(self.data['sheet'])
        self.email = Email(self.senderEmail, self.password, self.data['Subject'], self.data['Msg'])
        self.empEmail = self.df['Email'].values
        self.empFile = self.df['FileName'].values
        size = len(self.empEmail)
        for i in range(len(self.empEmail)):
            print(self.empEmail[i])
            response = self.email.sendEmail(self.empEmail[i], self.data['dir']+self.empFile[i])
            self.qlistWidget.addItem(response)
            self.isExist = True
            self.load = ((i + 1) / size) * 100
            time.sleep(0.05)
            self.progresBar.setValue(self.load)
        self.isExit = False
        
    def getLogs(self):
        return self.email.getLogs()