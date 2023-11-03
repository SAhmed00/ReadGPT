"""
This script interacts with the OpenAI GPT-3.5 Turbo model to create a chatbot-like conversation with users. It takes user input, sends it to the OpenAI API for processing, and then converts the response into voice output using the pyttsx3 library.

Required Modules:
- sys: Provides access to system-specific parameters and functions.
- openai: The OpenAI API library for interfacing with the GPT-3.5 Turbo model.
- pyttsx3: A text-to-speech library for generating voice output.
- time: Provides time-related functions for controlling speech output.

Main Function (main):
- The `main` function is the entry point of the script.
- It continuously prompts the user for input and interacts with the chatbot.
- User input is sent to the ChatGPT function to obtain a response.
- The response is printed and converted into voice output.

ChatGPT Function:
- The `ChatGPT` function interacts with the OpenAI GPT-3.5 Turbo model.
- It sends a list of messages, including user prompts and chatbot responses, to the model.
- The model generates a response, which is extracted and returned.

Pyttsx3 Initialization Function (initpyttsx3):
- The `initpyttsx3` function initializes the pyttsx3 text-to-speech engine.
- It sets properties for speech rate, volume, and voice type.

Read Output Function (readOutPut):
- The `readOutPut` function converts text into voice using the pyttsx3 engine.
- It reads the response and waits for the speech to finish.

Save Voice Output Function (save_voice_output):
- The `save_voice_output` function saves the voice output to an audio file.

Script Execution:
- The script begins by calling the `main` function when executed.
- It continually prompts the user for input and generates chatbot responses.
- To exit the program, the user can use the keyboard interrupt (Ctrl+C).

Note:
- Limited usage only.
- Make sure to set your OpenAI API key in the `ChatGPT` function.
- Ensure that you have the necessary Python modules installed before running the script.
"""
