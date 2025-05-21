#!/bin/bash
set -e
ZIP_NAME="hukuk-ai.zip"
echo "Creating $ZIP_NAME ..."
zip -r "$ZIP_NAME" . -x '*.git*' 'node_modules/*' 'frontend/node_modules/*' 'frontend/build/*' '*.pyc' '*__pycache__/*'
echo "Archive created: $ZIP_NAME"