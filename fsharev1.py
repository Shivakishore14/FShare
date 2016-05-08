from PyQt4 import QtCore, QtGui
import sys
import platform
import socket
import SimpleHTTPServer
import SocketServer
import os
import threading
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

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

class Ui_Form(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Fshare"))
		Form.resize(651, 343)
		self.flagh = False
		self.flagf = False
		self.horizontalLayout = QtGui.QHBoxLayout(Form)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.gridLayout = QtGui.QGridLayout()
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.horizontalLayoutPorts = QtGui.QHBoxLayout()
		self.horizontalLayoutPorts.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
		self.horizontalLayoutPorts.setObjectName(_fromUtf8("horizontalLayoutPorts"))
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayoutPorts.addItem(spacerItem)
		self.lPort = QtGui.QLabel(Form)
		self.lPort.setMaximumSize(QtCore.QSize(100, 25))
		self.lPort.setObjectName(_fromUtf8("label"))
		self.horizontalLayoutPorts.addWidget(self.lPort)
		self.etPort = QtGui.QTextEdit(Form)
		self.etPort.setMaximumSize(QtCore.QSize(100, 25))
		self.etPort.setObjectName(_fromUtf8("etPort"))
		self.horizontalLayoutPorts.addWidget(self.etPort)
		spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayoutPorts.addItem(spacerItem1)
		self.gridLayout.addLayout(self.horizontalLayoutPorts, 7, 0, 1, 1)
		spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
		self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
		self.layoutSubmit = QtGui.QHBoxLayout()
		self.layoutSubmit.setObjectName(_fromUtf8("layoutSubmit"))
		spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem10, 4, 0, 1, 1)
		self.btnShare = QtGui.QPushButton(Form)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.btnShare.sizePolicy().hasHeightForWidth())
		self.btnShare.setSizePolicy(sizePolicy)
		self.btnShare.setMaximumSize(QtCore.QSize(200, 100))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Monospace"))
		font.setPointSize(16)
		font.setBold(True)
		font.setWeight(75)
		self.btnShare.setFont(font)
		self.btnShare.setObjectName(_fromUtf8("btnShare"))
		self.layoutSubmit.addWidget(self.btnShare)
		self.gridLayout.addLayout(self.layoutSubmit, 15, 0, 1, 1)
		self.lTitle = QtGui.QLabel(Form)
		self.lTitle.setEnabled(True)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lTitle.sizePolicy().hasHeightForWidth())
		self.lTitle.setSizePolicy(sizePolicy)
		self.lTitle.setMaximumSize(QtCore.QSize(16777215, 120))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Monospace"))
		font.setPointSize(24)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.lTitle.setFont(font)
		self.lTitle.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.lTitle.setObjectName(_fromUtf8("lTitle"))
		self.gridLayout.addWidget(self.lTitle, 0, 0, 1, 1)
		self.horizontalLayoutSelect = QtGui.QHBoxLayout()
		self.horizontalLayoutSelect.setObjectName(_fromUtf8("horizontalLayoutSelect"))
		spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayoutSelect.addItem(spacerItem3)
		self.lShareChooser = QtGui.QLabel(Form)
		self.lShareChooser.setObjectName(_fromUtf8("lShareChooser"))
		self.horizontalLayoutSelect.addWidget(self.lShareChooser)
		self.btnRadioFtp = QtGui.QRadioButton(Form)
		self.btnRadioFtp.setObjectName(_fromUtf8("btnRadioFtp"))
		self.horizontalLayoutSelect.addWidget(self.btnRadioFtp)
		self.btnRadioHttp = QtGui.QRadioButton(Form)
		self.btnRadioHttp.setObjectName(_fromUtf8("btnRadioHttp"))
		self.horizontalLayoutSelect.addWidget(self.btnRadioHttp)
		spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayoutSelect.addItem(spacerItem4)
		self.gridLayout.addLayout(self.horizontalLayoutSelect, 10, 0, 1, 1)
		spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.gridLayout.addItem(spacerItem5, 8, 0, 1, 1)
		self.horizontalLayoutFolderShare = QtGui.QHBoxLayout()
		self.horizontalLayoutFolderShare.setSizeConstraint(QtGui.QLayout.SetFixedSize)
		self.horizontalLayoutFolderShare.setSpacing(6)
		self.horizontalLayoutFolderShare.setObjectName(_fromUtf8("horizontalLayoutFolderShare"))
		self.lPort_2 = QtGui.QLabel(Form)
		self.lPort_2.setMaximumSize(QtCore.QSize(16777215, 25))
		self.lPort_2.setObjectName(_fromUtf8("label_2"))
		self.horizontalLayoutFolderShare.addWidget(self.lPort_2)
		self.etFolder = QtGui.QTextEdit(Form)
		self.etFolder.setMaximumSize(QtCore.QSize(16777215, 25))
		self.etFolder.setObjectName(_fromUtf8("textEdit"))
		self.horizontalLayoutFolderShare.addWidget(self.etFolder)
		self.btnOpenFile = QtGui.QToolButton(Form)
		self.btnOpenFile.setMaximumSize(QtCore.QSize(16777215, 25))
		self.btnOpenFile.setObjectName(_fromUtf8("btnOpenFile"))
		self.horizontalLayoutFolderShare.addWidget(self.btnOpenFile)
		self.gridLayout.addLayout(self.horizontalLayoutFolderShare, 3, 0, 1, 1)
		spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.gridLayout.addItem(spacerItem6, 4, 0, 1, 1)
		spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.gridLayout.addItem(spacerItem7, 16, 0, 1, 1)
		self.verticalLayoutLogs = QtGui.QVBoxLayout()
		self.verticalLayoutLogs.setContentsMargins(10, -1, 10, -1)
		self.verticalLayoutLogs.setObjectName(_fromUtf8("verticalLayoutLogs"))
		self.etLogs = QtGui.QTextEdit(Form)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.etLogs.sizePolicy().hasHeightForWidth())
		self.etLogs.setSizePolicy(sizePolicy)
		self.etLogs.setMaximumSize(QtCore.QSize(16777215, 200))
		self.etLogs.setObjectName(_fromUtf8("etLogs"))
		self.verticalLayoutLogs.addWidget(self.etLogs)
		self.gridLayout.addLayout(self.verticalLayoutLogs, 14, 0, 1, 1)
		spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.gridLayout.addItem(spacerItem8, 2, 0, 1, 1)
		self.horizontalLayout.addLayout(self.gridLayout)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "Fshare", None))
		self.lPort.setText(_translate("Form", "Port : ", None))
		self.btnShare.setText(_translate("Form", "Start Sharing", None))
		self.lTitle.setText(_translate("Form", "F Share V1.1", None))
		self.lShareChooser.setText(_translate("Form", "Share over :", None))
		self.btnRadioFtp.setText(_translate("Form", "FTP", None))
		self.btnRadioHttp.setText(_translate("Form", "Http", None))
		self.lPort_2.setText(_translate("Form", "Folder To Share : ", None))
		self.btnOpenFile.setText(_translate("Form", "...", None))
		self.btnOpenFile.clicked.connect(self.openfile)
		self.btnShare.clicked.connect(self.selectSharing)
		self.initiatehttp()
		self.initiateftp()
		self.logs = ""
		self.location = ""
		self.etPort.insertPlainText("2121")
		self.getLocation()
		self.etFolder.setText(self.location)
		self.btnRadioFtp.setChecked(True)

	def getLocation(self):
		os = platform.system()
        	if os == 'Linux':
            		self.location = "/"            
        	elif os == 'Windows':
            		self.location = "C:\\"
        	else:
            		self.location = os.getcwd()
	
	def openfile(self):
		self.getLocation()
		location = str(QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', self.location , QtGui.QFileDialog.ShowDirsOnly))
		self.etFolder.setText(location)

	def getIp(self):
		ip = socket.gethostbyname(socket.gethostname())
		if ip is '127.0.0.1':
			ip = socket.gethostbyname(socket.getfqdn())
		return ip

	def initiatehttp(self):
		self.mservehttp = MyServerHttp()
	
	def initiateftp(self):
		self.mserveftp = MyServerFtp()

	def selectSharing(self):
		if self.btnRadioFtp.isChecked() == True:
			print "Ftp Server"
			self.startFtpSharing()
		else:
			print "Http Server"
			self.startHttpSharing()
	
	def startFtpSharing(self):
		port = str(self.etPort.toPlainText())
		nport = 0
		try:
                        nport = int(port)
                except Exception:
                        self.lPort.setStyleSheet('color : red')
			return
			pass
		if self.flagf:
			self.flagf = False
			self.mserveftp.serverStop()
			del self.mserveftp			
			self.initiateftp()
			self.btnShare.setText("Start Sharing")
			self.logs = "Sharing Stopped \n"
			self.etLogs.insertPlainText(self.logs)
			self.etLogs.moveCursor(QtGui.QTextCursor.End)
			return
		self.flagf = True
		self.lPort.setStyleSheet('color : black')
		port = str(self.etPort.toPlainText())
		self.location = str(self.etFolder.toPlainText())
		self.mserveftp.serverStart(nport,self.location)
		self.logs = "Sharing location : "+ self.location +"\nSharing on : " + self.getIp() + ":"+ port +"\n"
		self.etLogs.insertPlainText(self.logs)
		if nport < 1025:
			self.etLogs.insertPlainText("Use port greater than 1024 for proper working\n")
		self.etLogs.moveCursor(QtGui.QTextCursor.End)
		self.btnShare.setText("Stop Sharing")

	def startHttpSharing(self):
		port = str(self.etPort.toPlainText())
		nport = 0
		try:
                        nport = int(port)
                except Exception:
                        self.lPort.setStyleSheet('color : red')
			return
			pass
		if self.flagh:
			self.flagh = False
			self.mservehttp.serverStop()
			del self.mservehttp
			self.initiatehttp()
			self.btnShare.setText("Start Sharing")
			self.logs = "Sharing Stopped \n"
			self.etLogs.insertPlainText(self.logs)
			self.etLogs.moveCursor(QtGui.QTextCursor.End)
			return
		self.flagh = True
		self.lPort.setStyleSheet('color : black')
		port = str(self.etPort.toPlainText())
		self.location = str(self.etFolder.toPlainText())
		self.mservehttp.serverStart(nport,self.location)
		self.logs = "Sharing location : "+ self.location +"\nSharing on : " + self.getIp() + ":"+ port +"\n"
		self.etLogs.insertPlainText(self.logs)
		if nport < 1025:
			self.etLogs.insertPlainText("Use port greater than 1024 for proper working\n")
		self.etLogs.moveCursor(QtGui.QTextCursor.End)
		self.btnShare.setText("Stop Sharing")

class MyServerHttp:
	def __init__(self):
		self.port = 8080
	def __exit__(self, *err	):
        	self.close()
		
	def serverStart(self,port, location):
		self.port = port
		self.location = location
		class MyTCPServer(SocketServer.TCPServer):
			def server_bind(self):
				self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				self.socket.bind(self.server_address)
		self.Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
		self.server = MyTCPServer(("", self.port), self.Handler)
		os.chdir(self.location)
		thread = threading.Thread(target = self.server.serve_forever)
		thread.deamon = True
		thread.start()
		
	def serverStop(self):
		self.server.shutdown()

class MyServerFtp:
	def __init__(self):
		self.port = 8080
	def __exit__(self, *err	):
        	self.close()
	def serverStart(self,port,location):
		self.authorizer = DummyAuthorizer()
		#with r/w and read only
		self.authorizer.add_user('user', '12345', '.', perm='elradfmwM')
		self.authorizer.add_anonymous(location)

		self.handler = FTPHandler
		self.handler.authorizer = self.authorizer

		self.handler.banner = "ftp Server ready"
		self.address = ('', port)
		self.server = FTPServer(self.address, self.handler)

		self.server.max_cons = 256
		self.server.max_cons_per_ip = 5
		
		self.thread = threading.Thread(target = self.server.serve_forever)
		self.thread.deamon = True
		self.thread.start()
		#self.server.serve_forever()
	def serverStop(self):
		self.server.close_all()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_Form()
	ex.show()
	sys.exit(app.exec_())


