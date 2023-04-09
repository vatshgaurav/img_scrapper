from setuptools import setup, find_packages

setup(
    name="img_scrapper",
    version="0.0.13",
    description="python package to scrap image from google image search",
    author="Gaurav Vatsh",
    author_email="vatshgaurav@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.12.2",
        "bs4==0.0.1",
        "certifi==2022.12.7",
        "lxml==4.9.2",
        "requests==2.28.2",
        "soupsieve==2.4",
        "tomli==2.0.1",
        "urllib3==1.26.15",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
