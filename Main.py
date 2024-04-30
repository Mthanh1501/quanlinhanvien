from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from GUI import MenuGUI


def initComponents(window: QMainWindow):

    # Set the panel as the central widget of the main window
    window.setCentralWidget(MenuGUI.initComponents())


def main():
    # Khởi tạo ứng dụng
    app = QApplication([])

    # Tạo cửa sổ chính
    window = QMainWindow()
    
    # Đặt kích thước
    window.resize(1080, 720)
    window.setMaximumSize(1080,720)
    # Thiết lập tiêu đề, icon cho cửa sổ
    window.setWindowTitle("My App")
    window.setWindowIcon(QIcon('Icons/LeagueOfLegends.ico'))

    # Set background color using stylesheets
    window.setStyleSheet("background-color: #FFFFFF;")
    

    initComponents(window)

    # Hiển thị cửa sổ
    window.show()
 
    # Bắt đầu vòng lặp sự kiện
    app.exec()


if __name__ == "__main__":
    main()

def parityCheck(n: int):
    if n % 2 == 0: return True
    return False

def zeroCheck(n: int):
    if n == 0: return True
    return False