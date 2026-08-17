from langchain_groq import ChatGroq

from settings import MODEL_ID


model = ChatGroq(
    model=MODEL_ID,
    temperature=0
)


response = model.invoke(
    "In one sentence, explain what a cloud data platform is."
)


print("\nGroq model test\n")
print(response.content)