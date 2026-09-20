import bpy
import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.element
import ifcopenshell.util.unit
from collections import Counter
from pathlib import Path

# -------------------------------------------------------
# SETTINGS
# -------------------------------------------------------

IFC_PATH = r"D:\DTU\13 week - aug 26\41934\B308X.ifc"
TARGET_COLUMN = "S114"

# -------------------------------------------------------
# OPEN IFC MODEL
# -------------------------------------------------------

model = ifcopenshell.open(IFC_PATH)
unit_scale = ifcopenshell.util.unit.calculate_unit_scale(model)

columns = model.by_type("IfcColumn")


# -------------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------------

def safe_text(value):
    """Return an empty string when an IFC attribute is missing."""
    return str(value) if value is not None else ""


def get_column_type(column):
    """Return the assigned IFC type, if available."""
    return ifcopenshell.util.element.get_type(column)


def column_identification_text(column):
    """Combine identifiers that may contain S114."""
    column_type = get_column_type(column)

    values = [
        safe_text(column.Name),
        safe_text(column.Tag),
        safe_text(column.ObjectType),
        safe_text(column.Description),
    ]

    if column_type:
        values.extend([
            safe_text(column_type.Name),
            safe_text(column_type.Tag),
            safe_text(column_type.ElementType),
        ])

    return " | ".join(values)


def find_rectangular_profiles(column):
    """
    Find IfcRectangleProfileDef objects used by the column.
    Dimensions are returned in millimetres.
    """

    roots = []

    if column.Representation:
        roots.append(column.Representation)

    column_type = get_column_type(column)

    if column_type:
        representation_maps = getattr(
            column_type,
            "RepresentationMaps",
            None
        )

        if representation_maps:
            roots.extend(representation_maps)

    profiles = []
    processed_ids = set()

    for root in roots:
        try:
            entities = model.traverse(root)
        except Exception:
            continue

        for entity in entities:
            if entity.id() in processed_ids:
                continue

            processed_ids.add(entity.id())

            if entity.is_a("IfcRectangleProfileDef"):
                width_mm = float(entity.XDim) * unit_scale * 1000
                depth_mm = float(entity.YDim) * unit_scale * 1000

                smaller = min(width_mm, depth_mm)
                larger = max(width_mm, depth_mm)

                profiles.append((
                    round(larger, 1),
                    round(smaller, 1),
                    entity.ProfileName or "Unnamed profile"
                ))

    return profiles


def get_geometry_dimensions(column):
    """
    Estimate dimensions using the column geometry if no rectangular
    profile definition is found.
    """

    try:
        settings = ifcopenshell.geom.settings()
        shape = ifcopenshell.geom.create_shape(settings, column)

        vertices = shape.geometry.verts

        x_values = vertices[0::3]
        y_values = vertices[1::3]
        z_values = vertices[2::3]

        if not x_values or not y_values or not z_values:
            return None

        dimensions = [
            max(x_values) - min(x_values),
            max(y_values) - min(y_values),
            max(z_values) - min(z_values),
        ]

        # If dimensions appear to be in project units rather than metres,
        # convert them using the IFC unit scale.
        if max(dimensions) > 100:
            dimensions = [
                dimension * unit_scale
                for dimension in dimensions
            ]

        dimensions_mm = sorted([
            dimension * 1000
            for dimension in dimensions
        ])

        # For a normal vertical column, the two smallest dimensions
        # represent the cross-section.
        return (
            round(dimensions_mm[1], 1),
            round(dimensions_mm[0], 1),
            round(dimensions_mm[2], 1)
        )

    except Exception:
        return None


# -------------------------------------------------------
# ANALYSE COLUMNS
# -------------------------------------------------------

target_matches = []
section_distribution = Counter()
columns_without_dimensions = 0

for column in columns:

    identification = column_identification_text(column)
    profiles = find_rectangular_profiles(column)

    if profiles:
        for width, depth, profile_name in profiles:
            section_distribution[(width, depth)] += 1
    else:
        geometry_dimensions = get_geometry_dimensions(column)

        if geometry_dimensions:
            width, depth, height = geometry_dimensions
            section_distribution[(width, depth)] += 1
        else:
            columns_without_dimensions += 1

    if TARGET_COLUMN.lower() in identification.lower():
        target_matches.append((
            column,
            identification,
            profiles,
            get_geometry_dimensions(column)
        ))


# -------------------------------------------------------
# PREPARE RESULTS
# -------------------------------------------------------

results = []

results.append("FACT CHECK: COLUMN DIMENSION SUMMARY")
results.append("=" * 60)
results.append(f"Model checked: {Path(IFC_PATH).name}")
results.append(f"IFC schema: {model.schema}")
results.append(f"Total IfcColumn objects: {len(columns)}")
results.append(f"Target column: {TARGET_COLUMN}")
results.append(f"Target matches found: {len(target_matches)}")
results.append("")

results.append("REPORT CLAIMS")
results.append("-" * 60)
results.append(
    "Written summary: largest column cross-section = 450 x 200 mm"
)
results.append(
    "Table 3: column S114 cross-section = 520 x 200 mm"
)
results.append("")

results.append(f"RESULTS FOR {TARGET_COLUMN}")
results.append("-" * 60)

if not target_matches:
    results.append(
        f"No IfcColumn containing the identifier {TARGET_COLUMN} "
        "was found in Name, Tag, ObjectType or type information."
    )

for number, match in enumerate(target_matches, start=1):

    column, identification, profiles, geometry_dimensions = match

    storey = ifcopenshell.util.element.get_container(
        column,
        ifc_class="IfcBuildingStorey"
    )

    storey_name = (
        storey.Name
        if storey and storey.Name
        else "No storey identified"
    )

    results.append(f"Match {number}")
    results.append(f"GlobalId: {column.GlobalId}")
    results.append(f"Name: {column.Name}")
    results.append(f"Tag: {column.Tag}")
    results.append(f"Storey: {storey_name}")
    results.append(f"Identification information: {identification}")

    if profiles:
        for width, depth, profile_name in profiles:
            results.append(
                f"Rectangular profile: {width:.1f} x "
                f"{depth:.1f} mm"
            )
            results.append(f"Profile name: {profile_name}")

    elif geometry_dimensions:
        width, depth, height = geometry_dimensions

        results.append(
            f"Geometry-estimated cross-section: "
            f"{width:.1f} x {depth:.1f} mm"
        )
        results.append(
            f"Geometry-estimated length/height: {height:.1f} mm"
        )
        results.append(
            "Note: this is estimated from the geometric bounding box."
        )

    else:
        results.append(
            "No profile or usable geometry dimensions were found."
        )

    results.append("")


results.append("COLUMN SECTION DISTRIBUTION")
results.append("-" * 60)

if section_distribution:
    for section, count in sorted(
        section_distribution.items(),
        key=lambda item: (item[0][0] * item[0][1]),
        reverse=True
    ):
        width, depth = section

        results.append(
            f"{width:.1f} x {depth:.1f} mm: {count} occurrence(s)"
        )

    # Largest section according to cross-sectional area
    largest_section = max(
        section_distribution,
        key=lambda section: section[0] * section[1]
    )

    largest_width, largest_depth = largest_section

    results.append("")
    results.append(
        "Largest detected rectangular section by area: "
        f"{largest_width:.1f} x {largest_depth:.1f} mm"
    )

else:
    results.append("No column dimensions could be extracted.")

results.append("")
results.append(
    f"Columns without extractable dimensions: "
    f"{columns_without_dimensions}"
)


# -------------------------------------------------------
# DISPLAY AND SAVE RESULTS
# -------------------------------------------------------

report = "\n".join(results)

text_name = "Column_Dimension_Fact_Check.txt"

result_text = bpy.data.texts.get(text_name)

if result_text is None:
    result_text = bpy.data.texts.new(text_name)
else:
    result_text.clear()

result_text.write(report)

output_path = Path(IFC_PATH).with_name(
    "B308X_Column_Dimension_Fact_Check.txt"
)

output_path.write_text(report, encoding="utf-8")

print(report)
print(f"Results saved to: {output_path}")
