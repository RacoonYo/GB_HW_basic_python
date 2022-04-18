from requests import get, utils


def currency_rates(currency):
    currency_dict = {}
    _split_list = []
    _new_split_list = []

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    _split_list = content.split('<')

    for i in _split_list:
        _new_split_list.append(i.split('>'))

    for i in _new_split_list:
        if i[0] == 'CharCode':
            code = i[1]
        elif i[0] == 'Value':
            currency_dict[code] = [name, float(i[1].replace(',', '.'))]
        elif i[0] == 'Name':
            name = i[1]

    return currency_dict.get(currency.upper())


print(currency_rates('usd'))
print(currency_rates('EUR'))
print(currency_rates('PLL'))
