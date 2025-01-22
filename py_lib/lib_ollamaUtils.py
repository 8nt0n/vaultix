import ollama
import subprocess
import time


model_name = "llama3.2:1b"


def ollama_init():
    try:
        server_process = subprocess.Popen(["ollama", "serve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Ollama server is starting...")

        # Give the server some time to initialize
        time.sleep(5)

        # Check if the server is running (optional)
        import requests
        try:
            response = requests.get("http://localhost:11434")
            print(response.status_code)
            if response.status_code == 200:
                print("Ollama server is running.")
                return 1
            else:
                print("Ollama server is offline")
                return 1
        except requests.ConnectionError:
            print("Unable to connect to Ollama server.")
            return -1


    except Exception as e:
        print(f"An error occurred: {e}")


# 
# 
# 

def ollama_prompt(file):
    response =  ollama.chat(model=model_name, messages=[
        
        {"role": "user", "content" : 'Given the file: "Parasite.2019.1080p.BluRay.x264.AC3-KR.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Parasite"},

        {"role": "user", "content": 'Thats a Perfect Answer keep going like that! Given the file: "La.La.Land.2016.1080p.BluRay.x264.DD5.1.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "La La Land"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "El.Laberinto.Del.Fauno.2006.720p.BluRay.x264.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "El Laberinto Del Fauno"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Das.Leben.der.Anderen.2006.1080p.BluRay.DTS.x264.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Das Leben der Anderen"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Cidade.de.Deus.2002.1080p.BluRay.x264.PT.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Cidade de Deus"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Léon.Le.Professionnel.1994.1080p.BluRay.x264.FR.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Léon Le Professionnel"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "The.Dark.Knight.2008.1080p.BluRay.x264.DTS.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "The Dark Knight"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Forrest.Gump.1994.720p.BluRay.x264.ENG.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Forrest Gump"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Amélie.2001.720p.BluRay.x264.FR.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Amélie"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Spirited.Away.2001.1080p.BluRay.x264.DTS.JP.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Spirited Away"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Pulp.Fiction.1994.1080p.BluRay.DTS.x264.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Pulp Fiction"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Intouchables.2011.1080p.BluRay.x264.FR.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Intouchables"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Oldboy.2003.1080p.BluRay.x264.KR.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Oldboy"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Crouching.Tiger.Hidden.Dragon.2000.1080p.BluRay.x264.CH.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Crouching Tiger Hidden Dragon"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Life.is.Beautiful.1997.1080p.BluRay.x264.IT.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Life is Beautiful"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Schindlers.List.1993.1080p.BluRay.x264.DD5.1.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Schindler's List"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Joker.2019.1080p.BluRay.DD5.1.x264.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Joker"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "La.Haine.1995.720p.BluRay.x264.FR.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "La Haine"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "Rashomon.1950.720p.BluRay.x264.JP.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Rashomon"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "A.Separation.2011.1080p.BluRay.x264.IR.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "A Separation"},
    
        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "krabat.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Krabat"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "das boot.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Das Boot"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "goodfellas.mp4", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Goodfellas"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "der name der rose.avi", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Der Name der Rose"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "die welle.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Die Welle"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "fight club.mp4", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Fight Club"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "schindlers liste.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Schindlers Liste"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "arrival.mp4", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Arrival"},

        {"role": "user", "content" : 'Thats a Perfect Answer keep going like that! Given the file: "die_unendliche_geschichte.mkv", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'},
        {"role": "assistant", "content": "Die unendliche Geschichte"},

        {"role": "user", "content": f'Given the file: "{file}", extract the movie name only. Take into account that the movie name may be in a different language, so only focus on removing the meta information from the title. The title of the movie ALWAYS is in the original file name in some shape or form'}
    ])

    #get actual name from ollama
    response = response.get("message", {}).get("content", "No content found")

    return response
