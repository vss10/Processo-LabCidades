import unicodedata

def normalizar_texto(txt):
    txt = str(txt).strip().lower()

    txt = unicodedata.normalize("NFKD", txt)
    txt = txt.encode("ASCII", "ignore").decode("utf-8")

    return txt

situacoes_validas = {
    "em aberto": "EM ABERTO",
    "atrasado": "ATRASADO",
    "divida ativa": "DÍVIDA ATIVA",
    "pago": "PAGO",
    "parcelado": "PARCELADO",
    "quitado": "QUITADO"
}