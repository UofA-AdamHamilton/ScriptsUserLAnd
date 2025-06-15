# code to install dependencies for latex.
# you may need to run this vefore
# executing this script: chmod +x setup.sh


#!/bin/bash

# Name of the script to check
SCRIPT_NAME="laton"

# Check if the script exists and is executable
if [ -x "./$SCRIPT_NAME" ]; then
    echo "LaTeX Online editor ('$SCRIPT_NAME') is already installed."
else
    echo "LaTeX Online editor ('$SCRIPT_NAME') not found. Installing..."
    # Download and set permissions
    curl -L https://raw.githubusercontent.com/aslushnikov/latex-online/master/util/latexonline > "$SCRIPT_NAME"
    chmod 755 "$SCRIPT_NAME"
    
    # Confirm installation
    if [ -x "./$SCRIPT_NAME" ]; then
        echo "'$SCRIPT_NAME' successfully installed."
    else
        echo "Installation failed. Please check your internet connection and permissions."
        exit 1
    fi
fi


sudo apt update
sudo apt install --reinstall ca-certificates
sudo update-ca-certificates

sudo apt update
sudo apt install bzip2

