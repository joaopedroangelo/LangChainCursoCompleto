from langchain_ollama import ChatOllama

chat = ChatOllama(model="llama3.2:1b")

sintomas_usuario = input("Quais seus sintomas?\n")
prompt = "Você é um ASSISTENTE MÉDICO ESPECIALIZADO EM DIAGNÓSTICO." + "\n"
prompt += "Ajude o usuário a identificar a causa e sugira ações a serem tomadas." + "\n"
prompt += "Sintomas do usuário: \n"
prompt += sintomas_usuario

print(prompt)
print("Pensando...")
response = chat.invoke(prompt)

print("---------------")
print(response.content)  
