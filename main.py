from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import sys
import psycopg2

class MainWindow(QWidget):
	def __init__(self):
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
		QWidget.__init__(self)
		self.setWindowTitle('Authorization')
		self.setMaximumSize(QtCore.QSize(800,600))
		self.setMinimumSize(QtCore.QSize(800,600))
		self.label=QLabel('<p align="center">Hello!</p>',self)
		self.label.move(0,0)
		self.label.setStyleSheet("""background-color: rgb(255,255,255); font-size: 24px; color: rgb(0,0,0); font: bold "Times New Roman"; border-radius: 5px; min-width: 800; min-height: 600; max-width: 800; max-height: 600""")

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