import numpy as np
import matplotlib.pyplot as plt

def plot_array(array, cmap="gray", title="Title", xlabel="x", ylabel="y"):
    """
    Plots a 2D array as an image with a color map and color bar.
    
    The function takes a 2D NumPy array and displays it as an image using Matplotlib. 
    Each element in the array is represented by a color, and a color bar is added to 
    show the mapping of values to colors. By default, the color map is set to 'gray'.

    Input validation is performed to ensure that the input is a 2D NumPy array containing 
    only numeric values.

    Parameters
    ----------
    array : np.ndarray
        A 2D NumPy array containing numerical values.

    cmap : str, optional
        A string representing the colormap to use. Default is 'gray'.
        Options include 'viridis', 'plasma', 'inferno', 'magma', 'cividis', etc.

    title : str, optional
        The title of the plot. Default is "Title".

    xlabel : str, optional
        The label for the x-axis. Default is "x".

    ylabel : str, optional
        The label for the y-axis. Default is "y".

    Returns
    -------
    None
        Displays the matrix as an image and returns nothing.

    Raises
    ------
    ValueError
        If the input is not a 2D NumPy array.
        If the specified colormap is not valid.
        If the array contains non-numeric values.

    Example
    -------
    >>> array = np.array([[1.5, 0.2, 3.3], [4.1, 2.0, 1.2], [3.5, 0.1, 1.8]])
    >>> plot_array(array, cmap='viridis', title='My Plot', xlabel='Column', ylabel='Row')
    (Displays a plot of the array)
    """
    
    # Input validation
    if not isinstance(array, np.ndarray):
        raise ValueError("Input must be a NumPy array.")
    
    if array.ndim != 2:
        raise ValueError("Input must be a 2D array.")

    # Check if all elements are numeric
    if not np.issubdtype(array.dtype, np.number):
        raise ValueError("Array must contain only numeric values (integers or floats).")

    # Validate colormap
    if cmap not in plt.colormaps():
        raise ValueError(f"'{cmap}' is not a valid colormap. Please choose a valid colormap.")

    # Display the matrix as an image
    plt.imshow(array, cmap=cmap, interpolation='nearest')
    plt.colorbar()  # Add a color bar to indicate values
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return

    
def toggle(array, a=0, b=1):
    """
    Toggles the values in a NumPy array between two specified values `a` and `b`.

    The function replaces all instances of `a` in the input array with `b` and vice versa. 
    If no values for `a` and `b` are provided, the default values of `0` and `1` are used.
    
    Input validation is performed to ensure:
    - The input is a NumPy array.
    - The array contains exactly two unique values.
    - The values `a` and `b` are present in the array and of the same type as the array elements.

    Parameters
    ----------
    array : np.ndarray
        A NumPy array containing exactly two unique values.
    a : int, float, or str, optional
        The first value to toggle in the array (default is 0).
    b : int, float, or str, optional
        The second value to toggle in the array (default is 1).

    Returns
    -------
    toggled_array : np.ndarray
        A new NumPy array with all instances of `a` replaced with `b` and vice versa.
    
    Raises
    ------
    ValueError
        - If the input is not a NumPy array.
        - If the array does not contain exactly two unique values.
        - If both `a` and `b` are not present in the array.
    TypeError
        - If `a` and `b` are not of the same type as the elements in the array.

    Example
    -------
    >>> import numpy as np
    >>> array = np.array([[0, 1, 1], [1, 0, 0], [0, 1, 0]])
    >>> toggle(array)
    array([[1, 0, 0],
           [0, 1, 1],
           [1, 0, 1]])

    >>> array_str = np.array([['X', 'Y', 'Y'], ['Y', 'X', 'X'], ['X', 'Y', 'X']])
    >>> toggle(array_str, a='X', b='Y')
    array([['Y', 'X', 'X'],
           ['X', 'Y', 'Y'],
           ['Y', 'X', 'Y']])
    """
    
    # Input validation
    # Validate if the input array is a NumPy array
    if not isinstance(array, np.ndarray):
        raise ValueError("Input must be a NumPy array.")

    # Check if array contains exactly two unique values
    unique_values = np.unique(array)
    if len(unique_values) != 2:
        raise ValueError("Array must contain exactly two unique values.")

    # Check that both 'a' and 'b' are in the unique values
    if a not in unique_values or b not in unique_values:
        raise ValueError(f"Both 'a' ({a}) and 'b' ({b}) must be present in the array.")

    # Validate that 'a' and 'b' are of the same type as the elements in the array
    if not isinstance(a, type(unique_values[0])) or not isinstance(b, type(unique_values[0])):
        raise TypeError("'a' and 'b' must be of the same type as the array elements.")

    # If a or b are not found in the array, raise a warning
    if a not in array and b not in array:
        raise ValueError(f"Neither 'a' ({a}) nor 'b' ({b}) found in the array.")
        
    # Toggle the values of the array
    shape = np.shape(array)
    toggled_array = array.copy()
    for i in range(shape[0]):
        for j in range(shape[1]):
            if array[i,j] == a:
                toggled_array[i,j] = b
            if array[i,j] == b:
                toggled_array[i,j] = a
    return toggled_array
    
def plot_journey(location_history):
    # Convert the list of points to a NumPy array for easier manipulation
    data_array = np.array(location_history)

    # Extract x and y coordinates
    x = data_array[:, 0]
    y = data_array[:, 1]

    # Create a color gradient based on the y values
    # Normalize y values to the range [0, 1]
    norm = plt.Normalize(y.min(), y.max())
    colors = plt.cm.viridis(norm(y))  # You can change 'viridis' to other colormaps

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the line graph
    for i in range(len(x) - 1):
        ax.plot(x[i:i + 2], y[i:i + 2], color=colors[i])  # Plot each segment with its color

    # Add labels and title
    ax.set_title("Colored Line Graph of Points")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    # Create a ScalarMappable and add a colorbar
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
    sm.set_array([])  # Only needed for older versions of Matplotlib
    cbar = plt.colorbar(sm, ax=ax, label='Y values')  # Add color bar
    plt.grid()
    plt.show()
    
    
    #Add this to put circle of interest on points of graph!
    #from matplotlib.patches import Circle
    
    ## Create and add a circle patch
    #circle = Circle(intersection, 4, color='red', fill=False, linewidth=5, label='1st intersection')
    #ax.add_patch(circle)


    return
    
def generate_ulam_spiral(size=7, handedness="left"):
    """
    Generates an Ulam spiral of a specified size and handedness.

    The Ulam spiral is a visual representation of the sequence of natural numbers,
    arranged in a spiral pattern starting from the center of a grid. Prime numbers
    in this arrangement tend to form diagonal lines, making it useful for visualizing
    patterns in prime distribution.

    Parameters:
    ----------
    size : int, optional, default=7
        The size of the grid (number of rows and columns). Must be a positive integer.
        If an even number is given, it will be incremented by 1 to ensure the grid
        has an odd size, so the spiral can start from the exact center.
    
    handedness : str, optional, default="left"
        The direction of turns in the spiral. Accepted values are "Left" or "Right" 
        (case insensitive). "Left" generates a counterclockwise spiral, while "Right" 
        generates a clockwise spiral.

    Returns:
    -------
    np.ndarray
        A 2D numpy array of shape (size, size), where each cell contains an integer 
        in the sequence from 1 to size^2, arranged in the Ulam spiral pattern.

    Raises:
    ------
    ValueError
        If `size` is not a positive integer or if `handedness` is not one of 
        the accepted values.

    Examples:
    --------
    >>> generate_ulam_spiral()
    array([[37, 36, 35, 34, 33, 32, 31],
           [38, 17, 16, 15, 14, 13, 30],
           [39, 18,  5,  4,  3, 12, 29],
           [40, 19,  6,  1,  2, 11, 28],
           [41, 20,  7,  8,  9, 10, 27],
           [42, 21, 22, 23, 24, 25, 26],
           [43, 44, 45, 46, 47, 48, 49]])

    >>> generate_ulam_spiral(size=5, handedness='Right')
    array([[21, 22, 23, 24, 25],
           [20,  7,  8,  9, 10],
           [19,  6,  1,  2, 11],
           [18,  5,  4,  3, 12],
           [17, 16, 15, 14, 13]])
    """
    # Validate size
    if not isinstance(size, int) or size <= 0:
        raise ValueError("`size` must be a positive integer.")
    
    # Ensure size is odd for centering
    if size % 2 == 0:
        size += 1

    # Validate handedness
    if handedness.lower() not in ["left", "right"]:
        raise ValueError("`handedness` must be either 'Left' or 'Right' (case insensitive).")

    # Set direction change logic and initial direction based on handedness
    if handedness.lower() == "left":
        # Counterclockwise (left turn after each side)
        changing_direction = {"R": "U", "U": "L", "L": "D", "D": "R"}
        direction = "D"  # Start moving down
    else:
        # Clockwise (right turn after each side)
        changing_direction = {"R": "D", "D": "L", "L": "U", "U": "R"}
        direction = "U"  # Start moving up

    # Initialize spiral array and starting values
    ulam_spiral = np.zeros((size, size), dtype=np.int32)
    location = (size // 2, size // 2)
    current_number = 1
    ulam_spiral[location] = current_number

    # Begin spiral generation
    side_length = 0
    while current_number < size ** 2:
        side_length += 1
        for _ in range(2):  # Each side length occurs twice
            direction = changing_direction[direction]  # Update direction
            for _ in range(side_length):
                current_number += 1
                if current_number > size ** 2:
                    return ulam_spiral

                # Update location based on direction
                if direction == "R":
                    location = (location[0], location[1] + 1)
                elif direction == "U":
                    location = (location[0] - 1, location[1])
                elif direction == "L":
                    location = (location[0], location[1] - 1)
                elif direction == "D":
                    location = (location[0] + 1, location[1])

                ulam_spiral[location] = current_number
    return ulam_spiral


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

def determine_num_duplicates_in_list(input_list):
    """
    Determines the number of occurrences (duplicates) of each unique element in a list.

    Parameters:
    input_list (list): A list of elements to check for duplicates.
                       Elements can be of any hashable type (e.g., int, str, tuple).

    Returns:
    dict: A dictionary where keys are unique elements from the input list,
          and values are the count of occurrences of each element.

    Raises:
    TypeError: If input_list is not a list.
    ValueError: If input_list contains unhashable elements.

    Example:
    >>> input_list = ['apple', 'banana', 'apple', 'orange', 'banana']
    >>> determine_num_duplicates_in_list(input_list)
    {'apple': 2, 'banana': 2, 'orange': 1}
    """

    # Input validation
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")

    # Check if all elements are hashable
    try:
        set(input_list)
    except TypeError:
        raise ValueError("All elements in the list must be hashable.")

    # Calculate occurrences of each unique element
    unique_elements = set(input_list)
    duplicate_dict = {element: input_list.count(element) for element in unique_elements}

    return duplicate_dict