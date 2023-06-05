## Custom Pylint configuration integration in Pycharm

The assumption is that you already installed the `Pycharm Community Edition`. Else, [download](https://download-cf.jetbrains.com/python/pycharm-community-2017.1.2.exe) and install it.

**Step 1:** Install the pylint python module.

```bash
python -m pip install pylint
```

**Step 2:** Open pycharm. Under `File` -> `Settings`, go for `Tools` -> `External Tools`.

Click '+' button and add content as illustrated in the below screenshot.
![pylint configuration in pycharm](./pylint_integration_into_pycharm.JPG?raw=true "pylint configuration in pycharm")

**Step 3:** Click `ok` and in the settings windows, ensure to click `Apply` before closing the window.

**Step 4:** Copy the `custom_pylintnrc` file and paste it at the below location

```bash
C:\Users\<USER NAME>\.PyCharmCE2017.1\config\tools\custom_pylintnrc
```

_NOTE:_ Though this file can be placed anywhere, I would recommend to place it in the above location.

### Working with pylint in Pycharm

**Step 1:** Go to `Tools` -> `External Tools` -> `pylint`
![Running Pylint](./runningPylint.JPG?raw=true "Running Pylint")

Then, you can observe the output in pycharm console.

Below is the output for the attached `calculator.py` file.

```bash
C:\Python27\Scripts\pylint --rcfile ~\.PyCharmCE2017.1\config\tools\custom_pylintnrc calculator.py
************* Module calculator
C:  8, 0: Invalid argument name "a" (invalid-name)
C:  8, 0: Invalid argument name "b" (invalid-name)
C: 18, 0: Invalid argument name "a" (invalid-name)
C: 18, 0: Invalid argument name "b" (invalid-name)
C: 28, 0: Invalid argument name "a" (invalid-name)
C: 28, 0: Invalid argument name "b" (invalid-name)
C: 38, 0: Invalid argument name "a" (invalid-name)
C: 38, 0: Invalid argument name "b" (invalid-name)

------------------------------------------------------------------
Your code has been rated at 3.85/10 (previous run: 3.85/10, +0.00)
```
