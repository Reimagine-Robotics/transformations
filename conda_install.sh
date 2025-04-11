#!/bin/bash

# Script to create a conda environment with:
# -  Python 3.10
# -  transformations (editable install)
#
# Usage:
#   ./conda_install.sh
# This script assumes that conda is already installed and available in the PATH.
# Check if conda is installed with:
#   conda --version
#
# This script can be used to create a conda env for local development or testing.

ENV_NAME="transformations_env"
YAML_FILE="transformations_env.yaml"

# Create the conda environment
if conda env update -p "$ENV_NAME" --file "$YAML_FILE" --prune; then
  echo "Conda environment '$ENV_NAME' with Python 3.10 created successfully."
else
  echo "Failed to create conda environment '$ENV_NAME'."
  exit 1
fi
