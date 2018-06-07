# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cari_test.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName(_fromUtf8("Dialog1"))
        Dialog1.resize(400, 300)
        self.textBrowser = QtGui.QTextBrowser(Dialog1)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 401, 281))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        Dialog1.setWindowTitle(_translate("Dialog1", "Dialog", None))
        self.textBrowser.setProperty("placeholderText", _translate("Dialog1", "Qt is a C++ toolkit for cross-platform application development. Qt provides single-source portability across all major desktop operating systems. It is also available for embedded Linux and other embedded and mobile operating systems. Qt is available under three different licensing options designed to accommodate the needs of our various users. Qt licensed under our commercial license agreement is appropriate for development of proprietary/commercial software where you do not want to share any source code with third parties or otherwise cannot comply with the terms of the GNU LGPL version 3. Qt licensed under the GNU LGPL version 3 is appropriate for the development of Qt applications provided you can comply with the terms and conditions of the GNU LGPL version 3. Please see qt.io/licensing for an overview of Qt licensing. Copyright (C) 2017 The Qt Company Ltd and other contributors. Qt and the Qt logo are trademarks of The Qt Company Ltd. Qt is The Qt Company Ltd product developed as an open source project. See qt.io for more information.", None))

