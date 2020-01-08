"""
This script uses PyInstaller to build a binary version of the project
Just run python3 build.py on the target platform
The result files will be put in ./dist/Azur Iris
"""


import os
import PyInstaller.__main__

package_name = "Azur Iris"

PyInstaller.__main__.run([
    '--name=%s' % package_name,
    '--add-data=%s' % "azuriris.data;.",
    '--icon=%s' % os.path.join("azuriris.ico"),
    os.path.join('azuriris', 'azuriris.py'),
])
