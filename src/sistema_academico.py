from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QDialog, QLineEdit, QMessageBox
from lancamento_notas import LancamentoNotas

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema Acadêmico")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Bem-vindo ao Sistema Acadêmico", self)
        layout.addWidget(self.label)

        self.btn_cadastrar_aluno = QPushButton("Cadastrar Aluno", self)
        layout.addWidget(self.btn_cadastrar_aluno)

        self.btn_cadastrar_disciplina = QPushButton("Cadastrar Disciplina", self)
        layout.addWidget(self.btn_cadastrar_disciplina)

        self.btn_lancar_notas = QPushButton("Lançar Notas", self)
        layout.addWidget(self.btn_lancar_notas)

        self.btn_calcular_media = QPushButton("Calcular Média", self)
        layout.addWidget(self.btn_calcular_media)

        self.setLayout(layout)

        # Ligando o botão "Lançar Notas" ao método que abre o diálogo de lançamento
        self.btn_lancar_notas.clicked.connect(self.abrir_lancamento_notas)

    def abrir_lancamento_notas(self):
        # Abre o diálogo para inserir os dados do lançamento de nota
        dialog = LancamentoNotasDialog(self)
        dialog.exec_()


# Diálogo específico para lançar notas, fazendo uso do módulo LancamentoNotas.
class LancamentoNotasDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Lançar Notas")
        self.setGeometry(150, 150, 300, 200)

        layout = QVBoxLayout()

        self.matricula_input = QLineEdit(self)
        self.matricula_input.setPlaceholderText("Matrícula do aluno")
        layout.addWidget(self.matricula_input)

        self.disciplina_input = QLineEdit(self)
        self.disciplina_input.setPlaceholderText("Disciplina")
        layout.addWidget(self.disciplina_input)

        self.nota_input = QLineEdit(self)
        self.nota_input.setPlaceholderText("Nota (0 a 10)")
        layout.addWidget(self.nota_input)

        self.btn_lancar = QPushButton("Lançar", self)
        self.btn_lancar.clicked.connect(self.lancar)
        layout.addWidget(self.btn_lancar)

        self.setLayout(layout)

        # Cria uma instância para gerenciar as notas
        self.sistema_notas = LancamentoNotas()

    def lancar(self):
        matricula = self.matricula_input.text()
        disciplina = self.disciplina_input.text()
        try:
            nota = float(self.nota_input.text())
        except ValueError:
            QMessageBox.warning(self, "Erro", "Nota inválida! Informe um número.")
            return

        # Chama o método do módulo LancamentoNotas para lançar a nota
        self.sistema_notas.lancar_nota(matricula, disciplina, nota)
        QMessageBox.information(self, "Sucesso", "Nota lançada com sucesso!")
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
