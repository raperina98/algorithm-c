flow_tourists = 0
flow_jeep = 0

while(True):
    
    data = input().split();
    
    movement = data[0];
    
    if movement == 'ABEND':
        break;
        
    qtyTourists = int(data[1]);
    
    if movement == 'SALIDA':
        flow_tourists = flow_tourists + qtyTourists;
        flow_jeep = flow_jeep + 1;
    elif movement == 'VUELTA':
        flow_tourists = flow_tourists - qtyTourists;
        flow_jeep = flow_jeep - 1;
        
print(flow_tourists);
print(flow_jeep);


# [OK] validar string de fim do processamento

# [OK] tratar dados da quantidade de turistas
# [OK] verificacoes para soma e substracao
# para achar a diferença da quantidade que foi
# e voltou

# Percorrer todas as entradas de dados
# capturando o par de informacoes [movim., qtde turista]
# e verificar entrada e saída de turistas;

# crio uma variavel que armazenará o fluxo de turistas 
# com base na diferença das movimentacoes

# crio uma variavel que armazenará o fluxo de jeeps
# com base na diferença das movimentacoes

# se o movimento é SALIDA, 
# soma a quantidade que entrou com a quantidade que já estava no parque
# conta mais um jeep para dentro do parque
# se o movimento é VUELTA
# subtrai a quantidade que voltou com a quantidade que já estava no parque
# retira um jeep que estava dentro do parque
