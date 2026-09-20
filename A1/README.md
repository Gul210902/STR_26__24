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

---------------------------------------------------------------------------------
## Issue 2 — Incorrect column dimension summary

* **Discipline:** Structure
* **Related discipline:** None
* **Issue type:** Design documentation and modelling issue
* **Affected system:** Structure
* **IFC class:** `IfcColumn`
* **Model checked:** `B308X.ifc`
* **IFC schema:** IFC4X3

### Issue description

The structural report provides inconsistent information about the largest
column cross-section. Table 3 lists column S114 with a cross-section of
520 × 200 mm. However, the written summary immediately below the table
states that the largest column cross-section is 450 × 200 mm.

Because 520 × 200 mm is larger than 450 × 200 mm, the written summary does
not correspond with the information presented in Table 3. This could lead
to incorrect structural assessment, modelling or quantity calculations.

### Report reference

* Team 08 Client Report, page 22, Table 3
* Team 08 Client Report, page 22, paragraph immediately below Table 3

### Fact-check method

The claim was checked in `B308X.ifc` using Python and IfcOpenShell. The script (issue_4_column_fact_check.py) extracted all `IfcColumn` objects, searched their names, tags and type information for S114, extracted their cross-section dimensions and identified the largest detected rectangular column section.

The generated output is available in (issue_4_column_results.txt).


### Script results

* **Total `IfcColumn` objects:** 211
* **Columns matching S114:** 0
* **Detected occurrences of 520 × 200 mm:** 0
* **Largest detected rectangular section:** 1090 × 200 mm
* **Occurrences of 1090 × 200 mm:** 8
* **Columns without extractable dimensions:** 0

| Source          | Column/description       | Cross-section |
| --------------- | ------------------------ | ------------: |
| Written summary | Reported largest column  |  450 × 200 mm |
| Table 3         | Column S114              |  520 × 200 mm |
| B308X IFC model | Column S114              |     Not found |
| B308X IFC model | Largest detected section | 1090 × 200 mm |

The IFC model also contains several sections larger than the value stated
in the written summary.

| Detected cross-section | Occurrences |
| ---------------------: | ----------: |
|          1090 × 200 mm |           8 |
|           760 × 200 mm |           1 |
|           640 × 200 mm |           3 |
|           580 × 200 mm |           3 |
|           400 × 390 mm |           2 |
|           360 × 330 mm |           2 |

### Fact-check conclusion

The report inconsistency is confirmed because Table 3 gives column S114 a
cross-section of 520 × 200 mm, while the paragraph below the table states
that the largest column cross-section is 450 × 200 mm.

The IFC model does not contain an `IfcColumn` with S114 in its name, tag,
object type or assigned type information. Therefore, the 520 × 200 mm
section listed for S114 cannot be traced to a specific IFC object.

The script also did not detect a 520 × 200 mm column section. Instead, it
detected several sections larger than 450 × 200 mm, with the largest
detected section being 1090 × 200 mm. Therefore, neither report value is
fully supported by the IFC model.

This indicates a documentation inconsistency and a modelling-information
issue. The missing S114 identifier prevents reliable traceability between
the report and the IFC model.

### Possible solutions

#### Design solution

The structural engineer should verify the dimensions of column S114 and
confirm the actual largest column cross-section. Table 3 and the written
summary should then be corrected so that they contain consistent values.

#### Modelling solution

Every structural column should have a consistent identifier in its IFC
`Name`, `Tag` or type information. Column S114 should be identifiable in
the model, and its profile dimensions should correspond with the verified
structural schedule.

The unusually large detected sections should also be visually inspected to
confirm whether they represent actual column profiles, compound elements or
bounding-box dimensions.

#### Tool solution

An IfcOpenShell validation script should compare column identifiers and
dimensions between structural reports and IFC models. It should flag missing
column identifiers, scheduled dimensions that do not occur in the model and
modelled sections that exceed the reported maximum.

