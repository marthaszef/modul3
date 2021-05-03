thisshop =	{
  "warzywaniak": ["buraki","cebula"],
  "sportowy": ["sztangi"],
  "ogrodniczy":[ "kwiaty"]
}

newDict = {k.upper():[x.upper() for x in v] for k,v in thisshop.items()}

for k,v in newDict.items():
    print(f"Idę do {k}, kupuję tu następujące rzeczy: {v}.")

values=newDict.values()
print(values)
suma=sum([len(x) for x in values])
print(suma)

#print(f"Lista zakupów: {newDict}")
#print(f"Idę do {newDict.keys(k)}, kupuję tu następujące rzeczy: {v}.)
#print(f"Idę do {v}, kupuję tu następujące rzeczy: {v}")
print(f"W sumie kupuję {suma} produktów.")