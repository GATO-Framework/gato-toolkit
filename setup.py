from setuptools import setup, find_packages


def get_long_description():
    with open('README.md') as file:
        return file.read()


setup(
    name="gato-toolkit",
    version="0.1.0-rc2",
    description="A toolkit for furthering research on AI alignment.",
    url="https://github.com/FyZyX/gato-toolkit",
    author="Lucas Lofaro <lucasmlofaro@gmail.com>",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    license='MIT',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        "openai>=0.27.6",
        "pydantic>=1.10.7",
    ],
)
