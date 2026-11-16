
import chromadb
from sentence_transformers import SentenceTransformer
from extrair_pdf import extrair_pdf
from dividir_texto import dividir_texto

modelo = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

cliente = chromadb.PersistentClient(path="chroma_db")

try:
    cliente.delete_collection("documentos")
except ValueError:
    pass

colecao = cliente.create_collection(
    name="documentos"
)

paginas = extrair_pdf("data/documento.pdf")
trechos = dividir_texto(
    paginas,
    tamanho=1000,
    sobreposicao=150
)

textos = [trecho["texto"] for trecho in trechos]

embeddings = modelo.encode(textos).tolist()

colecao.upsert(
    ids=[str(i) for i in range(len(trechos))],
    embeddings=embeddings,
    documents=textos,
    metadatas=[
        {
            "documento": trecho["documento"],
            "pagina": trecho["pagina"]
        }
        for trecho in trechos
    ]
)

pergunta = "Como salvar um documento em PDF/A no Microsoft Word?"

embedding_pergunta = modelo.encode([pergunta]).tolist()

resultados = colecao.query(
    query_embeddings=embedding_pergunta,
    n_results=3
)

print("\nPergunta:", pergunta)
print("\nTrechos encontrados:")

for texto, metadata, distancia in zip(
    resultados["documents"][0],
    resultados["metadatas"][0],
    resultados["distances"][0]
):
    print(f"\nDocumento: {metadata['documento']}")
    print(f"Página: {metadata['pagina']}")
    print(f"Distância: {distancia:.4f}")
    print(texto)