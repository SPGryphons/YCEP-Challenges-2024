## Solution
## 1. Download Steghide:

- Visit the official Steghide download page (https://steghide.sourceforge.net/download.php) and download the Windows binary.

- Extract the files:

- Extract the downloaded ZIP file to a directory of your choice, for example, C:\Steghide.

- Add Steghide to the PATH:

Add the directory containing steghide.exe to your system's PATH. Here's how to do this:

- Right-click on the Start button and select "System".

- Click on "Advanced system settings".

- In the System Properties window, click on the "Environment Variables" button.

- In the Environment Variables window, find the "Path" variable in the "System variables" section and select it. Click on the "Edit" button.

- In the Edit Environment Variable window, click on "New" and add the path to the directory where steghide.exe is located (e.g., C:\Steghide).

- Click OK to close all windows.

- Open a new Command Prompt:

Close any open Command Prompt windows and open a new one to ensure the updated PATH is recognized.
Verify the installation:

Type steghide in the Command Prompt to see if the command is recognized. If it is, you should see Steghide's help output.

## 2. Run commands to extract secret.txt embedded in image file redbridge.jpg

- Open Command Prompt.

- Navigate to the directory containing redbridge.jpg:

*
cd path\to\your\directory
*

- Extract the embedded file:

*
steghide extract -sf redbridge.jpg
*

- Enter the passphrase when prompted. 
***THERE IS NO PASSPHRASE, JUST PRESS ENTER***

- Verify the extraction:

*
dir
*

List out the contents of secret.txt to get the flag:

*
type secret.txt
*

By following these steps, you can extract the secret.txt file from the redbridge.jpg image and display its contents using the Command Prompt.