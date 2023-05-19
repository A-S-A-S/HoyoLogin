# HoyoLogin

HoyoLogin is a straightforward Python script for claiming rewards from Hoyoverse games. It aims to provide a simple and efficient solution without excessive dependencies, convoluted code, or over-engineered user interactions.

## Requirements

- Python
- requests library (can be installed via `pip install requests`)

## Getting Started

1. Clone the repository to your local machine.
2. Create a file named `tokens.json` in the project directory.
3. Open the [Hoyolab website](https://www.hoyolab.com/home) in any browser.
4. In the browser console, execute the command `document.cookie` to retrieve the cookie value. Keep this value safe and do not share it with others.
5. Paste the cookie value inside the `tokens.json` file as shown below:

```json
{
    "RandomName": "cookie_value_here",
    "User2": "if you want to add another user"
}
```
6. (Optional) Edit the `login.bat` file:
   - Update the first line to specify the directory of the HoyoLogin project.
   - Update the second line to provide the full path to the Python interpreter and `main.py`.
7. (Optional) If you want to schedule the task, adjust the properties inside the `schedule_task.ps1` file according to your preferences.
8. (Optional) If you want to add Honkai Imact 3rd logic is the same. Just find current valid URI
