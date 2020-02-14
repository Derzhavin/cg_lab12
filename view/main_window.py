import os.path as path
from PyQt5 import QtWidgets, uic, QtGui

path_to_main_window = './main_window.ui'

UIMainWindow, QtBaseClass = uic.loadUiType(path.join(path.dirname(__file__), path_to_main_window))


class MainWindow(QtWidgets.QMainWindow, UIMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UIMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./imgs/app_icon.png'))

        self.comboBoxPrimitives.currentIndexChanged.connect(self.set_primitive)
        self.comboBoxTransparencyTest.currentIndexChanged.connect(self.test_transparency)
        self.comboBoxMixTest_1.currentIndexChanged.connect(self.test_mix_1)
        self.comboBoxMixTest_2.currentIndexChanged.connect(self.test_mix_2)
        self.horizontalSliderClippingX.sliderReleased.connect(self.set_clipping_x)
        self.horizontalSliderClippingY.sliderReleased.connect(self.set_clipping_y)
        self.horizontalSliderClippingHeight.sliderReleased.connect(self.set_clipping_height)
        self.horizontalSliderClippingWidth.sliderReleased.connect(self.set_clipping_width)

    def set_primitive(self):
        print('set_primitive')
        pass

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