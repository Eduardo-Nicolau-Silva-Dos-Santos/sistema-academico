class LancamentoNotas:
    """
    Classe para gerenciar o lançamento e manipulação das notas dos alunos.
    Cada aluno é identificado por sua matrícula e possui um dicionário
    com as disciplinas e as respectivas notas.
    """
    def __init__(self):
        # Dicionário para armazenar as notas.
        # Estrutura: { matricula: { disciplina: nota } }
        self.notas = {}

    def lancar_nota(self, matricula: str, disciplina: str, nota: float):
        """
        Lança uma nota para um aluno em uma determinada disciplina.
        """
        if not (0 <= nota <= 10):
            print("Nota inválida! A nota deve ser entre 0 e 10.")
            return

        if matricula not in self.notas:
            self.notas[matricula] = {}
        self.notas[matricula][disciplina] = nota
        print(f"Nota lançada: Aluno {matricula} - {disciplina}: {nota}")

    def atualizar_nota(self, matricula: str, disciplina: str, nota: float):
        """
        Atualiza a nota de um aluno em uma determinada disciplina.
        """
        if matricula in self.notas and disciplina in self.notas[matricula]:
            if not (0 <= nota <= 10):
                print("Nota inválida! A nota deve ser entre 0 e 10.")
                return
            self.notas[matricula][disciplina] = nota
            print(f"Nota atualizada: Aluno {matricula} - {disciplina}: {nota}")
        else:
            print("Registro de nota não encontrado. Utilize a função de lançamento para inserir a nota.")

    def remover_nota(self, matricula: str, disciplina: str):
        """
        Remove a nota de um aluno para uma disciplina específica.
        """
        if matricula in self.notas and disciplina in self.notas[matricula]:
            del self.notas[matricula][disciplina]
            print(f"Nota removida para o aluno {matricula} na disciplina {disciplina}.")
            # Se não houver mais notas para o aluno, opcionalmente remove o aluno do dicionário
            if not self.notas[matricula]:
                del self.notas[matricula]
        else:
            print("Registro de nota não encontrado.")

    def obter_nota(self, matricula: str, disciplina: str):
        """
        Retorna a nota de um aluno em uma disciplina ou None se não existir.
        """
        return self.notas.get(matricula, {}).get(disciplina)

    def listar_notas_aluno(self, matricula: str):
        """
        Lista todas as notas cadastradas para um determinado aluno.
        """
        return self.notas.get(matricula, {})

    def listar_todas_notas(self):
        """
        Retorna o dicionário completo de notas.
        """
        return self.notas

if __name__ == "__main__":
    # Exemplo de uso no modo CLI para teste do módulo
    sistema = LancamentoNotas()
    
    def menu():
        print("\n--- Sistema de Lançamento de Notas ---")
        print("1. Lançar Nota")
        print("2. Atualizar Nota")
        print("3. Remover Nota")
        print("4. Consultar Nota")
        print("5. Listar todas as notas de um aluno")
        print("6. Listar todos os registros")
        print("0. Sair")

    while True:
        menu()
        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            matricula = input("Digite a matrícula do aluno: ")
            disciplina = input("Digite a disciplina: ")
            try:
                nota = float(input("Digite a nota (0 a 10): "))
            except ValueError:
                print("Valor inválido para nota.")
                continue
            sistema.lancar_nota(matricula, disciplina, nota)

        elif opcao == '2':
            matricula = input("Digite a matrícula do aluno: ")
            disciplina = input("Digite a disciplina: ")
            try:
                nota = float(input("Digite a nova nota (0 a 10): "))
            except ValueError:
                print("Valor inválido para nota.")
                continue
            sistema.atualizar_nota(matricula, disciplina, nota)

        elif opcao == '3':
            matricula = input("Digite a matrícula do aluno: ")
            disciplina = input("Digite a disciplina a remover: ")
            sistema.remover_nota(matricula, disciplina)

        elif opcao == '4':
            matricula = input("Digite a matrícula do aluno: ")
            disciplina = input("Digite a disciplina: ")
            nota = sistema.obter_nota(matricula, disciplina)
            if nota is not None:
                print(f"Nota do aluno {matricula} na disciplina {disciplina}: {nota}")
            else:
                print("Nenhuma nota registrada para este aluno/disciplina.")

        elif opcao == '5':
            matricula = input("Digite a matrícula do aluno: ")
            notas = sistema.listar_notas_aluno(matricula)
            if notas:
                print(f"Notas do aluno {matricula}:")
                for disc, n in notas.items():
                    print(f"  {disc}: {n}")
            else:
                print("Nenhuma nota registrada para este aluno.")

        elif opcao == '6':
            registros = sistema.listar_todas_notas()
            if registros:
                print("Registros de notas:")
                for mat, notas_aluno in registros.items():
                    print(f"Aluno {mat}:")
                    for disc, n in notas_aluno.items():
                        print(f"  {disc}: {n}")
            else:
                print("Nenhuma nota registrada no sistema.")

        elif opcao == '0':
            print("Saindo do sistema de lançamento de notas.")
            break

        else:
            print("Opção inválida. Tente novamente.")