import requests
import re

gabaritos = [
        "https://www.sbc.org.br/documentos-da-sbc/send/212-2019/1247-gabarito-2019",
        "https://www.sbc.org.br/documentos-da-sbc/send/202-2018/1202-gabarito-2018",
        "https://www.sbc.org.br/documentos-da-sbc/send/201-2017/1179-gabarito-2017",
        "https://www.sbc.org.br/documentos-da-sbc/send/194-2016/1044-prova-2016",
        "https://www.sbc.org.br/documentos-da-sbc/send/192-2015/1033-gabarito-2015",
        "https://www.sbc.org.br/documentos-da-sbc/send/181-2014/956-gabarito",
        "https://www.sbc.org.br/documentos-da-sbc/send/180-2013/954-gabarito",
        "https://www.sbc.org.br/documentos-da-sbc/send/179-2012/952-gabarito",
        "https://www.sbc.org.br/documentos-da-sbc/send/157-2011/850-gabarito-ano2011",
        "https://www.sbc.org.br/documentos-da-sbc/send/160-2010/858-gabarito-ano2010"

    ]
provas = [
        "https://www.sbc.org.br/documentos-da-sbc/send/181-2014/957-cadernodequestoes-ano2014",
        "https://www.sbc.org.br/documentos-da-sbc/send/212-2019/1246-prova-2019",
        "https://www.sbc.org.br/documentos-da-sbc/send/202-2018/1203-prova-2018",
        "https://www.sbc.org.br/documentos-da-sbc/send/201-2017/1178-prova-2017",
        "https://www.sbc.org.br/documentos-da-sbc/send/194-2016/1045-prova-2016",
        "https://www.sbc.org.br/documentos-da-sbc/send/192-2015/1032-cadernodequestoes-ano2015",
        "https://www.sbc.org.br/documentos-da-sbc/send/180-2013/955-cadernodequestoes-ano2013",
        "https://www.sbc.org.br/documentos-da-sbc/send/179-2012/953-cadernodequestoes-ano2012",
        "https://www.sbc.org.br/documentos-da-sbc/send/157-2011/851-cadernodequestes-ano2011",
        "https://www.sbc.org.br/documentos-da-sbc/send/160-2010/859-cadernodequestes-ano2010"
    ]


def main():
    for prova in provas:
        baixar(prova, "prova")

    for gab in gabaritos:
        baixar(gab, "gabarito")



def baixar(url, tipo):
    anoProva = re.search(r"-\d{4}", url)
    if anoProva:
        anoProva = anoProva.group()
    else:
        anoProva = "desconhecido"
    print(f'{tipo} ano {anoProva} encontrada')
    r = requests.get(url, allow_redirects=True)
    nomeArquivo = f'{tipo}{anoProva}.pdf'
    print('baixando, aguarde ...')
    open(nomeArquivo, 'wb').write(r.content)





if __name__ == '__main__':
    main()
