""" from langchain.llms import OpenAI

# Abrir o ficheiro e ler o conteudo
def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
# Inicializar o modelo da OpenAI
gpt3 = OpenAI(api_key='')

# Definir uma funcao para pedir uma resposta da OpenAI 
def get_response(prompt):
    return gpt3(prompt)

# Ler os dados do txt
file_path = 'data.txt'
external_data = read_data_from_file(file_path)

# Obter resposta do GPT-3 e mostrar
prompt = f"Based on the following data: {external_data}, what TV show is this about?"

print("Resposta:", get_response(prompt)) """

from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

import getpass
import os

from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
  raise ValueError("A chave da OpenAI não foi encontrada. Verifique seu arquivo .env.")

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"])

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

model.invoke(messages)