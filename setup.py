import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="qa-empleo",
    version="0.0.0",  # TODO
    author="Rafael Aybar",
    description="En este proyecto se medirá el índice de fiabilidad de una empresa, así como la calidad de las ofertas que publica",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RafaelAybar/qa-empleo",
    keywords="ofertas empresa fiabilidad calidad",
    py_modules=["qa_empleo", "analizadorsintactico"],
    entry_points={
        "console_scripts": [
            "qa-empleo=qa_empleo:ejecutar",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
