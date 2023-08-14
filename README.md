# Game Bot Project 🎮🤖

The Game Bot Project is a machine learning-based bot that plays a game using the BizHawk emulator. The bot uses trained AI models to make strategic decisions within the game environment.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Training the AI Model](#training-the-ai-model)
- [Customizing the Bot](#customizing-the-bot)
- [API Details](#api-details)
- [Contributing](#contributing)

## Introduction 🌟

This project demonstrates the integration of machine learning with retro gaming. The bot interacts with the BizHawk emulator, receiving game states and predicting optimal actions based on AI models. It is designed for educational purposes and challenges participants to develop a bot that can play the game effectively.

## Prerequisites/Dependencies 📋

- Operating System: Windows 7 or above (64-bit)
- Python 3.6.3 or later 🐍
- BizHawk emulator (pre-requisites included in the attached zip)
- Street Fighter II Turbo (U).smc game ROM
- Necessary dependencies listed in the import statements of each script 📦

## Installation 💻

1. Clone or download this repository to your local machine.
2. Install the required dependencies using the following command:
3. pip install -r requirements.txt

## Usage 🚀

1. Start the BizHawk emulator and load the game ROM (Street Fighter II Turbo (U).smc).
2. For single-player mode, open the `single-player` folder; for two-player mode, open the `two-players` folder.
3. Run EmuHawk.exe and open the Tool Box from the Tools dropdown.
4. Follow the instructions in the provided documentation to execute the API code using the command prompt: python controller.py 1
5. Select your character(s) in the game and initiate the connection with the bot by clicking on the Gyroscope Bot icon.
6. The bot will make decisions based on the AI model and interact with the game.

## Components 🧩

The project consists of the following components:

- `controller.py`: The main script that communicates with the BizHawk emulator, establishing a connection with the game. It takes command-line arguments to control player 1 or 2.
- `Buttons.py`: Defines the Button class representing the SNES gamepad buttons.
- `Player.py`: Contains the Player class representing player attributes and actions.
- `GameState.py`: Defines the GameState class representing the game state.
- `Command.py`: Contains the Command class representing the command passed to the game.
- `Controller.py`: Contains the socket connection and communication logic.

## Training the AI Model 🤖🧠

1. Implement the `fight` function in the `bot.py` or `Bot.java` file. This function takes a `GameState` object and a player identifier as inputs. Use the provided information to set buttons in the `Command` object for the next time instance.
2. Generate a dataset by playing single-player mode, recording percepts and actions in a CSV file. This dataset will be used for training the AI model.
3. Train the AI model using the dataset and implement your bot's decision-making logic.

## Customizing the Bot 🛠️

- Modify the `fight` function in the `bot.py` or `Bot.java` file to adjust your bot's decision-making logic and actions.
- Experiment with different AI algorithms to improve bot performance.

## API Details 📜

Detailed information about the API's components and functionality can be found in the provided documentation. The API offers classes for buttons, players, game states, commands, and the main controller.

## Contributing 🤝

Contributions to this project are welcome! If you have suggestions, improvements, or bug fixes, feel free to fork this repository, make your changes, and submit a pull request.


**Good Luck 🤖🕹️**
