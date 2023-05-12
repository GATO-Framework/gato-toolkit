from setuptools import setup, find_packages

setup(
    name="gato-toolkit",
    version="0.1.0-rc1",
    description="A toolkit for furthering research on AI alignment.",
    url="https://github.com/FyZyX/gato-toolkit",
    author="Lucas Lofaro <lucasmlofaro@gmail.com>",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        "fastapi>=0.95.1",
        "openai>=0.27.6",
        "streamlit>=1.22.0",
    ],
)
