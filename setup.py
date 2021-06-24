import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vcf-creator",
    version="0.0.1",
    author="Animesh Singh Chouhan",
    author_email="animeshsingh.iitkgp@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/animesh-chouhan/vcf-creator",
    project_urls={
        "Bug Tracker": "https://github.com/animesh-chouhan/vcf-creator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"vcf_creator"},
    packages=setuptools.find_packages(where="vcf_creator"),
    python_requires=">=3.6",
)