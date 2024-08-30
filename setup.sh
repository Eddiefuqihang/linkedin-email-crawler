#!/bin/bash

# Install required Python packages
pip install -r requirements.txt

# Install ChromeDriver (for macOS)
brew install --cask chromedriver

echo "Setup complete. Make sure to place your Connections.csv file in the same directory as myprogram.py before running the script."
