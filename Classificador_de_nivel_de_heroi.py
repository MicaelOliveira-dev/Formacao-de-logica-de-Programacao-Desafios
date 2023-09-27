def elo():
    heroi = str(input())    
    heroi_xp = int(input())
    if heroi_xp < 1000:
        print(f"Seu heroi será: {heroi} e seu elo é Ferro")
    elif heroi_xp in range(1001, 2001):
        print(f"Seu heroi será: {heroi} e seu elo é Prata")
    elif heroi_xp in range(2001, 5001):
        print(f"Seu heroi será: {heroi} e seu elo é Ouro")
    elif heroi_xp in range(6001, 7001):
        print(f"Seu heroi será: {heroi} e seu elo é Platina")
    elif heroi_xp in range(7001, 8001):
        print(f"Seu heroi será: {heroi} e seu elo é Ascendente")
    elif heroi_xp in range(8001, 9001):
        print(f"Seu heroi será: {heroi} e seu elo é é Imortal")
    elif heroi_xp >= 10001:
        print(f"Seu heroi será: {heroi} e seu elo é Radiante")

elo()