# Ranking of stackoverflow Users

## Overview

This program takes the URL of stackoverflow users and generate their statistics based on their reputation, badges earned, people reached, etc., For generating the ranking/ position of a user, comparison is done against the Melbourne based users.

 ## Workflow

 The following points details the workflow process of this program:

* Pass the stackoverflow user's URL into the prompt.
* If an incorrect URL is provided, a message will be displayed to check the URL. Also, you have an option to exit or continue the program by typing 'Yes' or 'No'.
* If typed 'No', enter the URL again.
* If an incorrect URL is entered, step 2 is repeated.
* If a correct URL is entered, the output with the statistics of the user along with the ranking is displayed.

## Prerequisite

* python
* python packages (numpy, pandas and scipy)

## Quick Start

Before running the python script, make sure to add the python interpreter to the path.

**Note:** To add python to the path, add the location of the python interpreter in your computer to the environment variable. For stepwise process, see the article on https://geek-university.com/python/add-python-to-the-windows-path/.

##### Running the program:
1. Open the command prompt or any command line environment (bash, git bash, etc.).
2. Run the following command to check if python is added correctly to the path.
```shell
$> python --version
```
If running the above command shows a version of python, then the interpreter is added successfully to the path and supports subsequent operations.

3. If python is installed properly, go to your working directory where python is installed using the following command. Here, we move to the folder named user_ranking inside the edx folder.
```shell
$> cd edx/user_ranking
```
4. Run the python script located in your directory using the following command.
```shell
$> python user_ranking.py
```
5. Follow the prompt and get the result.

##### Additional Information:
When encountered with typical errors, run the following command in the command line.
1. Missing required dependencies ['numpy']
``` shell
$> pip uninstall pandas -y
$> pip uninstall numpy -y
$> pip install pandas
$> pip install numpy
```
This command is an uninstall and install sequence of pandas and numpy.

2. scipy - ImportError: DLL load failed: The specified module could not be found

```shell
$> conda remove --force numpy, scipy
$> pip install numpy, scipy
```
