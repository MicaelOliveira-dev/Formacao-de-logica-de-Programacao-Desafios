
def nivel(vitorias, derrotas):
    global saldo
    saldo = int(vitorias - derrotas)
    if saldo < 10:
        return "Ferro"
    elif 11 <= saldo < 20:
        return "Bronze"
    elif 21 <= saldo <= 50:
        return "Prata"
    elif 51 <= saldo <= 80:
        return "Ouro"
    elif 81 <= saldo <= 90:
        return "Diamante"
    elif 91 <= saldo <= 100:
        return "Lendario"
    elif saldo >= 101:
        return "Imortal"

def elo():
    try:
        elo = nivel(int(input()), int(input()))
        print(f"O Herói tem de saldo de **{saldo}** está no nível de **{elo}**")   
    except ValueError:
        print("Entrada inválida. Certifique-se de que a experiência seja um número inteiro válido.")

elo()