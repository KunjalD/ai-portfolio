def search_chunk(question, chunks):
    matches = []
    for chunk in chunks:
        if question.lower() in chunk.lower():
            matches.append(chunk)
    return matches