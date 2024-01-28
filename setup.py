#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = [
    "argh",
    "attr",
    "related",
    "cloudpickle",

    # ml
    "gin-config",
    "keras",
    "scikit-learn",
    # "tensorflow",

    # numerics
    "h5py",
    "numpy",
    "pandas",
    "scipy",
    "statsmodels",
	"descartes",
	"shapely",

    # Plotting
    "matplotlib",
    "plotnine",
    "seaborn",

    # genomics
    "pybigwig",
    "pybedtools",
    "modisco",
    # "pyranges",

    "joblib",
    "kipoi",
    "kipoi-utils",
    "kipoiseq",

    "papermill",
    "jupyter_client",
    "ipykernel",
    "nbconvert",
    "vdom",

    # utils
    "ipython",
    "tqdm",

    "genomelake @ git+https://github.com/pauldrinn/genomelake.git",
    "pysam",
]

optional = [
    "comet_ml",
    "wandb",
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
