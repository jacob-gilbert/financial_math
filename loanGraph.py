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
        self.grid.addWidget(loan_label, 0, 0)

        loan_button = QPushButton()
        loan_button.setText("Create Graph")
        self.grid.addWidget(loan_button, 2, 0)

        # connect button to function
        loan_button.clicked.connect(lambda: self.on_loan_button_clicked(loan_prin.text(), loan_int.text(), loan_time.text()))

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
        self.grid.addWidget(loan_container, 1, 0)

        self.grid.setSpacing(5)
        self.grid.setVerticalSpacing(0)
        self.setCentralWidget(container)


    def on_loan_button_clicked(self, amount, interest, time):
        self.plot_window = PlotWidget(amount, interest, time)
        self.plot_window.show()


class PlotWidget(QMainWindow):
    def __init__(self, amount, interest, time):
        super().__init__()

        # Layout
        container = QWidget()
        grid = QGridLayout()

        """temp_label = QLabel()
        temp_label.setText(f"Amount: {amount}, Interest: {interest}, Time {time}")
        grid.addWidget(temp_label)"""

        # create a canvas and add it to the layout
        self.canvas = FigureCanvas(Figure(figsize=(5,3)))
        grid.addWidget(self.canvas)

        # set our layout to the plot widget
        container.setLayout(grid)
        self.setCentralWidget(container)

        self.plot()

    def plot(self):
        ax = self.canvas.figure.add_subplot(111)
        ax.plot([0, 1, 2, 3], [10, 1, 20, 3], marker="o")
        ax.set_title("Sample Plot")
        ax.set_xlabel("Years")
        ax.set_ylabel("Total Amount")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    window.show()
    app.exec()