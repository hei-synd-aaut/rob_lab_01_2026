<strong style="color: red;">Development document, you don't normally need it for this robotics lab.</strong>



Pour dessiner le cercle ⭕️, j’ai:
- identifié empiriquement la position du gripper en position centrale 80 80.
- baissé arbitrairement la caméra en z à -50 pour avoir le qr code avec de la marge.
- identifiié les positions des angles du qr code sur l’image.
- dessiné un cercle ⭕️ qui passe par les 3 sommets.

Pour calibrer le système automatiquement il suffira de :
- placer la caméra en 80, 80 et-50 $basePosition$.
- mesurer la position de qr code $newPosition$.
- définir pcs tels que pcs = nouvelles positions-positions initiales.

:bulb: PCS contient les offsets en X,Y et Z, mais aussi les angles de rotation autour des axes X, Y et Z. Pour l'instant nous ne travaillons que sur 3 dimensions. L'angles autour de l'axe Z est possible car les pièces à placer sont rondes. Par contre, l'option autour des axes X et Y nécessiterai des axes supplémentaires sur le robot.

C’est finalement relativement simple.

## Principle
### To draw the circle ⭕️, I:
- empirically identified the gripper's position at the central 80° x 80° position.
- arbitrarily lowered the camera's Z-axis to -50° to get some leeway in the QR code.
- identified the positions of the QR code's corners on the image.
- drew a circle ⭕️ that passes through the three vertices.

### To calibrate the system automatically, simply:
- place the camera at 80°, 80°, and -50° using $basePosition$.
- measure the QR code's position using $newPosition$.
- define PCS such that $pcs$ = $newPosition - basePosition$.

:bulb: PCS contains the X, Y, and Z offsets, as well as the rotation angles around the X, Y, and Z axes. For now, we are only working in three dimensions. The angle around the Z axis is possible because the parts to be placed are round. However, the option around the X and Y axes would require additional axes on the robot.

Ultimately, it's relatively simple.