# Extracting Column Data from IFC for Capacity Checks

## Summary
**Title:** Extracting Column Data from IFC for Capacity Checks

**Description:** This beginner tutorial shows structural analysts how to load an IFC model with IfcOpenShell, extract column dimensions, materials and storeys, and combine them with external load data in a pandas table for later capacity checks.

## Tutorial information
| | |
|---|---|
| Course | 41934 Advanced BIM, DTU (A3: Teach) |
| Group | 24: Gulshan Kumar (s252589), Aida Amirbabaei (s216201) |
| Focus area | Structural Analysis |
| Role / level targeted | Analyst, Level 1 (beginner) *(confirm level on the course roles page)* |
| BIM use | 08: Structural Analysis |
| Learning need | Read column data from an IFC model and combine it with external load data (from our A2f information requirements) |
| Time needed | About 45–60 minutes |
| Formats | Jupyter Notebook + this Markdown README |
| License | MIT |

## Learning objectives
After this tutorial you can:
1. Open an IFC file with IfcOpenShell and read its schema, units and number of columns.
2. Extract for every `IfcColumn` its GlobalId, mark, storey, material, cross-section and length.
3. Handle columns whose geometry is not a simple rectangle.
4. Combine the IFC data with an external load table and detect columns with missing load data.

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
2. Open `tutorial.ipynb` in Jupyter or VS Code.
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
