import PyPDF2
import re


#conteudoQuestao = "inverso do valor da entrada" 
conteudoQuestao = input("Digite o trecho da questão. Exemplo: Seja a matris:\n") #BUSCANDO ESSE TRECHO DE PERGUNTA

pdefis = ["prova-2010.pdf",
          "prova-2012.pdf",
          "prova-2014.pdf",
          "prova-2016.pdf",
          "prova-2018.pdf",
          "prova-2011.pdf",
          "prova-2013.pdf",
          "prova-2015.pdf",
          "prova-2017.pdf",
          "prova-2019.pdf"]

for pdf in pdefis:
    object = PyPDF2.PdfFileReader(pdf)
    NumPages = object.getNumPages()

    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        text = PageObj.extractText()
        result = re.findall(conteudoQuestao, text)
        type(result)
        ano = re.search(r"-\d{4}", pdf).group()
        if result:
            print("###################################################")
            print(f"\n\nENCONTRADO na página {str(i+1)} do arquivo: {pdf}")
            print(f"\nRESPOSTA no arquivo: gabarito{ano}\n")
            print(f"[...] {result} [...]")
            print("###################################################")
