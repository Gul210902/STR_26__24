# 41934 AdvanceBIM

**Group members**

- Gulshan Kumar  (s252589)
- Aida Amirbabaei (s216201)

**Group number**: 24

**Focus area**: Structure

# Assignment A1 - Forensic BIM
**Identified Issues**:
1. "Inconsistent number of additional storeys"
- Related disciplines: Architecture and Materials/LCA 
- Issue type: Design issue
- Affected systems: Floor and Structure
- IFC class: IfcBuildingStorey

**Issue Description**:
The number of proposed additional storeys is not coordinated between
the disciplines. The architectural section states that one-and-a-half
storeys will be added, while the materials section assumes the addition
of two complete floors.

This creates an uncertain structural design basis because the number of
storeys determines the permanent loads, imposed loads and forces applied
to the existing columns and foundations. Page 24 provides a general
structural limit of two to three additional floors but does not establish
which design option must be analysed.
  
**Report reference**: Team 08 Client Report, pages 10, 24 and 40

**Possible solution**:
*Design solution*
The project team should agree on one vertical-extension scenario and use
the same number of storeys in the architectural, structural and materials
reports. The structural engineer should then verify the beams, columns
and foundations using the loads from this agreed design.

*Modelling solution*
The coordinated BIM model should contain the agreed number of
IfcBuildingStorey entities with consistent names, elevations and floor
geometry across all discipline models.

*Tool solution*
An IfcOpenShell script can count the IfcBuildingStorey entities and
compare their names and elevations between discipline models. The script
should report missing, duplicated or inconsistent storeys.
