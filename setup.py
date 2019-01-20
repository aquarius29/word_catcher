from setuptools import setup

setup(
    name='word_catcher',
    version='0.1',
    author='Tonis Tsagaris',
    description='Searches words in subtitles and cuts the scenes out',
    long_description=open('README.md').read(),
    install_requires=[
        "pysrt >= 1.1.1",
        "moviepy >= 0.2.3.5",
    ],
	zip_safe=False
	)