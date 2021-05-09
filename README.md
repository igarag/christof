<h1 align="center">
  <img src="./docs/christof-logo.png" alt="Christof" width="200">
  <br>
  Christof
  <br>
</h1>
Mini home surveillance project using a simple webcam.


[:es:](./README_ES.md) · [:gb:](./README.md)

## Install

- Vía poetry:

  ```bash
  poetry install
  ```

   *Note: For more information on the Poetry dependency manager visit [its documentation](https://python-poetry.org/docs/). The installation of the library can be done with the following command:*

    ```bash
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```

- Via requirements:

  ```bash
  pip install -r requirements.txt
  ```


## Run server

```bash
uvicorn app.main:app --reload 
```

## Future lines

- [ ] GPU access
- [ ] Jetson Nano full compatibility
- [ ] Full control of service using Telegram Bots
- [ ] Admin panel?