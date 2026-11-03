# Quality gates — GO / NO-GO

## Règle commune
La note auto-attribuée n'est pas une preuve. Il faut des livrables inspectables, et **l'accord explicite de l'utilisateur** avant tout passage de phase.

## Inventaire de référence — passe obligatoire
- Avant la modélisation, lister les éléments visibles et jugés significatifs de la référence approuvée : géométrie, props, végétation, textiles, signalétique, graffitis, équipements, salissures, corrosion.
- Pour chacun, renseigner : **présent dans la référence / modélisé / matérialisé ou texturé / vérifié visuellement / omis volontairement (raison)**. Les détails de matière peuvent être prévus pour la phase 3 et signalés « en attente » à la phase 2.
- Toute omission importante sans justification interdit **PASS**. Éviter l'exigence de reproduction au pixel près : prioriser ce qui est visible à la distance de caméra, la silhouette et le storytelling.
- Produire une comparaison **côte à côte référence / vrai rendu** à hauteur de joueur, avec cadrage, focale et lumière aussi comparables que possible ; indiquer les différences de perspective et les éléments que la comparaison ne permet pas de juger.
- Identifier et traiter les **trois écarts dominants** avant de soumettre la phase. Ne pas utiliser une image IA indépendante comme preuve du modèle.

### Gate 1 — Concept
- DA commune reconnaissable, identité propre de l'asset/zone
- Fonction, silhouette, échelle et construction plausibles
- Référence principale existante, plus décisions et défauts identifiés
- La scène n'est pas simplement « objet banal + néons »
- **Approbation utilisateur** pour modéliser

### Gate 2 — Modélisation
- Fichiers 3D ouverts / inspectés ; dimensions et axes mesurés
- Détails indispensables réellement géométriques ; props et textiles lisibles à distance de jeu, aucun blockout caché comme asset final
- Inventaire de référence renseigné ; éléments importants modélisés ou omissions explicitement justifiées
- UV, normales, pivots, alignements contrôlés
- Collisions adaptées au gameplay ; jointures testées si modularité
- Rendu clay issu du modèle ; export GLB inspecté
- **Approbation utilisateur** pour texturing final

### Gate 3 — PBR / Godot
- Textures PBR réellement présentes, raccordées et correctement interprétées
- Rendus neutres et contextuels provenant du vrai modèle
- Inventaire de référence complété (dressing, props, textiles, végétation, salissures) ; toutes les omissions majeures justifiées
- Comparaison côte à côte référence / vrai rendu à hauteur de joueur et trois écarts dominants traités
- Validation artistique **distincte** de la validation technique : silhouette, richesse visuelle, storytelling et fidélité vérifiés
- Godot importé/testé **ou explicitement non vérifié**
- Performance mesurée quand possible, sans FPS imaginés
- Fichiers sources, licences et limitations documentés
- **Approbation finale utilisateur**

### Statuts
- PASS : critères techniques observés ; accord utilisateur documenté quand requis.
- NEEDS_USER_APPROVAL : sortie prête à être revue, pas encore approuvée.
- BLOCKED : problème bloquant décrit avec preuves et étape de correction.
- NOT_TESTED : absence d'outil ou de preuve ; jamais équivalent à PASS.
