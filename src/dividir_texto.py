from src.extrair_pdf import extrair_pdf

def dividir_texto(paginas, tamanho=500, sobreposicao=100):
    trechos = []

    for pagina in paginas:
        texto = pagina["texto"]
        inicio = 0

        while inicio < len(texto):
            fim = inicio + tamanho

            trechos.append({
                "documento": pagina["documento"],
                "pagina": pagina["pagina"],
                "texto": texto[inicio:fim]
            })

            inicio += tamanho - sobreposicao

    return trechos


if __name__ == "__main__":
    paginas = extrair_pdf("data/documento.pdf")
    trechos = dividir_texto(paginas)

    print("Total de trechos:", len(trechos))

    for trecho in trechos[:3]:
        print(f"\nPágina {trecho['pagina']}")
        print(trecho["texto"])