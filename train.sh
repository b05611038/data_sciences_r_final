#!/bin/bash
if [[ -z "${python3}" ]]; then
  python3 src/training_process.py
else
  python src/training_process.py
fi
