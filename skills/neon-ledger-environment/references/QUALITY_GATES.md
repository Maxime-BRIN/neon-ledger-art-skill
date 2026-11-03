# Quality gates — GO / NO-GO

## Règle commune
La note auto-attribuée n'est pas une preuve. Il faut des livrables inspectables, et **l'accord explicite de l'utilisateur** avant tout passage de phase.

### Gate 1 — Concept
- DA commune reconnaissable, identité propre de l'asset/zone
- Fonction, silhouette, échelle et construction plausibles
- Référence principale existante, plus décisions et défauts identifiés
- La scène n'est pas simplement « objet banal + néons »
- **Approbation utilisateur** pour modéliser

### Gate 2 — Modélisation
- Fichiers 3D ouverts / inspectés ; dimensions et axes mesurés
- Détails indispensables réellement géométriques
- UV, normales, pivots, alignements contrôlés
- Collisions adaptées au gameplay ; jointures testées si modularité
- Rendu clay issu du modèle ; export GLB inspecté
- **Approbation utilisateur** pour texturing final

### Gate 3 — PBR / Godot
- Textures PBR réellement présentes, raccordées et correctement interprétées
- Rendus neutres et contextuels provenant du vrai modèle
- Godot importé/testé **ou explicitement non vérifié**
- Performance mesurée quand possible, sans FPS imaginés
- Fichiers sources, licences et limitations documentés
- **Approbation finale utilisateur**

### Statuts
- PASS : critères techniques observés ; accord utilisateur documenté quand requis.
- NEEDS_USER_APPROVAL : sortie prête à être revue, pas encore approuvée.
- BLOCKED : problème bloquant décrit avec preuves et étape de correction.
- NOT_TESTED : absence d'outil ou de preuve ; jamais équivalent à PASS.
