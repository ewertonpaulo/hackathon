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
        10-15
        pass

    def gestao_de_grosso(self):    
        return self.get_from_respostas(18) 
    
    def forma_administracao_grosso(self):       
        return self.get_from_respostas(19)

    def frase_representa(self):       
        return self.get_from_respostas(20) 

    def apoiadores_de_presidente_(self):      
        return self.get_from_respostas(21)

    def apoiadores_de_haddad(self):
        pass

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

# d = Capability()
# print(d.interessado_eleicao())
# print(d.opniao_governador())
# print(d.gestao_de_grosso())
# print(d.forma_administracao_grosso())
# print(d.frase_representa())
# print(d.apoiadores_de_presidente_())
# print(d.apoio_de_senador_honesto())
# print(d.sexo())
# print(d.primeiro_turno())
    

    