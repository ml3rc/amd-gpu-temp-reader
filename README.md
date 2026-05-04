# amd-gpu-temp-reader

A small Flask API for reading AMD GPU temperatures on Linux systems via `/sys/class/drm`.

## Overview

This project exposes a REST endpoint that returns the temperature of AMD GPUs found under `/sys/class/drm/card*/device/hwmon/hwmon*/temp1_input`.

## Requirements

- Linux with AMD GPU drivers
- Docker compose

## Run with Docker

Build and run the container:

```bash
docker-compose up --build
```

The service will be available on port `5000`.

### Notes

- The container mounts `/sys/class/drm` as read-only so the service can access GPU sensor paths.
- The endpoint returns a JSON object where each key is a DRM card path and each value is the temperature in degrees Celsius.

## API

- `GET /gpu-temp` - returns current AMD GPU temperatures as JSON.
