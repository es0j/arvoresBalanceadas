ROTACAO_A_DIREITA=0
ROTACAO_A_ESQUERDA=1
ROTACAO_DUPLA_DIREITA=2
ROTACAO_DUPLA_ESQUERDA=3

def rotSimplesDireita(noNaoAvl):
    avo=noNaoAvl.pai
    if avo.esquerdo==noNaoAvl:
        p=avo.esquerdo
    else:
        p=avo.direita

    u=p.esquerdo
    p.esquerdo = u.direito
    u.direito=p


def tipoRotacao(pontoNaoAvl):
    fDireito= pontoNaoAvl.direito
    fEsquerdo = pontoNaoAvl.esquerdo

    if fDireito.contarTamanho() < fEsquerdo.contarTamanho():
        #rotacao a direita
        if fEsquerdo.esquerdo.contarTamanho() >= fEsquerdo.direito.contarTamanho():
            #rotacao simples a direita
            print("rot simples direita")
            rotSimplesDireita(pontoNaoAvl)
            return ROTACAO_A_DIREITA
        else:
            print("rot dupla direita")
            return ROTACAO_DUPLA_DIREITA
    else:
        #rotacao a esquerda
        if fDireito.direito.contarTamanho() >= fDireito.esquerdo.contarTamanho():
            print("rot simples esquerda")
            return ROTACAO_A_ESQUERDA
        else:
            #filho interno eh maior, rodando dupla
            print("rot dupla esquerda")
            return ROTACAO_DUPLA_ESQUERDA

class no:
    def __init__(self,dado,pai=0,tipo=True,quantidade=1):
        self.tipo=tipo
        self.dado=dado
        self.pai=pai
        self.tamanho=0
        if quantidade==1:
            self.esquerdo=no(-1,self,False,0)
            self.direito=no(-1,self,False,0)
    def setarDireito(self,dado):
        self.direito=no(dado,self)
        return self.direito
    def setarEsquerdo(self,dado):
        self.esquerdo=no(dado,self)
        return self.esquerdo
    def contarTamanho(self):
        if self.tipo==False:
            return 0
        self.tamanho=max(self.esquerdo.contarTamanho(),self.direito.contarTamanho())+1
        return self.tamanho

    def isAvl(self):
        if self.esquerdo.tipo and self.direito.tipo:
            return int(abs(self.esquerdo.contarTamanho() - self.direito.contarTamanho())<=1)
        else:
            return int(True)
    def mostrarSubArvore(self,nivel,matriz,posicao,delta=0):
        #printMatriz(matriz)
        #print("\t"*inicializador,self.dado,self.contarTamanho())
        #print(len(matriz),len(matriz[0]),nivel,posicao,delta)
        matriz[nivel][posicao+delta]=str(self.dado)#+":"+str(self.contarTamanho())+":"+str(self.isAvl())
        posicao=posicao+delta 
        if self.esquerdo.tipo:
            self.esquerdo.mostrarSubArvore(nivel+1,matriz,posicao,-len(matriz[0])//2**(nivel+2))
        if self.direito.tipo:
            self.direito.mostrarSubArvore(nivel+1,matriz,posicao,len(matriz[0])//2**(nivel+2))
        return matriz

def printMatriz(m):
    for i in m:
        print ("".join(i))
    print("")

def criarMatriz(m,n):
    matriz=[]
    for i in range(m):
        matriz.append(["-"]*n)
    return matriz

s1= no(4)
s2=s1.setarDireito(2)
s3=s2.setarEsquerdo(1)
s4=s2.setarDireito (3)
s5=s1.setarEsquerdo (5)
s6=s3.setarDireito (1)


print(tipoRotacao(s1))

matriz=criarMatriz (40,40)
posicao=len(matriz[0])//2
printMatriz(s1.mostrarSubArvore(0,matriz,posicao))
