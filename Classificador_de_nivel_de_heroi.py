def calcular_elo(heroi_xp):
    if heroi_xp < 1000:
        return "Ferro"
    elif 1000 <= heroi_xp < 2000:
        return "Prata"
    elif 2000 <= heroi_xp < 5000:
        return "Ouro"
    elif 5000 <= heroi_xp < 7000:
        return "Platina"
    elif 7000 <= heroi_xp < 8000:
        return "Ascendente"
    elif 8000 <= heroi_xp < 10000:
        return "Imortal"
    else:
        return "Radiante"

def elo():
    try:
        heroi = str(input("Digite o nome do heroi: "))
        heroi_xp = int(input("Digite a experiência do heroi: "))
        
        elo_do_heroi = calcular_elo(heroi_xp)
        print(f"Seu heroi será: {heroi} e seu elo é {elo_do_heroi}")
    except ValueError:
        print("Entrada inválida. Certifique-se de que a experiência seja um número inteiro válido.")

elo()