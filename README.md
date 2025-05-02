# ShellAI: a macOS CLI utility for Google AI
[![homebrew](https://img.shields.io/badge/homebrew-shellai-brightgreen.svg)](https://github.com/MinaRoblox/homebrew-tap)

shellAI, created by me is a very simple Python program
developed using Typer and google-generativeapi.

Here is a valid use of the program:
```sh
shellAI prompt "The opposite of day is" --save-response
```

## Setting up
To set up, first use the apikey command to save your key
locally.

```sh
shellAI apikey {insertkeyhere}
```
Next, choose a model with this command:
```sh
shellAI model --model-choosed {modelname}
```

To view the availible models with your key, use
```sh
shellAI model --list-models
```

# MAKE SURE TO DELETE THE models/ attribute from the model name!


## 🛠 Install via Homebrew

```sh
brew tap minaroblox/tap
brew install shellai
```
