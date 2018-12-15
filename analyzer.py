from csv_handler import instance_csv
from senticnet_instance import Sentiment

class perfil:
    def __init__(self):
        self.interessado = {}

class Capability(object):
    def __init__(self, candidato):
        self.data = instance_csv()
        self.vencedor = candidato
        self.dados = self.data.get_all()
        self.perfil = perfil()

    def mais_contado(self, dic):
        votos = []
        for i in dic:
            votos.append(dic[i]['count'])
        for i in dic:
            if dic[i]['count'] == max(votos):
                return (i,max(votos))
            else:
                pass

    def get_from_respostas(self, indice):
        dic = {}
        respostas = set()
        for i in self.dados.respostas:
            respostas.add(i[indice])
        for i in respostas:
            dic[i] = {'count':0}
        
        for i in self.dados.respostas:
            if i[16] == self.vencedor:
                dic[i[indice]]['count'] += 1
        return dic

    def redes_sociais_respostas(self):
        dic = {}
        respostas = set()
        resp = []
        for i in self.dados.respostas:
            for y in range(10,16):
                respostas.add(i[y])
                h = (i[y],i[16])
                resp.append(h)
        for i in respostas:
            dic[i] = {'count':0}
        for i in resp:
            if i[1] == self.vencedor and i[0] != '':
                dic[i[0]]['count'] += 1
        return dic

    def sexo(self):
        return (self.mais_contado(self.get_from_respostas(5)),self.get_from_respostas(5))

    def idade(self):
        return (self.mais_contado(self.get_from_respostas(6)),self.get_from_respostas(6))

    def escolaridade(self):
        return (self.mais_contado(self.get_from_respostas(7)),self.get_from_respostas(7))

    def interessado_eleicao(self):
        return (self.mais_contado(self.get_from_respostas(8)),self.get_from_respostas(8))

    def opniao_governador(self):  
        return (self.mais_contado(self.get_from_respostas(9)),self.get_from_respostas(9))

    def meio_comunicação(self):       
        return (self.mais_contado(self.get_from_respostas(9)),self.get_from_respostas(9))

    def redes_sociais(self):
        return (self.mais_contado(self.redes_sociais_respostas()),self.redes_sociais_respostas())

    def melhores_propostas(self):    
        return (self.mais_contado(self.get_from_respostas(16)),self.get_from_respostas(16))

    def qual_gov_votaria(self):    
        return (self.mais_contado(self.get_from_respostas(17)),self.get_from_respostas(17))

    def gestao_de_grosso(self):    
        return (self.mais_contado(self.get_from_respostas(18)),self.get_from_respostas(18))
    
    def forma_administracao_grosso(self):       
        return (self.mais_contado(self.get_from_respostas(19)),self.get_from_respostas(19))

    def frase_representa(self):       
        return (self.mais_contado(self.get_from_respostas(20)),self.get_from_respostas(20))

    def apoiadores_de_presidente_(self):      
        return (self.mais_contado(self.get_from_respostas(21)),self.get_from_respostas(21))

    def apoio_bolsonaro(self):     
        return (self.mais_contado(self.get_from_respostas(22)),self.get_from_respostas(22))
    
    def primeiro_turno(self):     
        return (self.mais_contado(self.get_from_respostas(23)),self.get_from_respostas(23))

    def repetir_voto_papai(self):   
        return (self.mais_contado(self.get_from_respostas(24)),self.get_from_respostas(24)) 

    def repetir_voto_grosso(self):   
        return (self.mais_contado(self.get_from_respostas(25)),self.get_from_respostas(25))

    def apoio_de_senador_honesto(self):    
        return (self.mais_contado(self.get_from_respostas(26)),self.get_from_respostas(26))

def list_personas(p):
    return [p.sexo(),p.idade(),p.escolaridade(),p.interessado_eleicao(),p.opniao_governador(),
    p.meio_comunicação(), p.redes_sociais(), p.melhores_propostas(), p.qual_gov_votaria(), p.gestao_de_grosso(), p.forma_administracao_grosso(),
    p.frase_representa(), p.apoiadores_de_presidente_(), p.apoio_bolsonaro(), p.primeiro_turno(), p.repetir_voto_papai(), p.repetir_voto_grosso(),
    p.apoio_de_senador_honesto()]

def vencedor(candidato):
    sn = Sentiment()
    p = Capability(candidato)
    lista = list_personas(p)
    count = 0
    for i in lista:
        if sn.sentiment_avg(i[0][0]):
            count += i[0][1]
    return count

print(vencedor('0001-FILHO DE PAPAI (PSB)'))
