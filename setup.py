from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="whitelabel_community",
    version="0.1.0",
    author="Shivani.A",
    author_email="srishivani1007@gmail.com",
    description="A white-label community platform built with FastAPI and MongoDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Srishivani/whitelabel_community",
    packages=find_packages(include=['whitelabel_community', 'whitelabel_community.*']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.68.0",
        "pyjwt>=2.1.0",
        "python-jose[cryptography]",
        "passlib[bcrypt]",
        "python-multipart",
        "motor>=2.5.0",
        "pymongo>=3.12.0",
        "pydantic>=2.0.0",  # Updated version
        "pydantic-settings>=2.0.0",
        "python-dotenv>=0.19.0"
    ],
    extras_require={
        'test': [
            'pytest>=6.0.0',
            'pytest-asyncio>=0.18.0',
            'pytest-cov>=3.0.0'
        ],
        'dev': [
            'black',
            'flake8',
            'mypy',
            'isort'
        ]
    }
)
