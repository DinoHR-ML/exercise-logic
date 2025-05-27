while True:
    try:
        yearsold = input("Opa meu man, quantos anos vc tem? (999 para finalizar)\n" \
        "")
        years = int(yearsold)
        if years == 999:
            break
        elif years >= 18:
            print("Você é maior de idade")
        elif years <=17:
            print("Você é menor de idade")
    except ValueError:
        print("Escreve direito")