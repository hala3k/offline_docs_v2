from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QWidget, QHBoxLayout, QLabel, QTextEdit


class LabeledTextBoxAR(QLineEdit):
    def __init__(self, width=250, **kwargs):
        super().__init__()
        self.setMaximumWidth(width)
        self.setFixedHeight(33)
        self.setStyleSheet("border-radius: 10px; padding: 7px;")
        if "text" in kwargs:
            if type(kwargs['text']) == int:
                txt = str(kwargs['text'])
            else:
                txt = kwargs['text']
            self.setText(txt)

    def setMaximumWidth(self, p_int):
        self.setFixedWidth(p_int)


class LabeledTextArea(QWidget):
    text_value = ""

    def __init__(self, label, **kwargs):
        super().__init__()
        self.the_line = QHBoxLayout()
        if 'space' in kwargs:
            self.the_line.setSpacing(kwargs['space'])
        else:
            self.the_line.setSpacing(0)
        self.text_input = QTextEdit()
        # self.text_input.textChanged[str].connect(self.update_value)
        if ('place_holder' in kwargs and 'text' not in kwargs) or ('place_holder' in kwargs and 'text' in kwargs and kwargs['text'].strip() == 0):
            self.text_input.setPlaceholderText(kwargs['place_holder'])
        elif 'text' in kwargs and kwargs['text'].strip() > 0:
            self.text_input.setText(kwargs['text'])
            LabeledTextArea.text_value = kwargs['text']
        self.text_input.setStyleSheet("border-radius: 10px; padding: 7px; background-color: #fff")
        label = QLabel(label)
        if 'height' in kwargs:
            self.text_input.setFixedHeight(kwargs['height'])
            label.setFixedHeight(kwargs['height'])
        label.setAlignment(Qt.AlignTop)
        self.the_line.addWidget(label)
        self.the_line.addWidget(self.text_input)
        self.the_line.setAlignment(Qt.AlignTop)
        self.setLayout(self.the_line)

        if 'width' in kwargs:
            self.setFixedWidth(kwargs['width'])

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pass
        else:
            super().mousePressEvent(event)

    def setMaximumWidth(self, p_int):
        self.setFixedWidth(p_int)

    def setText(self, txt):
        self.text_input.setText(txt)
        LabeledTextArea.text_value = txt

    @staticmethod
    def text():
        return LabeledTextArea.text_value

    @staticmethod
    def toPlainText():
        return LabeledTextArea.text_value

    def update_value(self, txt):
        LabeledTextArea.text_value = txt