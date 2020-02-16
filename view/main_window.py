from os import path
from PyQt5 import QtWidgets, uic, QtGui, QtCore

from model import Model

from .drawing import *

path_to_main_window = './main_window.ui'
path_to_icon = './imgs/app_icon.png'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.model = Model('GL_POINTS', 'GL_NEVER', 'GL_ZERO', 'GL_ZERO', 0, 0, 20, 20)

        uic.loadUi(path.join(path.dirname(__file__), path_to_main_window), self)

        self.setWindowIcon(QtGui.QIcon(path_to_icon))

        init_gl_widget(self.gl_widget, self.model)

        self.comboBoxPrimitives.currentIndexChanged.connect(self.set_primitive)
        self.comboBoxTransparencyTest.currentIndexChanged.connect(self.test_transparency)
        self.comboBoxMixTest_1.currentIndexChanged.connect(self.test_mix_1)
        self.comboBoxMixTest_2.currentIndexChanged.connect(self.test_mix_2)
        self.horizontalSliderClippingX.sliderReleased.connect(self.set_clipping_x)
        self.horizontalSliderClippingY.sliderReleased.connect(self.set_clipping_y)
        self.horizontalSliderClippingHeight.sliderReleased.connect(self.set_clipping_height)
        self.horizontalSliderClippingWidth.sliderReleased.connect(self.set_clipping_width)

        self._init_combo_box(self.comboBoxPrimitives, self.model.primitive)
        self._init_combo_box(self.comboBoxTransparencyTest, self.model.transparency)
        self._init_combo_box(self.comboBoxMixTest_1, self.model.s_factor)
        self._init_combo_box(self.comboBoxMixTest_2, self.model.d_factor)

    @staticmethod
    def _init_combo_box(combo, text):
        index = combo.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)

    def set_primitive(self):
        self.model.primitive = self.comboBoxPrimitives.currentText()
        self.gl_widget.update()

    def test_transparency(self):
        print('test_transparency')
        pass

    def test_mix_1(self):
        print('test_mix_1')
        pass

    def test_mix_2(self):
        print('test_mix_2')
        pass

    def set_clipping_x(self):
        print('set_clipping_x')
        pass

    def set_clipping_y(self):
        print('set_clipping_y')
        pass

    def set_clipping_width(self):
        print('set_clipping_width')
        pass

    def set_clipping_height(self):
        print('set_clipping_height')
        pass