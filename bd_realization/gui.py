import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtAsyncio
from .logic import generate_default, calculate, save_values
from .models import Unit, AssemblyUnit, Part

current_unit: Unit | None = None
current_assembly_unit: AssemblyUnit | None = None
current_belt: Part | None = None
current_shift: Part | None = None


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.widget_classes = [StartWidget,  NodeWidget, AssemblyUnitWidget, Part1Widget,
                               Part2Widget, ResultWidget]
        self.current_stage = 0
        self.current_widget = None

        self.inner_layout = QtWidgets.QVBoxLayout(self)
        self.inner_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.load_stage()

    def load_stage(self):
        print("Loading stage... ", self.current_stage)
        if self.current_widget is not None:
            self.inner_layout.removeWidget(self.current_widget)
            self.current_widget.deleteLater()
        self.current_widget = self.widget_classes[self.current_stage]()
        print("Loaded! ", type(self.current_widget))
        self.inner_layout.addWidget(self.current_widget)
        self.current_widget.next_signal.connect(self.load_next_stage)

    @QtCore.Slot()
    def load_next_stage(self):
        self.current_stage += 1
        if self.current_stage >= len(self.widget_classes):
            self.current_stage = 0
        self.load_stage()


class StartWidget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Начать расчет числа ремней")
        self.button.clicked.connect(self.start)

        self.inner_layout = QtWidgets.QVBoxLayout(self)
        self.inner_layout.addWidget(self.button)

    @QtCore.Slot()
    def start(self):
        global current_unit, current_assembly_unit, current_belt, current_shift
        current_unit, current_assembly_unit, current_belt, current_shift = generate_default()
        self.next_signal.emit()


class NodeWidget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        if current_unit is None:
            return

        available_load = [
            "Спокойная нагрузка. Пусковая нагрузка до 120% номинальной",
            "Умеренные колебания нагрузки. Пусковая нагрузка до 150% номинальной",
            "Значительные колебания нагрузки. Пусковая нагрузка до 200% номинальной",
            "Весьма неравномерная и ударная нагрузка. Пусковая нагрузка до 300% номинальной"
        ]

        available_machine = [
            "Ленточные транспортеры",
            "Станки с непрерывным процессом резания: токарные, сверлильные, шлифовальные",
            "Пластинчатые транспортеры",
            "Станки-автоматы, фрезерные, зубофрезерные и револьверные станки",
            "Реверсивные приводы",
            "Станки строгальные, долбежные и зубодолбежные",
            "Транспортеры винтовые и скребковые",
            "Элеваторы",
            "Винтовые и эксцентриковые прессы с относительно тяжелыми маховиками",
            "Подъемники",
            "Винтовые и эксцентриковые прессы с относительно легкими маховиками",
            "Ножницы, молоты, бегуны, мельницы"
        ]

        available_engine = [
            "I",
            "II"
        ]

        self.inner_layout = QtWidgets.QVBoxLayout(self)
        self.inner_layout.addWidget(QtWidgets.QLabel("Введите параметры узла"))
        
        self.HN = QtWidgets.QComboBox()
        self.HN.addItems(available_load)
        if current_unit.HN is not None:
            self.HN.setCurrentText(current_unit.HN)
            
        self.TM = QtWidgets.QComboBox()
        self.TM.addItems(available_machine)
        if current_unit.TM is not None:
            self.TM.setCurrentText(current_unit.TM)

        self.TD = QtWidgets.QComboBox()
        self.TD.addItems(available_engine)
        if current_unit.TD is not None:
            self.TD.setCurrentText(current_unit.TD)

        self.inner_layout.addWidget(QtWidgets.QLabel("Характер нагрузки:"))
        self.inner_layout.addWidget(self.HN)
        self.inner_layout.addWidget(QtWidgets.QLabel("Тип машины:"))
        self.inner_layout.addWidget(self.TM)
        self.inner_layout.addWidget(QtWidgets.QLabel("Тип двигателя:"))
        self.inner_layout.addWidget(self.TD)
        self.button = QtWidgets.QPushButton("Перейти к вводу параметров передачи")
        self.button.clicked.connect(self.next)
        self.inner_layout.addWidget(self.button)

    @QtCore.Slot()
    def next(self):
        if current_unit is None:
            return
        current_unit.HN = self.HN.currentText()
        current_unit.TM = self.TM.currentText()
        current_unit.TD = self.TD.currentText()
        self.next_signal.emit()

class AssemblyUnitWidget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        if current_assembly_unit is None:
            return

        self.inner_layout = QtWidgets.QVBoxLayout(self)

        self.inner_layout.addWidget(QtWidgets.QLabel(
            f"Наименование: {current_assembly_unit.NSE}"))
        self.inner_layout.addWidget(QtWidgets.QLabel(
            f"Тип: {current_assembly_unit.TSE}"))
        self.inner_layout.addWidget(QtWidgets.QLabel(
            f"Вид: {current_assembly_unit.VSE}"))
        
        self.inner_layout.addWidget(QtWidgets.QLabel(
            "Введите параметры сборочной единицы"))
        
        self.u = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Передаточное число, u:"))
        self.inner_layout.addWidget(self.u)
        
        self.N = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Мощность, N:"))
        self.inner_layout.addWidget(self.N)

        self.button = QtWidgets.QPushButton("Перейти к вводу параметров детали")
        self.button.clicked.connect(self.next)
        self.inner_layout.addWidget(self.button)

    @QtCore.Slot()
    def next(self):
        if current_assembly_unit is None:
            return
        current_assembly_unit.u = float(self.u.text())
        current_assembly_unit.N = float(self.N.text())
        self.next_signal.emit()


class Part1Widget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        if current_belt is None:
            return
        
        self.inner_layout = QtWidgets.QVBoxLayout(self)

        self.inner_layout.addWidget(QtWidgets.QLabel(f"Наименование: {current_belt.ND}"))
        
        self.inner_layout.addWidget(QtWidgets.QLabel("Введите параметры детали"))

        self.profil = QtWidgets.QComboBox()
        self.profil.addItems(["К", "Л"])
        self.inner_layout.addWidget(QtWidgets.QLabel("Профиль (шифр) ремней, profil:"))
        self.inner_layout.addWidget(self.profil)

        self.L0 = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Исходная длина ремня, L0:"))
        self.inner_layout.addWidget(self.L0)
        
        self.L = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Длина ремня, L:"))
        self.inner_layout.addWidget(self.L)
        
        self.V = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Скорость ремня, V:"))
        self.inner_layout.addWidget(self.V)
        
        self.button = QtWidgets.QPushButton("Перейти к вводу параметров следующей детали")
        self.button.clicked.connect(self.next)
        self.inner_layout.addWidget(self.button)

    @QtCore.Slot()
    def next(self):
        if current_belt is None:
            return
        current_belt.profil = self.profil.currentText()
        current_belt.L0 = float(self.L0.text())
        current_belt.L = float(self.L.text())
        current_belt.V = float(self.V.text())
        self.next_signal.emit()

class Part2Widget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        if current_shift is None:
            return
        
        self.inner_layout = QtWidgets.QVBoxLayout(self)

        self.inner_layout.addWidget(QtWidgets.QLabel(f"Наименование: {current_shift.ND}"))
        
        self.inner_layout.addWidget(QtWidgets.QLabel("Введите параметры шкива"))

        self.DP1 = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Диаметр меньшего шкива, DP1:"))
        self.inner_layout.addWidget(self.DP1)

        self.alpha1 = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Угол обхвата, alpha1:"))
        self.inner_layout.addWidget(self.alpha1)

        self.button = QtWidgets.QPushButton("Перейти к этапу расчета")
        self.button.clicked.connect(self.next)
        self.inner_layout.addWidget(self.button)

    @QtCore.Slot()
    def next(self):
        if current_shift is None:
            return
        current_shift.DP1 = int(self.DP1.text())
        current_shift.alpha1 = float(self.alpha1.text())
        calculate(current_unit, current_assembly_unit, current_belt, current_shift)  # type: ignore
        self.next_signal.emit()

class ResultWidget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.inner_layout = QtWidgets.QVBoxLayout(self)

        self.inner_layout.addWidget(QtWidgets.QLabel(f"Число ремней: {current_assembly_unit.Z if current_assembly_unit else ''}"))

        self.save_button = QtWidgets.QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save)
        self.inner_layout.addWidget(self.save_button)

        self.cancel_button = QtWidgets.QPushButton("Отменить")
        self.cancel_button.clicked.connect(self.cancel)
        self.inner_layout.addWidget(self.cancel_button)

    @QtCore.Slot()
    def save(self):
        if current_unit is None or current_assembly_unit is None or current_belt is None or current_shift is None:
            return
        save_values(current_unit, current_assembly_unit, current_belt, current_shift)
        self.next_signal.emit()

    @QtCore.Slot()
    def cancel(self):
        self.next_signal.emit()

