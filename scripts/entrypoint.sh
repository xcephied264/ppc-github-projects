#!/usr/bin/env bash
set -euo pipefail

cd "${GITHUB_WORKSPACE:-/github/workspace}"

echo "Starting PPC To-Do CI/CD Pipeline"

echo "Running Python unit tests..."
python todo-test.py

echo "Updating index.html..."
bash scripts/update_index.sh "Passed"

if [ -f "index.html" ]; then
    echo "index.html generated successfully."
else
    echo "Error: index.html was not generated."
    exit 1
fi

echo "CI/CD Pipeline completed successfully."