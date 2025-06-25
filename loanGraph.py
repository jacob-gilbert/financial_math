from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QSizePolicy, QHBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create container and layout
        container = QWidget()
        self.grid = QGridLayout(container)

        self.setWindowTitle("Loan Grapher")
        self.setGeometry(100, 100, 500, 300)
        
        # create label, button and text boxes to for loan information
        loan_label = QLabel()
        loan_label.setText("Input Loan Information Below:")
        loan_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.grid.addWidget(loan_label, 5, 0)

        loan_button = QPushButton()
        loan_button.setText("Create Graph")
        self.grid.addWidget(loan_button, 7, 0)

        loan_prin = QLineEdit()
        loan_prin.setPlaceholderText("Principal")
        loan_prin.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        loan_int = QLineEdit()
        loan_int.setPlaceholderText("Interest")
        loan_int.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        loan_time = QLineEdit()
        loan_time.setPlaceholderText("Time")
        loan_time.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # create layout for loan info
        loan_container = QWidget()

        loan_info_layout = QHBoxLayout()
        loan_info_layout.setContentsMargins(0,0,0,0)
        loan_info_layout.setSpacing(5)
        loan_info_layout.addWidget(loan_prin)
        loan_info_layout.addWidget(loan_int)
        loan_info_layout.addWidget(loan_time)

        loan_container.setLayout(loan_info_layout)
        self.grid.addWidget(loan_container, 6, 0)

        # create the graph
        self.graph = PlotWidget()
        self.grid.addWidget(self.graph, 0, 0, 5, 3)

        self.grid.setSpacing(5)
        self.grid.setVerticalSpacing(0)
        self.setCentralWidget(container)



class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Layout
        grid = QGridLayout()

        # create a canvas and add it to the layout
        self.canvas = FigureCanvas(Figure(figsize=(5,3)))
        grid.addWidget(self.canvas)

        # set our layout to the plot widget
        self.setLayout(grid)

        self.plot()

    def plot(self):
        ax = self.canvas.figure.add_subplot(111)
        ax.plot([0, 1, 2, 3], [10, 1, 20, 3], marker="o")
        ax.set_title("Sample Plot")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    window.show()
    app.exec()