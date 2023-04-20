from Model import *


class DaoSexo:
    sexos = None

    @classmethod
    def salvar(cls, sexo: Sexo):
        with open('sexos.txt', 'a') as arq:
            arq.writelines(sexo.identificacao)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('sexos.txt', 'r') as arq:
            cls.sexos = arq.readlines()
        print(cls.sexos)

        cls.sexos = list(map(lambda x: x.replace('\n', ''), cls.sexos))
        sex = []
        for i in cls.sexos:
            sex.append(Sexo(i))

        return sex


class DaoPessoa:
    pessoa = None

    @classmethod
    def salvar(cls, humano: Paciente):
        with open('pessoas.txt', 'a') as arq:
            arq.writelines(
                humano.nome + "|" +
                humano.sexo.identificacao + "|" +
                str(humano.cpf) + "|" +
                str(humano.idade)
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('pessoas.txt', 'r') as arq:
            cls.pessoa = arq.readlines()
        cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa))
        cls.pessoa = list(map(lambda x: x.split('|'), cls.pessoa))

        pessoas = []
        for i in cls.pessoa:
            pessoas.append(Paciente(i[0], i[3], i[2], Sexo(i[1])))

        return pessoas


class DaoFicha:
    ficha = None

    @classmethod
    def salvar(cls, paciente: BancoDados):
        with open('banco_dados.txt', 'a') as arq:
            arq.writelines(
                paciente.paciente.nome + "|" +
                paciente.paciente.sexo.identificacao + "|" +
                str(paciente.paciente.cpf) + "|" +
                str(paciente.paciente.idade) + "|" +
                str(paciente.id) + "|" +
                str(paciente.horario)
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('banco_dados.txt', 'r') as arq:
            cls.ficha = arq.readlines()
        cls.ficha = list(map(lambda x: x.replace('\n', ''), cls.ficha))
        cls.ficha = list(map(lambda x: x.split('|'), cls.ficha))


        banco_dados = []
        for i in cls.ficha:
            banco_dados.append(BancoDados(i[4], Paciente(i[0], i[3], i[2], Sexo(i[1])), i[5]))
        return banco_dados

joao = Paciente('Joao', 76, '211.345.675-11', Sexo('Feminino'))
print(DaoFicha.ler())
