# Airfoil-Analysis-and-Conversion-of-.dat-Files-to-.png-Format

This Python script processes airfoil coordinate data from `.dat` files and performs analysis, including calculating the airfoil area and maximum thickness. The results are visualized and saved as PNG files.

## Features

- **Coordinate Extraction:** Reads X and Y coordinates from `.dat` files, assuming the first line is a header or comment.
- **Area Calculation:** Uses numerical integration (trapezoidal rule) to calculate the area enclosed by the airfoil coordinates.
- **Maximum Thickness Calculation:** Calculates the maximum thickness of the airfoil by finding the difference between the highest and lowest Y coordinates.
- **Visualization:** Plots the airfoil shape and annotates the plot with the calculated area and thickness.
- **Batch Processing:** Automatically processes all `.dat` files in the specified directory and saves the corresponding plots as PNG files.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

You can install the required packages using pip:

```bash
pip install numpy matplotlib
```
## Usage

1. Place your airfoil `.dat` files in the specified directory.
2. Update the `directory` and `directory_2` paths in the script to point to your input data folder and output image folder, respectively.
3. Run the script to process all files in the directory.

### Example Command

```bash
python airfoil_analysis.py

```
## What the Script Does:
- Reads each .dat file in the directory.
- Calculates the area and maximum thickness of the airfoil.
- Generates a plot of the airfoil shape.
- Saves the plot as a PNG file in the output directory.
  
## Example Output
After running the script, PNG files will be generated in the output directory, with each file named after the corresponding airfoil data file (e.g., 2032c_analysis.png). Each plot will display the airfoil shape along with annotations for the calculated area and maximum thickness.

## Applications
This tool can be used for:

- Analyzing airfoil shapes in aerospace engineering.
- Studying the aerodynamic properties of different airfoil designs.
- Supporting research in fluid dynamics and aerodynamics.
  
## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request.

## Acknowledgments

- [NumPy](https://numpy.org/) for numerical computations.
- [Matplotlib](https://matplotlib.org/) for data visualization.
