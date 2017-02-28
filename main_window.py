# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4 import QtGui, QtCore
from udivee.dicom_file import DicomFile


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/main_window.ui', self)
        self.setup_menu()
        self.show()

    def setup_menu(self):
        self.actionNew.setIcon(QtGui.QIcon('icons/document-new.png'))
        self.actionNew.setShortcut('Ctrl+N')
        self.actionNew.setStatusTip('New file')
        self.connect(self.actionNew,
                     QtCore.SIGNAL('triggered()'),
                     QtCore.SLOT('new_file()'))

        self.actionOpen.setIcon(QtGui.QIcon('icons/document-open.png'))
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.setStatusTip('Open file')
        self.connect(self.actionOpen,
                     QtCore.SIGNAL('triggered()'),
                     QtCore.SLOT('open_file()'))

        self.actionSave.setIcon(QtGui.QIcon('icons/document-save.png'))
        self.actionSave.setShortcut('Ctrl+S')
        self.actionSave.setStatusTip('Save file')
        self.connect(self.actionSave,
                     QtCore.SIGNAL('triggered()'),
                     QtCore.SLOT('save_file()'))

        self.actionClose.setShortcut('Ctrl+W')
        self.actionClose.setStatusTip('Close current file')
        self.connect(self.actionClose,
                     QtCore.SIGNAL('triggered()'),
                     QtCore.SLOT('close_file()'))

        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Quit udivee')
        self.connect(self.actionExit,
                     QtCore.SIGNAL('triggered()'),
                     QtCore.SLOT('close_application()'))

    @QtCore.pyqtSlot()
    def new_file(self):
        pass

    @QtCore.pyqtSlot()
    def open_file(self):
        # TODO: Open in last accessed folder
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.',
                                                     'DICOM files (*.dcm);;'
                                                     'All files (*.*)')
        ds = DicomFile().read(filename)
        print ds

    @QtCore.pyqtSlot()
    def save_file(self):
        pass

    @QtCore.pyqtSlot()
    def close_file(self):
        pass

    @QtCore.pyqtSlot()
    def close_application(self):
        self.close()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        print 'drop event'
        # get the relative position from the mime data
        mime = e.mimeData()
        if mime.hasUrls():
            urls = mime.urls()
            for url in urls:
                print unicode(url.toLocalFile())
        e.accept()
