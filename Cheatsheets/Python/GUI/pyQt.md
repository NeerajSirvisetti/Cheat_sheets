### **PyQt Cheat Sheet:**

**1. Import PyQt Modules:**
```python
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
```

---

**2. Create an Application and Main Window:**
```python
app = QApplication([])
window = QWidget()
window.setWindowTitle("My PyQt App")
```

---

**3. Layout Management:**
```python
layout = QVBoxLayout()
window.setLayout(layout)
```

---

**4. Widgets:**
```python
label = QLabel("Hello, PyQt!")
button = QPushButton("Click Me")
```

---

**5. Adding Widgets to Layout:**
```python
layout.addWidget(label)
layout.addWidget(button)
```

---

**6. Signals and Slots (Event Handling):**
```python
def button_clicked():
    label.setText("Button Clicked!")

button.clicked.connect(button_clicked)
```

---

**7. Styling and Theming:**
```python
app.setStyle("Fusion")
```

---

**8. Icons:**
```python
window.setWindowIcon(QIcon("icon.png"))
```

---

**9. Dialogs:**
```python
from PyQt5.QtWidgets import QMessageBox, QFileDialog

QMessageBox.information(window, "Information", "This is an information message.")
file_path, _ = QFileDialog.getOpenFileName(window, "Open File", ".", "Text Files (*.txt)")
```

---

**10. Menus and Actions:**
```python
from PyQt5.QtWidgets import QMenu, QAction

menu = QMenu("File")
action_open = QAction("Open")
menu.addAction(action_open)
```

---

**11. Toolbars:**
```python
from PyQt5.QtWidgets import QToolBar

toolbar = QToolBar("My Toolbar")
window.addToolBar(toolbar)
toolbar.addAction(action_open)
```

---

**12. Status Bar:**
```python
status_bar = window.statusBar()
status_bar.showMessage("Ready.")
```

---

**13. Grid Layout:**
```python
from PyQt5.QtWidgets import QGridLayout

grid_layout = QGridLayout()
window.setLayout(grid_layout)
```

---

**14. Tab Widget:**
```python
from PyQt5.QtWidgets import QTabWidget, QWidget

tab_widget = QTabWidget()
tab1 = QWidget()
tab2 = QWidget()
tab_widget.addTab(tab1, "Tab 1")
tab_widget.addTab(tab2, "Tab 2")
```

---

**15. File Handling:**
```python
with open("file.txt", "r") as file:
    content = file.read()
```

---

**16. Database Interaction:**
```python
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("my_database.db")
db.open()
query = QSqlQuery()
query.exec_("SELECT * FROM my_table")
```

---

**17. Custom Widgets and Graphics View:**
```python
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

scene = QGraphicsScene()
view = QGraphicsView(scene)
```

---

**18. Threading:**
```python
from PyQt5.QtCore import QThread, pyqtSignal

class MyThread(QThread):
    thread_signal = pyqtSignal(str)

    def run(self):
        # Your threaded code here
        self.thread_signal.emit("Thread finished.")
```

---

**19. Internationalization (i18n):**
```python
from PyQt5.QtCore import QTranslator, QLocale

translator = QTranslator()
translator.load("my_translation_file")
app.installTranslator(translator)
```

---

**20. Deploying PyQt Applications:**
```bash
pyinstaller --onefile my_app.py
```

---

For more in-depth understanding, consider referring to the official [PyQt documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/).
 