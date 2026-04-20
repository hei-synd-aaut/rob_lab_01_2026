
<strong style="color: red;">Development document, you don't normally need it for this robotics lab.</strong>


PCS access is done directly thru datalayer.

### Reading PCS positions

```datalayer
motion/kin/Robot/state/values/actual/pos/pcs
```

<div align="center">
    <img src="./img/PCS_Get_Positions.png"
         alt="Image lost: PCS_Get_Positions" 
         width="600">
    <figcaption>Get PCS position from datalayer</figcaption>
</div>

Using the struct of PCS in Node-RED

```js
var msg_x_pos = {payload: Math.round(msg.payload.pos[0] * 100) / 100};
var msg_y_pos = {payload: Math.round(msg.payload.pos[1] * 100) / 100};
var msg_z_pos = {payload: Math.round(msg.payload.pos[2] * 100) / 100};

return [msg_x_pos,
        msg_y_pos,
        msg_z_pos];
```

---

### Enabling PCS

<div align="center">
    <img src="./img/Enable_PCS.png"
         alt="Image lost: Enable_PCS" 
         width="600">
    <figcaption>Enable PCS from Node-RED</figcaption>
</div>

```js
// PCS On
var newMsg = {};
newMsg.payload = {
    "type":"object",
    "value": {
        "permType":"PermOn",
        "setName": "Pcs_1"
    }
}

return newMsg;
```

```js
// PCS Off
var newMsg = {};
newMsg.payload = {
    "type":"object",
    "value": {
        "permType":"PermOff",
        "setName": "Pcs_1"
    }
}

return newMsg
```

```js
// Write to
motion/kin/Robot/cmd/opt-pcs
```

### Using a PCS set
It means that PCS should be configured on the PLC/Motion


#### Default values on Unit 01




<!-- End of document -->


