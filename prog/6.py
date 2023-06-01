from PyQt5 import QtCore, QtWidgets
import sys


class MainClass():

    def calc(self):
        self.mainWindow.mainWindow_label_mass.setText(self.mainWindow.mainWindow_combobox.currentText())

    class mainWindowClass(QtWidgets.QMainWindow):

        def init(self, parent=None, fatherlyClass=None):
            QtWidgets.QMainWindow.init(self, parent)
            self.centralwidget = QtWidgets.QWidget()
            self.centralwidget.setObjectName("centralwidget")

            self.mainWindow_widthEdit = QtWidgets.QLineEdit()
            self.mainWindow_widthEdit.setObjectName("width")

            self.mainWindow_lengthEdit = QtWidgets.QLineEdit()
            self.mainWindow_lengthEdit.setObjectName("length")

            self.mainWindow_combobox = QtWidgets.QComboBox()
            self.mainWindow_combobox.addItems(
                ['Пластик','Алюминий','Соломка','Текстиль'])
            self.mainWindow_combobox.setObjectName(
                "material_type")

            self.mainWindow_label_mass = QtWidgets.QLabel()
            self.mainWindow_label_mass.setObjectName("label_mass")
            self.mainWindow_label_mass.setText(" ")

            self.mainWindow_label_width = QtWidgets.QLabel()
            self.mainWindow_label_width.setObjectName("label_width")
            self.mainWindow_label_width.setText("Ширина (см.)")

            self.mainWindow_label_length = QtWidgets.QLabel()
            self.mainWindow_label_length.setObjectName("label_length")
            self.mainWindow_label_length.setText("Высота (см.)")

            self.mainWindow_label_material_type = QtWidgets.QLabel()
            self.mainWindow_label_material_type.setObjectName(
                "label_material_type")
            self.mainWindow_label_material_type.setText("Материал")

            self.mainWindow_button_calc = QtWidgets.QPushButton('OK')
            self.mainWindow_button_calc.setObjectName("button_find")

            hboxWidth = QtWidgets.QHBoxLayout()
            hboxWidth.addWidget(self.mainWindow_label_width)
            hboxWidth.addWidget(self.mainWindow_widthEdit)
            hboxWidth.addSpacing(1)

            hboxLength = QtWidgets.QHBoxLayout()
            hboxLength.addWidget(self.mainWindow_label_length)
            hboxLength.addWidget(self.mainWindow_lengthEdit)

            hboxMaterial = QtWidgets.QHBoxLayout()
            hboxMaterial.addWidget(self.mainWindow_label_material_type)
            hboxMaterial.addWidget(self.mainWindow_combobox)

            hboxButton = QtWidgets.QHBoxLayout()
            hboxButton.addWidget(self.mainWindow_button_calc)

            vbox = QtWidgets.QVBoxLayout()
            vbox.addLayout(hboxLength)
            vbox.addLayout(hboxWidth)
            vbox.addLayout(hboxMaterial)
            vbox.addLayout(hboxButton)
            vbox.addWidget(self.mainWindow_label_mass)

            self.centralwidget.setLayout(vbox)
            self.setCentralWidget(self.centralwidget)

            self.mainWindow_button_calc.clicked.connect(fatherlyClass.calc)

    def init(self):
        self.depth = 0.5 * 0.01  # 0.5 cm

        self.mainWindow = self.mainWindowClass(fatherlyClass=self)
        self.mainWindow.setWindowTitle('Жалюзи')
        self.mainWindow.setWindowFlags(QtCore.Qt.Window)
        self.mainWindow.show()


if name == "main":
    app = QtWidgets.QApplication(sys.argv)
    gui = MainClass()
    sys.exit(app.exec_())