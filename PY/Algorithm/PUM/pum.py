'''
[ok] gerar numeros sequencias
    [ok] percorrer n vezes sendo n a quantidade de linhas de output
        [ok] a cada loop, será gerado 4 numeros sendo o quarto substituido pela palavra "PUM"
            [ok] vetor de contadores que incrementa +4 em todos os valores
            ou
            [ok] novo loop de 4 voltas para criar uma lista com os numeros sequecias
            
'''

'''
    SOLUTION #01
'''
def solution1():   

    N = int(input())

    cont = 0
    line = []

    for i in range(N):
        
        for j in range(4):
           
            cont = cont + 1
            
            if j == 3:
                line.append("PUM")
            else: 
                line.append(str(cont))
        
        print(' '.join(line))

        line = [] 

def solution2():   
  
    N = int(input())
        
    vetor = [1, 2, 3, 'PUM']

    for i in range(N):
       
        print(' '.join([str(v) for v in vetor]))

        for i in range(3):
            vetor[i] = vetor[i] + 4       

'''
SOLUTION #02
'''    
if __name__ == '__main__':
    print('1 - solution #01 \n2 - solution #02 ')

    option = input(':')

    if option == '1':
        solution1()
    elif option == '2':
        solution2() 
    else: 
        print('Então tá bom')

 
            

