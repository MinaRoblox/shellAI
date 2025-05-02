import typer
import google.generativeai as genai
import os
from typing import Optional
import time

app = typer.Typer()

homedir = os.path.expanduser('~')
foldersave = "shellAISaves"
promptModel = "{homedir}/{foldersave}/model.txt"

@app.command()
def apiKey(key: str):
    with open(f"{homedir}/{foldersave}/apiKey.txt", "w") as apiKeySaver:
        apiKeySaver.write(key)

    print(f"Your Google Generative API key has been saved in {homedir}/{foldersave}/apiKey.txt")

    pass

class Debug():
    debugmode = False
    
    def log(text):
        if Debug.debugmode == True:
            print(text)

@app.command()
def prompt(prompt: str, save_response: Optional[bool] = False):
    # Check if apiKey exists
    apiKeyPath = f"{homedir}/{foldersave}/apiKey.txt"
    if os.path.exists(apiKeyPath):
        pass
    else:
        print("You need to use the apikey command first before using this one!")
        exit(1)

    # Check if apiKey is a valid key
    with open(apiKeyPath, "r") as apiKeyFile:
        key = apiKeyFile.read()
        Debug.log(key)

    try:
        genai.configure(api_key=key)
        Debug.log("The key was configured!")

        # Initialize the model
        with open(f"{homedir}/{foldersave}/model.txt", "r") as modelsaver:
            modelname = modelsaver.read()
            Debug.log("Model name was gotten.")
        model = genai.GenerativeModel(modelname)
        Debug.log("Model was inserted.")

        # Generate text with a prompt
        response = model.generate_content(prompt)
        print(response.text)

        if save_response == True:
            with open(f"{homedir}/{foldersave}/response.md", "w") as responsesaver:
                responsesaver.write(response.text)

            print(f"Your response was saved in {homedir}/{foldersave}/response.md")                

    except:
        print("The key you inserted in the 'apikey' command is an invalid one.")
        exit(1)
    

    pass

@app.command()
def model(model_choosed: str = None, list_models: Optional[bool] = False):
    if model_choosed == None and list_models == True:
        # Check if apiKey is a valid key
        apiKeyPath = f"{homedir}/{foldersave}/apiKey.txt"
        with open(apiKeyPath, "r") as apiKeyFile:
            key = apiKeyFile.read()
            Debug.log(key)

            genai.configure(api_key=key)
            Debug.log("The key was configured!")
        
        # Set your API key
        genai.configure(api_key=key)

        # List available models
        models = genai.list_models()

        # Print available models and their info
        for model in models:
            if "generateContent" in model.supported_generation_methods:
                print(f"Name: {model.name}")
                print(f"Description: {model.description}")
                print(f"Input Token Limit: {model.input_token_limit}")
                print(f"Output Token Limit: {model.output_token_limit}")
                print("=" * 40)

    if model_choosed and list_models == True:
        print("Listing models and choosing a model can't be done at the same time.")
        print("Please delete the list_models option.")
        time.sleep(3)
        # Check if apiKey is a valid key
        apiKeyPath = f"{homedir}/{foldersave}/apiKey.txt"
        with open(apiKeyPath, "r") as apiKeyFile:
            key = apiKeyFile.read()
            Debug.log(key)

            genai.configure(api_key=key)
            Debug.log("The key was configured!")
        
        # Set your API key
        genai.configure(api_key=key)

        # List available models
        models = genai.list_models()

        # Print available models and their info
        for model in models:
            if "generateContent" in model.supported_generation_methods:
                print(f"Name: {model.name}")
                print(f"Description: {model.description}")
                print(f"Input Token Limit: {model.input_token_limit}")
                print(f"Output Token Limit: {model.output_token_limit}")
                print("=" * 40)

    if model_choosed and list_models == False:
        apiKeyPath = f"{homedir}/{foldersave}/apiKey.txt"
        with open(apiKeyPath, "r") as apiKeyFile:
            key = apiKeyFile.read()
            Debug.log(key)

            genai.configure(api_key=key)
            Debug.log("The key was configured!")
        genai.configure(api_key=key)
        # List available models
        models = genai.list_models()

        # Print available models and their info
        modellist = []
        for model in models:
            if "generateContent" in model.supported_generation_methods:
                modelname = model.name.replace("models/", "")
                modellist.append(modelname)

        Debug.log(modellist)

        if model_choosed in modellist:
            with open(f"{homedir}/{foldersave}/model.txt", "w") as modelsaver:
                modelsaver.write(model_choosed)

        else:
            print("Please enter a valid model from the google-generativeapi using --list-models")


if __name__ == "__main__":
    app()