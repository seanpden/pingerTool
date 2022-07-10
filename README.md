*Table of Contents:*

- [About the Project](#about-the-project)
	- [Built With](#built-with)
- [Getting Started](#getting-started)
	- [Prerequisites](#prerequisites)
	- [Installation](#installation)
- [Usage](#usage)
	- [Documentation](#documentation)
		- [Getters, Setters](#getters-setters)
		- [Functional methods](#functional-methods)
- [Roadmap/TODO](#roadmaptodo)

## About the Project
This is a simple tool I've built to track downtime on my local network. It pings to google (command can be changed with included methods) and logs any downtime with a timestamp in a named txt file (LOGGER.txt).

### Built With
- [Python](https://www.python.org)

## Getting Started
To get a local copy up and running, follow these steps.

### Prerequisites
You must have Python installed on your system. Preferably the most recent version.

### Installation
Download the repository OR
Clone the repository:
```sh
git clone <REPO>
```

## Usage
This project is meant to be altered and expanded based on user's custom case. You can either use the premade driver file (CD into folder, type "python3 pingerDriver.py") or you can start the command line python interpreter and run any additional methods. To quit continuous ping, press "CONTROL + C". Here is an example of running the same commands that are in the driver file then quitting by using the interpreter:
```sh
> python3
>>> import pinger
>>> variable = pinger.Pinger()
>>> variable.run()
>>> quit()
```

### Documentation
#### Getters, Setters
- getCMD(): gets the current command line command being used
- setCMD(cmd): sets the current command line command to use, format | cmd = ['cmd', 'cmd', ...]
- getOS(): gets the current operating system
- setOS(os): sets the current operating system, defaults to windows
- getMessages(): gets the current messages status
- setMessages(messages): sets the current messages status, True to show ALL messages in the console, false to just log downtime

#### Functional methods
- getAllResults(): prints and returns all console outputs
- getBadResults(): writes to file downtime (Currently records only if "bytes" doesn't appear in console output. Need to change to more accurately reflect console return)
- logger(): Inputs cmd to console, formats and writes downtime to file

## Roadmap/TODO
- [ ] fix redundency of logger() and getBadResults() methods
- [ ] refactor
- [ ] add additional functionality
- [ ] auto-detect OS and instatiate appropriate command
- [ ] add better output detection, currently records downtime only if "bytes" doesn't appear in console output