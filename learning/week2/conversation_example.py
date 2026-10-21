history = []

def add_message(role: str, content: str):
    history.append({
        "role": role,
        "content": content
    })

add_message("user", "My favorite color is blue")
add_message("assistant", "Got it!")
add_message("user", "What is my favorite color?")

for message in history:
    print(message)
    