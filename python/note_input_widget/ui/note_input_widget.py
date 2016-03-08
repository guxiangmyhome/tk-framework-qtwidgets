# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'note_input_widget.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_NoteInputWidget(object):
    def setupUi(self, NoteInputWidget):
        NoteInputWidget.setObjectName("NoteInputWidget")
        NoteInputWidget.resize(363, 203)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NoteInputWidget.sizePolicy().hasHeightForWidth())
        
        NoteInputWidget.setSizePolicy(sizePolicy)
        
        self.verticalLayout_5 = QtGui.QVBoxLayout(NoteInputWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        self.stacked_widget = QtGui.QStackedWidget(NoteInputWidget)
        self.stacked_widget.setObjectName("stacked_widget")
        
        self.note_editor_page = QtGui.QWidget()
        self.note_editor_page.setObjectName("note_editor_page")
        
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.note_editor_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.text_entry = NoteEditor(self.note_editor_page)
        self.text_entry.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_entry.setObjectName("text_entry")
        
        self.horizontalLayout.addWidget(self.text_entry)
        
        self.thumbnail = QtGui.QLabel(self.note_editor_page)
        self.thumbnail.setEnabled(True)
        self.thumbnail.setMinimumSize(QtCore.QSize(96, 75))
        self.thumbnail.setMaximumSize(QtCore.QSize(96, 75))
        self.thumbnail.setText("")
        self.thumbnail.setPixmap(QtGui.QPixmap(":/tk_framework_qtwidgets/rect_512x400.png"))
        self.thumbnail.setScaledContents(True)
        self.thumbnail.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.thumbnail.setObjectName("thumbnail")
        
        self.horizontalLayout.addWidget(self.thumbnail)
        
        self.button_h_layout = QtGui.QHBoxLayout()
        self.button_h_layout.setSpacing(0)
        self.button_h_layout.setObjectName("button_h_layout")
        
        self.close = QtGui.QToolButton(self.note_editor_page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tk_framework_qtwidgets.note_input_widget/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.close.setIcon(icon)
        self.close.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.close.setAutoRaise(True)
        self.close.setObjectName("close")
        self.close.setText("CANCEL")
        
        
        spacerItem = QtGui.QSpacerItem(100, 30, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        
        
        self.screenshot = QtGui.QToolButton(self.note_editor_page)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tk_framework_qtwidgets.note_input_widget/camera_hl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.screenshot.setIcon(icon1)
        self.screenshot.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.screenshot.setAutoRaise(True)
        self.screenshot.setObjectName("screenshot")
        


        self.button_h_layout.addWidget(self.screenshot)
        self.button_h_layout.addItem(spacerItem)
        
        self.submit = QtGui.QToolButton(self.note_editor_page)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        
        #self.submit.setSizePolicy(sizePolicy)
        self.submit.setText("SUBMIT")
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tk_framework_qtwidgets.note_input_widget/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        #self.submit.setIcon(icon2)
        self.submit.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.submit.setAutoRaise(True)
        self.submit.setObjectName("submit")
        

        self.button_h_layout.addWidget(self.close)
        self.button_h_layout.addWidget(self.submit)
        
        #self.horizontalLayout.addLayout(self.verticalLayout)
        
        self.button_frame = QtGui.QFrame()
        self.button_frame.setObjectName("button_frame")
        self.button_frame.setMinimumSize(QtCore.QSize(100,20))


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        #self.button_frame.setLayout(self.button_h_layout)
        #self.verticalLayout_2.addWidget(self.button_frame)
        self.verticalLayout_2.addLayout(self.button_h_layout)
        
        self.hint_label = QtGui.QLabel(self.note_editor_page)
        self.hint_label.setObjectName("hint_label")
        
        self.verticalLayout_2.addWidget(self.hint_label)
        
        self.stacked_widget.addWidget(self.note_editor_page)
        
        self.preview_page = QtGui.QWidget()
        self.preview_page.setObjectName("preview_page")
        
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.preview_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.new_note_frame = QtGui.QFrame(self.preview_page)
        self.new_note_frame.setStyleSheet("")
        self.new_note_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.new_note_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.new_note_frame.setObjectName("new_note_frame")
        
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.new_note_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        self.new_note_placeholder = QtGui.QLabel(self.new_note_frame)
        self.new_note_placeholder.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.new_note_placeholder.setObjectName("new_note_placeholder")
        
        self.verticalLayout_4.addWidget(self.new_note_placeholder)
        self.verticalLayout_3.addWidget(self.new_note_frame)
        
        self.stacked_widget.addWidget(self.preview_page)
        
        self.verticalLayout_5.addWidget(self.stacked_widget)

        self.retranslateUi(NoteInputWidget)
        self.stacked_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(NoteInputWidget)

    def retranslateUi(self, NoteInputWidget):
        NoteInputWidget.setWindowTitle(QtGui.QApplication.translate("NoteInputWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setToolTip(QtGui.QApplication.translate("NoteInputWidget", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("NoteInputWidget", "CANCEL", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshot.setToolTip(QtGui.QApplication.translate("NoteInputWidget", "Take a screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.screenshot.setText(QtGui.QApplication.translate("NoteInputWidget", "Attach Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setToolTip(QtGui.QApplication.translate("NoteInputWidget", "Create Note", None, QtGui.QApplication.UnicodeUTF8))
        self.hint_label.setText(QtGui.QApplication.translate("NoteInputWidget", "<small>You can add people by referring to them by @name.</small>", None, QtGui.QApplication.UnicodeUTF8))
        self.new_note_placeholder.setText(QtGui.QApplication.translate("NoteInputWidget", "Click to create a new note...", None, QtGui.QApplication.UnicodeUTF8))

from ..note_editor import NoteEditor
from . import resources_rc