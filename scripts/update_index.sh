#!/usr/bin/env bash
set -euo pipefail

STATUS="${1:-Passed}"
UPDATED_BY="${GITHUB_ACTOR:-local-run}"
UPDATED_AT=$(date -u '+%Y-%m-%d %H:%M:%S UTC')

cat > index.html <<EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PPC To-Do Application</title>
</head>
<body>
    <h1>PPC GitHub Projects</h1>
    <h2>To-Do Application</h2>

    <p>Automated Test Status: ${STATUS}</p>
    <p>Updated by: ${UPDATED_BY}</p>
    <p>Last Updated: ${UPDATED_AT}</p>
</body>
</html>
EOF

echo "index.html updated successfully."