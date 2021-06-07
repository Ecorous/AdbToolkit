Write-Output("Cloning the repository...")
git clone "https://github.com/ExoPlant/AdbToolkit/"
Write-Output("Python found, now creating run script")
Write-Output("python main.py") > run.ps1
Write-Output("Run.ps1 file created. Now exiting the script")