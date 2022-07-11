from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        # plot data: x, y values
        #color = self.palette().color(QtGui.QPalette.Window)  # Get the default window background,
        #self.graphWidget.setBackground(color)                # and make it the background color for the graph
        self.graphWidget.setBackground('w') # Background color
        self.graphWidget.setTitle("Thermocouple", color="k", size="10pt") # Graph title
        styles = {'color':'k', 'font-size':'17px'} # Labels
        self.graphWidget.setLabel('left', 'Temperature [°C]', **styles)
        self.graphWidget.setLabel('bottom', 'Hour [H]', **styles) 
        self.graphWidget.showGrid(x=True, y=True) # Grid
        self.graphWidget.addLegend() # Legend. Name must be provided in .plot() in order for legend to work
        pen = pg.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.SolidLine) # Line style
        self.data_line = self.graphWidget.plot(self.x, self.y, name = "Sensor 1", pen=pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append( randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()