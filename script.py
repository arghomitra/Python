import zipfile
import os
from pathlib import Path


zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
zipfile_.extractall()
zipfile_.close()
