## Getting started

1. Create a virtual environment using the below command and activate it

```bash
python -m venv env && source env/bin/activate
```

2. Install Django, daphne and channels

```bash
pip install django daphne channels
```

3. Set the large file path in `settings.py` in the `LARGE_FILE_PATH` variable

4. Start the Websocket server using Daphne

```bash
daphne core.asgi:application --port 8000
```

5. Open the `index.html` file in your web browser, or if your using VS Code you can launch it using the [Live server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension and test the functionality.