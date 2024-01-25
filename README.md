# Social Network

Simple project to analyze twitter data about 8th season of game of thrones.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/abolfazl-shishegar/Social-Network
    ```

2. Change into the project directory:

    ```bash
    cd Social-Network
    ```

3. Install the required packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Just run files!

## Requirements

Ensure you have the following Python packages installed:

- [NetworkX](https://networkx.github.io/): A Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
    ```bash
    pip install networkx
    ```

- [pandas](https://pandas.pydata.org/): A powerful data manipulation and analysis library.
    ```bash
    pip install pandas
    ```

- [NLTK](https://www.nltk.org/): The Natural Language Toolkit, a library for the Python programming language that provides tools for working with human language data.
    ```bash
    pip install nltk
    python -m nltk.downloader vader_lexicon punkt
    ```

- [Matplotlib](https://matplotlib.org/): A comprehensive library for creating static, animated, and interactive visualizations in Python.
    ```bash
    pip install matplotlib
    ```

You can install all the requirements at once by running (The nltk must be installed separately):

```bash
pip install -r requirements.txt
