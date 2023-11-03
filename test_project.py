from project import ChatGPT, initpyttsx3, readOutPut, save_voice_output
from pathlib import Path

def test_initpyttsx3():
    if initpyttsx3() == None:
        print("Error in initpyttsx3 library")
    
def test_readOutPut():
    #checking that whether pyttsx3 library reading output correctly or not
    assert readOutPut(initpyttsx3(),"hello world") == None
    assert readOutPut(initpyttsx3(),"CS50") != "CS50"
    assert readOutPut(initpyttsx3(),"Hello this was CS50 ") == None
    
def test_save_voice_output():
    #testing existing file
    first_file_name = 'file1.mp3'
    save_voice_output(initpyttsx3(),"hello world",first_file_name)
    first_file_path = Path(first_file_name)
    if first_file_path.exists():
        print(f"{first_file_name} is exist")
    #testing not existing file
    second_file_name = 'file2.mp3'
    second_file_path = Path(second_file_name)
    if second_file_path.exists():
        print(f"{second_file_name} is exist")
    else:
        print(f"{second_file_name} is not exist")
   