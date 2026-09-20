import bpy
import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.util.unit
from collections import Counter
from pathlib import Path

IFC_PATH = r"D:\DTU\13 week - aug 26\41934\B308X.ifc"

# IFC classes relevant to the structural investigation
STRUCTURAL_CLASSES = [
    "IfcColumn",
    "IfcBeam",
    "IfcSlab",
    "IfcWall",
    "IfcFooting",
]

# Open the IFC model
model = ifcopenshell.open(IFC_PATH)

# Convert IFC project units to metres
unit_scale = ifcopenshell.util.unit.calculate_unit_scale(model)

# Extract and sort all building storeys
storeys = model.by_type("IfcBuildingStorey")

storeys = sorted(
    storeys,
    key=lambda s: (
        s.Elevation is None,
        s.Elevation if s.Elevation is not None else 0
    )
)

# Prepare element counts
storey_counts = {
    storey.id(): Counter()
    for storey in storeys
}

unassigned = Counter()

# Find the storey containing each structural element
for ifc_class in STRUCTURAL_CLASSES:
    for element in model.by_type(ifc_class):

        container = ifcopenshell.util.element.get_container(
            element,
            ifc_class="IfcBuildingStorey"
        )

        if container and container.id() in storey_counts:
            storey_counts[container.id()][ifc_class] += 1
        else:
            unassigned[ifc_class] += 1

# Prepare report
results = []

results.append("FACT CHECK: EXISTING STOREY COUNT")
results.append("=" * 55)
results.append(f"Model checked: {Path(IFC_PATH).name}")
results.append(f"IFC schema: {model.schema}")
results.append(f"Total IfcBuildingStorey objects: {len(storeys)}")
results.append("")

for number, storey in enumerate(storeys, start=1):

    name = storey.Name or "Unnamed"
    long_name = storey.LongName or "Not specified"

    if storey.Elevation is None:
        elevation = "Not specified"
    else:
        elevation_m = storey.Elevation * unit_scale
        elevation = f"{elevation_m:.3f} m"

    results.append(f"STOREY {number}")
    results.append(f"Name: {name}")
    results.append(f"Long name: {long_name}")
    results.append(f"Elevation: {elevation}")
    results.append(f"GlobalId: {storey.GlobalId}")
    results.append("Structural elements assigned to this storey:")

    for ifc_class in STRUCTURAL_CLASSES:
        count = storey_counts[storey.id()][ifc_class]
        results.append(f"  {ifc_class}: {count}")

    results.append("")

results.append("STRUCTURAL ELEMENTS WITHOUT A STOREY")
results.append("-" * 55)

for ifc_class in STRUCTURAL_CLASSES:
    results.append(f"{ifc_class}: {unassigned[ifc_class]}")

results.append("")
results.append("REPORT CLAIMS FOR MANUAL COMPARISON")
results.append("-" * 55)
results.append(
    "Architecture, page 6: Ground floor, first floor and "
    "second floor = 3 storeys."
)
results.append(
    "Structure, page 17: Basement and one floor above "
    "ground = 2 storeys."
)
results.append("")
results.append(
    "Compare these claims with the IFC storey names, elevations "
    "and structural element counts listed above."
)

report = "\n".join(results)

# Display results inside Blender
result_text = bpy.data.texts.get("Fact_Check_Results.txt")

if result_text is None:
    result_text = bpy.data.texts.new("Fact_Check_Results.txt")
else:
    result_text.clear()

result_text.write(report)

# Save results beside the IFC file
output_path = Path(IFC_PATH).with_name(
    "Fact_Check_Storey_Count.txt"
)

output_path.write_text(report, encoding="utf-8")

print(report)
print(f"Results saved to: {output_path}")