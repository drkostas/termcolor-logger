# Termcolor Logger

[![GitHub license](https://img.shields.io/badge/license-Apache-blue.svg)](https://raw.githubusercontent.com/drkostas/termcolor-logger/master/LICENSE)

## About <a name = "about"></a>

A logger with text formatting using
termcolor. [PYPI Package](https://pypi.org/manage/project/termcolor-logger/releases/)

## Table of Contents

+ [Using the library](#using)
    + [Installing and using the library](#install_use)
    + [Creating a config file](#configuration)
    + [Set the required environment variables](#env_variables)
+ [Manually install the library](#manual_install)
    + [Prerequisites](#configuration)
    + [Install the requirements](#installing_req)
    + [Run the Unit Tests](#unit_tests)
+ [Continuous Integration](#ci)
+ [License](#license)

## Using the library <a name = "using"></a>

### Installing and using the library <a name = "install_use"></a>

First, you need to install the library either using pip:

```shell
$ pip install termcolor_logger
```

Then, import it and use it like so:

```python
from termcolor_logger import ColorLogger

fancy_logger = ColorLogger(logger_name='FancyMain',
                           color='blue',
                           on_color='on_red',
                           attrs=['underline', 'reverse', 'bold'])

ColorLogger.setup_logger(log_path="hi.log", debug=True, clear_log=True)

fancy_logger.info("You can customize the logger like this")
fancy_logger.info("You can customize each log message differently",
                  color="green", on_color="on_white", attrs=[])
```

## Manually install the library <a name = "manual_install"></a>

These instructions will get you a copy of the project up and running on your local machine for
development and testing purposes. See deployment for notes on how to deploy the project on a live
system.

### Prerequisites <a name = "prerequisites"></a>

You need to have a machine with
[anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed and
any Bash based shell (e.g. zsh) installed.

```ShellSession

$ conda -V
conda 4.10.1

$ echo $SHELL
/usr/bin/zsh

```

### Install the requirements <a name = "installing_req"></a>

All the installation steps are being handled by
the [Makefile](https://raw.githubusercontent.com/drkostas/termcolor-logger/master/Makefile). First,
create a file called `~/.pypirc` with your pypi login details, as follows:

```
[pypi]
username = your_pypi_username
password = your_pypi_password
```

Then, modify the python version and everything else you need in
the [settings.ini](https://raw.githubusercontent.com/drkostas/termcolor-logger/master/settings.ini).

Finally, execute the following commands:

```ShellSession
$ make create_env
$ conda activate termcolor_logger
$ make release
```

## License <a name = "license"></a>

This project is licensed under the MIT License - see
the [LICENSE](https://raw.githubusercontent.com/drkostas/termcolor-logger/master/LICENSE) file for
details.

<a href="https://www.buymeacoffee.com/drkostas" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>