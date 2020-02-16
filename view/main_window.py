from os import path
from PyQt5 import QtWidgets, uic, QtGui, QtCore

from model import Model

from .drawing import *

path_to_main_window = './main_window.ui'
path_to_icon = './imgs/app_icon.png'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.model = Model('GL_POINTS', 'GL_NEVER', 0, 'GL_ZERO', 'GL_ZERO', 0, 0, 200, 100)

        uic.loadUi(path.join(path.dirname(__file__), path_to_main_window), self)

        self.setWindowIcon(QtGui.QIcon(path_to_icon))

        init_gl_widget(self.gl_widget, self.model)

        self.comboBoxPrimitives.currentIndexChanged.connect(self.set_primitive)
        self.comboBoxTransparencyTest.currentIndexChanged.connect(self.test_transparency)
        self.horizontalSliderTransparencyTest.sliderReleased.connect(self.test_transparency_ref)
        self.comboBoxMixTest_1.currentIndexChanged.connect(self.test_mix_1)
        self.comboBoxMixTest_2.currentIndexChanged.connect(self.test_mix_2)
        self.horizontalSliderClippingX.sliderReleased.connect(self.set_clipping_x)
        self.horizontalSliderClippingY.sliderReleased.connect(self.set_clipping_y)
        self.horizontalSliderClippingHeight.sliderReleased.connect(self.set_clipping_height)
        self.horizontalSliderClippingWidth.sliderReleased.connect(self.set_clipping_width)

        self._init_combo_box(self.comboBoxPrimitives, self.model.primitive)
        self._init_combo_box(self.comboBoxTransparencyTest, self.model.func)
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
        self.model.func = self.comboBoxTransparencyTest.currentText()
        self.gl_widget.update()

    def test_transparency_ref(self):
        self.model.ref = int(self.horizontalSliderTransparencyTest.value())
        self.gl_widget.update()

    def test_mix_1(self):
        self.model.s_factor = self.comboBoxMixTest_1.currentText()
        self.gl_widget.update()

    def test_mix_2(self):
        self.model.d_factor = self.comboBoxMixTest_2.currentText()
        self.gl_widget.update()

    def set_clipping_x(self):
        self.model.clipping_x = int(self.horizontalSliderClippingX.value())
        self.gl_widget.update()

    def set_clipping_y(self):
        self.model.clipping_y = int(self.horizontalSliderClippingY.value())
        self.gl_widget.update()

    def set_clipping_width(self):
        self.model.clipping_width = int(self.horizontalSliderClippingWidth.value())
        self.gl_widget.update()

    def set_clipping_height(self):
        self.model.clipping_height = int(self.horizontalSliderClippingHeight.value())
        self.gl_widget.update()