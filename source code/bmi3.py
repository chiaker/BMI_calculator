import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QSizePolicy, QMessageBox, QRadioButton, QMessageBox, QButtonGroup, QTextEdit, QDialog
from PyQt5 import QtGui, QtWidgets


class BMIInfoDialogEng(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('BMI Information')
        app.setStyle('Fusion')
        self.info_label = QLabel('BMI (Body Mass Index) Information')
        self.info_text = QTextEdit()
        self.info_text.setReadOnly(True)
        self.info_text.setPlainText('The Body Mass Index (BMI) is a measure of body fat based on your weight and height. It is calculated by dividing your weight in kilograms by the square of your height in meters.\n\n'
                                    'The BMI provides an indication of whether you are underweight, normal weight, overweight, or obese. Here are the BMI categories:\n'
                                    '- BMI less than 18.5: Underweight\n'
                                    '- BMI 18.5 to 24.9: Normal weight\n'
                                    '- BMI 25 to 29.9: Overweight\n'
                                    '- BMI 30 or greater: Obese\n\n'
                                    'Please note that BMI is a general indicator and does not take into account factors such as muscle mass and distribution of fat.')

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.info_text)

        self.setLayout(layout)


class BMIInfoDialogRus(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Информация об ИМТ')

        self.info_label = QLabel('Информация об ИМТ (Индекс Массы Тела)')
        self.info_text = QTextEdit()
        self.info_text.setReadOnly(True)
        self.info_text.setPlainText('ИМТ (Индекс Массы Тела) - это числовое значение, которое позволяет оценить соответствие массы человека и его роста и, таким образом, косвенно судить о его степени недостатка или избытка веса. ИМТ широко используется для определения категорий веса и оценки связанных с этим рисков для здоровья.\n\n'
                                    'Полученное значение ИМТ сравнивается с определенными интервалами или категориями, которые обычно определяются Всемирной организацией здравоохранения (ВОЗ) или другими медицинскими организациями. Эти категории обычно включают:\n'
                                    '- ИМТ менее 18.5: Недостаточная масса тела (недостаток веса)\n'
                                    '- ИМТ от 18.5 до 24.9: Нормальная масса тела\n'
                                    '- ИМТ от 25 до 29.9: Избыточная масса тела (предожирение)\n'
                                    '- ИМТ 30 и выше: Ожирение\n\n'
                                    'Обратите внимание, что ИМТ является общим показателем и не учитывает такие факторы, как мышечная масса и распределение жира.')

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.info_text)

        self.setLayout(layout)


class BMIWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор ИМТ')
        self.language = 'RU'
        self.setup_ui()
        self.setMinimumSize(380, 300)
        self.setStyleSheet("QWidget{background-color: #FBFBFB;}")
        self.edit = QtWidgets.QLineEdit()
        self.edit.setFont(QtGui.QFont("Yu Gothic UI", 14))
        self.edit.setFixedHeight(40)
        self.edit.setFixedHeight(40)
        self.edit.setStyleSheet("""
                QLineEdit{
                    border: 1px solid #db2e4e;
                }
                """)

    def setup_ui(self):
        self.grats_label = QLabel('Введите ваш вес и рост:')
        self.grats_label.setFont(QtGui.QFont("Yu Gothic UI", 9))
        self.space_label = QLabel()
        self.weight_label = QLabel('Вес (кг):')
        self.weight_label.setFont(QtGui.QFont("Yu Gothic UI", 9))
        self.weight_input = QLineEdit()
        self.height_label = QLabel('Рост (см):')
        self.height_label.setFont(QtGui.QFont("Yu Gothic UI", 9))
        self.height_input = QLineEdit()
        self.result_label = QLabel()

        self.weight_input.setMaxLength(5)
        self.height_input.setMaxLength(5)

        self.calculate_button = QPushButton('Рассчитать ИМТ')
        self.calculate_button.clicked.connect(self.calculate_bmi)
        self.calculate_button.setFont(QtGui.QFont("Yu Gothic UI", 9))

        self.lang_group = QButtonGroup()

        self.lang_button_eng = QRadioButton('ENG')
        self.lang_button_eng.clicked.connect(lambda: self.change_language('ENG'))

        self.lang_button_ru = QRadioButton('RU')
        self.lang_button_ru.clicked.connect(lambda: self.change_language('RU'))
        self.lang_button_ru.setChecked(True)

        lang_layout = QHBoxLayout()
        self.lang_group.addButton(self.lang_button_eng)
        self.lang_group.addButton(self.lang_button_ru)

        self.info_button = QPushButton('Что такое ИМТ?')
        self.lang_group.addButton(self.info_button)
        self.info_button.clicked.connect(self.show_info_dialog)
        lang_layout.addWidget(self.info_button)

        lang_layout.addStretch()
        lang_layout.addWidget(self.lang_button_eng)
        lang_layout.addWidget(self.lang_button_ru)

        layout = QVBoxLayout()
        layout.addLayout(lang_layout)
        layout.addWidget(self.info_button)
        layout.addWidget(self.space_label)
        layout.addWidget(self.grats_label)
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.space_label)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.space_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.space_label)


        self.setLayout(layout)

    def calculate_bmi(self):
        weight_text = self.weight_input.text()
        height_text = self.height_input.text()

        if not weight_text or not height_text:

            if self.language == 'ENG':
                QMessageBox.warning(self, 'Warning', 'Please enter weight and height.')
            elif self.language == 'RU':
                QMessageBox.warning(self, 'Внимание', 'Пожалуйста, введите свой вес и рост')
            return

        try:
            weight = float(weight_text)
            height = float(height_text)
        except ValueError:
            if self.language == 'ENG':
                QMessageBox.warning(self, 'Warning', 'Invalid input. Please enter numeric values.')
            elif self.language == 'RU':
                QMessageBox.warning(self, 'Внимание', 'Пожалуйста, введите числовые значения.')
            return

        if weight <= 0 or height <= 0:
            if self.language == 'ENG':
                QMessageBox.warning(self, 'Warning', 'Weight and height must be greater than 0.')
            elif self.language == 'RU':
                QMessageBox.warning(self, 'Внимание', 'Вес и рост должны быть больше 0 и длинной не более 5 символов.')
            return

        if not float(weight * 10).is_integer():
            if self.language == 'ENG':
                QMessageBox.warning(self, 'Warning', 'Enter your weight with an accuracy of 1 decimal place')
            elif self.language == 'RU':
                QMessageBox.warning(self, 'Внимание', 'Укажите вес с точностью до 1 знака после запятой')
            return

        height = round(height/ 100, 4)

        bmi = round(weight / (height ** 2), 2)
        result = f"{self.get_bmi_text()}: {bmi:.2f} - {self.get_category(bmi)}"
        self.result_label.setText(result)
        self.result_label.setFont(QtGui.QFont("Yu Gothic Ui", 10, QtGui.QFont.Bold))

    def get_category(self, bmi):
        if self.language == 'ENG':
            if bmi <= 16:
                return 'Severe Thinness'
            elif bmi <= 18.5:
                return 'Underweight'
            elif bmi <= 25:
                return 'Normal'
            elif bmi <= 30:
                return 'Overweight'
            elif bmi <= 35:
                return 'Obese Class I'
            elif bmi < 40:
                return 'Obese Class II'
            elif bmi >= 40:
                return 'Obese Class III'
        elif self.language == 'RU':
            if bmi <= 16:
                return 'Выраженный дефицит массы тела'
            elif bmi <= 18.5:
                return 'Недостаточная (дефицит) масса тела'
            elif bmi <= 25:
                return 'Норма'
            elif bmi <= 30:
                return 'Избыточная масса тела (предожирение)'
            elif bmi <= 35:
                return 'Ожирение 1 степени'
            elif bmi < 40:
                return 'Ожирение 2 степени'
            elif bmi >= 40:
                return 'Ожирение 3 степени'

    def get_bmi_text(self):
        if self.language == 'ENG':
            return 'Your BMI'
        elif self.language == 'RU':
            return 'Ваш ИМТ'

    def change_language(self, language):
        self.language = language
        if language == 'ENG':
            self.setWindowTitle('BMI Calculator')
            self.weight_label.setText('Weight (kg):')
            self.height_label.setText('Height (cm):')
            self.calculate_button.setText('Calculate BMI')
            self.grats_label.setText('Enter your weight and height:')
            self.info_button.setText('What is BMI?')
            self.lang_button_eng.setText('ENG')
            self.lang_button_ru.setText('RU')
        elif language == 'RU':
            self.setWindowTitle('Калькулятор ИМТ')
            self.weight_label.setText('Вес (кг):')
            self.height_label.setText('Рост (см):')
            self.calculate_button.setText('Рассчитать ИМТ')
            self.grats_label.setText('Введите ваш вес и рост:')
            self.info_button.setText('Что такое ИМТ?')
            self.lang_button_eng.setText('ENG')
            self.lang_button_ru.setText('RU')

        self.lang_button_eng.adjustSize()
        self.lang_button_ru.adjustSize()

    def show_info_dialog(self):
        if self.language == 'ENG':
            info_dialog = BMIInfoDialogEng(self)
            info_dialog.exec_()
        elif self.language == 'RU':
            info_dialog = BMIInfoDialogRus(self)
            info_dialog.exec_()
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    widget = BMIWidget()
    widget.show()
    sys.exit(app.exec_())
