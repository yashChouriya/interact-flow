from setuptools import setup, find_packages
import os

# Read version from version.py
with open(os.path.join("src", "version.py"), "r", encoding="utf-8") as f:
    exec(f.read())

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = ["pynput>=1.7.6", "python-xlib>=0.33"]

setup(
    name="interactflow",
    version=__version__,
    author="InteractFlow Team",
    author_email="yashchouriya131+github@gmail.com",
    description="A powerful tool for recording and replaying user interactions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yashChouriya/interactflow",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "interactflow=src.main:main",
        ],
    },
)
