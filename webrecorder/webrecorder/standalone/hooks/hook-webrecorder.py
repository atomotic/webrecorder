from PyInstaller.utils.hooks import collect_data_files, copy_metadata
import os

from webrecorder.standalone.assetsutils import build

def rename(old, new, t):
    return [(n, v.replace(old, new)) for n, v in t]


# Build webassets bundle
curr_path = os.path.dirname(__file__)
assets_path = os.path.abspath(os.path.join(curr_path, '..', '..', 'config', 'assets.yaml'))
build(assets_path)

datas = []

# special package to put templates into to allow pyinstaller pkg_resources to find them
temp_pkg = 'wrtemp'

# move templates to separate 'wrtemp' package (only for bundled apps) to avoid
# issue with loading
init_py_path = os.path.abspath(os.path.join(curr_path, '..', '..', '__init__.py'))

datas.append((init_py_path, temp_pkg))

datas += rename('webrecorder' + os.path.sep,
                temp_pkg + os.path.sep,
                collect_data_files('webrecorder', subdir='templates'))

datas += collect_data_files('webrecorder', subdir='static')
datas += collect_data_files('webrecorder', subdir='config')

datas += copy_metadata('bottle')
