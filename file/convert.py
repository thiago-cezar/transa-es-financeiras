from datetime import datetime


def convert_data(data):
    conversion = []

    for transaction in data:
        cnab_data = {}
        convert = transaction.decode("utf-8")
        cnab_data["Tipo"] = convert[0:1]
        cnab_data["Data"] = str(datetime.strptime(convert[1:9], "%Y%m%d").date())
        cnab_data["Valor"] = int(convert[9:19]) / 100.00
        if int(convert[0:1]) in [2, 3, 9]:
            cnab_data["Valor"] = int(convert[9:19]) / 100.00 * -1
        cnab_data["CPF"] = convert[19:30]
        cnab_data["Cartão"] = convert[30:42]
        cnab_data["Hora"] = str(datetime.strptime(convert[42:48], "%H%M%S").time())
        cnab_data["Dono_da_loja"] = convert[48:62].strip()
        cnab_data["Nome_loja"] = convert[62:81].strip()

        conversion.append(cnab_data)

    return conversion
