# Contrat de données canonique

## Repères

- Valeurs numériques en mètres; `x,z` sont horizontaux, `y` vertical dans Godot.
- `origin_global` donne le coin sud-ouest local de la zone dans le monde. Les emprises et positions dans le fichier `zone_masterplan.json` sont **locales**. Coordonnée monde = origine globale + coordonnée locale.
- `bounds.width_x` et `bounds.length_z` définissent le rectangle [0,width]×[0,length].
- Rectangles axis-alignés `{"min_x":0,"max_x":5,"min_z":0,"max_z":8}` : `min < max`.
- Les bâtiments doivent définir **deux** rectangles: `reserved_footprint` (réservation, peut inclure une cour/retrait) et `built_footprint` (volume réel, inclus dans la réservation). La collision avec une voie concerne **le built_footprint**; la réservation peut avoir des zones non bâties.
- Les `roads` comportent `segments` rectangulaires (les réservations circulables). Une route courbe ou complexe peut être décomposée en segments; des intersections positives entre segments ne constituent pas une collision interdite.
- `connectors`: points de frontière entre zones et leur largeur utile, avec `target_zone_id` si connu. Les positions des connecteurs sont en coordonnées locales.
- Les parcours `routes`: polylignes de points locaux. La validation fournie garantit qu'ils restent à l'intérieur d'une couverture de voie approximative, sans garantir les collisions Godot ni la tournabilité de la capsule.
- `pois`: repères visuels et narratifs. Les projections verticales/volumes décoratifs ne doivent jamais être confondus avec les emprises au sol.

## Structure recommandée dans le projet Godot

`data/city/city_master_index.json` : registre global, statut et références.

`data/city/zones/<zone-id>/zone_masterplan.json` : données canoniques de la zone.

`data/city/zones/<zone-id>/style_guide.json` : identité artistique approuvée de la zone.

`data/city/zones/<zone-id>/decisions.md` : décisions humaines et arbitrages.

`data/city/zones/<zone-id>/evidence/` : captures, rapports, mesures.

`world/zones/<zone-id>/` : scènes Godot. Adapter à l'organisation réellement existante; ne pas dupliquer un projet déjà structuré.

## Identifiants

- District: `DIST-001`, `DIST-002`... ; zone ou extension: `ZONE-001` etc. Un ID persiste malgré le renommage.
- Bâtiments `B01`, voies `V01`, points `P01` : uniques **dans la zone**, pas forcément dans toute la ville.
- Connexions interzones exprimées en ID de zone + ID de connecteur: `ZONE-001/C-NORTH`.
- Ne jamais réassigner un ancien identifiant à un autre objet. Le registre contient les IDs réservés ou archivés.

## Validation

- Le schéma JSON (dossier `schemas/`) décrit le format. Le script `validate_city.py` effectue des contrôles géométriques et référentiels supplémentaires.
- Le masterplan est source de vérité géométrique *après validation humaine*, mais n'est jamais auto-validé parce qu'il est JSON.
- Les coordonnées, dimensions, arcs d'accès et retraits doivent être publiés dans les livrables de phase 1, sans approximations cachées.
- Pour un masterplan trop grand, découper en **zones nommées** et produire une vue d'ensemble plus des plans détaillés; ne pas produire un SVG tellement dense qu'il devient inutilisable.
