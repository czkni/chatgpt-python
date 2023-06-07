import openai
import pyttsx3
import speech_recognition as sr

# Definir a chave da API do OpenAI
openai.api_key = "insira_sua_chave_aqui"

# Inicializar o reconhecimento de voz
r = sr.Recognizer()

# Inicializar a engine de fala
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Selecionar a voz feminina brasileira "pt-br"
for voice in voices:
    if voice.name == 'Microsoft Maria Desktop - Portuguese(Brazil)':
        engine.setProperty('voice', voice.id)
        break

# Loop principal
while True:
    # Pedir um comando por voz ou por texto
    prompt = ""
    while not prompt:
        print("Digite um comando ou diga algo para começar:")
        # Tentar obter um comando por voz
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                prompt = r.recognize_google(audio, language='pt-BR')
                print("Comando de voz reconhecido:", prompt)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Erro ao acessar o serviço de reconhecimento de voz; {0}".format(e))
        # Se não obteve um comando por voz, tentar obter um comando por texto
        if not prompt:
            prompt = input("> ")

    # Verificar se o usuário quer sair
    if prompt.lower() == "sair":
        break

    # Gerar uma resposta
    model_engine = "text-curie-001"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=120,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Obter o texto da resposta
    text = response.choices[0].text.strip()
    print(text)

    # Converter o texto em fala usando pyttsx3
    engine.say(text)
    engine.runAndWait()

# Finalizar a engine de fala
engine.stop()
engine.runAndWait()
