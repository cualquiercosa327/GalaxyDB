import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
import os

root = ET.Element("objects")
ncategories = ET.SubElement(root, "categories")

classes = {}

# Process categories
with open("Categories.json", "r") as f:
    categories = json.load(f)

for category in categories:
    ncategory = ET.SubElement(ncategories, "category")
    ncategory.attrib["id"] = category["TagName"]
    ncategory.text = category["Name"]

# Process classes
for classfile in os.listdir("Classes"):
    classfile = "Classes/" + classfile
    if not os.path.isfile(classfile):
        continue

    with open(classfile, "r", encoding="utf-8") as f:
        clazz = json.load(f)

    classes[clazz["Name"]] = clazz

# Process objects
for objfile in os.listdir("Objects"):
    objfile = "Objects/" + objfile
    if not os.path.isfile(objfile):
        continue

    with open(objfile, "r", encoding="utf-8") as f:
        obj = json.load(f)

    nobject = ET.SubElement(root, "object")
    nobject.attrib["id"] = obj["InternalName"]
    nattributes = ET.SubElement(nobject, "attributes")
    nattributes.attrib["games"] = obj["Games"]
    nattributes.attrib["list"] = obj["List"]
    nattributes.attrib["category"] = obj["Category"]
    njapanese = ET.SubElement(nobject, "japname")
    njapanese.text = obj["JapaneseName"]
    nclass = ET.SubElement(nobject, "classname")
    nclass.text = obj["ClassName"]
    nname = ET.SubElement(nobject, "name")
    nname.text = obj["Name"]
    nname = ET.SubElement(nobject, "notes")
    nname.text = obj["Notes"]

    clazz = classes[obj["ClassName"]]
    nproperties = ET.SubElement(nobject, "properties")
    nrequired = ET.SubElement(nobject, "required")

    for propname, property in clazz["Properties"].items():
        nproperty = ET.SubElement(nproperties, "property")
        nproperty.attrib["id"] = propname
        nproperty.attrib["type"] = property["Type"]
        ndescription = ET.SubElement(nproperty, "description")
        ndescription.text = property["Description"]
        nvalues = ET.SubElement(nproperty, "values")

        for valint, value in property["Values"].items():
            nvalue = ET.SubElement(nvalues, "value")
            nvalue.attrib["id"] = valint
            nvalue.text = value

    for required in clazz["Required"]:
        nsetting = ET.SubElement(nrequired, "str")
        nsetting.text = required

# Write XML file
dom = MD.parseString(ET.tostring(root, encoding="utf-8"))

with open("objectdb.xml", "wb") as f:
    f.write(dom.toprettyxml(encoding="utf-8"))
    f.flush()
