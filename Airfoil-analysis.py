import numpy as np
import matplotlib.pyplot as plt
import os

# Directory containing airfoil data files
directory = "/content/drive/MyDrive/coord_seligFmt"

# List all files in the directory
files = os.listdir(directory)

for file_name in files:
    file_path = os.path.join(directory, file_name)

    # Read airfoil data from a file (assuming the file contains X and Y coordinates)
    with open(file_path, "r") as file:
        lines = file.readlines()
        # Skip the first line and start reading data from the second line
        data = [line.strip().replace('\t', ' ').split() for line in lines[1:]]

    # Extract X and Y coordinates from the data
    x_coordinates = []
    y_coordinates = []
    for point in data:
        if len(point) >= 2:  # Check if the line has at least two elements (X and Y coordinates)
            x_coord = point[0].replace(' ', '')  # Remove spaces in X coordinate
            y_coord = point[1].replace(' ', '')  # Remove spaces in Y coordinate
            if x_coord and y_coord:  # Check if both coordinates are not empty
                x_coordinates.append(float(x_coord))
                y_coordinates.append(float(y_coord))

    x_coordinates = np.array(x_coordinates)
    y_coordinates = np.array(y_coordinates)

    # Proceed with analysis if there are valid coordinates
    if len(x_coordinates) > 0 and len(y_coordinates) > 0:
        chord_length = max(x_coordinates) - min(x_coordinates)
        thickness = np.max(y_coordinates) - np.min(y_coordinates)

        # Calculate area using trapezoidal rule
        area = np.trapz(y_coordinates, x_coordinates)  # Using numerical integration

        # Visualize the airfoil
        plt.figure(figsize=(8, 6))

        # Plot the airfoil
        plt.plot(x_coordinates, y_coordinates)

        # Annotate the plot with calculated area and thickness
        plt.annotate(f"Area: {area:.2f}", xy=(0.05, 0.95), xycoords="axes fraction")
        plt.annotate(f"Max Thickness: {thickness:.4f}", xy=(0.05, 0.90), xycoords="axes fraction")

        # Add labels, title, and grid (no legend needed since there are no multiple lines with labels)
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.title(f"Airfoil Analysis: {file_name}")
        plt.axis('off')  # Turn off the axis for better visualization
        plt.grid(False)

        # Save the plot as an SVG file with the name of the airfoil file
        output_file_name = f"{file_name.split('.')[0]}_analysis.png"
        directory_2 = '/content/drive/MyDrive/image'
        file_path_s = os.path.join(directory_2, output_file_name)
        plt.savefig(file_path_s)

        # Close the current plot to start a new one for the next file
        plt.close()

        # Display a message with the calculated area and completion confirmation for each file
        print(f"Airfoil file: {file_name}, Area: {area:.2f}, Max Thickness: {thickness:.4f}, plotted")
    else:
        print(f"Airfoil file: {file_name} contains no valid coordinate data and was skipped.")
