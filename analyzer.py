from csv_handler import instance_csv

class perfil:
    def __init__(self):
        self.interessado = {}

class Capability:
    def __init__(self):
        self.data = instance_csv()
        self.vencedor = self.data.vencedor()
        self.dados = self.data.get_all()
        self.perfil = perfil()

    def mais_contado(self, dic):
        votos = []
        for i in dic:
            votos.append(dic[i]['count'])
        for i in dic:
            if dic[i]['count'] == max(votos):
                return i
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
        return self.get_from_respostas(5)

    def idade(self):
        return self.get_from_respostas(6)

    def escolaridade(self):
        return self.get_from_respostas(7)

    def interessado_eleicao(self):
        return self.get_from_respostas(8) 

    def opniao_governador(self):  
        return self.get_from_respostas(9)

    def meio_comunicação(self):       
        return self.get_from_respostas(9)

    def redes_sociais(self):
        return self.redes_sociais_respostas()

    def melhores_propostas(self):    
        return self.get_from_respostas(16)

    def qual_gov_votaria(self):    
        return self.get_from_respostas(17)

    def gestao_de_grosso(self):    
        return self.get_from_respostas(18) 
    
    def forma_administracao_grosso(self):       
        return self.get_from_respostas(19)

    def frase_representa(self):       
        return self.get_from_respostas(20) 

    def apoiadores_de_presidente_(self):      
        return self.get_from_respostas(21)

    def apoio_bolsonaro(self):     
        return self.get_from_respostas(22)
    
    def primeiro_turno(self):     
        return self.get_from_respostas(23)

    def repetir_voto_papai(self):   
        return self.get_from_respostas(24) 

    def repetir_voto_grosso(self):   
        return self.get_from_respostas(25)

    def apoio_de_senador_honesto(self):    
        return self.get_from_respostas(26)

class Persona:
    def __init__(self, candidato):
        self.c = Capability()
        self.sexo = self.c.mais_contado(self.c.sexo())
        self.idade = self.c.mais_contado(self.c.idade())
        self.escolaridade = self.c.mais_contado(self.c.escolaridade())
        self.interessado_eleicao = self.c.mais_contado(self.c.interessado_eleicao())
        self.opniao_governador = self.c.mais_contado(self.c.opniao_governador())
        self.meio_comunicação = self.c.mais_contado(self.c.meio_comunicação())
        self.redes_sociais = self.c.mais_contado(self.c.redes_sociais())
        self.melhores_propostas = self.c.mais_contado(self.c.melhores_propostas())
        self.qual_gov_votaria = self.c.mais_contado(self.c.qual_gov_votaria())
        self.gestao_de_grosso = self.c.mais_contado(self.c.gestao_de_grosso())
        self.forma_administracao_grosso = self.c.mais_contado(self.c.forma_administracao_grosso())
        self.frase_representa = self.c.mais_contado(self.c.frase_representa())
        self.apoiadores_de_presidente_ = self.c.mais_contado(self.c.apoiadores_de_presidente_())
        self.apoio_bolsonaro = self.c.mais_contado(self.c.apoio_bolsonaro())
        self.primeiro_turno = self.c.mais_contado(self.c.primeiro_turno())
        self.repetir_voto_papai = self.c.mais_contado(self.c.repetir_voto_papai())
        self.repetir_voto_grosso = self.c.mais_contado(self.c.repetir_voto_grosso())
        self.apoio_de_senador_honesto = self.c.mais_contado(self.c.apoio_de_senador_honesto())
