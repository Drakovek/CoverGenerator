#!/usr/bin/env python3

import re
import setuptools

console_scripts = ["cover-generator = cover_generator:main"]

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="CoverGenerator",
    version="0.2.0",
    author="Drakovek",
    author_email="DrakovekMail@gmail.com",
    description="Python utility for generating cover images for e-books.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Drakovek/CoverGenerator",
    packages=setuptools.find_packages(),
    package_data={"": ["*.json"]},
    include_package_data=True,
    install_requires=["CairoSVG>=2.5.1", "HTML-String-Tools>=0.2.0", "pillow>=8.0.0"],
    classifiers=["Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent"],
    python_requires='>=3.8',
    entry_points={"console_scripts": console_scripts}
)
