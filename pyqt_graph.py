
# https://www.learnpyqt.com/courses/graphics-plotting/plotting-pyqtgraph/

from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature_1 = [30,32,34,32,33,31,29,32,35,45]
        temperature_2 = [50,35,44,22,38,32,27,38,32,44]

        # color examples
        self.graphWidget.setBackground('w')
        # self.graphWidget.setBackground('#bbccaa')         # hex
        # self.graphWidget.setBackground((100,50,255))      # RGB each 0-255
        # self.graphWidget.setBackground((100,50,255,25))   # RGBA (A = alpha opacity)

        # # from PyQt5 import QtGui  # Place this at the top of your file.
        # self.graphWidget.setBackground(QtGui.QColor(100,50,254,25))

        # color = self.palette().color(QtGui.QPalette.Window)  # Get the default window background,
        # self.graphWidget.setBackground(color)

        # line colors
        pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.DashLine)

        self.graphWidget.setTitle("this is the title", color="b", size="30pt")

        # axis styles
        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('left', 'Temperature (C)', **styles)
        self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)

        # show grids
        self.graphWidget.showGrid(x=True, y=True )

        #Set Range
        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)

        self.graphWidget.addLegend()
        
        self.plot(hour, temperature_1, "Sensor1", 'r')
        self.plot(hour, temperature_2, "Sensor2", 'b')

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        # plot data: x, y values
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))



def main():
    app = QtWidgets.QApplication(sys.argv) 
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()