from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QSizePolicy, QHBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import FinPy as fp

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
        loan_button.clicked.connect(lambda: self.on_loan_button_clicked(loan_prin.text(), loan_int.text(), loan_pymnts.text(), loan_start.text()))

        loan_prin = QLineEdit()
        loan_prin.setPlaceholderText("Principal")
        loan_prin.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        loan_int = QLineEdit()
        loan_int.setPlaceholderText("Interest")
        loan_int.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        loan_pymnts = QLineEdit()
        loan_pymnts.setPlaceholderText("Number of Payments")
        loan_pymnts.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        loan_start = QLineEdit()
        loan_start.setPlaceholderText("Months until start")
        loan_start.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # create layout for loan info
        loan_container = QWidget()

        loan_info_layout = QGridLayout()
        loan_info_layout.setContentsMargins(0,0,0,0)
        loan_info_layout.setSpacing(5)
        loan_info_layout.addWidget(loan_prin, 0, 0)
        loan_info_layout.addWidget(loan_int, 0, 1)
        loan_info_layout.addWidget(loan_pymnts, 1, 0)
        loan_info_layout.addWidget(loan_start, 1, 1)

        loan_container.setLayout(loan_info_layout)
        self.grid.addWidget(loan_container, 1, 0)

        self.grid.setSpacing(5)
        self.grid.setVerticalSpacing(0)
        self.setCentralWidget(container)


    def on_loan_button_clicked(self, amount, interest, pymnts, start):
        if start == "":
            start = "0"
        if amount != "" and interest != "" and pymnts != "":
            if float(amount) > 0 and float(interest) > 0 and int(pymnts) > 0 and int(start) >= 0:
                try:
                    float(amount)
                    float(interest)
                    int(pymnts)
                    self.plot_window = PlotWidget(float(amount), float(interest), int(pymnts), int(start))
                    self.plot_window.show()
                except ValueError:
                    print("Error: At least one of the inputs was not a valid number")
            else:
                print("Error: At least one of the inputs was not a positive number")
        else:
            print("Error: At least one of the required inputs was left blank")


class PlotWidget(QMainWindow):
    def __init__(self, amount, interest, pymnts, start):
        super().__init__()

        self.amount = amount
        self.interest = (interest / 100) / 12
        self.payments = pymnts
        self.start = start

        # Layout
        container = QWidget()
        grid = QGridLayout()

        total_label = QLabel()
        self.mthly_pymnts = determine_mthly_pymnt(amount, (interest / 12) / 100, pymnts, start)
        total_label.setText(f"Each payment is ${self.mthly_pymnts} and there are {pymnts} payments \nfor a total of ${self.mthly_pymnts * pymnts}")
        grid.addWidget(total_label)

        # create a canvas and add it to the layout
        self.canvas = FigureCanvas(Figure(figsize=(5,3)))
        grid.addWidget(self.canvas)

        # set our layout to the plot widget
        container.setLayout(grid)
        self.setCentralWidget(container)

        self.plot()

    def plot(self):
        ax = self.canvas.figure.add_subplot(111)\

        curr_balance = self.amount
        balance_ot = [curr_balance]
        total_interest = 0
        for i in range(self.payments):
            interest = curr_balance * self.interest
            total_interest += interest

            curr_balance = curr_balance + interest - self.mthly_pymnts
            balance_ot.append(curr_balance)

        #ax.plot(balance_ot, [i for i in range(self.payments + 1)], marker="o")
        ax.plot([i for i in range(self.payments + 1)], balance_ot, marker="o")
        ax.set_title("Sample Plot")
        ax.set_xlabel("Months")
        ax.set_ylabel("Total Amount")


# uses the monthly payments formula to computer the amount needed to pay per month
# formula M = [Po * r * (1 + r)^n] / [(1 + r)^n - 1]
# if start is not zero the loan will accrue interest that is not being paid off yet
def determine_mthly_pymnt(principal, interest, num_payments, start):
    new_principal = principal * ((1 + interest) ** start)
    print(start, new_principal, principal)
    fvf = (1 + interest) ** num_payments
    numerator = new_principal * interest * fvf
    denominator = fvf - 1
    return round(numerator / denominator, 2)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()