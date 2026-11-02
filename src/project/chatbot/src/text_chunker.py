
def chunk_text(text:str, chunk_size:int = 100, overlap:int = 0) -> list[str]:
    chunks = []
    if chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer.")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Overlap must be a non-negative integer less than the chunk size.")
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])

        if i + chunk_size >= len(text):
            break
    return chunks

if __name__ == "__main__":
    sample_text = "This is a sample text that will be split into chunks. " * 20
    chunks = chunk_text(sample_text, chunk_size=50, overlap=10)
    for idx, chunk in enumerate(chunks):
        print(f"Chunk {idx + 1}: {chunk}\n")
