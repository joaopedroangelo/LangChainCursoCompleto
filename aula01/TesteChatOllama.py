from langchain_ollama import ChatOllama

chat = ChatOllama(model="llama3.2:1b")

response = chat.invoke("Conte uma piada.")

print(response.response_metadata)  # Dicionário com informações adicionais
