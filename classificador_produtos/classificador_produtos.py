def avaliar_temperatura(temp_atual):
    if temp_atual < 2:
        return "ALERTA: Risco de congelamento"
    elif 2 <= temp_atual <= 8:
        return "Estoque seguro"
    else:
        return "ALERTA: Risco de estrago"


status_visor = int(input("Em que temperatura estáo sensor?").strip())

rtemp = avaliar_temperatura(status_visor)

print(f"\nA temperatura está em {status_visor}°C.\n\n{rtemp}")
