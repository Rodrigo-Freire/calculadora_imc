#Cálculadora de Índice de Massa Corporal e Classificação segundo a OMS

#Apresentação do programa
import time
print ('Olá, eu sou uma calculadora de Índice de Massa Corporal (IMC)!');

time.sleep(3)
print('  ');
print ('Vou te ajudar a calcular o seu IMC e te dizer em qual classificação você esta!');

#Pergunta inicial para rodar ou não a calculadora
time.sleep(3);
print('  ');
calcular_imc = int(input('Você gostaria de calcular seu IMC? (Digite 1 para SIM e 2 para NÃO): '));

#Laço de repetição da calculadora
while calcular_imc == 1:
    #Variáveis para input de dados do usuário
    time.sleep(1);
    print('  ');
    peso = float(input('Informe seu peso em Kg sem as casas decimais (ex: 75):'));

    time.sleep (1)
    print('  ');
    altura = float(input('Agora informe sua altura no formato "0.00":'));

    time.sleep(2);
    print('  ');
    print('Hum... deixa eu calcular aqui, aguarde um momento.')

    #Cálculo do IMC
    calculo_imc = int(peso / (altura ** 2));

    #Saída do resultado
    time.sleep(4)
    print('  ');
    print('Seu IMC é igual a', calculo_imc);
    print('  ');

    #Classificação segundo a OMS
    time.sleep(2)
    if calculo_imc >= 0 and calculo_imc < 18.5:
        print('Você está abaixo do peso ideal!')
    elif calculo_imc >= 18.5 and calculo_imc < 25:
        print('Você está no peso ideal. Parabéns!')
    elif calculo_imc >= 25 and calculo_imc < 29.9:
        print('Você está levemente acima do peso ou com sobrepeso.')
    elif calculo_imc >= 29.9 and calculo_imc < 34.9:
        print('Você está com Obesidade Grau I.')
    elif calculo_imc >= 34.9 and calculo_imc < 40:
        print('Você está com Obesidade Grau II.')
    else:
        print('Você está com Obesidade Grau III.')
    
    time.sleep(3)
    print('  ');
    calcular_imc = int(input('Você gostaria de calcular novamente? (Digite 1 para SIM e 2 para NÃO): '))
    
#Finalização da calculadora
print('Obrigado por usar nossa calculadora! Até Mais!')
