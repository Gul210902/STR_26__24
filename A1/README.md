# 41934 AdvanceBIM

**Group members**

- Gulshan Kumar  (s252589)
- Aida Amirbabaei (s216201)

**Group number**: 24

**Focus area**: Structure

# Assignment A1 - Forensic BIM
**Identified Issues**:

Issue 1. "Inconsistent number of additional storeys"
  Related disciplines: Architecture and Materials/LCA
  Issue type: Design issue
  Affected systems: Floor and Structure
  IFC class: IfcBuildingStorey
  Evidence: Team 08 Client Report, pages 10, 24 and 40
  
- **Report reference**: Structural Report, p. 1, section 1.1.1

## Description of script
The script opens the IFC structural model (`25-06-D-STR.ifc`) and counts the number of `IfcBuildingStorey` elements. It checks the numbers of storeys in IFC model in order to verify the claim of the report. The script also checks the storey name and compare it to the elevation in order to check the validity of the storey name.

### Analyst notes
- The script searches for all `IfcBuildingStorey` entities in the IFC model.  
- It prints the number of storeys and lists the name and the elevation of all the storeys.
- It asserts the claim of the report about the type and number of storeys  

### Manager notes
- Script used: [`check_storey.py`](./check_storey.py)  
- This script validates the reported number of storeys in the structural model and the type of each storey.
