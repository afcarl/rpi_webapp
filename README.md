# WEB APP

## Configuration
The configuration for this application is done by setting
the following environment variables:

``` bash
export SETTINGS=/full/path/to/config.py
```
This config.py contains the settings that will override default_settings.py. If SETTINGS is not set, the application will only use default_settings.py.

``` bash
export FLASK_APP=rpi_webapp/app.py
```
This application can then be launched from within the root directory.

If the application is to be run in development mode (reloader and debug):
``` bash
export FLASK_ENV=development
```

## Usage

After configuration, the flask app can be launched with:
``` bash
flask run
```




