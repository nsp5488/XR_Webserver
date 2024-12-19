# Usage

## Running Locally

### Note: This application will only run on Linux / OSX based systems since poppler is not supported on Windows

- Generate a virtual environment

```[bash]
python -m venv <your_venv_name>
source <your_venv_name>/bin/activate
pip install -r requirements.txt
```

- Run the application:
  `python webserver.py`
- Navigate to <http://127.0.0.1:5000> to access the upload page
- <http://127.0.0.1:5000/uploads/><code\> returns a JSON containing the number of slides in the presentation
- <http://127.0.0.1:5000/uploads/><code\>?index={N} returns the Nth slide of the presentation

## Building as a Docker Container

- Building this as a Docker container enables the service to run on any operating system:

- Build the container: `docker build -t <container_name>:latest .`
- To run the container locally execute `docker run -it -p 0.0.0.0:8000 -v <volume-name> <container_name>:latest` where volume-name can be a custom volume that is declared elsewhere, or a temporary volume with any name.

## Deploying Container to a hosting provider

- To push the container to a hosting provider (e.g. GCP or AWS) build the container with the appropriate name for the instance that you're building to (Google Cloud run using the Artifact Registry with Google Cloud Storage mounted as a volume is convenient, for AWS offerings Elastic Container Services with an S3 bucket mounted as a volume is a popular alternative).

- Get the appropriate tag for your container, then execute `docker push <container_name>:latest`
