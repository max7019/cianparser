import codecs
from setuptools import setup

with codecs.open("README.md", "r", "utf-8") as file:
    read_me_description = file.read()


setup(
    name='cianparser',
    version='0.4.11',
    description='Parser information from Cian website',
    url='https://github.com/lenarsaitov/cianparser',
    author='Lenar Saitov',
    author_email='lenarsaitov1@yandex.ru',
    license='MIT',
    packages=['cianparser'],
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='python parser requests cloudscraper beautifulsoup cian realstate',
    install_requires=['cloudscraper', 'beautifulsoup4', 'transliterate', 'lxml', 'datetime'],
)
