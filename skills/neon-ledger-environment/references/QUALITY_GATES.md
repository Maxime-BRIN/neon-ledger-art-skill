# Quality gates — GO / NO-GO (Visual Fidelity V1.2)

## Proportionnalité V1.4

Lire `ITERATION_MODES.md` et enregistrer le mode choisi. Les gates ci-dessous sont **complets au jalon final FULL**; en FAST/STANDARD, ne relancer que les contrôles touchés ou invalidés. Des preuves précédentes pertinentes et toujours valides sont réutilisables. `NOT_TESTED` ne devient jamais `PASS` par héritage.

- **FAST :** 1 vue A/B réelle et contrôle runtime ciblé, source/géométrie inchangées vérifiées simplement, résumé bref. Ne pas recréer matrice de référence, 9 rendus, audit de licences de sources inchangées, mesure VRAM ou audit UV complet par défaut.
- **STANDARD :** changements locaux structurels/UV/shaders coûteux, tests ciblés, captures pertinentes et métriques liées aux risques.
- **FULL :** livraison `ART_READY`, publication/intégration, zone/kit final : preuves détaillées, performance et acceptation humaine.
- **Autonomie :** concept et périmètre de production explicitement approuvés permettent plusieurs corrections/missions internes sans nouvelle sollicitation; l'accord reste obligatoire pour toute modification canonique, transfert/acquisition non autorisés, élargissement du périmètre, changement de DA et livraison finale.
- Le gate de fidélité artistique reste impératif à la **livraison**, mais un FAST réussi ne clôture pas des éléments majeurs simplement différés.

## Gate rapide de convergence artistique V1.5

Avant de livrer le résultat de la mission, même en FAST, vérifier sur la capture réelle :

- La cible d'entretien est-elle lisible **immédiatement à distance TPP** et sous éclairage neutre si le matériau est l'enjeu ?
- L'intensité et la couverture approuvées sont-elles perceptibles, ou a-t-on réintroduit une patine minime par défaut ?
- Les grandes masses de salissure et les couches d'entretien dominent-elles le look lorsque le brief exige de la négligence importante ?
- Les matériaux sont-ils physiquement distincts (plâtre, acier peint, oxyde, pollution) et les défauts artificiels évités ?
- Le delta est-il significatif par rapport à la base, sans perte de fonctions, de forme ou de budget ?
- En l'absence de progrès, réessayer en interne ou signaler **une méthode bloquée**, sans s'arrêter simplement sur « encore trop propre ».

La comparaison ne garantit jamais `ART_READY` sans revue finale humaine. Préserver les exceptions de surfaces entretenues; ne pas saturer mécaniquement tous les éléments.

## Règle commune
La note auto-attribuée n'est pas une preuve. Il faut des livrables inspectables. **L'accord explicite** est requis au concept et à la livraison finale, et entre missions seulement en mode supervisé; le mode autonome ne franchit jamais un changement de périmètre non approuvé.

## Gate 0 — Décision sourcer / adapter / créer
- Preuve de recherche interne (fichiers du projet, catalogue Notion quand accessible) et externe lorsque les outils le permettent ; ne pas annoncer une recherche non exécutée.
- Pour chaque candidat retenu : lien vers **la fiche de l'asset précis**, auteur, preuve de licence, autorisation d'usage commercial/modification, éventuelle attribution, format, qualité du mesh et matériaux, coût d'adaptation, compatibilité Godot vérifiée ou non vérifiée.
- Décision motivée **RÉUTILISER / ADAPTER / CRÉER** ; éviter création si un asset convenable est disponible ; ne pas sélectionner sur la seule étiquette « gratuit ».
- Pas de téléchargement, d'intégration ou d'attribution de licence vérifiée en l'absence de preuve de droits suffisante. Respecter les limitations de redistribution dans les dépôts publics.
- Présenter la décision et obtenir l'accord requis avant les modifications de projet.
- Les voies RÉUTILISER / ADAPTER n'exigent pas de nouveau concept IA : appliquer gates de géométrie, PBR et Godot selon travaux réels, sans prétendre avoir créé l'asset.

## Gate 1A — choix de DA préalable à toute image (V1.3)

Lire `DA_ROUTING.md`. Enregistrer `project_identity`, `da_source`, `da_status` et `image_reference_status` :
- **Neon Ledger confirmé :** DA globale + DA de zone et concepts approuvés. En création originale sans image adéquate, outil disponible = concept image de base obligatoire avant modélisation, soumis à approbation. Le langage visuel recherché est un cyberpunk dense, habité et stratifié, dans l'esprit de la richesse de *Cyberpunk 2077* mais sans copie d'éléments protégés ni style imposé contre une DA locale approuvée.
- **Autre projet avec DA :** concept uniquement dans cette DA, sans transfert des invariants artistiques propres à Neon Ledger.
- **Autre projet sans DA :** `BLOCKED_NEEDS_DA` jusqu'à réponse explicite de l'utilisateur; pas d'image ni de modélisation par supposition.
- **Projet incertain :** demander confirmation; le nom du Skill ne démontre pas l'identité du dépôt.
- **Référence déjà approuvée :** ne pas créer une image concurrente sans demande. **Outil indisponible :** le signaler, proposer voie textuelle seulement après définition de la DA.
- Une image générée est un **concept proposé**, jamais l'approbation humaine ni la preuve du modèle 3D.

## Gate 1 — source de référence et disponibilité des images
- Vérifier d'abord le gate DA 1A ci-dessus. Identifier la voie suivie : **image utilisateur/projet**, **concept IA généré**, ou **spécification textuelle enrichie** ; consigner l'origine, le caractère proposé ou approuvé, et les limites.
- Une image pertinente fournie prévaut sur une nouvelle génération automatique ; **pour la voie CRÉER uniquement**, une génération est obligatoire en l'absence d'image pertinente, si l'outil est réellement disponible et si l'utilisateur ne l'a pas exclue.
- Si aucune image ne peut être générée, une **référence textuelle approuvée** constitue un livrable valide de phase 1 : ne pas déclarer la gate bloquée pour seule absence d'image. Vérifier que les éléments observables sont assez précis pour être contrôlés au rendu.
- Pour une référence textuelle, remplacer les comparaisons visuelles source/rendu impossibles par une **matrice critères textuels approuvés / rendu réel / écarts / preuves**. Ne jamais inventer un côte-à-côte ou une capture.
- La génération d'une image ou l'enrichissement textuel ne valent **jamais** approbation implicite pour passer à la modélisation.

## Visual Fidelity & Detail Gate V1.2 — transversal et bloquant

Lire `VISUAL_FIDELITY.md` et présenter la matrice `../templates/visual-fidelity-matrix.md`. Distinguer **géométrie validée** de **rendu fidèle à la référence approuvée** : le volume d'un bâtiment ou 70 modules conformes ne suffisent pas si les détails essentiels attendus par **la portée du kit courant** sont absents.

- `MAJOR` : façade générique incompatible avec le concept approuvé; commerce sans identité lorsqu'il relève du kit livré; grands réseaux/équipements/signaux architecturaux de référence supprimés sans arbitrage; répétition mécanique contradictoire avec le brief; pseudo-détails en plans plats quand ils modifient la silhouette.
- `BLOCKER` : modification non autorisée des emprises, ouvertures ou gabarits; détail mettant en échec la largeur utile/TPP; source concept IA prétendue mesh final; ressource tierce intégrée sans preuve de droits.
- **No-Go ART_READY** en présence d'un `MAJOR` non corrigé sur les éléments inclus dans la portée approuvée. **Différer proprement** un besoin appartenant à K02/K03/K04 avec ID, kit propriétaire, dépendance et approbation humaine; ne pas le compter comme réalisé, mais ne pas faire échouer K01 pour un détail explicitement commandé plus tard.
- Preuves : côte à côte images de référence / captures du mesh réel sous caméra comparable + vue neutre + TPP Godot si accessible; état réel de chaque famille; 3 écarts dominants, statut avant/après et impact performance.
- La fidélité **ne se note pas au pixel près**, et aucune quantité décorative ni palette néon universelle n'est imposée. Elle est évaluée par silhouette, identité, profondeur, densité pertinente, lisibilité des usages et vie perçue selon le concept local.
- Les concepts générés sont **artistiques**, non cotés. Toute saillie de toiture, garde-corps, enseigne ou support hors emprise validée doit être adapté ou soumis à autorisation, sans contournement silencieux.

## Inventaire de référence — passe obligatoire
- Avant la modélisation, lister les éléments visibles et jugés significatifs de la référence approuvée : géométrie, props, végétation, textiles, signalétique, graffitis, équipements, salissures, corrosion.
- Pour chacun, renseigner : **présent dans la référence / modélisé / matérialisé ou texturé / vérifié visuellement / omis volontairement (raison)**. Les détails de matière peuvent être prévus pour la phase 3 et signalés « en attente » à la phase 2.
- Toute omission importante sans justification interdit **PASS**. Éviter l'exigence de reproduction au pixel près : prioriser ce qui est visible à la distance de caméra, la silhouette et le storytelling.
- Produire une comparaison **côte à côte référence / vrai rendu** lorsqu'une image de référence existe ; sinon utiliser la matrice des critères textuels approuvés, sans inventer de comparaison. Pour la réutilisation d'un modèle, comparer également la fiche/source aux rendus réels. à hauteur de joueur, avec cadrage, focale et lumière aussi comparables que possible ; indiquer les différences de perspective et les éléments que la comparaison ne permet pas de juger.
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
- Inventaire de référence et matrice visuelle renseignés ; détails majeurs relevant de cette phase réellement produits, ou corrections/exception humaine explicites
- UV, normales, pivots, alignements contrôlés
- Collisions adaptées au gameplay ; jointures testées si modularité
- Rendu clay issu du modèle ; export GLB inspecté
- **Approbation utilisateur** pour texturing final en mode supervisé; en mode autonome autorisé, gate technique interne avant poursuite sans interrompre l'utilisateur

### Gate 3 — PBR / Godot
- Textures PBR réellement présentes, raccordées et correctement interprétées
- Rendus neutres et contextuels provenant du vrai modèle
- Inventaire de référence complété (dressing, props, textiles, végétation, salissures) ; toutes les omissions majeures justifiées
- Comparaison côte à côte référence / vrai rendu à hauteur de joueur et trois écarts dominants traités
- Validation artistique **distincte** de la validation technique : silhouette, richesse visuelle, storytelling et fidélité vérifiés selon la matrice; ne pas déclarer `ART_READY` avant disparition des `MAJOR` du périmètre livré
- Godot importé/testé **ou explicitement non vérifié**
- Performance mesurée quand possible, sans FPS imaginés
- Fichiers sources, licences et limitations documentés
- **Approbation finale utilisateur**

### Statuts
- PASS : critères techniques observés ; accord utilisateur documenté quand requis.
- NEEDS_USER_APPROVAL : sortie prête à être revue, pas encore approuvée.
- BLOCKED : problème bloquant décrit avec preuves et étape de correction.
- NOT_TESTED : absence d'outil ou de preuve ; jamais équivalent à PASS.
