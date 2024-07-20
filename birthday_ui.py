# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'birthday.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(662, 482)
        font = QFont()
        font.setBold(False)
        widget.setFont(font)
        widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayoutWidget = QWidget(widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 661, 481))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 20)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout.addWidget(self.label)

        self.inputPlainText = QPlainTextEdit(self.verticalLayoutWidget)
        self.inputPlainText.setObjectName(u"inputPlainText")
        self.inputPlainText.setTabChangesFocus(True)
        self.inputPlainText.setDocumentTitle(u"")
        self.inputPlainText.setPlainText(u"")

        self.verticalLayout.addWidget(self.inputPlainText)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout.addWidget(self.label_2)

        self.outputPlainText = QPlainTextEdit(self.verticalLayoutWidget)
        self.outputPlainText.setObjectName(u"outputPlainText")
        self.outputPlainText.setUndoRedoEnabled(False)
        self.outputPlainText.setReadOnly(True)
        self.outputPlainText.setPlainText(u"")
        self.outputPlainText.setOverwriteMode(True)

        self.verticalLayout.addWidget(self.outputPlainText)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 50))
        self.pushButton.setMaximumSize(QSize(150, 50))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(widget)

        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("widget", u"\uc0dd\uc77c\uc790\ub97c \uacf5\ubc31\uc744 \uad6c\ubd84\uc790\ub85c \uc785\ub825\ud558\uc138\uc694", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"\ucd9c\ub825", None))
        self.pushButton.setText(QCoreApplication.translate("widget", u"\ubcc0\ud658", None))
    # retranslateUi

