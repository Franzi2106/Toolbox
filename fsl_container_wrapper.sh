#!/usr/bin/env bash
# Run FSL commands within the Singularity container configured via
# the FSL_SINGULARITY_IMAGE environment variable. This allows tools
# like FLIRT, BET and RobustFOV to be executed even when FSL is not
# installed natively on the system.

if [ -z "${FSL_SINGULARITY_IMAGE}" ]; then
  echo "FSL_SINGULARITY_IMAGE environment variable not set" >&2
  exit 1
fi

if ! command -v singularity >/dev/null 2>&1; then
  echo "singularity executable not found on PATH" >&2
  exit 1
fi

exec singularity exec "$FSL_SINGULARITY_IMAGE" "$@"
