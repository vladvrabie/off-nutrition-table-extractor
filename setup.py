import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nutrition_extractor",
    version="0.0.1",
    author="Sagar Panchal",
    description="Package for detecting nutritional tables/data from images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vladvrabie/off-nutrition-table-extractor",
    packages=setuptools.find_packages(
        include=["nutrition_extractor", "nutrition_extractor.*"]
    ),
    license="AGPL-3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'tensorflow==1.15',
        'Pillow',
        'opencv-python',
        'pytesseract',
        'easydict',
    ],
    extras_require={
        'interactive': ['matplotlib', 'jupyter'],
    },
    package_data={
        'nutrition_extractor': ['data/models/*'],
    },
)
