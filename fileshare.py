from PyQt4 import QtCore, QtGui
import sys

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

class Ui_Fshare(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
	def setupUi(self, Fshare):
		Fshare.setObjectName(_fromUtf8("Fshare"))
		Fshare.resize(680, 448)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8("../lrnqt/2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Fshare.setWindowIcon(icon)
		self.etFolder = QtGui.QTextEdit(Fshare)
		self.etFolder.setGeometry(QtCore.QRect(150, 100, 431, 31))
		self.etFolder.setObjectName(_fromUtf8("etFolder"))
		self.btnOpenFile = QtGui.QToolButton(Fshare)
		self.btnOpenFile.setGeometry(QtCore.QRect(600, 100, 26, 29))
		self.btnOpenFile.setObjectName(_fromUtf8("btnOpenFile"))
		self.title = QtGui.QLabel(Fshare)
		self.title.setGeometry(QtCore.QRect(230, 20, 271, 61))
		font = QtGui.QFont()
		font.setPointSize(22)
		font.setBold(True)
		font.setWeight(75)
		self.title.setFont(font)
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		self.title.setObjectName(_fromUtf8("title"))
		self.lShareFolder = QtGui.QLabel(Fshare)
		self.lShareFolder.setGeometry(QtCore.QRect(30, 100, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.lShareFolder.setFont(font)
		self.lShareFolder.setObjectName(_fromUtf8("lShareFolder"))
		self.lPort = QtGui.QLabel(Fshare)
		self.lPort.setGeometry(QtCore.QRect(250, 160, 31, 31))
		self.lPort.setObjectName(_fromUtf8("lPort"))
		self.etPort = QtGui.QTextEdit(Fshare)
		self.etPort.setGeometry(QtCore.QRect(300, 160, 104, 31))
		self.etPort.setObjectName(_fromUtf8("etPort"))
		self.btnShare = QtGui.QPushButton(Fshare)
		self.btnShare.setGeometry(QtCore.QRect(220, 350, 261, 71))
		font = QtGui.QFont()
		font.setPointSize(16)
		self.btnShare.setFont(font)
		self.btnShare.setObjectName(_fromUtf8("btnShare"))
		self.etLogs = QtGui.QPlainTextEdit(Fshare)
		self.etLogs.setGeometry(QtCore.QRect(10, 240, 651, 75))
		self.etLogs.setObjectName(_fromUtf8("etLogs"))

		self.retranslateUi(Fshare)
		QtCore.QMetaObject.connectSlotsByName(Fshare)

	def retranslateUi(self, Fshare):
		Fshare.setWindowTitle(_translate("Fshare", "Fshare", None))
		self.btnOpenFile.setText(_translate("Fshare", "...", None))
		self.title.setText(_translate("Fshare", "F share v1.0", None))
		self.lShareFolder.setText(_translate("Fshare", "folder to share", None))
		self.lPort.setText(_translate("Fshare", "port", None))
		self.btnShare.setText(_translate("Fshare", "Start Sharing", None))

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_Fshare()
	ex.show()
	sys.exit(app.exec_())

