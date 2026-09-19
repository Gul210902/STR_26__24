# 41934 AdvanceBIM

**Group members**

- Gulshan Kumar  (s252589)
- Aida Amirbabaei (s216201)

**Group number**: 24

**Focus area**: Structure

# Assignment A1 - Forensic BIM
**Identified Issues**:
1. "Inconsistent existing storey count"
- Related disciplines: Architecture 
- Issue type: Design issue
- Affected systems: Floor, Space and Structure
- IFC class: IfcBuildingStorey

**Issue Description**:
The architectural and structural sections provide inconsistent descriptions of the existing building storeys. The architectural section states that Building 308 comprises three storeys: a ground floor, first floor and second floor. However, the structural section states that the building consists of a basement and only one floor above ground.

It is unclear whether the disciplines are using different names for the same levels or whether one level has been excluded from the structural assessment. This creates uncertainty about the structural levels, elements and loads included in the analysis.
  
**Report reference**: Team 08 Client Report, page 6, Section 1.1, and page 17, Section 2.

**Possible solution**

*Design solution:*
The architecture and structure teams should establish a common definition for every existing level based on its elevation and function. The agreed storey names and number of storeys should then be used consistently in all reports, drawings and structural calculations.

*Modelling solution:*
Each physical building level should be represented by the correct IfcBuildingStorey entity. Storey names, elevations and spatial containment should be checked to ensure that structural elements are assigned to the correct level.

*Tool solution:*
An IfcOpenShell script can extract all IfcBuildingStorey entities and display their names and elevations. The results can then be compared with the architectural and structural claims to determine the actual number and designation of storeys in the IFC model.

2. "Inconsistent number of additional storeys"
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

**Possible solution**

*Design solution:*
The project team should agree on one vertical-extension scenario and use
the same number of storeys in the architectural, structural and materials
reports. The structural engineer should then verify the beams, columns
and foundations using the loads from this agreed design.

*Modelling solution:*
The coordinated BIM model should contain the agreed number of
IfcBuildingStorey entities with consistent names, elevations and floor
geometry across all discipline models.

*Tool solution:*
An IfcOpenShell script can count the IfcBuildingStorey entities and
compare their names and elevations between discipline models. The script
should report missing, duplicated or inconsistent storeys.
