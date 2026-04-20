<strong style="color: red;">Development document, you don't normally need it for this robotics lab.</strong>

# Kinematic Activation

## How to select Coordinate System
That is that: 

> See documnentation of MC_MoveDirectAbsolute

You can select between :

| Name | Initial | Comment |
|------|---------|---------|
| MCS | x | machine coordinate system |
| WCS | | world coordinate system |
| PCS | | product coordinate system |
| ACS | | axis coordinate system |


```iecst

```

CoordSystem
MC_COORD_SYS MCS Reference to the applicable
coordinate system:
ACS, MCS, WCS, PCS
Default is MCS

MB_ActiveKinMCSP (FB)
FUNCTION_BLOCK MB_ActiveKinMCSP

Short description
This kinematics command option permanently activate a MCS (machine coordinate system) transformation for all motion commands until deactivate it or switch to another one MCS. Use MB_DeactiveKinMCSP to deactivate.

Functional description
You can set a offset/orientation for your MCS (machine coordinate system).
When active, all following motion command positions refer to this MCS.
Multiple MCS set can be predefined per kinematics. Currently, this function only working with robot kinematics.
Parameter description:
SetName: The name of the mcs offsets and orientation. The mcs have to be configured in the datalayer

Add mcs (motion/kin/<kin_name>/cfg/coord-systems/mcs) before calling this function.

# For PCS Product Coordinate System / TCP
See: documentation Motion App, 6.5.4 KinPCSP, KinPCSToolP - Command option for kinematic product
coordinate system

Note: TCP replace PCS
See KinToolLengthsP - Non static tool offset

## Set
A tool data record contains data for:
-   offset values: Δx, Δy, Δz,that describe the position of the tool zero point in relation to the tool center point (TCP)
● Units of the offset values Δx, Δy, Δz

# Activation of PCs
```json
{
    "groupName": "Pcs_1",
    "sets": [
        "QR_Code"
    ]
}
```
motion/kin/Robot/cmd/opt-pcs

```json
{
    "type":"object","value":
    {
        "permType":"PermOn",
        "setName": "Pcs_1"
    }
}

```
The parameter "permType" can assume the values "PermOn", “PermOff".

# Configuration of the PCS
motion/cfg/coord-systems/pcs/sets/QR_Code/offset-xyz


```JSON
{
    "setName": "QR_Code",
    "offsetXYZ": [
        2.2,
        1.1,
        0.56
    ],
    "orientation": [
        1,
        0,
        0
    ],
    "offsetAux": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ],
    "relativeToPCS": false,
    "offsetXYZUnits": [
        "mm",
        "mm",
        "mm"
    ],
    "orientationUnits": [
        "deg",
        "deg",
        "deg"
    ],
    "offsetAuxUnits": [
        "mm",
        "mm",
        "mm",
        "mm",
        "mm",
        "mm",
        "mm",
        "mm",
        "mm",
        "mm"
    ]
}

```