# Plate Scanner app

# Overview
[Kivy](https://kivy.org/doc/stable/) application using [Camera4Kivy](https://github.com/Android-for-Python/Camera4Kivy) library to get images from the Android camera. Analyzes image using OpenCV, detects plate code and decrypts it

Available only on Android devices

# For developers
You should work on Mac OS or Linux. If you are running on Windows, you need to install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

## Installation
Clone repo to local computer
```
git clone https://github.com/Befrimon/Plate-Scanner.git
cd Plate-Scanner
```

Create and activate virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```

Install required dependencies
`python -m pip install -r requirements.txt`

## Run
Build and run the application using buildozer. The first build may take a long time
```
python -m buildozer -v android debug
python -m buildozer android deploy run logcat | grep python
```


