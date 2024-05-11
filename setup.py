from setuptools import setup, find_packages

setup(
    name="msuliot.helpers",
    version="1.24.511",
    author="Michael Suliot",
    author_email="michael@suliot.com",
    description="Some basic helper functions for AI projects",
    long_description=open('README.md').read(),
    url="https://github.com/msuliot/package-helpers.git",
    packages=find_packages(),
    install_requires=[
        'pymongo',
        'openai',
        'pinecone-client'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
