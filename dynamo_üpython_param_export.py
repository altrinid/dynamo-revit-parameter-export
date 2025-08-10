# Dynamo Python Script (IronPython-compatible)
# Inputs:
#   IN[0] = elements (list of Revit elements)
#   IN[1] = param_names (list of strings)
#   IN[2] = csv_path (string)
#
# Output:
#   OUT = {"rows": int, "path": csv_path}

import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

import csv, os

elements = IN[0] or []
param_names = [p for p in (IN[1] or []) if p]
csv_path = IN[2]

def get_param_val(el, name):
    p = el.LookupParameter(name)
    if p is None:
        return ""
    if p.StorageType == StorageType.String:
        return p.AsString() or ""
    if p.StorageType == StorageType.Double:
        try: return p.AsDouble()
        except: return ""
    if p.StorageType == StorageType.Integer:
        try: return p.AsInteger()
        except: return ""
    if p.StorageType == StorageType.ElementId:
        try: return p.AsElementId().IntegerValue
        except: return ""
    try:
        return p.AsValueString() or ""
    except:
        return ""

rows = []
header = ["ElementId", "Category", "Name"] + param_names
for el in elements:
    try:
        eid = el.Id.IntegerValue
        cat = el.Category.Name if el.Category else ""
        name = el.Name if hasattr(el, "Name") else ""
        row = [eid, cat, name]
        for pname in param_names:
            row.append(get_param_val(el, pname))
        rows.append(row)
    except:
        pass

# ensure directory
folder = os.path.dirname(csv_path) if csv_path else ""
if folder and not os.path.isdir(folder):
    os.makedirs(folder)

if csv_path:
    with open(csv_path, "w") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(r)

OUT = {"rows": len(rows), "path": csv_path or ""}
