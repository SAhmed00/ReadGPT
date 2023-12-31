# Required modules
import sys, openai, pyttsx3, time


# Main function
def main():
    userprompt = [{"role": "user", "content": "Introduce your self!"}]
    engine = initpyttsx3()
    try:
        while True:
            prompt = input("Write here: ")
            if prompt:
                userprompt.append({"role": "user", "content": prompt})
                ChatGPTResponse = ChatGPT(userprompt)
                for _ in range(1):
                    for eachchar in ChatGPTResponse:
                        time.sleep(0.001)
                        print(eachchar, end="", flush=True)
                    readOutPut(engine, ChatGPTResponse)
                    print()
                    save_voice_output(engine, ChatGPTResponse, "voice_output.mp3")
    except (KeyboardInterrupt, EOFError):
        print()
        sys.exit("Program Exit")


# Chatgpt or openai api function which will handle or integrate chatgpt with this program. This function is almost from openai api playground script
def ChatGPT(prompt):
    openai.api_key = "USE YOUR OPEN AI KEY"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    answer = response.choices[0].message.content
    return answer


# pyttsx3 initiallization function.
def initpyttsx3():
    """FROM PYTTSX3 DOCUMENTATION"""
    engine = pyttsx3.init()
    """RATE"""
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 200)

    """VOLUME"""
    volume = engine.getProperty("volume")
    engine.setProperty("volume", 1)

    """VOICE"""
    voices = engine.getProperty("voices")
    # changing index, changes voices. 1 for female 0 for male.
    engine.setProperty("voice", voices[1].id)
    return engine


def readOutPut(engine, response):
    engine.say(response)
    engine.runAndWait()


def save_voice_output(engine, text, file_name):
    engine.save_to_file(text, file_name)
    engine.runAndWait()


if __name__ == "__main__":
    main()
