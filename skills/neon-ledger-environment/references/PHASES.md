# Trois missions — contrôles proportionnés et autonomie V1.6

## Routage des modes V1.4

Avant de commencer, lire `ITERATION_MODES.md`. Choisir FAST, STANDARD ou FULL suivant les dépendances réellement modifiées. Réutiliser les preuves toujours valides, les scènes/caméras et les sources déjà autorisées. Après concept approuvé et autorisation de production, missions 2–3 peuvent s'enchaîner **sans interruptions humaines internes** dans le périmètre autorisé; soumettre le livrable final à revue. Ne jamais transformer une retouche FAST en nouvel audit complet sauf anomalie détectée.

## Étape 0 — Sourcer avant une nouvelle création ou adaptation (FAST sur asset approuvé exempté)
- Appliquer `ASSET_SOURCING.md` : projet + Notion → sources gratuites → inspection et licence → décision RÉUTILISER, ADAPTER ou CRÉER.
- Si RÉUTILISER : présenter la source, son usage prévu, sa licence prouvée et les vérifications à effectuer ; pas de concept IA ni de remodélisation inutiles.
- Si ADAPTER : proposer un brief d'adaptation limité (meshes, matériaux, proportions, optimisation), avec preuve de droits de modification ; approuver ce brief avant les modifications.
- Si CRÉER : suivre les phases 1, 2 et 3 ainsi que le routage des références visuelles de `SKILL.md`.
- La recherche peut conclure `NOT_TESTED` si accès ou preuves absents ; pas de validation factice.



## Fidélité artistique transversale — V1.2

Lire `VISUAL_FIDELITY.md` et remplir `../templates/visual-fidelity-matrix.md` lorsque des concepts visuels approuvés existent ou qu'un brief demande une richesse de détails spécifique. La matrice suit les détails par famille, kit responsable, état de production, conformité de gabarit et importance TPP. Ne jamais clôturer la matrice au seul motif que la géométrie globale est correcte.

## Mission 1 — Art direction & concept
- Identifier d'abord le projet et appliquer `DA_ROUTING.md` : bible globale Neon Ledger uniquement si ce projet est confirmé; sinon DA du projet/prompt; si DA externe absente, question obligatoire et arrêt avant toute génération.
- **Pour la voie CRÉER uniquement, choisir d'abord la source de référence selon `SKILL.md`** : image pertinente fournie = la privilégier ; aucune image + outil image réellement disponible = générer d'abord un concept principal ; sans outil image (ou sur refus explicite de génération) = construire une référence textuelle précise, proposer son enrichissement lorsque le brief est vague.
- En cas de référence textuelle, expliciter les propriétés contrôlables (silhouette, dimensions, matériaux, assemblages, fixations, détails visibles, usage, usure, distance caméra), marquer les hypothèses et soumettre la version enrichie à approbation avant toute modélisation.
- Construire un brief **court** : objet, fonction, marqueurs de silhouette, matières, ambiance, composition et limites de fabrication.
- Pour la voie CRÉER, créer **un concept principal** si outil image disponible ; selon l'asset : hero shot, vue produit ou cadrage environnement. Ne pas imposer une vue d'immeuble à un petit prop.
- Pour Neon Ledger sans concept pertinent déjà approuvé : **produire un concept de base du nouvel asset en style cyberpunk Neon Ledger** si l'outil image est accessible, sans recopier d'éléments spécifiques d'une autre œuvre. Pour un autre projet, appliquer sa DA explicitée sans contamination cyberpunk; si absente, demander avant toute création.
- Produire 3 choix visuels forts, 3 contraintes de réalisation et les 3 défauts majeurs.
- Sur retour négatif : préserver les acquis et corriger les 3 plus gros défauts ; pas de régénération massive automatique.
- Après approbation, produire si nécessaire orthographies, gros plans, variantes et dimensions de référence.
- Ne jamais confondre concept, plan à l'échelle et mesh.
- **Gate art :** vérifier que le concept exprime réellement les marqueurs forts de DA demandés, pas simplement le bâti générique avec quelques accents lumineux; détailler les familles visibles à produire et celles qui relèvent d'un autre kit/phase.

## Lookdev témoin dès le début (V1.5)

Pour un bâtiment/kit nouveau : avant de multiplier les modules, construire **un témoin simple représentatif avec les matériaux de niveau final** et comparer dans Godot à la référence approuvée, à distance TPP et sous une lumière pertinente. Valider le caractère (entretien, couverture, intensité) sur ce témoin, puis étendre les modules. Cela évite 70 composants parfaitement modélisés mais trop propres. Les contraintes métriques font autorité; ne pas contourner d'emprises pour reproduire une image artistique.

Pour une adaptation de matériau sur mesh existant, sauter concept et modélisation si approuvés/unchanged; suivre FAST ou STANDARD et `WEATHERING.md` et `MATERIAL_PIPELINE.md`. L'objectif est un rendu visiblement satisfaisant à distance, pas une accumulation de normal maps.

## Production par familles et assemblage modulaire (V1.6)

Lire `PRODUCTION_EFFICIENCY.md` si la mission implique plusieurs assets ou façades. Après un témoin visuellement validé, mutualiser textures, modules, accessoires et matériaux; décliner des variantes utiles plutôt que construire chaque bâtiment indépendamment. Les assemblages paramétriques suivent le JSON canonique et les limites approuvées, **sans répétition automatique du même habillage partout**.

Préférer Godot seul pour une petite adaptation de prop/matière déjà compatible; Blender reste pertinent pour maillages, UV, rig, baking ou transformations géométriques. Chercher des assets externes seulement lorsque la création/adaptation le justifie, avec licences et autorisations exactes.

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
- Produire une capture du véritable assemblage 3D à angle proche du concept, ainsi qu'un rendu clay; évaluer profondeur, variation et densité perceptible de détails, par façade. Une ossature cohérente mais très pauvre en détail reste `GEOMETRY_PASS / VISUAL_INCOMPLETE` si les familles majeures du périmètre de cette phase sont absentes.
- Une primitive de blockout reste autorisée **uniquement si explicitement marquée provisoire** dans l'inventaire et le rapport ; elle interdit de présenter l'asset correspondant comme final.
- Conserver les choix d'optimisation : petits détails non structurants via normal maps ou decals plutôt que géométrie excessive.

## Mission 3 — PBR, lookdev, Godot 4
- Pour les assets réutilisés/adaptés, inspecter matériaux, textures, dépendances et licence avant import **si nouvelles sources ou preuves absentes**; réutiliser les preuves antérieures encore valides. Ne pas imposer un retexturing complet si les PBR existants sont conformes.
- Matériaux adaptés à la zone : BaseColor sRGB, Normal, Roughness, Metallic, AO si pertinent, Emission si nécessaire.
- UV et texel density vérifiés lors de leur création/modification ou du gate final; **ne pas refaire l'audit UV entier pour un simple changement de roughness sur UV inchangés**. Tileables, trim sheets, decals ou atlas selon le coût réel.
- Chaque surface visible reçoit un matériau PBR crédible, avec textures lorsque nécessaires ; les exceptions (matières uniformes ou shaders procéduraux justifiés) sont documentées. Éviter les simples couleurs plates sur surfaces riches.
- Dégradations causales (eau, friction, chaleur, corrosion, entretien) ; ne pas salir automatiquement les zones aisées ou les objets neufs.
- Passe de vieillissement **selon le contrat d'entretien approuvé** : ponctuel, étendu ou dominant. **« Non uniforme » n'implique pas « peu sale »**. Façade longtemps négligée = pollution et humidité dominantes possibles; conserver causes, couches, zones plus récentes et réponses par matière. Lire `WEATHERING.md` et agir **macro → moyen → micro**.
- Vérifier le dressing visible dans la référence : plantes, props, textiles, enseignes, graffitis abstraits/illisibles par défaut (aucun texte ni marque fictive non validés).
- Rendu neutre **et** éclairage contextuel pour le gate final FULL; en FAST choisir seulement la ou les vues utiles au défaut corrigé. Le rendu doit rester convaincant sans post-traitement extrême.
- Import GLB dans Godot 4, contrôle de la hiérarchie, matériaux, dimensions, collisions, ombres et performance **si Godot accessible**.
- Captures issues du modèle réel, distinctes des images IA conceptuelles.
- Comparer côte à côte la référence approuvée et le rendu final à hauteur de joueur, en signalant les différences de caméra/lumière et les trois écarts visuels dominants. Ajouter une vue sous éclairage neutre : le contraste et le bloom ne doivent pas masquer un manque de géométrie ou de matériaux. Vérifier K01–K04 selon la répartition approuvée, sans attendre d'un kit seul les détails réservés aux suivants.
- Licences et origines documentées pour les ressources tierces.
