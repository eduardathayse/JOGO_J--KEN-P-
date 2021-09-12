# DESAFIO

# Permite fazer com que o script "espere" um pouco  
import time

# Permite limpar a tela 
import os 


class JOGO_PPT:
    ''' Classe do jogo pedra, papel e tesoura'''

    def __init__(self):
        '''Função inicial (iniciando variáveis)'''
        self.pedra = 1
        self.papel = 2
        self.tesoura = 3
    
    #def pedra(self):
        #self.pedra = 1
        
    #def papel(self):
        #self.papel = 2
    
    #def tesora(self):
        #self.tesora = 3
        
    def cabecalho(self):
        ''' Função para imprimir o cabeçalho do jogo'''
        print('_=_=_=_=_=_=_=_=_= JOGO ✊✋🖖 _=_=_=_=_=_=_=_=_=')
    
    def comparar(self, op1, op2):
        '''
        Função para comparar todas as condições possíveis
        para saber quem ganhou!
        '''
        if (op1 == self.pedra and op2 == self.tesoura):
            #print('pedra ganhou')
            print('JOGADOR 1 GANHOU!!')
        elif (op1 == self.pedra and op2 == self.papel):
            #print('papel ganhou')
            print('JOGADOR 2 GANHOU!!')
        elif (op1 == self.papel and op2 == self.tesoura):
            #print('tesoura ganhou')
            print('JOGADOR 2 GANHOU!!')
        elif (op1 == self.papel and op2 == self.pedra):
            #print('papel ganhou')
            print('JOGADOR 1 GANHOU!!')
        elif (op1 == self.tesoura and op2 == self.papel):
            #print('tesoura ganhou')
            print('JOGADOR 1 GANHOU!!')
        elif (op1 == self.tesoura and op2 == self.pedra):
            #print('pedra ganhou')
            print('JOGADOR 2 GANHOU!!')
        else:
            print('EMPATE!!!')
        
class Jogador1:
    '''Classe do jogador 1 '''
    def __init__(self):
        '''Função inicial (iniciando variáveis)'''
        self.opcao = ''
        
    def jogar(self):
        '''Função que permite o jogador 1 jogar'''
        op = int(input('1 - PEDRA\n2 - PAPEL\n3 - TESORA\nEscolha: '))
        return op
        
class Jogador2:
    '''Classe do jogador 2 '''
    def __init__(self):
        '''Função inicial (iniciando variáveis)'''
        self.opcao = ''
        
    def jogar(self):
        '''Função que permite o jogador 2 jogar'''
        op = int(input('1 - PEDRA\n2 - PAPEL\n3 - TESORA\nEscolha: '))
        return op
        

# ================= SCRIPT DO JOGO =================

jogo = JOGO_PPT()
jogador1 = Jogador1()
jogador2 = Jogador2()

print('\x1b[2J') # Comando para limpar a tela | se não funcionar usar o os.system('cls)
jogo.cabecalho()
op1 = jogador1.jogar()
print('\x1b[2J')
jogo.cabecalho()
op2 = jogador2.jogar() 
print('\x1b[2J')
jogo.cabecalho()
print('Carregando...')
time.sleep(4)
print('\x1b[2J')
jogo.cabecalho()
jogo.comparar(op1, op2)
#print('┈┈┈┈┈┈┈╱▔╲┈┈┈┈┈┈\n┈┈┈┈┈┈▕╲╲╲▏┈┈┈┈┈\n┈┈╱▔╲┈┈╲▂╱┈┈┈┈┈┈\n┈▕╲╲▕╱▔╱╲╱╲┈┈┈┈┈\n┈┈╲▂╱▏╲╲▕▋▋╱▔▇┈┈\n┈┈┈┈▕╲╱▔┈┈┈┈▁╱┈┈\n┈┈┈┈┈╲▏┈◥▇▇◤┈┈┈┈\n┈┈┈┈┈┈╲▂▂▂╱┈┈┈┈┈')
print('\n\n\n░░░░░░░░░░░░░░░░░░░░░░█████████\n░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███\n░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███\n░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███\n░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██\n░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██\n░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██\n██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█\n░░████████████░░░█████████████████')








