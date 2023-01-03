# Combination Generator

This script generates combinations from given numbers, with a specified number of elements in each combination. The project is currently in the process of making the script, but a larger-scale combinatorics library is also in the works.

### Installation
To install the project, simply clone the code.

### Usage
To generate combinations, call the **`generate_combinations()`** function. The **`numbers`** parameter should contain the numbers you want to combine, and the **`length`** parameter should contain a number specifying the number of elements in each combination.

**Example:**

*1.) Input:* **`generate_combinations([1, 2, 3, 4, 5], 2)`**
*1.) Output:* **`[[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]`**

*2.) Input:* **`generate_combinations([2, 2, 2, 3, 4], 3)`**
*2.) Output:* **`[[2, 2, 2], [2, 2, 3], [2, 2, 4], [2, 2, 3], [2, 2, 4], [2, 3, 4], [2, 2, 3], [2, 2, 4], [2, 3, 4], [2, 3, 4]]`**

*3.) Input:* **`generate_combinations(['a', 'b', 'c', 'd'], 2)`**
*3.) Output:* **`[['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd'], ['c', 'd']]`**

The code has been tested with Python 3.11.1, but it should work with earlier versions as well, as it does not use any libraries.

### Errors
The code has been extensively tested and should not have any errors. However, if you do find an error, you can report it on the **`Issues`** tab. I will try to respond and fix the code.

### License
This script is shared under the MIT License.
