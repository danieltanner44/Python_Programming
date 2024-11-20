import numpy as np
import my_modules.development as mmd

def print_array(array, *mapping):
    """
        Prints a formatted 2D array with optional custom symbol mapping for string arrays
        with two distinct elements or numeric arrays based on a threshold.

        Parameters:
        ----------
        array : np.ndarray
            A 2D NumPy array containing either strings or integers. The array must be homogeneous in type,
            meaning all elements should either be strings or integers. For string arrays, it should contain
            exactly two distinct elements for mapping to work.

        mapping : tuple, optional
            A tuple that specifies how to map elements in the `array` when printing. The expected mapping format
            depends on the type of elements in `array`:
            - If `array` contains strings, `mapping` should contain exactly two elements (str, str), where:
                - `mapping[0]` replaces occurrences of the first unique string.
                - `mapping[1]` replaces occurrences of the second unique string.
            - If `array` contains integers, `mapping` should contain exactly three elements (str, str, int), where:
                - `mapping[0]` is used to replace values below or equal to the threshold.
                - `mapping[1]` is used to replace values above the threshold.
                - `mapping[2]` is the integer threshold used to compare each array element.

        Returns:
        -------
        None
            This function prints the array directly and returns None.

        Raises:
        ------
        ValueError
            If `array` is not a 2D NumPy array, if its elements are neither all strings nor all integers,
            or if `mapping` is provided but does not meet the requirements for the given array type.

        Notes:
        ------
        - The function adjusts the column width dynamically based on the length of the largest element for consistent formatting.
        - When a string array with more than two distinct elements is provided, or if `mapping` for a string array
          does not contain exactly two elements, the function will terminate and print an error message.
        - For numeric arrays, if `mapping` does not contain exactly three elements, or if the third element is
          not an integer, the function will terminate and print an error message.

        Example:
        -------
        ```python
        # Example with a string array:
        array = np.array([["A", "B", "A"], ["B", "A", "B"], ["A", "A", "B"]])
        mapping = ("#", ".")
        print_array(array, mapping)

        # Example with a numeric array:
        numeric_array = np.array([[10, 40, 60], [80, 20, 70], [50, 30, 90]])
        mapping = ("#", ".", 50)
        print_array(numeric_array, mapping)
        ```
        """
    # Input validation
    # Validate that array is a 2D NumPy array
    if not isinstance(array, np.ndarray) or array.ndim != 2:
        print("Error: 'array' must be a 2D NumPy array.")
        return

    # Validate array content: all elements must be either strings or integers
    if not all(isinstance(element, (str, int, np.integer)) for row in array for element in row):
        print("Error: All elements in 'array' must be either strings or integers.")
        return

    # Check if mapping is provided and validate based on array content
    if mapping:
        mapping = mapping[0]
        if all(isinstance(element, str) for row in array for element in row):  # String array
            if len(mapping) != 2:
                print("Error: Mapping for a string array must contain exactly two elements.")
                return

        elif all(isinstance(element, (int, np.integer)) for row in array for element in row):  # Numeric array
            if len(mapping) != 3:
                print(
                    "Error: Mapping for a numeric array must contain three elements: (below_threshold_str, above_threshold_str, threshold).")
                return
            if not isinstance(mapping[2], (int, np.integer)):
                print("Error: The third element in the numeric mapping must be an integer threshold.")
                return

        else:
            print("Error: Array elements are neither entirely strings nor entirely numeric.")
            return

    # Proceed with printing of the array
    if mapping:
        if len(mapping) != 2:
            print("Error: Mapping must contain at least two elements.")
            return

        # Convert String Array
        if mapping and all(isinstance(element, str) for row in array for element in row):
            set_elements = set(array.flatten())  # Flatten the array and get unique elements
            if len(set_elements) != 2:
                print("Error: Input string array must contain exactly two distinct elements.")
                return
            set_elements_list = list(set_elements)
            aoc_array = np.empty(shape=np.shape(array), dtype=np.str_)
            for i, row in enumerate(array):
                for j, element in enumerate(row):
                    aoc_array[i, j] = mapping[0] if element == set_elements_list[0] else mapping[1]
            array = aoc_array

            # Convert numeric array based on threshold mapping
        elif mapping and all(isinstance(element, (int, np.integer)) for row in array for element in row):
            aoc_array = np.empty(shape=np.shape(array), dtype=np.str_)
            for i, row in enumerate(array):
                for j, element in enumerate(row):
                    aoc_array[i, j] = mapping[0] if element <= mapping[2] else mapping[1]
            array = aoc_array

    # Calculate the width of the widest entry for column alignment
    width = max(len(str(entry)) for row in array for entry in row)

    # Construct a format string for each row based on the number of columns
    row_format = " ".join([f"{{:>{width}}}"] * len(array[0]))

    # Print each row using the generated format string
    for row in array:
        print(row_format.format(*row))

    return

def main():
    array = mmd.generate_ulam_spiral(size=13, handedness="left")
    array = [['B','A','B','A'],['B','B','A','A'],['A','A','B','B']]
    array = np.array(array, dtype=np.str_)
    threshold = 50
    mapping = ["#", "."]  # Mapping for the numeric array conversion
    print_array(array)

if __name__ == "__main__":
    main()
