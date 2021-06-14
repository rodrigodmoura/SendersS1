from setuptools import setup
APP = ['dialog1.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True, 
    'site_packages': True,
    'packages': ['wx', 'requests'],
    'plist': {
        'CFBundleName': 'Subreddit',
    }
}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

