sozluk = {}
print(type(sozluk))
sozluk = {"book":"kitap",
"pencil":"kalem","table":"masa"}
print(sozluk["book"])
sozluk["book"] = "KİTAP"
print("1",sozluk.get("recommodation"))
print("2",sozluk.items())
print("3",sozluk.keys())
print("4",sozluk.values())
sozluk.update({"try":"deneme"})
print("5",sozluk)
sozluk.pop("try")
print("6",sozluk)
sozluk.popitem()
print("7",sozluk)
liste = ["Faruk","Hakkı","Mahmut","Soner",
"Işınsu","Berkcan","Çiğdem"]
sozluk = dict.fromkeys(liste,100)
print("8",sozluk)


