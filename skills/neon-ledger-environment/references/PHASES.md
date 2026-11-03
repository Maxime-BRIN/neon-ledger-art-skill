# Trois missions, une seule à la fois

## Mission 1 — Art direction & concept
- Lire bible globale, profil de zone et références.
- Construire un brief **court** : objet, fonction, marqueurs de silhouette, matières, ambiance, composition et limites de fabrication.
- Créer **un concept principal** si outil image disponible ; selon l'asset : hero shot, vue produit ou cadrage environnement. Ne pas imposer une vue d'immeuble à un petit prop.
- Produire 3 choix visuels forts, 3 contraintes de réalisation et les 3 défauts majeurs.
- Sur retour négatif : préserver les acquis et corriger les 3 plus gros défauts ; pas de régénération massive automatique.
- Après approbation, produire si nécessaire orthographies, gros plans, variantes et dimensions de référence.
- Ne jamais confondre concept, plan à l'échelle et mesh.

## Mission 2 — Géométrie 3D Blender
- Utiliser uniquement les références **approuvées** ; indiquer celles introuvables.
- Choisir des unités métriques et des proportions physiques crédibles ; modularité seulement si utile.
- Véritables volumes et ouvertures lorsque requis, bevels, supports, points d'attache, shading, topologie adaptée au temps réel.
- UV0 ; UV secondaires seulement selon le besoin du pipeline. Pivots, orientations, conventions de nommage et matériaux préparatoires.
- Collisions pertinentes selon gameplay, séparées de l'apparence ; pas de collisions parasites.
- Produire et **exécuter** les scripts si Blender accessible, inspecter modèles et rendus clay. Ne pas inventer les validations.
- Exports glTF 2.0 / GLB, modèles source et métriques si l'environnement le permet.

## Mission 3 — PBR, lookdev, Godot 4
- Matériaux adaptés à la zone : BaseColor sRGB, Normal, Roughness, Metallic, AO si pertinent, Emission si nécessaire.
- UV et texel density vérifiés ; tileables, trim sheets, decals ou atlas selon le coût réel.
- Dégradations causales (eau, friction, chaleur, corrosion, entretien) ; ne pas salir automatiquement les zones aisées ou les objets neufs.
- Rendu neutre **et** éclairage contextuel. Le rendu doit rester convaincant sans post-traitement extrême.
- Import GLB dans Godot 4, contrôle de la hiérarchie, matériaux, dimensions, collisions, ombres et performance **si Godot accessible**.
- Captures issues du modèle réel, distinctes des images IA conceptuelles.
- Licences et origines documentées pour les ressources tierces.
