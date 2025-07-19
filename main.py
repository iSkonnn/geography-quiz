restantes = 27
restantesmundo = 193
achadosmundo = 0;
achados = 0
paises_jaforam = [];
achadosafrica = 0;
achadosoceania = 0;
achadosasia = 0;
achadossa = 0;
achadosna = 0;
achadosac = 0;
achadoseu = 0;
salomao = ["ILHAS SALOMÃO", "SALOMAO", "ILHAS SALOMAO","SALOMÃO"]
marshall = ["ILHAS MARSHALL", "MARSHALL"]
paises_mundo = [
    "AFEGANISTÃO", "ALBÂNIA", "ARGÉLIA", "ANDORRA", "ANGOLA", "ANTÍGUA E BARBUDA", "ARGENTINA", "ARMÊNIA", "AUSTRÁLIA", "ÁUSTRIA",
    "AZERBAIJÃO", "BAHAMAS", "BAHRAIN", "BANGLADESH", "BARBADOS", "BELARUS", "BÉLGICA", "BELIZE", "BENIN", "BUTÃO", "BOLÍVIA",
    "BÓSNIA E HERZEGOVINA", "BOTSWANA", "BRASIL", "BRUNEI", "BULGÁRIA", "BURKINA FASO", "BURUNDI", "CABO VERDE", "CAMBOJA", "CAMARÕES",
    "CANADÁ", "REPÚBLICA CENTRO-AFRICANA", "CHADE", "CHILE", "CHINA", "COLÔMBIA", "COMORES", "CONGO", "COSTA RICA", "CROÁCIA", "CUBA",
    "CHIPRE", "REPÚBLICA TCHECA", "DINAMARCA", "DJIBOUTI", "DOMINICA", "REPÚBLICA DOMINICANA", "TIMOR-LESTE", "EQUADOR", "EGITO", "EL SALVADOR",
    "GUINÉ EQUATORIAL", "ERITREIA", "ESTÔNIA", "ESWATINI", "ETIÓPIA", "FIJI", "FINLÂNDIA", "FRANÇA", "GABÃO", "GÂMBIA", "GEÓRGIA",
    "ALEMANHA", "GANA", "GRÉCIA", "GRANADA", "GUATEMALA", "GUINÉ", "GUINÉ-BISSAU", "GUIANA", "HAITI", "HONDURAS", "HUNGRIA",
    "ISLÂNDIA", "ÍNDIA", "INDONÉSIA", "IRÃ", "IRAQUE", "IRLANDA", "ISRAEL", "ITÁLIA", "JAMAICA", "JAPÃO", "JORDÂNIA", "CAZAQUISTÃO",
    "QUÊNIA", "KIRIBATI", "COREIA DO NORTE", "COREIA DO SUL", "KUWAIT", "QUIRGUISTÃO", "LAOS", "LETÔNIA", "LÍBANO", "LESOTO", "LIBÉRIA",
    "LÍBIA", "LIECHTENSTEIN", "LITUÂNIA", "LUXEMBURGO", "MADAGASCAR", "MALAWI", "MALÁSIA", "MALDIVAS", "MALI", "MALTA", "ILHAS MARSHALL",
    "MAURITÂNIA", "MAURÍCIO", "MÉXICO", "MICRONÉSIA", "MOLDÁVIA", "MÔNACO", "MONGÓLIA", "MONTENEGRO", "MARROCOS", "MOÇAMBIQUE", "MYANMAR",
    "NAMÍBIA", "NAURU", "NEPAL", "PAÍSES BAIXOS", "NOVA ZELÂNDIA", "NICARÁGUA", "NÍGER", "NIGÉRIA", "MACEDÔNIA DO NORTE", "NORUEGA", "OMÃ",
    "PAQUISTÃO", "PALAU", "PANAMÁ", "PAPUA NOVA GUINÉ", "PARAGUAI", "PERU", "FILIPINAS", "POLÔNIA", "PORTUGAL", "CATAR", "ROMÊNIA",
    "RÚSSIA", "RUANDA", "SÃO CRISTÓVÃO E NEVIS", "SANTA LÚCIA", "SÃO VICENTE E GRANADINAS", "SAMOA", "SAN MARINO", "SÃO TOMÉ E PRÍNCIPE",
    "ARÁBIA SAUDITA", "SENEGAL", "SÉRVIA", "SEYCHELLES", "SERRA LEOA", "SINGAPURA", "ESLOVÁQUIA", "ESLOVÊNIA", "ILHAS SALOMÃO", "SOMÁLIA",
    "ÁFRICA DO SUL", "SUDÃO DO SUL", "ESPANHA", "SRI LANKA", "SUDÃO", "SURINAME", "SUÉCIA", "SUÍÇA", "SÍRIA", "TAIWAN", "TAJIQUISTÃO",
    "TANZÂNIA", "TAILÂNDIA", "TOGO", "TONGA", "TRINDADE E TOBAGO", "TUNÍSIA", "TURQUIA", "TURCOMENISTÃO", "TUVALU", "UGANDA", "UCRÂNIA",
    "EMIRADOS ÁRABES UNIDOS", "REINO UNIDO", "ESTADOS UNIDOS", "URUGUAI", "UZBEQUISTÃO", "VANUATU", "CIDADE DO VATICANO", "VENEZUELA",
    "VIETNÃ", "IÊMEN", "ZÂMBIA", "ZIMBÁBUE"
]
africa = [
    "ARGÉLIA", "ANGOLA", "BENIN", "BOTSWANA", "BURKINA FASO", "BURUNDI", "CABO VERDE", "CAMARÕES", "COMORES", "CONGO", "COSTA DO MARFIM", "DJIBUTI",
    "EGITO", "ERITREIA", "ESWATINI", "ETIÓPIA", "GABÃO", "GÂMBIA", "GANA", "GUINÉ", "GUINÉ-BISSAU", "GUINÉ EQUATORIAL", "LESOTO", "LIBÉRIA", "LÍBIA",
    "MADAGASCAR", "MALAWI", "MALI", "MARROCOS", "MAURITÂNIA", "MAURÍCIO", "MOÇAMBIQUE", "NAMÍBIA", "NÍGER", "NIGÉRIA", "QUÊNIA", "RUANDA", "SÃO TOMÉ E PRÍNCIPE",
    "SENEGAL", "SEYCHELLES", "SERRA LEOA", "SOMÁLIA", "SUDÃO", "SUDÃO DO SUL", "TANZÂNIA", "TOGO", "TUNÍSIA", "UGANDA", "ZÂMBIA", "ZIMBÁBUE"
]
america_do_norte = [
    "CANADÁ", "ESTADOS UNIDOS", "MÉXICO"
]
america_central = [
    "ANTÍGUA E BARBUDA", "BAHAMAS", "BARBADOS", "BELIZE", "COSTA RICA", "CUBA", "DOMINICA", "REPÚBLICA DOMINICANA", "EL SALVADOR", "GRANADA", "GUATEMALA",
    "HAITI", "HONDURAS", "JAMAICA", "NICARÁGUA", "PANAMÁ", "SANTA LÚCIA", "SÃO CRISTÓVÃO E NEVIS", "SÃO VICENTE E GRANADINAS"
]
america_do_sul = [
    "ARGENTINA", "BOLÍVIA", "BRASIL", "CHILE", "COLÔMBIA", "EQUADOR", "GUIANA", "PARAGUAI", "PERU", "SURINAME", "URUGUAI", "VENEZUELA", "TRINDADE E TOBAGO"
]
asia = [
    "AFEGANISTÃO", "ARÁBIA SAUDITA", "ARMÊNIA", "AZERBAIJÃO", "BANGLADESH", "BAHRAIN", "BRUNEI", "BUTÃO", "CAMBOJA", "CAZAQUISTÃO", "CHINA", "CHIPRE",
    "COREIA DO NORTE", "COREIA DO SUL", "EMIRADOS ÁRABES UNIDOS", "FILIPINAS", "GEÓRGIA", "ÍNDIA", "INDONÉSIA", "IRÃ", "IRAQUE", "ISRAEL", "JAPÃO",
    "JORDÂNIA", "KUWAIT", "LAOS", "LÍBANO", "MALÁSIA", "MALDIVAS", "MONGÓLIA", "MYANMAR", "NEPAL", "OMÃ", "PAQUISTÃO", "QATAR", "QUIRGUISTÃO",
    "SINGAPURA", "SÍRIA", "SRI LANKA", "TAILÂNDIA", "TAIWAN", "TAJIQUISTÃO", "TURCOMENISTÃO", "TURQUIA", "UZBEQUISTÃO", "VIETNÃ", "IÊMEN"
]
europa = [
    "ALBÂNIA", "ALEMANHA", "ANDORRA", "ARMÊNIA", "ÁUSTRIA", "AZERBAIJÃO", "BÉLGICA", "BIELORRÚSSIA", "BÓSNIA E HERZEGOVINA", "BULGÁRIA", "CHIPRE",
    "CROÁCIA", "DINAMARCA", "ESLOVÁQUIA", "ESLOVÊNIA", "ESPANHA", "ESTÔNIA", "FINLÂNDIA", "FRANÇA", "GEÓRGIA", "GRÉCIA", "HOLANDA", "HUNGRIA",
    "IRLANDA", "ITÁLIA", "KOSOVO", "LETÔNIA", "LIECHTENSTEIN", "LITUÂNIA", "LUXEMBURGO", "MACEDÔNIA DO NORTE", "MALTA", "MOLDÁVIA", "MÔNACO",
    "MONTENEGRO", "NORUEGA", "POLÔNIA", "PORTUGAL", "REINO UNIDO", "REPÚBLICA TCHECA", "ROMÊNIA", "RÚSSIA", "SAN MARINO", "SÉRVIA", "SUÉCIA",
    "SUÍÇA", "UCRÂNIA", "VATICANO"
]

oceania = [
    "AUSTRÁLIA", "FIJI", "ILHAS MARSHALL", "MICRONÉSIA", "NAURU", "NOVA ZELÂNDIA", "PALAU", "PAPUA NOVA GUINÉ",
    "ILHAS SALOMÃO", "SAMOA", "ILHAS TONGA", "TUVALU", "VANUATU", "KIRIBATI"
]

estados_brasil = ["ACRE", "ALAGOAS", "AMAPÁ", "AMAZONAS", "BAHIA", "CEARÁ", "DISTRITO FEDERAL", "ESPÍRITO SANTO", "GOIÁS", "MARANHÃO", "MATO GROSSO",
                  "MATO GROSSO DO SUL", "MINAS GERAIS", "PARÁ", "PARAÍBA", "PARANÁ", "PERNAMBUCO", "PIAUÍ", "RIO DE JANEIRO", "RIO GRANDE DO NORTE",
                  "RIO GRANDE DO SUL", "RONDÔNIA", "RORAIMA", "SANTA CATARINA", "SÃO PAULO", "SERGIPE", "TOCANTINS"]
estados_jaforam = []
porcentagem = (achados / 27) * 100
game = input("Insira o modo de jogo BRASIL ou MUNDO: ").upper()
if game == "BRASIL":
    print("\nAinda há:", restantes, "estados", " / ", porcentagem, "%")
while restantes > 0 and game == "BRASIL":
    estado = input("Insira o nome de um estado do Brasil: ").upper()

    if estado in estados_brasil:
        if estado not in estados_jaforam:
            restantes -= 1
            achados += 1
            porcentagem = round((achados / 27) * 100, 2)
            print("\nAinda há:", restantes, "estados", " / ", porcentagem, "%")
            estados_jaforam.append(estado)
        else:
            print("\nVocê já escreveu esse estado!")
    else:
        print("\nEsse estado não existe!")
while restantesmundo > 0 and game == "MUNDO":
    pais = input("Insira o nome de um país: ").upper()
    if(pais in salomao):
        pais = "ILHAS SALOMÃO"
    elif(pais in marshall):
        pais = "ILHAS MARSHALL"
    if(pais in paises_mundo):
        if pais not in paises_jaforam:
            if(pais in africa):
                achadosafrica+=1;
            elif(pais in america_do_norte):
                achadosna+=1;
            elif(pais in america_do_sul):
                achadossa+=1;
            elif(pais in america_central):
                achadosac+=1;
            elif(pais in asia):
                achadosasia+=1;
            elif(pais in oceania):
                achadosoceania+=1;
            elif(pais in europa):
                achadoseu+=1;
            print("\nÁfrica:",achadosafrica,"/",len(africa))
            print("América Central:",achadosac,"/",len(america_central))
            print("América do Norte",achadosna,"/",len(america_do_norte))
            print("América do Sul:",achadossa,"/",len(america_do_sul))
            print("Ásia:",achadosasia,"/",len(asia))
            print("Europa:",achadoseu,"/",len(europa))
            print("Oceania:",achadosoceania,"/",len(oceania))
            restantesmundo-=1;
            achadosmundo+=1;
            porcentagem = round((achadosmundo / 193) * 100, 2)
            print("\nAinda há:", restantesmundo, "países", " / ", porcentagem, "%")
            paises_jaforam.append(pais)
        else:
            print("\nVocê já escreveu esse país!")
    else:
        print("\nEsse país não existe!")
print("\nParabéns, você ganhou!")
game = input("\nInsira o modo de jogo BRASIL ou MUNDO: ").upper()
