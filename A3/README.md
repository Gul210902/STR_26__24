# Extracting Column Data from IFC for Capacity Checks

## Summary
**Title:** Extracting Column Data from IFC for Capacity Checks

**Description:** This beginner-level tutorial demonstrates how to extract structural column information from an IFC model, combine it with structural report data, estimate column loads, and calculate simplified axial utilization ratios using Python.

## Tutorial information
| | |
|---|---|
| Course | 41934 Advanced BIM, DTU (A3: Teach) |
| Group | 24: Gulshan Kumar (s252589), Aida Amirbabaei (s216201) |
| Focus area | Structural Analysis |
| Role / level targeted | Analyst, Level 1 (beginner) |
| BIM use | 08: Structural Analysis |
| Learning need | Learn how to extract column geometry and material properties from an IFC model using IfcOpenShell, integrate external structural loading data, and perform preliminary column capacity assessments, including the calculation and interpretation of an illustrative utilization ratio. |
| Time needed | About 60–90 minutes |
| Formats | Markdown + Jupyter Notebook. |
| License | MIT |

## Learning objectives
After this tutorial you will be able to:
1. Open an IFC model using IfcOpenShell, identify its schema and units, and retrieve structural column elements (IfcColumn).
2. Extract column identifiers, storeys, coordinates, section dimensions, and available length data from the IFC model, and classify the structural members.
3. Compare extracted IFC column information with structural documentation and integrate external loading data using Python and pandas.
4. Estimate floor load distribution and accumulated column loads using a simplified tributary area and vertical load-transfer method.
5. Calculate and visualize illustrative axial utilization ratios for retained reinforced-concrete and new glulam columns, while identifying the limitations of the simplified analysis.

## What you need
* Python 3.10 or newer and Jupyter Notebook.
* Required Python libraries: `pip install ifcopenshell pandas matplotlib`
* Save `tutorial_A3.ipynb` in your working folder and place `26-08-STR.ifc` and all three CSV files in a `data` subfolder within the same working folder.

## Files
The A3 folder contains the Jupyter Notebook and the following input files:
```
tutorial_A3.ipynb                Main tutorial notebook.
26-08-STR.ifc                    Proposed structural IFC model (to be added).
report_table6_columns_full.csv   Column dimensions and reinforcement data.
report_load_cases.csv            Loading data from the structural report.
assumptions_DEMO.csv             Assumed parameters for demonstration calculations.
```
The notebook also generates floor-loading data and saves the results in the results/ folder.

## Set up and run
1. Install: `py -m pip install notebook ipykernel ifcopenshell pandas matplotlib`.
2. Download the folder and place `26-08-STR.ifc` in `data/` alongside the provided CSV files.
3. Open `tutorial_A3.ipynb` in Jupyter or VS Code (with Python and Jupyter extensions).
4. Restart the kernel, run the cells in order, and complete the exercises.
5. Give the feedback at the end of the notebook.

## Notes
* The report_load_cases.csv file contains loading information extracted from the structural report, while assumptions_DEMO.csv contains assumed parameters used in the simplified calculations. Additional synthetic floor-loading regions are generated within the notebook. The resulting utilization ratios are illustrative and do not represent verified structural design results.
* The report table was typed by hand from the structural report. Check it against the original.
* The results do not represent verified structural utilization. Actual design assessments require validated loading, material properties, appropriate design combinations, and relevant structural resistance checks.

## Peer Review and Feedback
