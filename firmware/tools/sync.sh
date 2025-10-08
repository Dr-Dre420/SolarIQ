#!/usr/bin/env bash
set -e
mpremote connect auto fs cp firmware/main.py :main.py
mpremote connect auto fs cp firmware/modules/* :modules/
mpremote connect auto soft-reset

#mpremote
