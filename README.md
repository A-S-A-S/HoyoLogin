# HoyoLogin

HoyoLogin is a straightforward Python script for claiming rewards from Hoyoverse games. It aims to provide a simple and efficient solution without excessive dependencies, convoluted code, or over-engineered user interactions.

## Requirements

- Python

## Getting Started

1. Clone the repository to your local machine.
2. Open the [Hoyolab website](https://www.hoyolab.com/home) in any browser.
3. In the browser console, execute the command `document.cookie` to retrieve the cookie value. Keep this value safe and do not share it with others.
4. Run the setup script by following these steps:

   - Open a PowerShell terminal as Administrator (To schedule tasks using the Task Scheduler, administrative privileges are required. Press the Windows key + X. From the menu, select "Windows PowerShell (Admin)")
   - Navigate to the project directory (e.g. `cd C:\Projects\HoyoLogin`)
   - Execute the following command:
     ```powershell
     ./setup.ps1
     ```
 5. Follow the instructions provided by the setup script.

## Troubleshooting

### 'message': 'Not logged in'

If you encounter the following error:
```bash
{'data': None, 'message': 'Not logged in', 'retcode': -100}
```
You need to claim a reward manually at least once and then reclaim the cookie.

### 0x1 in Task Scheduler
The error code 0x1 in Task Scheduler typically indicates that the command or script executed by the scheduled task has completed with a non-zero exit code. <br/>
Run login.bat to see the actual error message

### It stopped working

If the script stopped working, try renewing the cookie by repeating the steps to retrieve the cookie value from the browser console.