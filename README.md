# chatgpt-python
Um código base para realizar consultas ao ChatGPT utilizando o Python.

O arquivo Python disponibilizado nesse repositório, cria uma espécie de assistente virtual realizando requisições
pela API da OPENAI, e retornando o resultado questionado pelo usuário.

Favor acessar diretamente as orientações disponibilizadas pela OPENAI, pois existem muitos parâmetros que não foram
utilizados neste projeto, e que podem ser muito úteis na tomada das requisições.

Importações: 
Fiz a importação de 3 bibliotecas principais:
- openai (Nativa do ChatGPT).
- pyttsx3 (Biblioteca para gerar o aúdio apartir de um texto)
- speech_recognition (Biblioteca para reconhecer os comandos de voz)

![1](https://github.com/czkni/chatgpt-python/assets/127226763/990c517e-66fc-40b7-b509-94de63bf2ea1)

Definição de chave de API:
Para conseguir enviar as requisições pela API é necessário localizar sua chave, que está disponível no seu perfil (Conforme
imagem abaixo).

1) https://platform.openai.com/account/api-keys -> Link de acesso.
2) Cria uma chave secreta conforme print abaixo:

 ![3](https://github.com/czkni/chatgpt-python/assets/127226763/3db4cdef-be96-4c2b-a540-6aa689e254a3)
 
3) Após gerar a chave, substituir no seguinte trecho do código:
![2](https://github.com/czkni/chatgpt-python/assets/127226763/ab18670a-66d7-4546-b8d4-5d6cd4d7b335)

Parâmetros:
Ao enviar a requisição pela API, é necessário passar alguns parâmetros juntamente:
- Engine: Modelo de geração de texto.
- Prompt: Solicitação de texto do usuário.

![parametros](https://github.com/czkni/chatgpt-python/assets/127226763/c9ff8f5d-6389-4040-b9c0-5d1846fe2e13)

Feito, já é possível utilizar o código disponibilizado acima para realizar solicitações diretamente ao ChatGPT.

https://github.com/czkni/chatgpt-python/assets/127226763/06553f03-2a28-4289-8e5c-39a0c40e56c8

Espero que este código te ajude de alguma forma!

