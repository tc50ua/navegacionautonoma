import speech_recognition as sr

def escuchar_palabras():
    # Crear un objeto reconocedor de voz
    reconocedor = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as source:
        print("Ajustando el ruido. Por favor, espere...")
        reconocedor.adjust_for_ambient_noise(source, duration=5)
        print("Listo para escuchar palabras.")

        while True:
            try:
                # Escuchar la entrada de voz
                audio = reconocedor.listen(source, timeout=5)

                # Reconocer la entrada de voz utilizando Google Speech Recognition
                palabra_dicha = reconocedor.recognize_google(audio).lower()
                print("Palabra dicha: {}".format(palabra_dicha))

            except sr.UnknownValueError:
                print("No se ha entendido la palabra.")
            except sr.RequestError as e:
                print("Error en la solicitud al servicio de reconocimiento de voz; {0}".format(e))

if __name__ == "__main__":
    escuchar_palabras()