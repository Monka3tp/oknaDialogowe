# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(539, 402)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 9, 501, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.countryEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.countryEdit.setReadOnly(True)
        self.countryEdit.setObjectName("countryEdit")
        self.horizontalLayout.addWidget(self.countryEdit)
        self.countryButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.countryButton.setObjectName("countryButton")
        self.horizontalLayout.addWidget(self.countryButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 110, 501, 101))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.colorLabel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.colorLabel.setText("")
        self.colorLabel.setObjectName("colorLabel")
        self.horizontalLayout_2.addWidget(self.colorLabel)
        self.colorFrame = QtWidgets.QFrame(parent=self.horizontalLayoutWidget_2)
        self.colorFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.colorFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.colorFrame.setObjectName("colorFrame")
        self.horizontalLayout_2.addWidget(self.colorFrame)
        self.colorButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.colorButton.setObjectName("colorButton")
        self.horizontalLayout_2.addWidget(self.colorButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(19, 209, 501, 91))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(parent=self.horizontalLayoutWidget_3)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.fontButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.fontButton.setObjectName("fontButton")
        self.horizontalLayout_3.addWidget(self.fontButton)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 300, 501, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_4)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_4.addWidget(self.saveButton)
        self.readButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_4)
        self.readButton.setObjectName("readButton")
        self.horizontalLayout_4.addWidget(self.readButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Twoje państwo: "))
        self.countryButton.setText(_translate("Dialog", "Wybierz państwo"))
        self.colorButton.setText(_translate("Dialog", "Wybierz kolor"))
        self.fontButton.setText(_translate("Dialog", "Wybierz czcionkę"))
        self.saveButton.setText(_translate("Dialog", "Zapisz"))
        self.readButton.setText(_translate("Dialog", "Wczytaj"))
