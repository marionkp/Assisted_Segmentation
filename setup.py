import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="assisted_segmentation",
    version="0.0.1post1",
    author="Marion Peres",
    author_email="marionkperes@gmail.com",
    description="Package to assist with manual segmentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marionkp/Assisted_Segmentation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
