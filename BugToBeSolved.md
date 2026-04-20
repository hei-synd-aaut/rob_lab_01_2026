<strong style="color: red;">Development document, you don't normally need it for this robotics lab.</strong>

# Mercredi 22 octobre 2025.

# Fichier Python NodeOneShotBasler
Il faut modifier le fichier pour retourner au système un offset arrondi au centième.

# Principal problème:
Il faut déterminer les zeros du système
    Idéalement en même temps que la synchro de la cinématique.

## MC_COORD_SYSTEM
## MC_COORD_SYSTEM.MCS
Reference to the applicable coordinate system: ACS, MCS, WCS, PCS, **default is MCS**.    

Problème avec Clearing manuel
Problème avec CheckAxes -> Mettre une alarme pour que cela fonctionne.

## Problème général
Généralisation des alarmes, c'est à dire Numéro d'ID.
-   Il faut mettre une explication.


## Init position MCS
Il faut clarifier et mettre un exemple pour initialiser la position 

## Kinematic Enable / Disable
Ne fonctionne pas toujours.


## Bug avec Gripper
-   Il faudrait vérifier pour que le gripper fonctionne toujours !

## Généralisation SC
-   Il faudrait une page pour récupérer tous les SC.

## Généralisation ErrorId
Utiliser ceci: 
(usiEmId := THIS^.UniqueID, usiCMId := 4);


## Gripper
Controller avec isOpen and isClosed --> puis alarme.

```iecst
   cmGripper        : CM_Gripper(usiEmId := THIS^.UniqueID, usiCMId := 1);
   cmModuleAxis_X   : CM_ModuleAxis_X(usiEmId := THIS^.UniqueID, usiCMId := 2);
   cmModuleAxis_Y   : CM_ModuleAxis_Y(usiEmId := THIS^.UniqueID, usiCMId := 3);
   cmModuleAxis_Z   : CM_ModuleAxis_Z(usiEmId := THIS^.UniqueID, usiCMId := 4);
```

## Errors at starting
Il faut que je retrouve la suppression des alarmes au démarrage.

## Group Reset Error
Il faut changer la logique.
Le GroupReset doit être activé par Reset ou Clear mais pas dans ErrorStop ! (oui mais, problème avec les axes en Reset....)

## A propos du mode manuel
-	Les commandes ACS ne sont disponibles que pour le mode manuel.
-	Ou pour la partie Resetting en manuel ET production

