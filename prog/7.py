from PyQt5.QtWidgets import *

import os
os.system('cls')
class Widget(QWidget):
    def init(self):
        super().init()

        self.label = QLabel('Формат')

        self.radio_button_1 = QRadioButton('9х12')
        self.radio_button_1.setChecked(True)
        self.label2 = QLabel('Current: ' + self.radio_button_1.text())
        self.radio_button_2 = QRadioButton('10х15')
        self.radio_button_3 = QRadioButton('18х24')

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button_1)
        self.button_group.addButton(self.radio_button_2)
        self.button_group.addButton(self.radio_button_3)

        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

        layout1 = QVBoxLayout()
        layout1.addWidget(self.label)
        layout1.addWidget(self.radio_button_1)
        layout1.addWidget(self.radio_button_2)
        layout1.addWidget(self.radio_button_3)
        layout2 = QHBoxLayout()
        label2=QLabel('Количество:')
        Text2=QLineEdit()
        layout2.addWidget(label2)
        layout2.addWidget(Text2)
        layout1.addLayout(layout2)
        button1=QPushButton('ok')
        layout1.addWidget(button1)
        layout1.addWidget(self.label2)
        self.setLayout(layout1)
    def _on_radio_button_clicked(self, button):
        self.label2.setText('Current: ' + button.text())


if name == 'main':
    app = QApplication([])

    w = Widget()
    w.show()

    app.exec()