def data_por_extenso(data):
    dia, mes, ano = data.split("/")
    
    meses = {
        "01": "janeiro",
        "02": "fevereiro",
        "03": "março",
        "04": "abril",
        "05": "maio",
        "06": "junho",
        "07": "julho",
        "08": "agosto",
        "09": "setembro",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro"
    }
    
    data_extenso = dia + " de " + meses[mes] + " de " + ano
    return data_extenso

data = input("Digite uma data no formato DD/MM/AAAA: ")
data_extenso = data_por_extenso(data)
print("Data por extenso:", data_extenso)
