#!/bin/bash
#
# Bootstrap virtualenv environment and requirements locally
#
# NOTE: This script expects to be run from the project root with
# ./bootstrap.sh

set -o pipefail

if [ ! $VIRTUAL_ENV ]; then
  virtualenv -p python3 ./venv
fi

venv/bin/pip install "pip>=8.0"

venv/bin/pip install -r requirements.txt
