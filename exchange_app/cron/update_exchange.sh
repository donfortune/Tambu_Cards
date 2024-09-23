#!/bin/bash

# Define paths to your project and virtual environment
PROJECT_DIR="/Users/mac/Tambu_Cards/exchange_app/"  # Updated to the correct path
VENV_DIR="/Users/mac/Tambu_Cards/venv"               # Update this with the path to your virtual environment
LOG_DIR="$PROJECT_DIR/cron"                           # Directory for the log file
LOG_FILE="$LOG_DIR/cron.log"                          # Log file to capture any output/errors

# Create the log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Navigate to the project directory
cd "$PROJECT_DIR"

# Run the Django management command to update exchange rates
python manage.py update_exchange_rate >> "$LOG_FILE" 2>&1
