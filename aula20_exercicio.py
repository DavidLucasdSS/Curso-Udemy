while True:
    print(3 * '@#', 'COMPARADOR', 3 * '#@')
    print()
    print(3 * '=', 'números com casas, utilizar "."', 3 * '=')
    print()

    numero1 = input('Digite um número para a comparação: ')
    numero2 = input('Digite o segundo valor: ')

    # Converte a str digitada para float
    try:
        fnumero1 = float(numero1)
        fnumero2 = float(numero2)

        if fnumero1 > fnumero2:
            print(f'O número {numero1} é maior que o número {numero2}.')
        elif fnumero1 == fnumero2:
            print(f'O número {numero1} é igual ao número {numero2}.')
        else:
            print(f'O número {numero2} é maior que o número {numero1}.')
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

    # Pergunta ao usuário se deseja continuar
    continuar = input("Deseja fazer outra comparação? (s/n): ").strip().lower()
    if continuar != 's':
        break
