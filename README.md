# Raspberry Pi Hello World

A minimal Python web app that serves `Hello, world!` and is packaged as a Docker
image for 64-bit Raspberry Pi operating systems (`linux/arm64`).

## Run locally

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open <http://localhost:8080>.

## Build and run the container

```bash
docker build -t hello-pi .
docker run --rm -p 8080:8080 hello-pi
```

## GitHub Actions

The workflow in `.github/workflows/build-image.yml` runs on pushes to `main` and
can also be started manually. It builds and publishes a `linux/arm64` image to
GitHub Container Registry:

```bash
docker pull ghcr.io/OWNER/REPOSITORY:latest
docker run --rm -p 8080:8080 ghcr.io/OWNER/REPOSITORY:latest
```

Replace `OWNER/REPOSITORY` with the GitHub repository path. The Raspberry Pi
must run a 64-bit OS to use this image.
