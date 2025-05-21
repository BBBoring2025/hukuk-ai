#!/bin/bash
set -e

# Repo cleanup script
echo "Starting repository cleanup..."

# Calculate initial .git directory size
initial_size=$(du -sh .git | cut -f1)
echo "Initial .git directory size: $initial_size"

# Create/update .gitignore
cat > .gitignore <<'EOG'
# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
dist/
build/

# Python
__pycache__/
*.py[cod]
*.so
*.egg-info/
*.pyd
*.pyc

# Virtual environments
venv/
ENV/
.env
.env.*

# Compiled assets
frontend/build/
backend/**/__pycache__/

# Logs
logs/
*.log

# Project outputs (models, embeddings, data)
vector_db/
ai_components/embeddings/
data/
models/

# Sensitive or confidential data
client_data/
confidential_docs/
private/
secrets.*
keys/
certs/

# IDE / OS files
.DS_Store
*.swp
.idea/
.vscode/

# Test/coverage outputs
coverage/
*.cover
*.py,cover
EOG

echo ".gitignore created/updated."

git add .gitignore

# Paths to remove from git tracking if present
paths_to_remove=(
    "frontend/node_modules"
    "frontend/build"
    "logs"
    ".DS_Store"
)

removed_count=0
for path in "${paths_to_remove[@]}"; do
    if git ls-files --error-unmatch "$path" >/dev/null 2>&1; then
        echo "Removing $path from git tracking..."
        git rm -r --cached "$path"
        ((removed_count++))
    fi
done
# Remove __pycache__ directories and *.pyc files
pycache_files=$(git ls-files | grep "__pycache__" || true)
if [ -n "$pycache_files" ]; then
    echo "$pycache_files" | xargs git rm -r --cached
    ((removed_count+=$(echo "$pycache_files" | wc -l)))
fi

pyc_files=$(git ls-files "*.pyc" || true)
if [ -n "$pyc_files" ]; then
    echo "$pyc_files" | xargs git rm --cached
    ((removed_count+=$(echo "$pyc_files" | wc -l)))
fi

echo "Files/directories removed from tracking: $removed_count"

# Update create_zip.sh script
cat > create_zip.sh <<'EOS'
#!/bin/bash
set -e
ZIP_NAME="hukuk-ai.zip"
echo "Creating $ZIP_NAME ..."
zip -r "$ZIP_NAME" . -x '*.git*' 'node_modules/*' 'frontend/node_modules/*' 'frontend/build/*' '*.pyc' '*__pycache__/*'
echo "Archive created: $ZIP_NAME"
EOS
chmod +x create_zip.sh

git add create_zip.sh

echo "Committing changes..."

git commit -m "Cleanup repository and add automation script" || echo "No changes to commit."

final_size=$(du -sh .git | cut -f1)
echo "Final .git directory size: $final_size"

echo "Cleanup completed."

echo "Initial size: $initial_size"
echo "Final size:   $final_size"
