edad = int(input("Edad de la persona: "))
tieneId = input("Tiene id?: ").upper()
enLista = input("Se encuentra en la lista?: ").upper()
pagoEntrada = input("Pago la entrada?: ").upper()
esVip = input("La persona es VIP?: ").upper()
acompañanteOk = input("El acompañantes cumple con todos los requisitos?: ").upper()

if edad < 18:
  print("❌ NO ENTRA: Menor de edad ❌")

elif esVip == "SI":
  print("ENTRA: Miembro VIP ⚜")
  
elif tieneId != "SI":
  print("❌ NO ENTRA: Sin identificación válida ❌")
  
elif enLista != "SI" or pagoEntrada != "SI":
    print("❌ NO ENTRA: No está en lista y no pagó la entrada ❌")

elif acompañanteOk == "NO":
  print("❌ NO ENTRA: Acompañante no cumple las reglas ❌")

else:
  print("✔ ENTRA: Cumple todos los requisitos ✔")