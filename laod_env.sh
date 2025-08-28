#!/usr/bin/env bash
set -a
if [ -f ".env" ]; then
  source .env
  echo "Environment variables loaded from .env"
else
  echo ".env file not found."
fi
set +a
