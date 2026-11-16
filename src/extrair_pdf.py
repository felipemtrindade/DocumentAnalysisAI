from pathlib import Path
from pypdf import PdfReader

def extrair_pdf(caminho):
    leitor = PdfReader(caminho)
    paginas = []

    for numero, pagina in enumerate(leitor.pages, start=1):
        texto = pagina.extract_text()

        if texto and texto.strip():
            paginas.append({
                "documento": Path(caminho).name,
                "pagina": numero,
                "texto": texto.strip()
            })

    return paginas


if __name__ == "__main__":
    caminho = "data/documento.pdf"

    paginas = extrair_pdf(caminho)

    print("Páginas com texto:", len(paginas))

    for pagina in paginas[:3]:
        print(f"\nPágina {pagina['pagina']}")
        print(pagina["texto"][:500])