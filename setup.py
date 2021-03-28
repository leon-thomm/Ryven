from setuptools import setup, find_packages



setup(
    name='ryven',
    version='0.0.0',
    license='MIT',
    description='Flow-based visual scripting editor for Python',
    author='Leon Thomm',
    author_email='l.thomm@mailbox.org',
    packages=[
        
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.8',
    install_requires=['PySide2'],
)
