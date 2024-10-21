# Usage
* Activate the virtual environment in the server/ directory:
```source ./server/bin/activate```
* Run the application:
```python webserver.py```
* Navigate to http://127.0.0.1:5000 to access the upload page
* http://127.0.0.1:5000/uploads/<code> returns a JSON containing the number of slides in the presentation
* http://127.0.0.1:5000/uploads/<code>?index={N} returns the Nth slide of the presentation
