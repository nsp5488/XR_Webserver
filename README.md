# Usage

* Activate the virtual environment in the server/ directory:
```source ./server/bin/activate```[bash]
* Run the application:
```python webserver.py``[bash]
* Navigate to <http://127.0.0.1:5000> to access the upload page
* <http://127.0.0.1:5000/uploads/><code\> returns a JSON containing the number of slides in the presentation
* <http://127.0.0.1:5000/uploads/><code\>?index={N} returns the Nth slide of the presentation

```[bash]

docker build -t us-central1-docker.pkg.dev/xr-image-server/xr-webserver/image:latest . && \
docker push us-central1-docker.pkg.dev/xr-image-server/xr-webserver/image:latest

```
