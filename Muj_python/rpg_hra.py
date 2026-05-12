print("Stojis pred restauraci.\nCo udelas?")

def start():
    funkce = [
    jit_dovnitr,
    domu
    ]

    volby = [
    "jit dovnitr",
    "odejit domu"
    ]

    menu(volby, funkce)

def jit_dovnitr():
    print()
    print("Vesel jsi dovnitra cisnik te usadil")
    objednat()
def domu():
    print()
    print("jdes domu ale citis vuni restaurace tak se vratis a jdes dovnitr")
    objednat()

def menu(volby, funkce):
    for i in range(len(volby)):
        print(f"{i + 1}: {volby[i]}")
    volba = int(input("Zadej cislo volby: ")) - 1
    if 0 <= volba < len(funkce):
        handler = funkce[volba]
        handler()
    else:
        print("neplatne cislo")
        menu(volby, funkce)

#---------------------------------------------------------------------

def objednat():
    print()
    print("Prisel cisnik a mas si objednat.\n Co si objednas?")
    volby = [
        "steak",
        "testoviny",
        "pizza"
    ]

    funkce = [
        steak,
        testoviny,
        pizza
    ]

    menu(volby, funkce)


def steak():
    print()
    print("Objednal jsi si steak. \nDojedl jsi steak")
    choice = "bilkoviny"
    food = "steak"
    vysvetleni(choice, food)


def testoviny():
    print()
    print("Objednal jsi si testoviny. \nDojedl jsi testoviny")
    choice = "sacharidy"
    food = "testoviny"
    vysvetleni(choice, food)


def pizza():
    print()
    print("Objednal jsi si pizzu. \nDojedl jsi pizzu")
    choice = "zeleninu"
    food = "pizza"
    vysvetleni(choice, food)

#----------------------------------------

def vysvetleni(choice, food):
    print()
    print(f"Objednal jsi si vysvetleni. \nProtoze jsi snedl {food} tak jsi do tela dostal {choice}")
    print()
    print("Odchazis z restaurace spokojen")

start()