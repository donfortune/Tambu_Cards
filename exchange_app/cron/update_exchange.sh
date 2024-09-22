#!/bin/bash

# Define paths to your project and virtual environment
PROJECT_DIR="/Users/mac/Tambu_Cards/"        # Update this with your actual project path
VENV_DIR="/Users/mac/Tambu_Cards/venv"        # Update this with the path to your virtual environment
LOG_FILE="$PROJECT_DIR/cron/cron.log"      # Log file to capture any output/errors

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Navigate to the project directory
cd "$PROJECT_DIR"

# Run the Django management command to update exchange rates
python manage.py update_exchange_rate >> "$LOG_FILE" 2>&1
