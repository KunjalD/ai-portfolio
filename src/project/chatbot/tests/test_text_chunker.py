
from project.chatbot.src.text_chunker import chunk_text


def test_chunk_text():

    assert chunk_text("abcdefji", 4) == ["abcd", "efji"]
    assert chunk_text("", 3) == []
    assert chunk_text("abcdef", 2, 1) == ["ab", "bc", "cd", "de", "ef"]
    assert chunk_text("abcdefghij", 5, 2) == ["abcde", "defgh", "ghij"]
    try:
        chunk_text("abc", 0)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Chunk size must be a positive integer."

    try:
        chunk_text("abc", 3, -1)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Overlap must be a non-negative integer less than the chunk size."