from datetime import datetime


class Sexo:
    def __init__(self, identificacao):
        self.identificacao = identificacao


class Paciente:
    def __init__(self, nome, idade, cpf, sexo: Sexo):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.sexo = sexo


class BancoDados:
    def __init__(self, id, paciente: Paciente, horario: datetime):
        self.id = id
        self.horario = horario
        self.paciente = paciente
