import os.path as path
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import OpenGL.GL as gl

from model import *
from drawing import *

path_to_main_window = './main_window.ui'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi(path.join(path.dirname(__file__), path_to_main_window), self)

        self.setWindowIcon(QtGui.QIcon('./imgs/app_icon.png'))

        init_gl(self.gl_widget)

        self.comboBoxPrimitives.currentIndexChanged.connect(self.set_primitive)
        self.comboBoxTransparencyTest.currentIndexChanged.connect(self.test_transparency)
        self.comboBoxMixTest_1.currentIndexChanged.connect(self.test_mix_1)
        self.comboBoxMixTest_2.currentIndexChanged.connect(self.test_mix_2)
        self.horizontalSliderClippingX.sliderReleased.connect(self.set_clipping_x)
        self.horizontalSliderClippingY.sliderReleased.connect(self.set_clipping_y)
        self.horizontalSliderClippingHeight.sliderReleased.connect(self.set_clipping_height)
        self.horizontalSliderClippingWidth.sliderReleased.connect(self.set_clipping_width)

        self._init_comboBox(self.comboBoxPrimitives, gl.GL_LINES.__repr__())
        self._init_comboBox(self.comboBoxTransparencyTest, gl.GL_LESS.__repr__())
        self._init_comboBox(self.comboBoxMixTest_1, gl.GL_ONE.__repr__())
        self._init_comboBox(self.comboBoxMixTest_2, gl.GL_ONE.__repr__())

        self.model = Model(gl.GL_POINT, gl.GL_NEVER, gl.GL_ZERO, gl.GL_ZERO, 0, 0, 20, 20)

    def _init_comboBox(self, combo, text):
        index = combo.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)

    def set_primitive(self):
        text = self.comboBoxPrimitives.currentText()
        
        if text == 'GL_POINTS':
            model.primitive = gl.GL_POINTS
            points()
            return
        
        if text == 'GL_LINES':
            model.primitive = gl.GL_LINES
            lines()
            return
        
        if text == 'GL_LINE_STRIP':
            model.primitive = gl.GL_LINE_STRIP
            line_strip()
            return
        
        if text == 'GL_LINE_LOOP':
            model.primitive = gl.GL_LINE_LOOP
            line_loop()
            return
        
        if text == 'GL_TRIANGLES':
            model.primitive = gl.GL_TRIANGLES
            triangles()
            return
        
        if text == 'GL_TRIANGLE_STRIP':
            model.primitive = gl.GL_TRIANGLE_STRIP
            triangle_strip()
            return
        
        if text == 'GL_TRIANGLE_FAN':
            model.primitive = gl.GL_TRIANGLE_FAN
            triangle_fan()
            return
        
        if text == 'GL_QUADS':
            model.primitive = gl.GL_QUADS
            quads()
            return
        
        if text == 'GL_QUAD_STRIP':
            model.primitive = gl.GL_QUAD_STRIP
            quad_strip()
            return

        if text == 'GL_POLYGON':
            model.primitive = gl.GL_POLYGON
            polygon()
            return

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