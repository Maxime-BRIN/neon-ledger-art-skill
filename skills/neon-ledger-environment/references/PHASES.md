# Trois missions, une seule à la fois

## Étape 0 — Sourcer avant de créer (obligatoire pour les assets 3D)
- Appliquer `ASSET_SOURCING.md` : projet + Notion → sources gratuites → inspection et licence → décision RÉUTILISER, ADAPTER ou CRÉER.
- Si RÉUTILISER : présenter la source, son usage prévu, sa licence prouvée et les vérifications à effectuer ; pas de concept IA ni de remodélisation inutiles.
- Si ADAPTER : proposer un brief d'adaptation limité (meshes, matériaux, proportions, optimisation), avec preuve de droits de modification ; approuver ce brief avant les modifications.
- Si CRÉER : suivre les phases 1, 2 et 3 ainsi que le routage des références visuelles de `SKILL.md`.
- La recherche peut conclure `NOT_TESTED` si accès ou preuves absents ; pas de validation factice.



## Mission 1 — Art direction & concept
- Lire bible globale, profil de zone et références.
- **Pour la voie CRÉER uniquement, choisir d'abord la source de référence selon `SKILL.md`** : image pertinente fournie = la privilégier ; aucune image + outil image réellement disponible = générer d'abord un concept principal ; sans outil image (ou sur refus explicite de génération) = construire une référence textuelle précise, proposer son enrichissement lorsque le brief est vague.
- En cas de référence textuelle, expliciter les propriétés contrôlables (silhouette, dimensions, matériaux, assemblages, fixations, détails visibles, usage, usure, distance caméra), marquer les hypothèses et soumettre la version enrichie à approbation avant toute modélisation.
- Construire un brief **court** : objet, fonction, marqueurs de silhouette, matières, ambiance, composition et limites de fabrication.
- Pour la voie CRÉER, créer **un concept principal** si outil image disponible ; selon l'asset : hero shot, vue produit ou cadrage environnement. Ne pas imposer une vue d'immeuble à un petit prop.
- Produire 3 choix visuels forts, 3 contraintes de réalisation et les 3 défauts majeurs.
- Sur retour négatif : préserver les acquis et corriger les 3 plus gros défauts ; pas de régénération massive automatique.
- Après approbation, produire si nécessaire orthographies, gros plans, variantes et dimensions de référence.
- Ne jamais confondre concept, plan à l'échelle et mesh.

## Mission 2 — Géométrie 3D Blender
- Pour une adaptation approuvée, conserver autant que possible les géométries correctes et travailler uniquement sur les changements nécessaires ; ne pas refaire le modèle de zéro sans raison documentée.
- Utiliser uniquement les références **approuvées** ; indiquer celles introuvables.
- Choisir des unités métriques et des proportions physiques crédibles ; modularité seulement si utile.
- Véritables volumes et ouvertures lorsque requis, bevels, supports, points d'attache, shading, topologie adaptée au temps réel.
- UV0 ; UV secondaires seulement selon le besoin du pipeline. Pivots, orientations, conventions de nommage et matériaux préparatoires.
- Collisions pertinentes selon gameplay, séparées de l'apparence ; pas de collisions parasites.
- Produire et **exécuter** les scripts si Blender accessible, inspecter modèles et rendus clay. Ne pas inventer les validations.
- Exports glTF 2.0 / GLB, modèles source et métriques si l'environnement le permet.

### Passe obligatoire — fidélité géométrique et dressing (mission 2)
- Établir un **inventaire des éléments visibles** sur la référence approuvée avant de modéliser : détails architecturaux, props au sol/en façade, textiles, végétation, enseignes, tags et éléments techniques.
- Tout élément important et lisible à **5–15 m** doit avoir une silhouette reconnaissable. Un carton n'est pas un cube brut, un sac poubelle n'est pas une boîte, un linge n'est pas un simple plan rectangulaire ; adapter le niveau de complexité à sa taille à l'écran.
- Pour les textiles visibles : drapé crédible, attaches/fil/pinces quand discernables et épaisseur apparente si nécessaire ; les textures de tissu relèvent de la phase 3.
- Pour les équipements : supports et connexions crédibles, pas de câbles/tuyaux flottants.
- Une primitive de blockout reste autorisée **uniquement si explicitement marquée provisoire** dans l'inventaire et le rapport ; elle interdit de présenter l'asset correspondant comme final.
- Conserver les choix d'optimisation : petits détails non structurants via normal maps ou decals plutôt que géométrie excessive.

## Mission 3 — PBR, lookdev, Godot 4
- Pour les assets réutilisés/adaptés, inspecter matériaux, textures, dépendances et licence avant import ; ne pas imposer un retexturing complet si les PBR existants sont conformes.
- Matériaux adaptés à la zone : BaseColor sRGB, Normal, Roughness, Metallic, AO si pertinent, Emission si nécessaire.
- UV et texel density vérifiés ; tileables, trim sheets, decals ou atlas selon le coût réel.
- Chaque surface visible reçoit un matériau PBR crédible, avec textures lorsque nécessaires ; les exceptions (matières uniformes ou shaders procéduraux justifiés) sont documentées. Éviter les simples couleurs plates sur surfaces riches.
- Dégradations causales (eau, friction, chaleur, corrosion, entretien) ; ne pas salir automatiquement les zones aisées ou les objets neufs.
- Passe de vieillissement **localisé** : coulures sous rebords, climatiseurs et évacuations ; rouille aux fixations ; crasse aux pieds des murs ; tags sur surfaces accessibles. Éviter le bruit uniformément réparti.
- Vérifier le dressing visible dans la référence : plantes, props, textiles, enseignes, graffitis abstraits/illisibles par défaut (aucun texte ni marque fictive non validés).
- Rendu neutre **et** éclairage contextuel. Le rendu doit rester convaincant sans post-traitement extrême.
- Import GLB dans Godot 4, contrôle de la hiérarchie, matériaux, dimensions, collisions, ombres et performance **si Godot accessible**.
- Captures issues du modèle réel, distinctes des images IA conceptuelles.
- Comparer côte à côte la référence approuvée et le rendu final à hauteur de joueur, en signalant les différences de caméra/lumière et les trois écarts visuels dominants.
- Licences et origines documentées pour les ressources tierces.
