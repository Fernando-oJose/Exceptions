from abc import ABC, abstractmethod


class verificaTitulacao(Exception):
    pass

class idadeProf(Exception):
    pass

class verificaCurso(Exception):
    pass

class idadeAluno(Exception):
    pass

class verificaCPF(Exception):
    pass

class Pessoa:
    def __init__(self, nome, idade, endereco, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco
        self.__cpf = cpf

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade

    def getEndereco(self):
        return self.__endereco
    
    def getCPF(self):
        return self.__cpf

    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, titulacao):
        super().__init__(nome, idade, endereco, cpf)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('Nome: {} Idade: {} Endereço: {} Cpf: {} Titulação: {}'.format(nome, idade, endereco, cpf, titulacao))

class Aluno(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, curso):
        super().__init__(nome, idade, endereco, cpf)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('Nome: {} Idade: {} Endereço: {} Cpf: {} Curso: {}'.format(nome, idade, endereco, cpf, curso))

if __name__ == "__main__":

    listaAlunos = [
        ('Giovana', 20, 'Rua Dom Pedro', 1234, 'CCO'),
        ('Hugo', 16, 'Rua Olavo Gomes', 4321, 'SIN'),
        ('Mauricio', 26, 'Rua Major Pinheiros', 5678, 'ADM'),
        ('Gerson', 8, 'Rua Jaime Oliveira', 8765, 'ECO'),
        ('Vitor', 24, 'Rua Comendador', 5050, 'CCO')
    ]
    listaProfs = [
        ('Alex', 34, 'Rua Ribeiro', 1010, 'Doutor'),
        ('Jorge', 22, 'Rua Batista', 2020, 'Doutor'),
        ('Alessandro', 46, 'Rua Coronel Almeida', 3030, 'Mestre'),
        ('Marcos', 28, 'Rua Barão', 4040, 'Mestre'),
        ('Ana', 33, 'Rua Dutra', 5050, 'Doutor')
    ]

    cadastro = {}

    for nome, idade, endereco, cpf, curso in listaAlunos:
        try:
            if idade < 18:
                raise idadeAluno()
            
            if curso != "CCO" and curso != "SIN":
                raise verificaCurso()

            if cpf in cadastro:
                raise verificaCPF()

        except idadeAluno:
            print('Idade do aluno é menor que 18')
            print()
        
        except verificaCurso:
            print("O curso '%s' é inválido" % curso)
            print()
        
        except verificaCPF:
            print("O Cpf '%d' já está cadastrado" % cpf)
            print()
        
        else:
           aluno_aux = Aluno(nome, idade, endereco, cpf, curso)
           cadastro[cpf] = aluno_aux
           aluno_aux.printDescricao()
           print()

    for nome, idade, endereco, cpf, titulacao in listaProfs:
        try:
            if titulacao != "Doutor":
                raise verificaTitulacao()

            if idade < 30:
                raise idadeProf()

            if cpf in cadastro:
                raise verificaCPF()
        
        except verificaTitulacao:
            print("Titulação '%s' não permitida" % titulacao)
            print()
        
        except idadeProf:
            print("Idade '%d' menor do que a permitida" % idade)
            print()
        
        except verificaCPF:
            print("O Cpf '%d' já está cadastrado" % cpf)
            print()

        else:
            prof_aux = Professor(nome, idade, endereco, cpf, titulacao)
            cadastro[cpf] = prof_aux
            prof_aux.printDescricao()
            print()
    
 
    
        

