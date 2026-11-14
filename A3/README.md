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
4. Calculate/visualize **illustrative characteristic load differences**
5. Explain why a real `N_Ed/N_Rd` check needs verified design actions and resistances, and other structural checks.

## What you need
* Python 3.10 or newer and Jupyter
* `pip install ifcopenshell pandas`
* The course structural model `26-08-STR.ifc`. Put it in the `data/` folder.

## Files
```
README.md                                   this file
tutorial.ipynb                              the tutorial (start here)
data/report_table6_existing_columns.csv     existing column sizes typed from the structural report, Table 6
data/loads_example.csv                      INVENTED example loads, for practising only
data/26-08-STR.ifc                          (you add this file)
```

## How to run
1. Download this folder and add `26-08-STR.ifc` to `data/`.
2. Open `tutorial.ipynb` in Jupyter or VS Code (with the Python and Jupyter extensions installed).
3. Run the cells from top to bottom. Do the three "Your turn" exercises.
4. Give feedback with the questions at the end of the notebook.

## The three steps
1. **Load the IFC model**: open the file, check schema and units.
2. **Extract column geometry and material**: storey, material, profile dimensions, quantities, and a check against the report.
3. **Import existing and additional loads**: read a CSV and join it to the IFC data using the column mark.

## Notes
* `loads_example.csv` contains made-up numbers and no real loads.
* The report table was typed by hand from the structural report. Check it against the original.
* Steps after this tutorial (load combinations, axial resistance, utilization) are not covered.
