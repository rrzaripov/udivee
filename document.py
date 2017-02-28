# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4 import QtGui, QtCore
from udivee.dicom_file import DicomFile


class Document(QtGui.QWidget):
    def __init__(self):
        super(Document, self).__init__()
        uic.loadUi('ui/document.ui', self)

    def load_file(self, filename):
        pass
