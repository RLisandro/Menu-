class Tarefas(object):
    def __init__(self,nome,qut_ativ ):
        self.nome =nome    
        self.qut_ativ = 0
        def  __str__ (self):
            return f"{self.nome} "        
        def qut_Ativ(self):
            return self.qut_ativ
        def list_nomes(self):
            return self.lst_nomes
        def quat_Num(self):
            return self.qut_ativ
lst_cadastro = [ ]
lst_nome=[]
def cadastro_aluno(): 
    nome = input("..........Aluno digite seu nome : ").title()    
    cadastro2 = {"nome":nome }
    lst_nome.append(cadastro2) 
    qut_ativ = int(input("\n........Digite a quantidade de atividades executadas:  "))
    mat = input("\n........Digite a matéria referente a atividade:  ")
    cadastro1 = {"atividade":qut_ativ,"..........materia":mat}
    lst_cadastro.append(cadastro1)
    print("Os cadastros foram adicionados", lst_aluno)      
 
def relatorio_nome():
    print("." * 10, "Relatório dos Nomes que realizaram  as atividades", "." * 10)
    for cadastro2  in lst_nome:
            print(f"\t\n{cadastro2 ['nome']} ")            
while True: 
    print("""\t\t\tMenu\n
                    0- Finalizar o Programa
                    1- Cadastrar Alunos e Atividades
                    2- Relatório Nomes     \t\t    """)
    opcao = int(input("\n\t\tEscolha uma opção (0 - 2):  "))
    if opcao == 0:
        print("\n......................Você saiu do menu!")
        break
    elif opcao == 1: cadastro_aluno()    
    elif opcao == 2: relatorio_nome()
        
   '''Fazer outra classe e outro menu '''
 
    
