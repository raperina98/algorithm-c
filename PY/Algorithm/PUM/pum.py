'''
[] gerar numeros sequencias
    [ok] percorrer n vezes sendo n a quantidade de linhas de output
        [ok] a cada loop, será gerado 4 numeros sendo o quarto substituido pela palavra "PUM"
            [] vetor de contadores que incrementa +4 em todos os valores
            ou
            [ok] novo loop de 4 voltas para criar uma lista com os numeros sequecias
            
'''

if __name__ == '__main__':
    
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
        
    

            

