code = input("Insert the code on the stamped egg")

if "UK" in code:
    country = "United Kingdom"
    code = code.replace("UK","")
elif "NL" in code:
    country = "Netherlands"
    code = code.replace("NL","")
elif "FR" in code:
    country = "France"
    code = code.replace("FR","")
elif "BE" in code:
    country = "Belgium"
    code = code.replace("BE","")
elif "DE" in code:
    country = "Germany"
    code = code.replace("DE","")
elif "ES" in code:
    country = "Spain"
    code = code.replace("ES","")

if code[0] == "0":
    farmingMethod = "Organic"
    code = code.replace("0","",1)
elif code[0] == "1":
    farmingMethod = "Free Range"
    code = code.replace("1","",1)
elif code[0] == "2":
    farmingMethod = "Barn"
    code = code.replace("2","",1)
elif code[0] =="3":
    farmingMethod = "Cage"
    code = code.replace("3","",1)

print(farmingMethod, "Egg Country of Origin:",country,"Farm Id:",code)
