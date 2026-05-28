body = 0

otazky = [
    "kolik je 3 + 5?", 
    "8",
    "jakou barvu ma obloha?",
    "modrou"
]

a = int(input(otazky[0]))
if a == 8:
    print("Spravne")
    body += 1

else:
    print("Spatne")


b = input(otazky[2])
if b == "modrou":
    print("spravne")
    body += 1
else:
    print("Spatne")

if body < 2:
    print("Neprosel jsi testem")
