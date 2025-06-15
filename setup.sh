# code to install dependencies for latex.
# you may need to run this vefore
# executing this script: chmod +x setup.sh


#!/bin/bash

# Name of the script to check
SCRIPT_NAME="laton"

# Check if the script exists and is executable
# -x returns true if file is executable
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

# Function to check and install required packages
# -s is true if the file exists and is not empty
# dpkg is the package directory
install_if_missing() {
    PKG_NAME=$1
    if ! dpkg -s "$PKG_NAME" &> /dev/null; then
        echo "Package '$PKG_NAME' is not installed. Installing..."
        sudo apt-get update
        sudo apt-get install -y "$PKG_NAME"
    else
        echo "Package '$PKG_NAME' is already installed."
    fi
}

# Check for required packages
install_if_missing "bzip2"
install_if_missing "ca-certificates"
install_if_missing "micro"
install_if_missing "python3"
install_if missing "pip"
install_if_missing "python3-venv"


# starts up the python virtual environment
#!/bin/bash

VENV_DIR="venv"
REQ_FILE="requirements.txt"

# Step 1: Create the virtual environment if needed
# -f is true if the file exists and is neither a directory
# or spexial service
if [ ! -f "$VENV_DIR/bin/activate" ]; then
    echo "Virtual environment not found. Creating..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment."
        exit 1
    fi
fi

# Step 2: Activate the virtual environment
echo "Activating virtual environment..."
# Note: This must be sourced to persist in current shell if run directly
source "$VENV_DIR/bin/activate"

# Step 3: Install dependencies if requirements.txt exists
if [ -f "$REQ_FILE" ]; then
    echo "Installing dependencies from $REQ_FILE..."
    pip install --upgrade pip
    pip install -r "$REQ_FILE"
else
    echo "No $REQ_FILE file found. Skipping dependency installation."
fi

# Optional: Confirm environment setup
echo "Environment setup complete."
python --version
pip list
