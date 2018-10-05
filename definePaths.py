
from pathlib import Path

userPath = Path.cwd()
desktopPath = userPath / 'Desktop'

GADGET_G_path = desktopPath / 'RunGadget/G_Perts/'
StablePath = 'G_Perts/Stable_structures/'
desktopStablePath = desktopPath / StablePath
figurePath = desktopStablePath / 'figures/'
textFilesPath = desktopStablePath / 'text_files/'
MartinPath = 'Martin_IC_and_Final_Edd_and_OM/'
textMartinPath = textFilesPath / MartinPath
hdf5Path = desktopPath / 'G_Perts/hdf5_files/'
nosyncPath = userPath / 'nosync/RunGadget/'
