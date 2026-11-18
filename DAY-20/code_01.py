#Prerequisites
#pip install chromadb sentence-transformers openai
import os

SAMPLE_FILE = "sample_document.txt"

def create_sample_file():
    sample_text = (
        "Artificial Intelligence (AI) is transforming industries across the globe. "
        "Machine learning, a core branch of AI, enables computers to learn patterns from data without being explicitly programmed. "
        "Deep learning goes a step further by using multi-layered neural networks to process complex inputs like images, audio, and text. "
        "Retrieval-Augmented Generation (RAG) is a modern AI architecture that combines information retrieval with text generation. "
        "Instead of relying solely on a language model's static training data, RAG fetches relevant facts from an external knowledge base. "
        "To make large documents searchable, text is first divided into smaller overlapping chunks. "
        "Chunk overlap ensures that important context at the boundaries of a split is preserved across adjacent segments. "
        "These text chunks are then converted into numerical vectors called embeddings and stored in a vector database like Chroma."
    )
    with open(SAMPLE_FILE, "w", encoding="utf-8") as f:
        f.write(sample_text)

def split_text_into_chunks(text, chunk_size=150, chunk_overlap=30):
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size.")

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += (chunk_size - chunk_overlap)

    return chunks

def main():
    if not os.path.exists(SAMPLE_FILE):
        create_sample_file()

    # Load the sample TXT document
    with open(SAMPLE_FILE, "r", encoding="utf-8") as f:
        document_text = f.read()

    # Configure chunk size and overlap (in characters)
    CHUNK_SIZE = 180
    CHUNK_OVERLAP = 40

    chunks = split_text_into_chunks(
        document_text,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    print(f"Loaded '{SAMPLE_FILE}' ({len(document_text)} characters).")
    print(f"Divided into {len(chunks)} chunks (Size: {CHUNK_SIZE}, Overlap: {CHUNK_OVERLAP}):\n")
    print("=" * 60)

    for idx, chunk in enumerate(chunks, start=1):
        print(f"Chunk #{idx} (Length: {len(chunk)} chars):")
        print(f"\"{chunk}\"")
        print("-" * 60)

if __name__ == "__main__":
    main()
