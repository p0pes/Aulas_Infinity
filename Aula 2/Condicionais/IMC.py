Alt = float(input("Insira a sua altura: "))
Pes = float(input("Insira seu peso: "))

IMC = float(Pes/(Alt * Alt))

if IMC <= 18 :
    print(f"Você está abaixo do peso. Seu IMC é {IMC:.2f})")
elif IMC <= 24 :
    print(f"Você está no peso normal. Seu IMC é {IMC:.2f}")
elif IMC <= 30 :
    print(f"Você esté acima do peso. Seu IMC é {IMC:.2f}")
elif IMC <= 40 :
    print(f"Você está obeso. Seu IMC é {IMC:.2f}")
elif IMC >40 :
    print(f"Você esta muito enorme. Seu IMC é {IMC:.2f}")