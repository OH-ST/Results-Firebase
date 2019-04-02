from setuptools import setup

setup(name='otrresultsfb',
      version='0.1',
      description='Python script for control of Tenma Power supplies over serial',
      url='https://github.com/danielcrowley/OpenTestRig-Results-Firebase',
      author='Daniel Crowley',
      author_email='crowley.daniel@gmail.com',
      license='MIT',
      packages=['otrresultsfb'],
      install_requires=[
        'requests==2.18.0',
        'firebase_admin'
    ])
