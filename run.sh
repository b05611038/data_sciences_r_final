#!/bin/bash
if [[ -z "${python3}" ]]; then
  python3 src/main.py
else
  python src/main.py
fi
