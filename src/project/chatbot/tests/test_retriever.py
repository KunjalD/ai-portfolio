from project.chatbot.src.retriever import search_chunk

def test_retriever_search_chunk():
    chunks = [
        "Copyright registration is optional.",
        "Registration creates a public record.",
        "Patents protect inventions."
    ]
    
    assert search_chunk("registration", chunks) == ["Copyright registration is optional.", "Registration creates a public record."]
    assert search_chunk("PATENTS", chunks) == ["Patents protect inventions."]
    assert search_chunk("trademark", chunks) == []