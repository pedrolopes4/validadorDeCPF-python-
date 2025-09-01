cpf = input("escreva seu CPF:") # Recebe o CPF

cpf = cpf.replace('.', '')  # Remove todos os pontos

cpf = cpf.replace('-', '')  # Remove o traço

# Valida o CPF

if cpf[0] == cpf[1] == cpf[2]:
        print("CPF inválido!")

elif cpf[3] == cpf[4] == cpf[5]:
        print("CPF inválido!")

elif cpf[6] == cpf[7] == [8]:
        print("CPF inválido!")

elif len(cpf) == 10:
        print("CPF válido!")

else:
        print("CPF válido!")

# Descobre onde o usuário mora comm base no úlltimo número do CPF

if cpf[10] == "1":
    moradia = str(input("Você é mora em: Distrito Federal (DF) ou Goiás (GO) ou Mato Grosso do Sul (MS) ou Mato Grosso (MT) ou Tocantins (TO)?"))
    if moradia == "MT" or "MS" or "GO" or "DF" or "TO":
        True
    else:
         print("Utilize apenas a sigla do estado correspondente, e em maiúsculo!")

elif cpf[10] == "2":
    moradia = str(input("Você é mora em: Acre (AC) ou Amazonas (AM) ou Amapá (AP) ou Pará (PA) ou Rondônia (RO) ou Roraima (RR)?"))
    if moradia == "AC" or "AM" or "AP" or "PA" or "RO" or "RR":
        True
    else:
        print("Utilize apenas a sigla do estado correspondente, e em maiúsculo!")

elif cpf[10] == "3":
    moradia = str(input("Você mora em: Ceará (CE) ou Maranhão (MA) ou Piauí (PI)?"))
    if moradia == "MA" or  "PI":
        True
    else:
        print("Utilize apenas a sigla do estado correspondente, e em maiúsculo!")

elif cpf[10] == "4":
    moradia = str(input("Você mora em: Alagoas (AL) ou Paraíba (PB) ou Pernambuco (PE) ou Rio Grande do Norte (RN)?"))
    if moradia == "AL" or "PB" or "PE" or "RN":
        True
    else:
        print("Utilize apenas a sigla do estado correspondende, e em maiúsculo!")

elif cpf[10] == "5":
    moradia = str(input("Você mora em: Bahia (BA) ou Sergipe (SE)?"))
    if moradia  == "BA" or "SE":
        True
    else:
        print("Utilize apenas a sigla do estado correspondente, e em maiúsculo!")

elif cpf[10] == "6":
    moradia = ("Minas Gerais (MG)")

elif cpf[10] == "7":
    moradia = str(input("Você mora em:Espírito Santo (ES) ou Rio de Janeiro (RJ)?"))
    if moradia == "ES" or "RJ":
        True
    else:
        print("Utilize apenas a sigla do estado correspondente, e em maiúsculo!")

elif cpf[10] == "8":
    moradia = str(input("Você mora em: São Paulo (SP)."))

elif cpf[10] == "9":
    moradia = str(input("Você mora em: Paraná (PR) ou Santa Catarina (SC)?"))
    if moradia == "PR" or "SC":
        True
    else:
        print("Utilize apenas a sigla do estado correspondente, e em maiúsculo!")

elif cpf[10] == "0":
    moradia = ("Rio Grande do Sul (RS).")

else:
    print("CPF inválido!")

# Imprime onde o usuário mora

print(moradia)
