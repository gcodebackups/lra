# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Kumaresan\Dev\Python\lra\uis\winMain.ui'
#
# Created: Mon Dec 19 11:03:08 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 791)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_16 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_7.setMargin(1)
        self.gridLayout_7.setSpacing(1)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.frame_4 = QtGui.QFrame(self.groupBox)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_8.setMargin(1)
        self.gridLayout_8.setSpacing(1)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        spacerItem = QtGui.QSpacerItem(272, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        self.lblStatus = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        self.lblStatus.setFont(font)
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.gridLayout_8.addWidget(self.lblStatus, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame_5 = QtGui.QFrame(self.groupBox)
        self.frame_5.setFrameShape(QtGui.QFrame.Panel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_12 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_12.setMargin(1)
        self.gridLayout_12.setSpacing(1)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.tbStatus = QtGui.QTextBrowser(self.frame_5)
        self.tbStatus.setFrameShape(QtGui.QFrame.NoFrame)
        self.tbStatus.setObjectName(_fromUtf8("tbStatus"))
        self.gridLayout_12.addWidget(self.tbStatus, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_5, 1, 0, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dckRenderTasks = QtGui.QDockWidget(MainWindow)
        self.dckRenderTasks.setObjectName(_fromUtf8("dckRenderTasks"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_4 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 30))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setMargin(1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnStartRender = QtGui.QToolButton(self.frame)
        self.btnStartRender.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnStartRender.setAutoRaise(True)
        self.btnStartRender.setObjectName(_fromUtf8("btnStartRender"))
        self.gridLayout_2.addWidget(self.btnStartRender, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.dockWidgetContents)
        self.frame_2.setFrameShape(QtGui.QFrame.Panel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_3.setMargin(1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tblMainList = QtGui.QTableWidget(self.frame_2)
        self.tblMainList.setFrameShape(QtGui.QFrame.NoFrame)
        self.tblMainList.setAlternatingRowColors(True)
        self.tblMainList.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tblMainList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblMainList.setObjectName(_fromUtf8("tblMainList"))
        self.tblMainList.setColumnCount(0)
        self.tblMainList.setRowCount(0)
        self.gridLayout_3.addWidget(self.tblMainList, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)
        self.dckRenderTasks.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dckRenderTasks)
        self.dckProperties = QtGui.QDockWidget(MainWindow)
        self.dckProperties.setObjectName(_fromUtf8("dckProperties"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents_2)
        self.scrollArea.setFrameShape(QtGui.QFrame.Panel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 134, 337))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_6 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.frame_3 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_13 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_13.setMargin(1)
        self.gridLayout_13.setSpacing(1)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.frmPropFileInfo = QtGui.QGroupBox(self.frame_3)
        self.frmPropFileInfo.setFlat(True)
        self.frmPropFileInfo.setObjectName(_fromUtf8("frmPropFileInfo"))
        self.gridLayout_10 = QtGui.QGridLayout(self.frmPropFileInfo)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.label_5 = QtGui.QLabel(self.frmPropFileInfo)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_10.addWidget(self.label_5, 0, 0, 1, 1)
        self.lePropFileName = QtGui.QLineEdit(self.frmPropFileInfo)
        self.lePropFileName.setReadOnly(True)
        self.lePropFileName.setObjectName(_fromUtf8("lePropFileName"))
        self.gridLayout_10.addWidget(self.lePropFileName, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.frmPropFileInfo)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_10.addWidget(self.label_6, 1, 0, 1, 1)
        self.lePropFilePath = QtGui.QLineEdit(self.frmPropFileInfo)
        self.lePropFilePath.setReadOnly(True)
        self.lePropFilePath.setObjectName(_fromUtf8("lePropFilePath"))
        self.gridLayout_10.addWidget(self.lePropFilePath, 1, 1, 1, 1)
        self.gridLayout_13.addWidget(self.frmPropFileInfo, 0, 0, 1, 1)
        self.frmPropFrameRange = QtGui.QGroupBox(self.frame_3)
        self.frmPropFrameRange.setFlat(True)
        self.frmPropFrameRange.setCheckable(True)
        self.frmPropFrameRange.setChecked(False)
        self.frmPropFrameRange.setObjectName(_fromUtf8("frmPropFrameRange"))
        self.gridLayout_9 = QtGui.QGridLayout(self.frmPropFrameRange)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_3 = QtGui.QLabel(self.frmPropFrameRange)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_9.addWidget(self.label_3, 0, 0, 1, 1)
        self.lePropStartFrame = QtGui.QLineEdit(self.frmPropFrameRange)
        self.lePropStartFrame.setText(_fromUtf8(""))
        self.lePropStartFrame.setObjectName(_fromUtf8("lePropStartFrame"))
        self.gridLayout_9.addWidget(self.lePropStartFrame, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.frmPropFrameRange)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_9.addWidget(self.label_4, 1, 0, 1, 1)
        self.lePropEndFrame = QtGui.QLineEdit(self.frmPropFrameRange)
        self.lePropEndFrame.setText(_fromUtf8(""))
        self.lePropEndFrame.setObjectName(_fromUtf8("lePropEndFrame"))
        self.gridLayout_9.addWidget(self.lePropEndFrame, 1, 1, 1, 1)
        self.gridLayout_13.addWidget(self.frmPropFrameRange, 1, 0, 1, 1)
        self.frmPropProjPath = QtGui.QGroupBox(self.frame_3)
        self.frmPropProjPath.setFlat(True)
        self.frmPropProjPath.setCheckable(True)
        self.frmPropProjPath.setChecked(False)
        self.frmPropProjPath.setObjectName(_fromUtf8("frmPropProjPath"))
        self.gridLayout_11 = QtGui.QGridLayout(self.frmPropProjPath)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.lePropProjPath = QtGui.QLineEdit(self.frmPropProjPath)
        self.lePropProjPath.setText(_fromUtf8(""))
        self.lePropProjPath.setObjectName(_fromUtf8("lePropProjPath"))
        self.gridLayout_11.addWidget(self.lePropProjPath, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.frmPropProjPath, 2, 0, 1, 1)
        self.frmPropButtons = QtGui.QGroupBox(self.frame_3)
        self.frmPropButtons.setTitle(_fromUtf8(""))
        self.frmPropButtons.setFlat(True)
        self.frmPropButtons.setObjectName(_fromUtf8("frmPropButtons"))
        self.gridLayout_14 = QtGui.QGridLayout(self.frmPropButtons)
        self.gridLayout_14.setMargin(2)
        self.gridLayout_14.setSpacing(2)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem2, 0, 0, 1, 1)
        self.btnPropApply = QtGui.QToolButton(self.frmPropButtons)
        self.btnPropApply.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnPropApply.setAutoRaise(True)
        self.btnPropApply.setObjectName(_fromUtf8("btnPropApply"))
        self.gridLayout_14.addWidget(self.btnPropApply, 0, 1, 1, 1)
        self.gridLayout_13.addWidget(self.frmPropButtons, 4, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem3, 3, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_3, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.dckProperties.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dckProperties)
        self.dckColumns = QtGui.QDockWidget(MainWindow)
        self.dckColumns.setObjectName(_fromUtf8("dckColumns"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.gridLayout_15 = QtGui.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_15.setMargin(0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.lstColumns = QtGui.QListWidget(self.dockWidgetContents_3)
        self.lstColumns.setFrameShape(QtGui.QFrame.Panel)
        self.lstColumns.setAlternatingRowColors(True)
        self.lstColumns.setObjectName(_fromUtf8("lstColumns"))
        self.gridLayout_15.addWidget(self.lstColumns, 0, 0, 1, 1)
        self.dckColumns.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dckColumns)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(18, 18))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dckLog = QtGui.QDockWidget(MainWindow)
        self.dckLog.setObjectName(_fromUtf8("dckLog"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents_4)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tbLog = QtGui.QTextBrowser(self.dockWidgetContents_4)
        self.tbLog.setFrameShape(QtGui.QFrame.NoFrame)
        self.tbLog.setObjectName(_fromUtf8("tbLog"))
        self.gridLayout.addWidget(self.tbLog, 0, 0, 1, 1)
        self.dckLog.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dckLog)
        self.actionRenderTasks = QtGui.QAction(MainWindow)
        self.actionRenderTasks.setCheckable(True)
        self.actionRenderTasks.setChecked(True)
        self.actionRenderTasks.setObjectName(_fromUtf8("actionRenderTasks"))
        self.actionProperties = QtGui.QAction(MainWindow)
        self.actionProperties.setCheckable(True)
        self.actionProperties.setChecked(True)
        self.actionProperties.setObjectName(_fromUtf8("actionProperties"))
        self.actionColumns = QtGui.QAction(MainWindow)
        self.actionColumns.setCheckable(True)
        self.actionColumns.setChecked(True)
        self.actionColumns.setObjectName(_fromUtf8("actionColumns"))
        self.actionLog = QtGui.QAction(MainWindow)
        self.actionLog.setCheckable(True)
        self.actionLog.setChecked(True)
        self.actionLog.setObjectName(_fromUtf8("actionLog"))
        self.toolBar.addAction(self.actionRenderTasks)
        self.toolBar.addAction(self.actionProperties)
        self.toolBar.addAction(self.actionColumns)
        self.toolBar.addAction(self.actionLog)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Status: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblStatus.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.dckRenderTasks.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Render Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStartRender.setText(QtGui.QApplication.translate("MainWindow", "Start Render", None, QtGui.QApplication.UnicodeUTF8))
        self.tblMainList.setSortingEnabled(True)
        self.dckProperties.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.frmPropFileInfo.setTitle(QtGui.QApplication.translate("MainWindow", "File Info:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.frmPropFrameRange.setTitle(QtGui.QApplication.translate("MainWindow", "Frame Range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Start Frame:", None, QtGui.QApplication.UnicodeUTF8))
        self.lePropStartFrame.setProperty(_fromUtf8("flagFullName"), QtGui.QApplication.translate("MainWindow", "Start Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.lePropStartFrame.setProperty(_fromUtf8("flagShortName"), QtGui.QApplication.translate("MainWindow", "s", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "End Frame:", None, QtGui.QApplication.UnicodeUTF8))
        self.lePropEndFrame.setProperty(_fromUtf8("flagFullName"), QtGui.QApplication.translate("MainWindow", "End Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.lePropEndFrame.setProperty(_fromUtf8("flagShortName"), QtGui.QApplication.translate("MainWindow", "e", None, QtGui.QApplication.UnicodeUTF8))
        self.frmPropProjPath.setTitle(QtGui.QApplication.translate("MainWindow", "Proj Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.lePropProjPath.setProperty(_fromUtf8("flagFullName"), QtGui.QApplication.translate("MainWindow", "Project Path", None, QtGui.QApplication.UnicodeUTF8))
        self.lePropProjPath.setProperty(_fromUtf8("flagShortName"), QtGui.QApplication.translate("MainWindow", "proj", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPropApply.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.dckColumns.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Customize Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.dckLog.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRenderTasks.setText(QtGui.QApplication.translate("MainWindow", "Render Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProperties.setText(QtGui.QApplication.translate("MainWindow", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColumns.setText(QtGui.QApplication.translate("MainWindow", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog.setText(QtGui.QApplication.translate("MainWindow", "Log", None, QtGui.QApplication.UnicodeUTF8))

