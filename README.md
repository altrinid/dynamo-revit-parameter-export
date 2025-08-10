# Dynamo Revit — Parameter Export to CSV

A Dynamo graph for **Autodesk Revit** that exports selected element parameters to **CSV** using a single **Python Script** node.

## What it does
- Select elements by **Category** or from selection.
- Exports `ElementId`, `Category`, `Name` + any parameter names you list (e.g., `Type Name`, `Level`, `Fire Rating`).
- Writes a clean **CSV** you can open in Excel.

## Prerequisites
- Autodesk **Revit** (tested with 2022/2023)
- **Dynamo for Revit** 2.x (IronPython or CPython)

## Build the graph (5 minutes)
1. Open **Revit** → **Dynamo**.
2. Place nodes:
   - `Categories` → choose one (Walls/Doors/...)
   - `All Elements of Category`
   - `String` nodes for parameter names → collect with `List.Create`
   - `File Path` (CSV save path)
   - `Python Script` (single node)
3. Connect:
   - Elements → `IN[0]`
   - Param names list → `IN[1]`
   - CSV path → `IN[2]`
4. Open the Python node, paste code from `scripts/dynamo_python_param_export.py`, click **Accept**.
5. **Run**. CSV will be written to the chosen path.

## Example output
See [`docs/example_output.csv`](docs/example_output.csv).

| ElementId | Category | Name      | Type Name | Level  | Fire Rating |
|-----------|----------|-----------|-----------|--------|-------------|
| 123456    | Walls    | Basic 200 | Basic 200 | Level1 | REI60       |

## Files
- `scripts/dynamo_python_param_export.py` — code for the Python node
- `docs/example_output.csv` — example result
- `LICENSE`, `.gitignore`

## License
MIT

## Credits
Author: **Rodion Dykhanov**
