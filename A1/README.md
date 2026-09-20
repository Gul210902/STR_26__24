# 41934 AdvanceBIM

**Group members**

- Gulshan Kumar  (s252589)
- Aida Amirbabaei (s216201)

**Group number**: 24

**Focus area**: Structure

# Assignment A1 - Forensic BIM
**Identified Issues**:
## Issue 1 — Inconsistent existing storey count

- **Discipline:** Structure
- **Related discipline:** Architecture
- **Issue type:** Design coordination and modelling issue
- **Affected systems:** Floor, Space and Structure
- **IFC class:** `IfcBuildingStorey`
- **Model checked:** `B308X.ifc`
- **IFC schema:** IFC4X3

### Issue description

The architectural and structural sections provide inconsistent descriptions
of the existing building storeys. The architectural section describes three
storeys: ground floor, first floor and second floor. The structural section
describes a basement and only one floor above ground.

It is unclear whether the disciplines use different names for the same
levels or whether some levels were excluded from the structural assessment.

### Report references

- Team 08 Client Report, page 6, Section 1.1
- Team 08 Client Report, page 17, Section 2

### Fact-check method

The claim was checked in `B308X.ifc` using Python and IfcOpenShell. The
script extracted all `IfcBuildingStorey` objects and recorded their names,
elevations and assigned structural elements.

### Script results

| IFC storey | Elevation | Interpretation |
|---|---:|---|
| ES_Stue | 41.000 m | Ground floor |
| Temp. Level 1 | 41.000 m | Temporary/duplicate level |
| E1_1. sal | 44.670 m | First floor |
| Temp. Level 1 | 44.670 m | Temporary/duplicate level |
| E2_2. sal | 48.710 m | Second floor |
| ET_TAG | 51.420 m | Roof level |

The IFC contains six `IfcBuildingStorey` entities, but these do not represent
six separate occupied floors. It contains three clearly named occupied
floors, one roof level and two temporary storeys located at the same
elevations as other storeys.

### Fact-check conclusion

The IFC model supports the architectural statement because it contains a
ground floor, first floor and second floor.

The structural statement is not supported by the IFC model. No storey is
identified as a basement, and the IFC contains two clearly named floors
above the ground floor.

The fact-check therefore confirms an inconsistency between the structural
report and the IFC model. It also identifies a modelling issue because two
`IfcBuildingStorey` entities named “Temp. Level 1” duplicate the elevations
of the ground and first floors.

### Possible solutions

#### Design solution

The architectural and structural teams should agree on a coordinated level
schedule that clearly identifies the basement, occupied floors, technical
levels and roof.

#### Modelling solution

The temporary storeys should be reviewed and removed if they are unnecessary.
All storeys should use clear and consistent names, such as Basement, Ground
Floor, First Floor, Second Floor and Roof.

#### Tool solution

An IfcOpenShell validation script should group storeys by elevation and flag
duplicated levels, temporary names and differences between the report and
IFC model.

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
