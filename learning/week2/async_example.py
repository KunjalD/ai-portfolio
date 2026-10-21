import asyncio

async def fetch_answer(question: str) -> str:
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    return f"Answer to {question}"

async def main():
    answers = await fetch_answer("What is RAG??")
    print(answers)

asyncio.run(main())

