# 41934 AdvanceBIM

**Group members**

- Gulshan Kumar  (s252589)
- Aida Amirbabaei (s216201)

**Group number**: 24

**Focus area**: Structure
## A2a: About our group
**Q: How much do you agree with the following statement: I am confident coding in Python**
A: 0. This is the first time that both of us are coding in Python
Our group’s focus area is columns, and we work as analysts

## A2b: Identify Claim
* **Selected Building:** Building #2601
* **Claim to Check:** Verification of structural integrity and cross-sectional dimensions of primary load-bearing structural elements (beams and columns) against design requirements.
* **Description:** The report for Building #2601 specifies design requirements for load-bearing elements. We aim to verify whether the structural elements modeled in the OpenBIM IFC file meet the required geometric and material specifications (cross-sectional area, structural function, and material attributes).
* **Justification:** Ensuring structural safety and compliance is critical in early design phases. Automated verification prevents costly design errors and structural miscalculations before assembly.

## A2c: Use Case
* **How to check:** Extract beam and column geometry and material parameters from the IFC model, compare them against structural calculations/design limits, and highlight non-compliant elements.
* **Timing:** Conceptual and Detailed Design Phase.
* **Information required:** Geometric properties (length, width, depth, volume) and structural material properties.
* **Phase:** Design Phase.
* **BIM Purpose:** Analyse & Communicate.
* **BIM Use Case:** Structural Analysis & Model Checking / Rule Checking.

### Process BPMN Diagram
![BPMN Process Diagram](./IMG/A2c_process_diagram.svg)

## A2d: Scope the use case
The automated Python tool using `IfcOpenShell` will replace the manual verification stage. It will automatically parse the IFC model, identify `IfcBeam` and `IfcColumn` entities, extract structural dimensions and material properties, evaluate compliance against pre-defined structural criteria, and output an automated validation report.

![BPMN Scoped Diagram](./IMG/A2d_scoped_diagram.svg)

## A2e: Tool Idea
* **Description:** An open-source Python tool leveraging `IfcOpenShell` that scans an IFC model for structural load-bearing elements (`IfcBeam`, `IfcColumn`), verifies their cross-sectional properties and material data, and generates a compliance report for structural engineers.
* **Business Value:** Reduces manual checking time by over 80%, minimizes human error, and improves structural coordination across teams.
* **Societal Value:** Enhances structural safety, optimizes material usage to reduce concrete waste, and supports sustainable construction practices.

![Tool BPMN Diagram](./IMG/A2e_tool_diagram.svg)

## A2f: Information Requirements
* **Required Information:** Element structural classification, geometry (profile dimensions, length), structural load-bearing property flag, and material association.
* **IFC Location:** 
  * `IfcBeam` and `IfcColumn` entities
  * `IfcPropertySet` (e.g., `Pset_BeamCommon`, `Pset_ColumnCommon`)
  * `LoadBearing` attribute (Boolean)
  * `IfcMaterial` / `IfcMaterialSelect` via `IfcRelAssociatesMaterial`
* **In Model:** Yes, these standard elements and properties exist in standard IFC4 / IFC2X3 structural models.
* **IfcOpenShell Implementation Plan:**
  * Use `ifcopenshell.open()` to load the model.
  * Use `file.by_type('IfcBeam')` and `file.by_type('IfcColumn')` to filter structural elements.
  * Retrieve property sets using `ifcopenshell.util.element.get_psets()`.
  * Extract bounding box / quantities for geometric validation.

## A2g: Software License
* **Selected License:** MIT License
* **Justification:** The MIT License is a permissive open-source license that allows free use, modification, and distribution with minimal restrictions. It is ideal for educational OpenBIM tools and encourages collaboration within the AEC industry.
