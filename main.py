from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import sys
import psycopg2

class MainWindow(QWidget):
	def __init__(self):
		self.n = 2
		QWidget.__init__(self)
		self.setWindowTitle('MTUCI is the best university ever!')
		self.setMaximumSize(QtCore.QSize(640,480))
		self.setMinimumSize(QtCore.QSize(640,480))
		self.main = QWidget(self)
		self.layout = QVBoxLayout(self.main)


		
		self.monday = QWidget(self)
		self.tuesday = QWidget(self)
		self.wednesday = QWidget(self)
		self.thursday = QWidget(self)
		self.friday = QWidget(self)
		self.saturday = QWidget(self)
		self.sunday = QWidget(self)
		self.monday1 = QWidget(self)
		self.tuesday1 = QWidget(self)
		self.wednesday1 = QWidget(self)
		self.thursday1 = QWidget(self)
		self.friday1 = QWidget(self)
		self.saturday1 = QWidget(self)
		self.sunday1 = QWidget(self)
		

		self.table_widget('Monday',2)
		self.monday.layout = QVBoxLayout(self)
		self.monday.layout.addWidget(self.table)
		self.monday.setLayout(self.monday.layout)


		self.table_widget('Monday', 1)
		self.monday1.layout = QVBoxLayout(self)
		self.monday1.layout.addWidget(self.table)
		self.monday1.setLayout(self.monday1.layout)

		
		self.table_widget('Tuesday',2)
		self.tuesday.layout = QVBoxLayout(self)
		self.tuesday.layout.addWidget(self.table)
		self.tuesday.setLayout(self.tuesday.layout)

		self.table_widget('Tuesday', 1)
		self.tuesday1.layout = QVBoxLayout(self)
		self.tuesday1.layout.addWidget(self.table)
		self.tuesday1.setLayout(self.tuesday1.layout)

		self.table_widget('Wednesday',2)
		self.wednesday.layout = QVBoxLayout(self)
		self.wednesday.layout.addWidget(self.table)
		self.wednesday.setLayout(self.wednesday.layout)

		self.table_widget('Wednesday',1)
		self.wednesday1.layout = QVBoxLayout(self)
		self.wednesday1.layout.addWidget(self.table)
		self.wednesday1.setLayout(self.wednesday1.layout)

		self.table_widget('Thursday',2)
		self.thursday.layout = QVBoxLayout(self)
		self.thursday.layout.addWidget(self.table)
		self.thursday.setLayout(self.thursday.layout)

		self.table_widget('Thursday', 1)
		self.thursday1.layout = QVBoxLayout(self)
		self.thursday1.layout.addWidget(self.table)
		self.thursday1.setLayout(self.thursday1.layout)

		self.table_widget('Friday',2)
		self.friday.layout = QVBoxLayout(self)
		self.friday.layout.addWidget(self.table)
		self.friday.setLayout(self.friday.layout)

		self.table_widget('Friday', 1)
		self.friday1.layout = QVBoxLayout(self)
		self.friday1.layout.addWidget(self.table)
		self.friday1.setLayout(self.friday1.layout)

		self.table_widget('Saturday',2)
		self.saturday.layout = QVBoxLayout(self)
		self.saturday.layout.addWidget(self.table)
		self.saturday.setLayout(self.saturday.layout)

		self.table_widget('Saturday', 1)
		self.saturday1.layout = QVBoxLayout(self)
		self.saturday1.layout.addWidget(self.table)
		self.saturday1.setLayout(self.saturday1.layout)

		self.table_widget('Sunday',2)
		self.sunday.layout = QVBoxLayout(self)
		self.sunday.layout.addWidget(self.table)
		self.sunday.setLayout(self.sunday.layout)

		self.table_widget('Sunday', 1)
		self.sunday1.layout = QVBoxLayout(self)
		self.sunday1.layout.addWidget(self.table)
		self.sunday1.setLayout(self.sunday1.layout)

		self.frame = QFrame(self)
		self.frame.resize(640,480)
		self.frame.move(0,0)
		self.frame.setStyleSheet("""color: rgb(240,240,240); background-color: rgb(240,240,240)""")


		self.tabs = QTabWidget(self)
		self.tabs.resize(600,450)
		self.tabs.move(20,15)
		self.tabs.addTab(self.monday,"Monday")
		self.tabs.addTab(self.tuesday,"Tuesday")
		self.tabs.addTab(self.wednesday,"Wednesday")
		self.tabs.addTab(self.thursday,"Thursday")
		self.tabs.addTab(self.friday,"Friday")
		self.tabs.addTab(self.saturday,"Saturday")
		self.tabs.addTab(self.sunday,"Sunday")
		self.switch_button = QPushButton('Switch week',self)
		self.switch_button.clicked.connect(self.switcher)
		self.switch_button.setStyleSheet("""min-height: 25; min-width: 100; max-height: 25; max-width: 100;""")
		self.switch_button.move(495, 5)
		self.layout.addWidget(self.tabs)
		self.layout.addWidget(self.switch_button)
		self.setLayout(self.layout)



	def switcher(self):
		if self.n == 2:
			self.n = 1
		else:
			self.n = 2
		a = self.tabs.currentIndex()
		if self.n == 1:
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.addTab(self.monday1,"Monday")
			self.tabs.addTab(self.tuesday1,"Tuesday")
			self.tabs.addTab(self.wednesday1,"Wednesday")
			self.tabs.addTab(self.thursday1,"Thursday")
			self.tabs.addTab(self.friday1,"Friday")
			self.tabs.addTab(self.saturday1,"Saturday")
			self.tabs.addTab(self.sunday1,"Sunday")
			self.tabs.setCurrentIndex(a)
			self.setWindowTitle('MTUCI is the best university ever! even week')
		else:
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.removeTab(0)
			self.tabs.addTab(self.monday,"Monday")
			self.tabs.addTab(self.tuesday,"Tuesday")
			self.tabs.addTab(self.wednesday,"Wednesday")
			self.tabs.addTab(self.thursday,"Thursday")
			self.tabs.addTab(self.friday,"Friday")
			self.tabs.addTab(self.saturday,"Saturday")
			self.tabs.addTab(self.sunday,"Sunday")
			self.tabs.setCurrentIndex(a)
			self.setWindowTitle('MTUCI is the best university ever! odd week')


	def table_widget(self, day, week):

		try:

			t1 = "postgres"#DATABASE NAME!
			t2 = "postgres"#USER NICKNAME!
			t3 = "postgres"#USER PASSCODE!
			t4 = "5432"#PORT!
			t5 = "test"#TABLE NAME!

			conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4)
			cur_sql = conn.cursor()
			cur_sql.execute('SELECT * FROM '+str(t5))

		except Exception as error:

			print('Something wrong with postgresql autorization. Error: '+str(error))
		try:
			self.table = QTableWidget(self)
			self.table.setColumnCount(3)
			self.table.setRowCount(5)
			self.table.setMinimumWidth(560)
			self.table.setMinimumHeight(385)
			self.table.move(40, 50)
			self.table.setHorizontalHeaderLabels(['Class','Time','Have any sense?']) 
			self.table.setItem(0, 1, QTableWidgetItem('9:30-11:05'))
			self.table.setItem(1, 1, QTableWidgetItem('11:20-12:55'))
			self.table.setItem(2, 1, QTableWidgetItem('13:10-14:45'))
			self.table.setItem(3, 1, QTableWidgetItem('15:25-17:00'))
			self.table.setItem(4, 1, QTableWidgetItem('17:15-18:50'))

			day = self.coverterDAYtoNUM(day)

			if week %2 != 0:
				if day == 1:
					cur_sql.execute("SELECT md1 FROM book")
				elif day == 2:
					cur_sql.execute("SELECT tu1 FROM book")
				elif day == 3:
					cur_sql.execute("SELECT wd1 FROM book")
				elif day == 4:
					cur_sql.execute("SELECT th1 FROM book")
				elif day == 5:
					cur_sql.execute("SELECT fd1 FROM book")				
				elif day == 6:
					cur_sql.execute("SELECT sd1 FROM book")
				elif day == 7:
					cur_sql.execute("SELECT sud FROM book")			
			else:
				if day == 1:
					cur_sql.execute("SELECT md2 FROM book")
				elif day == 2:
					cur_sql.execute("SELECT tu2 FROM book")				
				elif day == 3:
					cur_sql.execute("SELECT wd2 FROM book")
				elif day == 4:
					cur_sql.execute("SELECT th2 FROM book")				
				elif day == 5:
					cur_sql.execute("SELECT fd2 FROM book")
				elif day == 6:
					cur_sql.execute("SELECT sd2 FROM book")				
				elif day == 7:
					cur_sql.execute("SELECT sud FROM book")

			answer_help = cur_sql.fetchall()
			for i in range(len(answer_help)):
				self.table.setItem(i, 0, QTableWidgetItem(str(answer_help[i])[2:-3]))
				self.table.setItem(i, 2, QTableWidgetItem(str('No')))
				self.table.setStyleSheet("""background: rgb(255,255,255); border: 0px""")

			self.table.resizeColumnsToContents()
		except Exception as error:
			pass
	def coverterDAYtoNUM(self, today):
		if today == "Monday":
			return 1
		elif today == 'Tuesday':
			return 2
		elif today == 'Wednesday':
			return 3
		elif today == 'Thursday':
			return 4
		elif today == 'Friday':
			return 5
		elif today == 'Saturday':
			return 6
		elif today == 'Sunday':
			return 7



class Control:
	def __init__(self):
		pass
	def main(self):
		self.main = MainWindow()
		self.main.show()
app = QApplication(sys.argv)
screen = Control()
screen.main()
sys.exit(app.exec_())