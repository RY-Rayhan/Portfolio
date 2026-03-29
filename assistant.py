import datetime

print("=" * 40)
print("   Bonjour ! Je suis ton assistant.")
print("=" * 40)

while True:
    print("\nQue veux-tu savoir ?")
    print("1 - L'heure")
    print("2 - La date")
    print("3 - Quitter")

    choix = input("\nTon choix : ")

    if choix == "1":
        heure = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\nIl est actuellement : {heure}")

    elif choix == "2":
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        print(f"\nNous sommes le : {date}")

    elif choix == "3":
        print("\nAu revoir !")
        break

    else:
        print("\nJe n'ai pas compris, tape 1, 2 ou 3.")
