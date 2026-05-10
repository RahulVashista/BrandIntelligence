#!/usr/bin/env bash
set -euo pipefail

echo "[*] Starting BrandIntelligence with legacy Docker build compatibility..."
export DOCKER_BUILDKIT=0
export COMPOSE_DOCKER_CLI_BUILD=0

if command -v docker-compose >/dev/null 2>&1; then
  docker-compose up --build
else
  docker compose up --build
fi
