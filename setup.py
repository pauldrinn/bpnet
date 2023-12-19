#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = [
    "argh",
    "attr",
    "related",
    "cloudpickle>=1.0.0",

    "concise==0.6.7",
    "deepexplain",

    # ml
    "gin-config",
    "keras==2.3.1",
    "scikit-learn==0.21.3",
    # "tensorflow",

    # numerics
    "h5py==2.9.0",
    "numpy==1.17.5",
    "pandas==1.0.3",
    "scipy==1.4.1",
    "statsmodels==0.11.1",

    # Plotting
    "matplotlib==3.0.2",
    "plotnine",
    "seaborn",

    # genomics
    "pybigwig==0.3.18",
    "pybedtools==0.7.10",  # remove?
    "modisco==0.5.3.0",
    # "pyranges",

    "joblib",
    "cloudpickle>=1.0.0",  # - remove?
    "kipoi>=0.6.8",
    "kipoi-utils>=0.3.0",
    "kipoiseq>=0.2.2",

    "papermill",
    "jupyter_client>=6.1.2",
    "ipykernel",
    "nbconvert>=5.5.0",
    "vdom>=0.6",

    # utils
    "ipython",
    "tqdm",

    # Remove
    "genomelake==0.1.4",
    "pysam==0.15.3",  # replace with pyfaidx
]

optional = [
    "comet_ml",
    "wandb==0.8.7",
    "fastparquet",
    "python-snappy",
    "ipywidgets",  # for motif simulation
]

test_requirements = [
    "pytest>=3.3.1",
    "pytest-cov>=2.6.1",
    # "pytest-xdist",
    "gdown",   # download files from google drive
    "virtualenv",
]

dependency_links = [
    "deepexplain @ git+https://github.com/kundajelab/DeepExplain.git@#egg=deepexplain-0.1"
]


setup(
    name="bpnet",
    version='0.0.23',
    description=("BPNet: toolkit to learn motif synthax from high-resolution functional genomics data"
                 " using convolutional neural networks"),
    author="Ziga Avsec",
    author_email="avsec@in.tum.de",
    url="https://github.com/kundajelab/bpnet",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        "dev": test_requirements,
        "extras": optional,
    },
    license="MIT license",
    entry_points={'console_scripts': ['bpnet = bpnet.__main__:main']},
    zip_safe=False,
    keywords=["deep learning",
              "computational biology",
              "bioinformatics",
              "genomics"],
    test_suite="tests",
    package_data={'bpnet': ['logging.conf']},
    include_package_data=True,
    tests_require=test_requirements
)
