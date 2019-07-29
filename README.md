# GalaxyDB
**GalaxyDB** is a public object database for **Super Mario Galaxy** where you can find information regarding every object in the game. You may contribute to this database by sharing your findings. The tools require **Python 3**.

# Objects
Each object's information is stored in a corresponding JSON file which consists of these properties:

| Field | Description |
| ----- | ----------- |
| InternalName | Internal object name |
| JapaneseName | Japanese name found in *ObjNameTable* |
| ClassName | Class name (for properties and more) |
| Name | Descriptive name |
| List | Preferred object list (see below) |
| Category | Category the object belongs to (for browsing purposes) |
| Notes | Additional notes on the object's functionality and usage |

Here's an example of *SunakazeKun*:
```
{
    "InternalName": "SunakazeKun",
    "JapaneseName": "スナカゼクン",
    "ClassName": "Sandstorm",
    "Name": "Tweester",
    "Games": "both",
    "List": "Obj",
    "Category": "enemy",
    "Notes": null
}
```

### List
Objects are sorted into various smaller lists. The following files are supported by the game:

| List | Description |
| ---- | ----------- |
| Obj | Any kind of object |
| ChildObj | Child objects |
| MapParts | MapParts objects |
| Start | Spawn points |
| PlanetObj | Gravity controllers |
| AreaObj | Area controllers |
| CameraCube | Camera areas |
| Sound | Sound controllers |
| DemoObj | Cutscene controllers |
| GeneralPos| Named positions |
| DebugMove | Debug positions (unused) |

### Categories
Object categories are defined in **Categories.json**. *TagName* is referenced in an object's *Category* field.
```
[
	{
		"TagName": "unknown",
		"Name": "Unknown"
	},
	{
		"TagName": "planet",
		"Name": "Planets"
	},
	{
		"TagName": "platform",
		"Name": "Platforms"
	},
	{
		"TagName": "transport",
		"Name": "Transport"
	},
...
]
```

# Classes
| Field | Description |
| ----- | ----------- |
| Name| Class name |
| Properties | Dictionary of supported Obj_args |
| Required | List of required settings |

Here's an example of *Sandstorm*:
```
{
    "Name": "Sandstorm",
    "Properties": {
		"Obj_arg0": {
			"Type": "bool",
			"Values": {},
			"Description": "Has debris?"
		}
	},
    "Required": [
		"CommonPath_ID"
	]
}
```
Each Obj_arg entry consists of a data type identifier, a dictionary of special-purpose values and a description of its function. In SMG1, Obj_args can be of the following three data types:
* **int**: 32-bit signed integer
* **float**: 32-bit floating point value
* **bool**: boolean value (*true* or *false*)
