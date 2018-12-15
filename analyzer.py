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

    def interessado_eleicao(self):
        dic = self.get_from_respostas(8) 
        # return dic
        return self.mais_contado(dic)



    def opniao_governador(self):
        dic = self.get_from_respostas(9)       
        return self.mais_contado(dic)

    def meio_comunicação(self):
        dic = self.get_from_respostas(9)       
        return self.mais_contado(dic)

    def redes_sociais(self):
        pass

    def gestao_de_grosso(self):
        dic = self.get_from_respostas(18)       
        return self.mais_contado(dic)
    
    def forma_administracao_grosso(self):
        dic = self.get_from_respostas(19)       
        return self.mais_contado(dic)

    def frase_representa(self):
        dic = self.get_from_respostas(20)       
        return self.mais_contado(dic)

    def apoiadores_de_presidente_(self):
        dic = self.get_from_respostas(21)       
        return self.mais_contado(dic)

    def apoiadores_de_haddad(self):
        pass

    def apoio_bolsonaro(self):
        dic = self.get_from_respostas(22)       
        return self.mais_contado(dic)

    def repetir_voto(self):
        pass

    def apoio_de_senador_honesto(self):
        dic = self.get_from_respostas(26)       
        return self.mais_contado(dic)
    
d = Capability()
print(d.interessado_eleicao())
print(d.opniao_governador())
print(d.gestao_de_grosso())
print(d.forma_administracao_grosso())
print(d.frase_representa())
print(d.apoiadores_de_presidente_())
print(d.apoio_de_senador_honesto())
    

    