# Automation framework
This is a simple Python code that shows practice testing skills using Selenium, Playwright, API, Appium.
## Install
1. Install Python 3.10 or higher [official website](https://www.python.org/downloads/)
2. Install OpenJDK 17 [official website](https://learn.microsoft.com/ru-ru/java/openjdk/download)

## *For macOS and Linux*
* Make sure [Homebrew](https://brew.sh/) is installed.
* In a terminal, run this command:

Allure:
```bash
brew install allure
```

Android Studio:

```bash
brew install android-studio
```

Android Studio will be installed in the /usr/local/bin folder.

Start Android Studio by typing in the terminal:
```bash
android-studio
```
### Warning
**Phone model and android version used for tests ->** Pixel 8 API 30(Android 11.0("R") | x86
## *For Windows*

Allure:
* Make sure [Scoop](https://scoop.sh/) is installed
* Make sure Java version 8 or above installed, and its directory is specified in the `JAVA_HOME` environment variable.
* In a terminal, run this command:
```bash
scoop install allure
```
Android Studio:

Here is the entire process of installing Android Studio, setting up environment variables, and setting up the driver for mobile testing:
https://appium.io/docs/en/2.0/quickstart/uiauto2-driver/

### Warning
**Phone model and android version used for tests ->** Pixel 8 API 30(Android 11.0("R") | x86

3. Clone the repository 
```bash
git clone https://github.com/Matterlinkk/automation_framework
```
4. Go to the project directory
```bash
cd automation_framework
```
5. Install the required packages
```bash
pip install -r requirements.txt
```
6. Run the script
```bash
pytest -v -s
```

## Usage
There are two use cases:
1. Run tests without generating an allure report
```bash
pytest -v -s
```   
2. Run tests with generating an allure report
```bash
pytest -v -s --alluredir allure-reports
```
After the tests are completed, run the created report
```bash
allure serve allure-reports
```
