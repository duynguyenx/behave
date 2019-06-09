# Behave UI Testing

## Repo Structure

```sh
tests/
├── behave
│   ├── browser      //< create webdrivers instances
│   ├── conf         //< configuration files (users, constants, config, etc)
│   ├── features     //< test automation home folder (following BDD Style)
│   │   ├── steps   //< python steps implementation files for the scenarios
│   │   ├── environment.py  //< global hooks for test script
│   ├── helpers      //< helpers of testing framework
│   ├── pageobjects  //< page container (following the page object pattern)
│   ├── resources    //< store files related to the framework (browser drivers, json config files, ...)
│   └── requirements.txt //< store libraries for the testing framework
```

## Getting Started

This is the quick and easy getting started assuming you already have git and pip installed.

```sh
# navigate into the tests/behave directory

cd tests/behave

# Create a virtual environment to run Behave tests (optional)
Follow directions mentioned in https://www.jetbrains.com/help/pycharm/2016.2/creating-virtual-environment.html

# If you don't have python 3
brew install python3

# Set env variable for Python 3 path
echo "export PYTHONPATH=/usr/local/lib/python3.6" >> ~/.bashrc

# Install the required items
sudo pip install -r requirements.txt

# Download and extract the latest [chrome-driver](http://chromedriver.storage.googleapis.com/index.html), then copy that to:
resources/<chrome-driver-file>

# to run all the test scenarios:
behave

# to run scenarios with specific tags:
behave -k --tags id-1
```

## Behave Test Runner

Behave supports several [command-line arguments](https://behave.readthedocs.io/en/latest/behave.html) that you can use for your convenience, like so:

```sh

# If you want behave to not display snippets/source
behave -q, –quiet

# If you want behave to stop running at the first failure
behave -stop

# Only execute features or scenarios with specific tags
behave -t, -tags

# Do not display skipped tests to avoid noises
behave -k

# Specify a formatter for behave to display
behave -f, -format
```

#### Tags

Tags are a great way to organize features and scenarios. A scenario or feature can have as many tags as you like, just separate them with spaces. To understand more about tags please see [Controlling things with tags](https://behave.readthedocs.io/en/latest/tutorial.html#controlling-things-with-tags).

## IDE

### PyCharm

We prefer to use the new [PyCharm](https://www.jetbrains.com/pycharm/) 
For working in PyCharm, I would also recommend:

* [Setup, Configure and Execute Behave](http://blog.jetbrains.com/pycharm/2014/09/feature-spotlight-behavior-driven-development-in-pycharm/)

