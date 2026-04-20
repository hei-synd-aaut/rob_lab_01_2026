"""
Applies adaptive thresholding to grayscale image using Gaussian-weighted sum of neighborhood values.

Parameters:
    gray: Input grayscale image
    255: Maximum value to use with the threshold (white)
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C: Adaptive method - Gaussian-weighted sum of neighborhood
    cv2.THRESH_BINARY: Thresholding type - binary threshold
    11: Size of pixel neighborhood used to calculate threshold value (must be odd)
    2: Constant subtracted from weighted mean (C)

Returns:
    Binary image where pixels above threshold are set to 255 (white), 
    and pixels below threshold are set to 0 (black)
"""


En bref — préférez des blocs try/except petits et ciblés plutôt que des imbrications inutiles.

Principes :
- Attraper des exceptions spécifiques (éviter bare except/Exception).
- Séparer les blocs si les opérations sont indépendantes.
- Imbriquer uniquement si la seconde opération dépend nécessairement du succès de la première.
- Utiliser else pour le code qui doit s'exécuter quand aucun exception n'est levée, et finally pour le nettoyage.
- Journaliser ou relancer si vous ne pouvez pas gérer l'erreur correctement.

Exemples :

Mauvaise pratique (imbrication inutile) :
```python
try:
    a = op1()
    try:
        b = op2(a)
    except ValueError:
        handle_value_error()
except IOError:
    handle_io_error()
```

Bonne pratique — opérations indépendantes :
```python
try:
    a = op1()
except IOError as e:
    handle_io_error(e)

try:
    b = op2()
except ValueError as e:
    handle_value_error(e)
```

Bonne pratique — dépendance entre opérations (imbrication justifiée, ou else) :
```python
try:
    a = op1()
except IOError as e:
    handle_io_error(e)
else:
    try:
        b = op2(a)
    except ValueError as e:
        handle_value_error(e)
```

Règle courte : préférez la clarté et des exceptions ciblées — imbriquez seulement quand la logique l'exige.

```python
# Extracting the 'cxcy' value from qrInfo
qr_info = (('https://www.hevs.ch/fr/hautes-ecoles/haute-ecole-d-ingenierie/',), 
           [{'confidence': 0.9536973834037781, 
             'bbox_xyxy': array([1977.7, 884.82, 2851.6, 1763.6], dtype=float32), 
             'cxcy': (2414.64404296875, 1324.227783203125)}])

# Accessing 'cxcy'
cxcy_value = qr_info[1][0]['cxcy']
print(cxcy_value)
```

```python
import numpy as np

# Coordinates of the polygon
polygon = np.array([[1976.2, 181.6],
                    [2848, 181.6],
                    [2848, 1090.4],
                    [1937.6, 1056.2]])

# Calculate the orientation in degrees
def calculate_orientation(polygon):
    # Get the first two points
    p1 = polygon[0]
    p2 = polygon[1]
    
    # Calculate the angle in radians
    angle_rad = np.arctan2(p2[1] - p1[1], p2[0] - p1[0])
    
    # Convert to degrees
    angle_deg = np.degrees(angle_rad)
    
    return angle_deg

orientation = calculate_orientation(polygon)
print(f'Orientation of the polygon on the X-axis: {orientation}°')
```