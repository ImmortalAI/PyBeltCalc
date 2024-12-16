import asyncio
from .database import create_db_and_tables
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from .gui import MyWidget
from bd_realization.constant_tables.table1_8 import fill_table as table1
from bd_realization.constant_tables.table2_1 import fill_table as table2
from bd_realization.constant_tables.table2_4 import fill_table as table3
from bd_realization.constant_tables.table2_7 import fill_table as table4
from bd_realization.constant_tables.table2_8 import fill_table as table5
from bd_realization.constant_tables.table2_9 import fill_table as table6

if __name__ == "__main__":
    print(sys.argv)

    create_db_and_tables()
    if len(sys.argv) > 1 and sys.argv[1] == "fill":
        print("Filling constant tables")
        table1()
        table2()
        table3()
        table4()
        table5()
        table6()
    app = QtWidgets.QApplication([])
    app.setApplicationName("Расчет числа поликлиновых ремней на клиноременной передаче")
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())