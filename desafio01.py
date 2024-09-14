import openai;
from dotenv import load_dotenv, find_dotenv

_= load_dotenv(find_dotenv())


client = openai.Client()



resposta = client.chat.completions.create(
    messages=userMsg,
    model="gpt-3.5-turbo",
    max_tokens=1000,
    temperature=0
)
for stream_resposta in resposta:
    texto = stream_resposta.cho
    print(texto)
    # print(resposta.choices[0].message.content)
    # userMsg.append(resposta.choices[0].message.model_dump(exclude_none=True))
    # return userMsg

    
user_input = input("Digite sua mensagem: ")
conversation = [{'role': 'user', 'content': user_input}]    

geracao_texto(conversation)