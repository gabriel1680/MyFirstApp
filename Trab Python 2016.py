import os
listadeprodutos={}
def menuhelp():
    help(menuinicio)
    help(menualterar)
    help(menuconsultar)
    help(categ)
    help(menuhelp)
def menuconsultar():
    print(""" 
     Digite (i) para ver todos os produtos
 
     Digite (a) para ver todos os alimentos
 
     Digite (r) para ver todas as roupas
 
     Digite (p) para pesquisar um produto específico
 
     Digite (v) para voltar
 
     """)
def menuinicio():
    print("""
     Digite (a) para alterar o estoque

     Digite (c) para consultar
 
     Digite (e) para ajuda

     Digite (s) para sair

    """)
def menualterar():
    print("""
     Digite (a) para adicionar
     
     Digite (e) para excluir
     
    """)  
def categ(cadastrocateg):
    if cadastrocateg =="a":
       listadeprodutos.fromkeys(["alimento"])
       categoria="alimento"
    elif cadastrocateg=="r":
        listadeprodutos.fromkeys(["roupa"])
        categoria="roupa"
    return (categoria)
def alimentoroupa():
    print("""
     Digite (a) para alimento
    
     Digite (r) para roupa
     
     Digite (v) para voltar
    """)
produtopreçoa={}
produtopreçor={}
k=0
contaadicionados=0
contaexcluidos=0
opção=""
while opção!= "s":
    menuinicio()    
    opção=input("""
     Escolha uma opção: """)
    os.system('cls' if os.name == 'nt' else 'clear')
    if opção =="a":
        menualterar()
        adicionaexclui=input("     Escolha uma opção: ")
        os.system('cls' if os.name == 'nt' else 'clear')  
        while adicionaexclui=="a":
            alimentoroupa()           
            cadastrocateg=input("     Escolha uma opção: ")
            os.system('cls' if os.name == 'nt' else 'clear')         
            contaadicionados+=1        
            cat=categ(cadastrocateg)               
            if cat=="alimento":
                print("")                 
                produtoa=input("     Escreva o nome do produto: ")
                print("") 
                print("     Caso o preço possua centavos, utilizar ponto ao invés de virgula.")
                print("") 
                preçoa=float(input("     Digite o preço: R$ "))
                os.system('cls' if os.name == 'nt' else 'clear')
                preçoal=str("%.2f" %preçoa) 
                a="R$"
                a+=preçoal
                produtopreçoa[produtoa]=a
                listadeprodutos["alimento"]=produtopreçoa
                print("")                 
                print("     Produto adicionado com sucesso!")
                print("")                 
                print("     No estoque:", listadeprodutos)             
            elif cat=="roupa":
                print("")                 
                produtor=input("     Escreva o nome do produto: ")
                print("")                 
                print("     Caso o preço possua centavos, utilizar ponto ao invés de virgula.")  
                print("")                 
                preçor=float(input("    Digite o preço: R$ "))
                os.system('cls' if os.name == 'nt' else 'clear')
                preçoro=str("%.2f" %preçor)
                r="R$"
                r+=preçoro 
                produtopreçor[produtor]=r
                listadeprodutos["roupa"]=produtopreçor
                print("")                
                print("     Produto adicionado com sucesso! ")
                print("")                
                print("     No estoque:", listadeprodutos)  
                print("") 
            print("") 
            continuar=input("     Pressione enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear') 
            print("")            
            print("     Para adicionar outros produtos, digite (a)")
            print("")
            print("     Para voltar digite (v)")
            print("")
            adicionaexclui=input("     Escolha uma opção: ")
            os.system('cls' if os.name == 'nt' else 'clear')            
            print("")
            print("     ", contaexcluidos, "produto(s) excluido(s)")
            print("")    
            print("     ", contaadicionados, "produto(s) adicionado(s)")    
            totalprodutos=contaadicionados - contaexcluidos    
            print("")    
            print("     ", totalprodutos, "produto(s) restante(s) no estoque")    
            print("")
            continuar=input("     Pressione enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')             
            continue
        while adicionaexclui=="e":
             print("")
             print("     No estoque:", listadeprodutos)        
             print("")        
             print("     Digite (a) para alimento")
             print("")
             print("     Digite (r) roupa")
             print("")         
             cadastrocateg=input("     Escolha uma opção: ")
             os.system('cls' if os.name == 'nt' else 'clear')        
             contaexcluidos+=1        
             if cadastrocateg=="a":       
                 print("")            
                 excluialimento=input("     Digite o nome do produto a ser excluido: ")
                 del produtopreçoa[excluialimento]
                 os.system('cls' if os.name == 'nt' else 'clear')              
                 print("")            
                 print("     Produto excluido com sucesso!")
                 print("")            
                 print("     No estoque:", listadeprodutos)
                 print("")
                 print("") 
             elif cadastrocateg=="r":
                print("")            
                excluiroupa=input("     Digite o nome do produto a ser excluido: ")
                del produtopreçor[excluiroupa]
                os.system('cls' if os.name == 'nt' else 'clear')             
                print("")            
                print("     Produto excluido com sucesso!")
                print("")            
                print("     No estoque:", listadeprodutos)
             print("")
             print("     Para excluir outros produtos, digite (e)")
             print("")
             print("     Para voltar digite (v)")
             print("")
             adicionaexclui=input("     Escolha uma opção:")
             os.system('cls' if os.name == 'nt' else 'clear')  
             print("")
             print("     ", contaexcluidos, "produto(s) excluido(s)")
             print("")    
             print("     ", contaadicionados, "produto(s) adicionado(s)")    
             totalprodutos=contaadicionados - contaexcluidos    
             print("")    
             print("     ", totalprodutos, "produto(s) restante(s) no estoque")    
             print("")
             continuar=input("     Pressione enter para continuar...")
             os.system('cls' if os.name == 'nt' else 'clear') 
             break
    while opção=="c":
        menuconsultar()
        consulta=input("     Escolha uma opção: ")        
        os.system('cls' if os.name == 'nt' else 'clear') 
        while consulta=="i":
            v=set(produtopreçor.keys())        
            w=set(produtopreçoa.keys())        
            x=len(produtopreçoa)
            y=len(produtopreçor)
            z=x+y
            print("")        
            print("     Lista dos produtos: ", listadeprodutos)        
            print("")        
            print("     Roupas:", v, "e Alimentos:", w )        
            print("")        
            print("    ", z, "produto(s) restante(s) no estoque")
            print("")        
            continuar=input("     Pressione enter para continuar...")        
            os.system('cls' if os.name == 'nt' else 'clear')            
            menuconsultar()            
            consulta=input("     Escolha uma opção:")            
            os.system('cls' if os.name == 'nt' else 'clear')        
            continue
        while consulta=="a":       
            print("")        
            print("    ", set(produtopreçoa.keys()))        
            print("")        
            print("    ", len(produtopreçoa), "alimento(s) no estoque")       
            print("")
            continuar=input("     Pressione enter para continuar...")        
            os.system('cls' if os.name == 'nt' else 'clear')        
            menuconsultar()            
            consulta=input("     Escolha uma opção:")          
            os.system('cls' if os.name == 'nt' else 'clear')              
            break
        while consulta=="r":   
            print("")        
            print("     ", set(produtopreçor.keys()))        
            print("")        
            print("     ", len(produtopreçor), "roupa(s) no estoque")
            print("")                
            consulta=input("     Pressione enter para continuar...")            
            os.system('cls' if os.name == 'nt' else 'clear')              
                        
            continue
        while consulta=="p":        
            print("")        
            print("     No estoque: ", listadeprodutos)        
            alimentoroupa()
            consultac=input("     Escolha uma opção: ")            
            k+=1        
            os.system('cls' if os.name == 'nt' else 'clear')        
            if consultac=="a":        
                print("")             
                consultaalimento=input("     Digite o nome do produto a ser pesquisado: ")
                os.system('cls' if os.name == 'nt' else 'clear')                
                if produtopreçoa.get(consultaalimento) == None :
                    print("")               
                    print("     Não temos esse produto no estoque")
                    print("")
                    continuar=input("     Pressione o enter para continuar")
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif produtopreçoa.get(consultaalimento) != None:
                    print("     ", consultaalimento, "custa: R$", produtopreçoa[consultaalimento], "reais")
                    print("")
                    continuar=input("     Pressione o enter para continuar")
                    os.system('cls' if os.name == 'nt' else 'clear')
            elif consultac =="r":
                print("")            
                consultaroupa=input("     Digite o nome do produto a ser pesquisado: ")
                if produtopreçor.get(consultaroupa)== None:
                    os.system('cls' if os.name == 'nt' else 'clear')                    
                    print("")
                    print("     Não temos esse produto no estoque")
                    print("")
                    print("")
                    continuar=input("     Pressione o enter para continuar...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif produtopreçor.get(consultaroupa)!=None:
                    print("")                    
                    print("     ", consultaroupa, "Custa", produtopreçor[consultaroupa] )
                    print("")
                    continuar=input("     Pressione o enter para continuar...")
                    os.system('cls' if os.name == 'nt' else 'clear')
            elif consultac!="a" and consultac!="r":        
                print("")
                consulta=input("     Pressione enter para continuar...")            
                os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if consulta=="v":
            print("")            
            opção=input("     Pressione enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        continue
    
    if opção=="e":
         menuhelp()
         os.system("pause")
         os.system("cls" if os.name == 'nt' else 'clear')
    elif opção=="s":
        print("")         
        print("     Obrigado por usar nosso programa!")
