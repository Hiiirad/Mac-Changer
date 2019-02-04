# Change Mac Address
[![License](http://img.shields.io/:license-mit-blue.svg)](LICENSE)

Hi everybody :)

* There are a lot of reasons to change mac address such as anonymity, sabotage in network etc.
My program will provide a lot of options for you to change your interface(s)'s mac address.
* oui.csv file contains all of standard OUI (Organizationally Unique Identifier) part of a mac address (first half of a mac address or first 24bit of mac address)

## Getting Started
This program will only works on **Linux** systems and I believe it would be work perfectly on Macbooks. My OS is Ubuntu 18.04 and I design this program to run on all debian-based linux systems. The installation process will be different if you use other linux distributions.

## Features:
* Everything in this program is in lowercase. So it is case-insensitive. This program has no problem working with uppercase letters, but output of program is always in lowercase.
- [x] Every interface and mac address that user desire to change will be validate with *Regular Expression (Regex)*.
- [x] Users can decide which interface they want to change (*Wireless or Ethernet*).
- [x] Program can set a completely random mac:
    - This random mac can be just randomly selected from hex characters.
    - Or it can be based on **Standard OUI from IEEE** which you can access it from here ([Text File](http://standards-oui.ieee.org/oui/oui.txt) and [CSV File](http://standards-oui.ieee.org/oui/oui.csv)).
- [x] Original mac address of interfaces will be save at ```/tmp/``` so user can reverse mac address back to normal choose reverse option.
- [x] Commands for apply these changes are different based on kernel version. Program can detect it and run different kind of codes. (Ubuntu 18.04's kernel version is 4.15)
- [ ] *Fuzzy String Matching* for searching in OUIs. There are more than 17K names of organizations with different OUIs which is alot to process and show users to choose from them.

### Prerequisites
```
sudo apt install git
```
```
git clone https://github.com/Hiiirad/Mac-Changer.git
```
### Installing
I prefer using [Anaconda](https://www.anaconda.com/) instead of using [Pip or PyPI](https://pypi.org/), but you decide which is good for you.
 - Using Pip:
    - ```sudo apt install python3-pip```
    - ```pip install pip```
    - ```pip install -r requirements.txt```
 - Using Anaconda: Installation process is completely documented [here](https://docs.anaconda.com/anaconda/install/linux/).

### Upgrading
* Pip:
    ```
    pip install -U pip
    ```
* Anaconda:
    ```
    conda update --all
    ```

### Version check to verify installation
* Pip:
    ```
    pip --version
    ```
* Anaconda:
    ```
    conda --version
    ```

## Usage
If kernel version of your OS is older than 4.15 you should run this program like this:
```
python3 mac-changer.py
```
Otherwise:
```
python mac-changer.py
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
