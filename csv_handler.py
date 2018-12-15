import csv

class dic_class:
  def __init__(self, perguntas, respostas):
    self.perguntas = perguntas
    self.respostas = respostas

class instance_csv:
    def __init__(self):
        self.data = self.get_all()

    def read(self):
        arquivo = open('DESAFIO HACKATON DEZEMBRO 2018.csv', encoding='utf8')
        return csv.reader(arquivo, delimiter=';')

    def get_all(self):
        perguntas = []
        respostas = []
        count = 0
        linhas = self.read()
        for i in linhas:
            if count == 0:
                for y in i:
                    perguntas.append(y)
            else:
                respostas.append(i)
            count+=1
        return dic_class(perguntas,respostas)

    def get_all_candidates(self):
        candidates = set()
        data = self.data.respostas.copy()
        for i in data:
            if i[16] not in ('null-null','0004-NÃO SABE','0003-NENHUM DELES', '0005-NÃO RESPONDEU'):
                candidates.add(i[16])
        return candidates

def votes(respostas, candidatos):
    for candidato in candidatos:
        count=0
        for resposta in respostas:
            if resposta[16] == candidato:
                count += 1
        print('votos de %s: %d' %(candidato,count))

i = instance_csv()
dic = i.get_all()

print(i.get_all_candidates())
votes(dic.respostas,i.get_all_candidates())