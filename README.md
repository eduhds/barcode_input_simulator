# barcode_input_simulator

![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=plastic&logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=plastic&logo=macos&logoColor=F0F0F0)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=plastic&logo=windows&logoColor=white)
[![Built with Devbox](https://jetpack.io/img/devbox/shield_moon.svg)](https://jetpack.io/devbox/docs/contributor-quickstart/)

## Usage

Download from releases.

```sh
# Run json file containing array of codes
# ["code1", "code2", "code3", ...]
python barcode_input_simulator.pyz -f example.json

# Run list of codes
python barcode_input_simulator.pyz -l code1 code2 code3
```

## Development

```sh
devbox shell

pipenv install

python __main__.py -f assets/example.json
```

## Known issues

- Try running with `python3` instead `python` to avoid version and symlink errors.
- On macOS you need to trust your Terminal/IDE apps to solve error: _This process is not trusted! Input event monitoring will not be possible until it is added to accessibility clients._
  - Open **System Preferences > Security and Privacy > Privacy Tab**
  - Select **Accssibility** and **Input monitoring**
  - Click on **+** to add apps

|                                                          |                                                             |
| -------------------------------------------------------- | ----------------------------------------------------------- |
| <img src="assets/macos-accessibility.png" width="300" /> | <img src="assets/macos-input-monitoring.png" width="300" /> |

## Credits

- [moses-palmer/pynput](https://github.com/moses-palmer/pynput)
