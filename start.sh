#!/bin/bash

echo "Starting the application..."

log_file=logs/$(date '+%Y-%m-%d')_app.log

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a $log_file
}


log "Activating virtual environment..."
python3 -m venv myenv

source myenv/bin/activate

log "Downloading videos"
python3 videodownloader.py 'nextfuckinglevel'






deactivate
log "Deactivating virtual environment..."