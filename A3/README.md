# Extracting Column Data from IFC for Capacity Checks

## Summary
**Title:** Extracting Column Data from IFC for Capacity Checks

**Description:** This is a beginner tutorial on opening an IFC model, reading `IfcColumn` properties, joining external load data and understanding the difference between a load increase and a structural utilization ratio.

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
| Formats | Markdown + Jupyter Notebook + optional solution notebook. |
| License | MIT |

## Learning objectives
After this tutorial you will be able to:
1. Open an IFC file with IfcOpenShell and Read IFC units and identify columns.
2. Extract each IfcColumn element's GlobalId, structural mark, storey, material associations, cross-sectional dimensions, and length using IfcOpenShell.
3. Match extracted data to a structural report and an external load CSV.
4. Calculate/visualize *illustrative characteristic load differences*
5. Explain why a real `N_Ed/N_Rd` check needs verified design actions and resistances, and other structural checks.

## What you need
* Python 3.10 or newer and Jupyter Notebook.
* Required Python libraries: `pip install ifcopenshell pandas matplotlib`
* Save `tutorial_A3_extended.ipynb` in your working folder and place `26-08-STR.ifc` and both CSV files in a `data` subfolder within the same working folder.

## Files
```
README.md                                   this file
tutorial.ipynb                              the tutorial (start here)
data/report_table6_existing_columns.csv     existing column sizes typed from the structural report, Table 6
data/loads_example.csv                      INVENTED example loads, for practising only
data/26-08-STR.ifc                          (you add this file)
```

## Set up and run
1. Install: `py -m pip install notebook ipykernel ifcopenshell pandas matplotlib`.
2. Download the folder and place `26-08-STR.ifc` in `data/` alongside the provided CSV files.
3. Open `tutorial.ipynb` in Jupyter or VS Code (with Python and Jupyter extensions).
4. Restart the kernel, run the cells in order, and complete the exercises.
5. Give the feedback at the end of the notebook.

## Notes
* `loads_example.csv` contains made-up numbers and no real loads.
* The report table was typed by hand from the structural report. Check it against the original.
* Steps after this tutorial (load combinations, axial resistance, utilization) are not covered.

## Peer Review and Feedback
