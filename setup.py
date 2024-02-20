from setuptools import setup, find_packages

setup(
    name='clusterfudge',  # Name used on PyPI (make it unique)
    version='0.0.3',
    description='Clusterfudge Python client library.',
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',
    author='Clusterfudge',
    author_email='pip@clusterfudge.com',
    url='https://github.com/clusterfudgeai/python', 
    packages=find_packages(),  # Finds packages automatically
   install_requires=[
        "dataclasses; python_version<'3.7'",
        "dataclasses-json",
        "grpcio",
        "protobuf",
   ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Or your minimum Python requirement
)