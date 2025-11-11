#!/usr/bin/env bash
set -e
# ativa venv local (usuário cria venv local)
source venv/bin/activate || true
python -m src.application
