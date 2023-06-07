from PyQt5.QtWidgets import *
from qtpy import QtWidgets
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime, openpyxl, qdarkstyle, sqlite3


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1438, 875)

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1611, 811))

		font = QtGui.QFont()
		font.setFamily("DejaVu Sans Mono")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)

		self.tabWidget.setFont(font)
		self.tabWidget.setObjectName("tabWidget")

		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")

		self.widget = QtWidgets.QWidget(self.tab)
		self.widget.setGeometry(QtCore.QRect(12, 12, 391, 38))
		self.widget.setObjectName("widget")

		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.label = QtWidgets.QLabel(self.widget)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(15)
		font.setBold(False)
		font.setWeight(50)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.horizontalLayout_2.addWidget(self.label)
		self.dateEdit = QtWidgets.QDateEdit(self.widget)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.dateEdit.setFont(font)
		self.dateEdit.setAutoFillBackground(False)
		self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
		self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
		self.dateEdit.setCalendarPopup(True)
		d = QDate.currentDate().addDays(-31)
		self.dateEdit.setDate(QtCore.QDate(d))
		self.dateEdit.setObjectName("dateEdit")
		self.horizontalLayout_2.addWidget(self.dateEdit)
		self.label_2 = QtWidgets.QLabel(self.widget)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(15)
		font.setBold(False)
		font.setWeight(50)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_2.addWidget(self.label_2)
		self.dateEdit_2 = QtWidgets.QDateEdit(self.widget)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.dateEdit_2.setFont(font)
		self.dateEdit_2.setMaximumDate(QtCore.QDate(2050, 12, 31))
		self.dateEdit_2.setMinimumDate(QtCore.QDate(2022, 1, 1))
		self.dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
		self.dateEdit_2.setCalendarPopup(True)
		d_2 = QDate.currentDate()
		self.dateEdit_2.setDate(d_2)
		self.dateEdit_2.setObjectName("dateEdit_2")
		self.horizontalLayout_2.addWidget(self.dateEdit_2)
		self.widget1 = QtWidgets.QWidget(self.tab)
		self.widget1.setGeometry(QtCore.QRect(476, 720, 831, 36))
		self.widget1.setObjectName("widget1")

		self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.toolButton = QtWidgets.QToolButton(self.widget1)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.toolButton.setFont(font)
		self.toolButton.setObjectName("toolButton")
		self.horizontalLayout.addWidget(self.toolButton)
		self.toolButton_2 = QtWidgets.QToolButton(self.widget1)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.toolButton_2.setFont(font)
		self.toolButton_2.setObjectName("toolButton_2")
		self.horizontalLayout.addWidget(self.toolButton_2)
		self.toolButton_3 = QtWidgets.QToolButton(self.widget1)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.toolButton_3.setFont(font)
		self.toolButton_3.setObjectName("toolButton_3")
		self.horizontalLayout.addWidget(self.toolButton_3)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.toolButton_5 = QtWidgets.QToolButton(self.widget1)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.toolButton_5.setFont(font)
		self.toolButton_5.setObjectName("toolButton_5")
		self.horizontalLayout.addWidget(self.toolButton_5)
		self.toolButton_4 = QtWidgets.QToolButton(self.widget1)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.toolButton_4.setFont(font)
		self.toolButton_4.setObjectName("toolButton_4")
		self.horizontalLayout.addWidget(self.toolButton_4)
		self.tableWidget = QtWidgets.QTableWidget(self.tab)
		self.tableWidget.setGeometry(QtCore.QRect(474, 7, 931, 711))
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans Mono")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)

		self.tableWidget.setFont(font)
		self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget.setColumnCount(5)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		font = QtGui.QFont()
		font.setPointSize(14)
		item.setFont(font)
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, item)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(4, item)    		

		self.widget2 = QtWidgets.QWidget(self.tab)
		self.widget2.setGeometry(QtCore.QRect(12, 57, 451, 300))
		self.widget2.setObjectName("widget2")
		self.gridLayout = QtWidgets.QGridLayout(self.widget2)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")
		# --------
		self.lineEdit = QtWidgets.QLineEdit(self.widget2)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(15)
		font.setBold(False)
		font.setWeight(50)
		self.lineEdit.setFont(font)
		self.lineEdit.setObjectName("lineEdit")
		self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
		# --------
		self.lineEdit_2 = QtWidgets.QLineEdit(self.widget2)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(15)
		font.setBold(False)
		font.setWeight(50)
		self.lineEdit_2.setFont(font)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
		# --------
		self.lineEdit_3 = QtWidgets.QLineEdit(self.widget2)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(15)
		font.setBold(False)
		font.setWeight(50)
		self.lineEdit_3.setFont(font)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
		# --------
		self.lineEdit_4 = QtWidgets.QLineEdit(self.widget2)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(15)
		font.setBold(False)
		font.setWeight(50)
		self.lineEdit_4.setFont(font)
		self.lineEdit_4.setObjectName("lineEdit")
		self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 1)
		# --------
		self.lineEdit_5 = QtWidgets.QLineEdit(self.widget2)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(15)
		font.setBold(False)
		font.setWeight(50)
		self.lineEdit_5.setFont(font)
		self.lineEdit_5.setObjectName("lineEdit")
		self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 1)
		# --------
		self.lineEdit_6 = QtWidgets.QLineEdit(self.widget2)
		self.lineEdit_6.setFont(font)
		self.lineEdit_6.setObjectName("lineEdit_6")
		self.gridLayout.addWidget(self.lineEdit_6, 7, 1, 1, 1)
		# --------
		self.label_01 = QtWidgets.QLabel(self.widget2)
		self.label_01.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(50)
		self.label_01.setFont(font)
		self.label_01.setObjectName("label_01")
		self.gridLayout.addWidget(self.label_01, 0, 0, 1, 2)
		# --------
		self.label_02 = QtWidgets.QLabel(self.widget2)
		self.label_02.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(50)
		self.label_02.setFont(font)
		self.label_02.setObjectName("label_01")
		self.gridLayout.addWidget(self.label_02, 4, 0, 1, 2)
		# --------
		self.label_6 = QtWidgets.QLabel(self.widget2)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")
		self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
		# --------
		self.label_4 = QtWidgets.QLabel(self.widget2)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
		# --------
		self.label_5 = QtWidgets.QLabel(self.widget2)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
		# --------
		self.label_7 = QtWidgets.QLabel(self.widget2)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.label_7.setFont(font)
		self.label_7.setObjectName("label_7")
		self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
		# --------
		self.label_8 = QtWidgets.QLabel(self.widget2)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.label_8.setFont(font)
		self.label_8.setObjectName("label_8")
		self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
		# --------
		self.label_9 = QtWidgets.QLabel(self.widget2)
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(False)
		font.setWeight(50)
		self.label_9.setFont(font)
		self.label_9.setObjectName("label_9")
		self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
		# --------
		self.tabWidget.addTab(self.tab, "")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1338, 26))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.action = QtWidgets.QAction(MainWindow)
		self.action.setObjectName("action")
		self.menuFile.addAction(self.action)
		self.menuFile.addSeparator()
		self.menubar.addAction(self.menuFile.menuAction())

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "с"))
		self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy.MM.dd"))
		self.label_2.setText(_translate("MainWindow", "по"))
		self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "yyyy.MM.dd"))
		self.toolButton.setText(_translate("MainWindow", "Добавить"))
		self.toolButton_2.setText(_translate("MainWindow", "Удалить"))
		self.toolButton_3.setText(_translate("MainWindow", "Excel"))
		self.toolButton_5.setText(_translate("MainWindow", "График"))
		self.toolButton_4.setText(_translate("MainWindow", "Обновить"))
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Дата"))
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Доход"))
		item = self.tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Расход"))
		item = self.tableWidget.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "Остаток"))
		item = self.tableWidget.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "Комментарий"))
		self.label_01.setText(_translate("MainWindow", "За период"))
		self.label_02.setText(_translate("MainWindow", "Средний"))
		self.label_6.setText(_translate("MainWindow", "Остаток"))
		self.label_4.setText(_translate("MainWindow", "Доход"))
		self.label_5.setText(_translate("MainWindow", "Расход"))
		self.label_7.setText(_translate("MainWindow", "Доход"))
		self.label_8.setText(_translate("MainWindow", "Расход"))
		self.label_9.setText(_translate("MainWindow", "Остаток"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Финансы"))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.action.setText(_translate("MainWindow", "Выбрать БД"))

	def add_financ(self):
		inputDialog = Dialog_ADD()
		rez = inputDialog.exec()
		if not rez:
			QMessageBox.information(Dialog_ADD(), 'Внимание', "Диалог сброшен.")
			return
		date = inputDialog.date_edit_name.text()
		date_str = str(date)
		INC = str(inputDialog.line_edit_age.text())
		Outc = str(inputDialog.line_edit_gender.text())
		if not date or not INC or not Outc:
			QMessageBox.information(Dialog_ADD(), 'Внимание', 'Заполните пожалуйста все поля.')
			return
		else:
			INC_int = float(INC)
			INC_str = str(INC_int)
			Outc_int = float(Outc)
			Outc_str = str(Outc_int)
			Sum_int = INC_int - Outc_int
			Sum_str = str(Sum_int)
		con = sqlite3.connect('FinanceDB')
		cur = con.cursor()
		sqlstr = """
                            Insert Into Finance
                            (Date, Income, Outcome, Sum)
                            VALUES (?,?,?,?)
                            """
		cur.execute(sqlstr, [date_str, INC_str, Outc_str, Sum_str])
		con.commit()

	def Delete_financ(self):
		input_dialog = Dialog_Delete()
		rez = input_dialog.exec()
		if not rez:
			QMessageBox.information(Dialog_Delete(), 'Внимание', 'Диалог сброшен.')
			return
		date = input_dialog.date_edit_date_1.text()
		date_2 = input_dialog.date_edit_date_2.text()
		date_str = str(date)
		date_str_2 = str(date_2)
		if not date or not date_str_2:
			QMessageBox.information(Dialog_Delete(), 'Внимание', 'Заполните пожалуйста все поля.')
			return
		con = sqlite3.connect('FinanceDB')
		cur = con.cursor()
		try:
			sqlstr = """
                                Delete from Finance
                                Where Finance.Date BETWEEN ? and ?
                                """
			cur.execute(sqlstr, [date_str, date_str_2])
		except sqlite3.DatabaseError as err:
			print(err)
		else:
			con.commit()

	def Load_Data(self):
		con = sqlite3.connect('FinanceDB')
		try:
			date_in = self.dateEdit.text()
			date_out = self.dateEdit_2.text()
			cur = con.cursor()
			sqlstr = """
                        SELECT Date, round(income, 2), round(outcome, 2), round(sum, 2), Comment
                        FROM Finance 
                        WHERE Finance.Date BETWEEN ? and ?
						order by Date
					"""
			tablerow = 0
			results = cur.execute(sqlstr, [date_in, date_out])
			for row in results:
				self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
				self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))

				income = QtWidgets.QTableWidgetItem(str('{:,.2f}'.format(row[1]).replace(',', ' ')))
				income.setTextAlignment(QtCore.Qt.AlignRight)
				self.tableWidget.setItem(tablerow, 1, income)

				outcome = QtWidgets.QTableWidgetItem(str('{:,.2f}'.format(row[2]).replace(',', ' ')))
				outcome.setTextAlignment(QtCore.Qt.AlignRight)
				self.tableWidget.setItem(tablerow, 2, outcome)

				sum = QtWidgets.QTableWidgetItem(str('{:,.2f}'.format(row[3]).replace(',', ' ')))
				sum.setTextAlignment(QtCore.Qt.AlignRight)
				self.tableWidget.setItem(tablerow, 3, sum)
				
                

				tablerow += 1
			self.tableWidget.setRowCount(tablerow)
		except sqlite3.DatabaseError as err:
			print(err)
		else:
			con.close()

	def Sum_Month(self):
		con = sqlite3.connect('FinanceDB')
		cur = con.cursor()
		try:
			date_in = self.dateEdit.text()
			date_out = self.dateEdit_2.text()
			sqlstr = """
                        SELECT SUM(Income), Sum(Outcome), Sum(Sum)
                        FROM Finance
                        WHERE Finance.Date BETWEEN ? and ?
                        """
			for row in cur.execute(sqlstr, [date_in, date_out]):
				Line = self.lineEdit
				if row[0] is None:
					Line.setText(str(row[0]))
				else:
					Line.setText(str('{:,.2f}'.format(row[0]).replace(',', ' ')))

				Line_2 = self.lineEdit_2
				if row[1] is None:
					Line_2.setText(str(row[1]))
				else:				
					Line_2.setText(str('{:,.2f}'.format(row[1]).replace(',', ' ')))

				Line_3 = self.lineEdit_3
				if row[2] is None:
					Line_3.setText(str(row[2]))
				else:
					Line_3.setText(str('{:,.2f}'.format(row[2]).replace(',', ' ')))

		except sqlite3.DatabaseError as err:
			print(err)
		else:
			con.close()

	def Figure(self):
		inputDialog = Window()
		rez = inputDialog.exec()

	def Avg_Month(self):
		con = sqlite3.connect('FinanceDB')
		cur = con.cursor()
		try:
			date_in = self.dateEdit.text()
			date_out = self.dateEdit_2.text()

			sqlstr = """                        
					Select avg(total_income), avg(total_outcome), avg(total_sum)
                    from(
                        SELECT SUM(Income) total_income, Sum(Outcome) total_outcome, Sum(Sum) total_sum
                        FROM Finance
                        WHERE strftime('%Y', substr(Date,1,4)||'-'||substr(Date,6,2)||'-'||substr(Date,9,2)) BETWEEN  "2020" and "2030"
                        GROUP BY strftime('%m', substr(Date,1,4)||'-'||substr(Date,6,2)||'-'||substr(Date,9,2))
			            )
                        """
			for row in cur.execute(sqlstr):
				Line_4 = self.lineEdit_4
				if row[0] is None:
					Line_4.setText(str(row[0]))
				else:
					Line_4.setText(str('{:,.2f}'.format(row[0]).replace(',', ' ')))

				Line_5 = self.lineEdit_5
				if row[1] is None:
					Line_5.setText(str(row[1]))
				else:				
					Line_5.setText(str('{:,.2f}'.format(row[1]).replace(',', ' ')))

				Line_6 = self.lineEdit_6
				if row[2] is None:
					Line_6.setText(str(row[2]))
				else:
					Line_6.setText(str('{:,.2f}'.format(row[2]).replace(',', ' ')))
		except sqlite3.DatabaseError as err:
			print(err)
		else:
			con.commit()

	@staticmethod
	def show_warning_messagebox():
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)

		# setting message for Message Box
		msg.setText("Эта функция будет в следующем обновление.")

		# setting Message box window title
		msg.setWindowTitle("Информация")

		# declaring buttons on Message Box
		msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

		# start the app
		retval = msg.exec_()

	def Big_Data_Insert(self):
		'''Экспорт данных из xlsx в sqlite'''

		inputDialog = Dialog_Big_Data_Insert()
		rez = inputDialog.exec()
		if not rez:
			QMessageBox.information(Dialog_Big_Data_Insert(), 'Внимание', 'Диалог сброшен.')
			return


class Dialog_ADD(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Добавить данные')

		self.date_edit_name = QtWidgets.QDateEdit()
		d = QDate.currentDate()
		self.date_edit_name.setDate(d)
		self.date_edit_name.setDisplayFormat("yyyy.MM.dd")
		self.date_edit_name.setMaximumDateTime(
			QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
		self.date_edit_name.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
		self.date_edit_name.setCalendarPopup(True)
		self.line_edit_age = QLineEdit()
		self.line_edit_gender = QLineEdit()

		form_layout = QFormLayout()
		form_layout.addRow('Дата:', self.date_edit_name)
		form_layout.addRow('Доход:', self.line_edit_age)
		form_layout.addRow('Расход:', self.line_edit_gender)

		button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
		button_box.accepted.connect(self.accept)
		button_box.rejected.connect(self.reject)

		main_layout = QVBoxLayout()
		main_layout.addLayout(form_layout)
		main_layout.addWidget(button_box)
		self.setLayout(main_layout)


class Dialog_Big_Data_Insert(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Добавить данные из Excel')
		self.resize(900, 50)
		self.setMaximumHeight(50)

		self.toolbutoon = QToolButton()
		self.toolbutoon.setText("Выбрать файл")
		self.toolbutoon.clicked.connect(lambda: self.open_file_1())
		self.lineEdit = QLineEdit()

		button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
		button_box.accepted.connect(lambda: self.Big_Data_Insert())
		button_box.clicked.connect(self.accept)
		button_box.rejected.connect(self.reject)

		main_layout = QGridLayout()
		main_layout.addWidget(self.lineEdit, 0, 1)
		main_layout.addWidget(self.toolbutoon, 0, 2)
		main_layout.addWidget(button_box, 1, 1)
		self.setLayout(main_layout)

	def Big_Data_Insert(self):
		# 1. Создание и подключение к базе
		# Имя базы
		base_name = 'FinanceDB'

		# метод sqlite3.connect автоматически создаст базу, если ее нет
		connect = sqlite3.connect(base_name)
		# курсор - это специальный объект, который делает запросы и получает результаты запросов
		cursor = connect.cursor()

		# 2. Работа c xlsx файлом
		# Читаем файл и лист1 книги excel
		file = self.lineEdit.text()
		file_to_read = openpyxl.load_workbook(file, data_only=True)
		sheet = file_to_read["Лист1"]

		# Цикл по строкам начиная со второй (в первой заголовки)
		for row in range(2, sheet.max_row + 1):
			# Объявление списка
			data = []
			# Цикл по столбцам от 1 до 5 (6 не включая)
			for col in range(1, 6):
				# value содержит значение ячейки с координатами row col
				value = sheet.cell(row, col).value
				# Список который мы потом будем добавлять
				data.append(value)

			# 3. Запись в базу и закрытие соединения
			# Вставка данных в поля таблицы
			cursor.execute("INSERT INTO Finance VALUES (?, ?, ?, ?, ?);", (data[0], data[1], data[2], data[3], data[4]))

		# сохраняем изменения
		connect.commit()
		# закрытие соединения
		connect.close()

	def open_file_1(self):
		self.file_name = QtWidgets.QFileDialog.getOpenFileName(None, "Open", "", "CSV Files (*.xlsx)")
		if self.file_name[0] != '':
			self.lineEdit.setText(self.file_name[0])


class Dialog_Delete(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Удаление данных')

		self.date_edit_date_1 = QtWidgets.QDateEdit()
		d = QDate.currentDate()
		self.date_edit_date_1.setDate(d)
		self.date_edit_date_1.setDisplayFormat("yyyy.MM.dd")
		self.date_edit_date_1.setMaximumDateTime(
			QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
		self.date_edit_date_1.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
		self.date_edit_date_1.setCalendarPopup(True)

		self.date_edit_date_2 = QtWidgets.QDateEdit()
		d = QDate.currentDate()
		self.date_edit_date_2.setDate(d)
		self.date_edit_date_2.setDisplayFormat("yyyy.MM.dd")
		self.date_edit_date_2.setMaximumDateTime(
			QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
		self.date_edit_date_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
		self.date_edit_date_2.setCalendarPopup(True)
		self.label = QtWidgets.QLabel()
		self.label.setText("Удалить данные")

		form_layout = QFormLayout()
		form_layout.addRow(self.label)
		form_layout.addRow('С:', self.date_edit_date_1)
		form_layout.addRow('По:', self.date_edit_date_2)

		button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
		button_box.accepted.connect(self.accept)
		button_box.rejected.connect(self.reject)

		main_layout = QVBoxLayout()
		main_layout.addLayout(form_layout)
		main_layout.addWidget(button_box)
		self.setLayout(main_layout)


class Window(QDialog):

	# constructor
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)

		_translate = QtCore.QCoreApplication.translate

		def cm_to_inch(value):
			return value / 2.54

		# Настройки графика
		self.figure = plt.figure(figsize=(10, 10), dpi = 100)
		self.resize(1800, 1000)

		# this is the Canvas Widget that
		# displays the 'figure'it takes the
		# 'figure' instance as a parameter to __init__
		self.canvas = FigureCanvas(self.figure)

		# this is the Navigation widget
		# it takes the Canvas widget and a parent
		self.toolbar = NavigationToolbar(self.canvas, self)

		# Just some button connected to 'plot' method
		self.button = QPushButton('Построить график')

		# adding action to the button
		self.button.clicked.connect(self.plot)

		# Настройки ввода даты_1
		self.dateEdit = QtWidgets.QDateEdit(self.canvas)
		self.dateEdit.setAutoFillBackground(False)
		self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
		self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
		self.dateEdit.setCalendarPopup(True)
		d = QDate.currentDate().addDays(-30)
		self.dateEdit.setDate(QtCore.QDate(d))
		self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy.MM.dd"))
		self.dateEdit.setObjectName("dateEdit")

		# Настройки ввода даты_2
		self.dateEdit_2 = QtWidgets.QDateEdit(self.canvas)
		self.dateEdit_2.setAutoFillBackground(False)
		self.dateEdit_2.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
		self.dateEdit_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
		self.dateEdit_2.setCalendarPopup(True)
		self.dateEdit_2.setObjectName("dateEdit_2")
		self.dateEdit_2.move(130, 0)
		self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "yyyy.MM.dd"))
		d_2_1 = QDate.currentDate()
		d_2 = d_2_1.addDays(1)
		self.dateEdit_2.setDate(d_2)

		# Настройка CheckBox Доход
		self.checkBox = QtWidgets.QCheckBox(self.canvas)
		self.checkBox.move(255, 1)
		self.checkBox.setText(_translate("MainWindow", "Доход"))
		self.checkBox.setChecked(True)

		# Настройка CheckBox Расход
		self.checkBox_2 = QtWidgets.QCheckBox(self.canvas)
		self.checkBox_2.move(355, 1)
		self.checkBox_2.setText(_translate("MainWindow", "Расход"))
		self.checkBox_2.setChecked(True)

		# Настройка CheckBox Остаток
		self.checkBox_3 = QtWidgets.QCheckBox(self.canvas)
		self.checkBox_3.move(455, 1)
		self.checkBox_3.setText(_translate("MainWindow", "Остаток"))
		self.checkBox_3.setChecked(True)

		# creating a Vertical Box layout
		layout = QVBoxLayout()

		# adding tool bar to the layout
		layout.addWidget(self.toolbar)

		# adding canvas to the layout
		layout.addWidget(self.canvas)

		# adding push button to the layout
		layout.addWidget(self.button)

		# setting layout to the main window
		self.setLayout(layout)

	# action called by the push button
	def plot(self):
		# задаём даты от до
		date_1 = self.dateEdit.text()
		date_2 = self.dateEdit_2.text()

		# подключаемся к БД
		con = sqlite3.connect('FinanceDB')
		cur = con.cursor()
		sqlstr = """
                            Select Date, income, outcome, sum
                            From Finance
                            Where Date between ? and ?
                            order by Date
                            """
		cur.execute(sqlstr, [date_1, date_2])
		records = cur.fetchall()

		# задаём первоначальные массивы
		Date_0 = []
		Income = []
		Outcome = []
		Sum = []

		a = 0
		# добавляем в массивы данные из запроса
		for row in records:
			Date_0.append([row[0]])
			Income.append(row[1])
			Outcome.append(row[2])
			Sum.append(row[3])
			a += 1

		Date_1 = []

		# форматируем список в списке в строки в списке
		for i in Date_0:
			a = "".join(i)
			i = datetime.datetime.strptime(a, '%Y.%m.%d').strftime('%d.%m.%Y')
			Date_1.append(i)

		# clearing old figure
		self.figure.clear()

		# create an axis
		ax = self.figure.add_subplot()

		# форматируем даты из списка в специальный код воспринимаемый matplotlib
		ax.grid()
		ax.set_title("Финансы")
		ax.set_xlabel("Даты")
		ax.set_ylabel("Руб.")
		ax.set_xticklabels(Date_1, rotation=45)

		if self.checkBox.isChecked() and (self.checkBox_2.isChecked() or self.checkBox_3.isChecked()):
			ax.set_ylim(ymin=-abs((max(Outcome) * 1.5)), ymax=(max(Income) * 1.5))
		elif self.checkBox.isChecked():
			ax.set_ylim(ymax=(max(Income) * 1.5))
		elif self.checkBox_2.isChecked():
			ax.set_ylim(ymin=-abs((max(Outcome) * 1.5)))
		elif self.checkBox_3.isChecked():
			ax.set_ylim(ymin=(min(Sum) * 1.5), ymax=(max(Sum) * 1.5))

		cnt_dates = []
		a = 0
		for i in Date_1:
			a += 1
			cnt_dates.append(a)

		ax.set_xticks(cnt_dates)

		date_income = []
		date_sum = []

		x = 1.0
		x = float(x)
		Outcome_1 = Outcome.copy()
		Outcome_1.append(x)
		Outcome_2 = Outcome.copy()
		Outcome_2.insert(0, float(1.0))

		Outcome_percent = []
		Income_percent = []
		Sum_percent = []

		for a, b in zip(Outcome[::1], Outcome[1::1]):
			if a == 0:
				continue
			else:
				c = 100 * (b - a) / a
				c = round(c, 2)
				Outcome_percent.append(c)

		for a, b in zip(Income[::1], Income[1::1]):
			if a == 0:
				continue
			else:
				c = 100 * (b - a) / a
				c = round(c, 2)
				Income_percent.append(c)

		for a, b in zip(Sum[::1], Sum[1::1]):
			if a == 0:
				continue
			else:
				c = 100 * (b - a) / a
				c = round(c, 2)
				Sum_percent.append(c)

		if self.checkBox.isChecked():
			for i in cnt_dates:
				i += 0.1
				date_income.append(i)
			p1 = ax.bar(date_income, Income, width=0.1, color="blue", label="Доход")
			ax.bar_label(p1, label_type='edge', color="blue")
			ax.plot(date_income, Income, color="blue", label="Изменение Дохода", ls="--", alpha=0.25)

			for i, j, z in zip(date_income, Income, Income_percent):
				j += 5000
				i += -abs(0.1)
				if z > 0:
					z = "+" + str(z) + "%"
					ax.annotate(z, xy=(i, j), color="green")
				else:
					z = str(z) + "%"
					ax.annotate(z, xy=(i, j), color="red")
			ax.legend()

		if self.checkBox_2.isChecked():
			Outcome = [-x for x in Outcome]
			p2 = ax.bar(cnt_dates, Outcome, width=0.1, color="red", label="Расход")
			ax.bar_label(p2, label_type='edge', color="red")
			ax.plot(cnt_dates, Outcome, color="red", label="Изменение Расхода", ls="--", alpha=0.25)
			for i, j, z in zip(cnt_dates, Outcome, Outcome_percent):
				j += -abs(max(Outcome) * 0.8)
				i += -abs(0.1)
				if z > 0:
					z = "+" + str(z) + "%"
					ax.annotate(z, xy=(i, j), color="red")
				else:
					z = str(z) + "%"
					ax.annotate(z, xy=(i, j), color="green")
			ax.legend()

		if self.checkBox_3.isChecked():
			for i in cnt_dates:
				i += -0.1
				date_sum.append(i)
			p3 = ax.bar(date_sum, Sum, width=0.1, color="green", label="Остаток")
			ax.bar_label(p3, label_type='edge', color="green")
			ax.plot(date_sum, Sum, color="green", label="Изменение остатка", ls="--", alpha=0.25)
			for i, j, z in zip(date_sum, Sum, Sum_percent):
				if j > 0:
					j_1 = j + 5000
					i += -abs(0.1)
					if z > 0:
						z = "+" + str(z) + "%"
						ax.annotate(j, xy=(i, j_1), color="green")
					else:
						z = str(z) + "%"
						ax.annotate(j, xy=(i, j_1), color="red")
				else:
					j_1 = j -abs(2500)
					i += -abs(0.1)
					if z > 0:
						z = "+" + str(z) + "%"
						ax.annotate(j, xy=(i, j_1), color="red")
					else:
						z = str(z) + "%"
						ax.annotate(j_1, xy=(i, j_1), color="green")

			ax.legend()

		# refresh canvas
		self.canvas.draw()


if __name__ == '__main__':
	import sys

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	# app.setStyleSheet(qdarkstyle.load_stylesheet())

	ui.toolButton_4.clicked.connect(lambda: ui.Load_Data())
	ui.toolButton_4.clicked.connect(lambda: ui.Sum_Month())
	ui.toolButton_4.clicked.connect(lambda: ui.Avg_Month())
	ui.toolButton_5.clicked.connect(lambda: ui.Figure())
	ui.toolButton_3.clicked.connect(lambda: ui.Big_Data_Insert())

	date_1 = ui.dateEdit
	date_1.setMinimumDate(QDate(2022, 1, 1))
	date_1.setMaximumDate(QDate(2050, 12, 31))

	date_2 = ui.dateEdit_2
	date_2.setMinimumDate(QDate(2022, 1, 1))
	date_2.setMaximumDate(QDate(2050, 12, 31))

	ui.toolButton.clicked.connect(lambda: ui.add_financ())

	ui.toolButton_2.clicked.connect(lambda: ui.Delete_financ())

	sys.exit(app.exec_())
