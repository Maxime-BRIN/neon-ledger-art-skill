---
name: neon-ledger-environment
description: Direction artistique et production 3D cohérente avec Neon Ledger pour tous types d'assets, props, bâtiments, rues et environnements, avec phases concept, Blender, PBR et Godot 4. À utiliser dès qu'une création visuelle ou 3D doit respecter la DA du jeu.
---

# Neon Ledger Environment Art

Objectif : produire des visuels distinctifs et des assets techniquement exploitables, **sans uniformiser les quartiers ni confondre rendu séduisant et asset validé**.

## Charger seulement le nécessaire
1. Lire `references/NEON_LEDGER_ART_BIBLE.md`.
2. Lire `references/ZONES.md` pour la zone demandée, s'il existe un profil.
3. Lire `references/PHASES.md` uniquement pour la phase actuelle.
4. Pour une étape de validation, lire `references/QUALITY_GATES.md`.
5. Utiliser les modèles de `templates/` si le brief ou le rapport est absent.

## Routage du brief
Identifier : **type d'asset, zone, usage gameplay, échelle/dimensions, distance caméra, phase, contraintes disponibles, références existantes**.
- Ne pas inventer de lore ou de décisions de DA « officielles » pour une zone non documentée. Distinguer faits, hypothèses et propositions.
- Si une information manque sans bloquer : poser une hypothèse explicite et réversible ; si elle bloque réellement, demander uniquement le détail nécessaire.
- Les bâtiments modulaires demandent une grille ; les props uniques, véhicules et personnages **n'héritent pas** d'une grille de façade.
- Weakland ≠ tout Neon Ledger. Ne pas appliquer « HLM délabré, béton humide, néon magenta » par défaut à chaque asset.
- Préserver une identité commune : stratification urbaine, contrastes socio-économiques, technologies intégrées à leurs fonctions, signalétique diégétique, composition lisible à hauteur de joueur.
- Adapter le niveau de détails à la cible et à la distance caméra ; AAA est une ambition de rendu, pas une garantie.
- Prioriser **une sortie visuelle principale** par itération ; produire planches techniques et variantes après validation si elles sont utiles au type d'asset.
- Corriger les **3 défauts majeurs** plutôt que réécrire tout le prompt.

## Routage obligatoire des références — avant la phase 1
Déterminer pour **chaque asset**, avant tout concept ou modélisation, si une référence visuelle pertinente est fournie (image jointe, image de projet ou concept déjà approuvé), si l'agent dispose **réellement** d'un outil de génération d'images, et si le brief textuel est suffisamment précis. Une image générique d'ambiance n'est pas automatiquement une référence d'asset.
1. **Image pertinente fournie** : l'utiliser prioritairement, sans la remplacer ni régénérer par défaut. Identifier ses éléments visibles, son statut (proposée/approuvée) et ses limites. Si la référence est ambiguë, proposer une interprétation et solliciter validation ; ne pas traiter une image non approuvée comme canon.
2. **Aucune image pertinente + génération d'images disponible** : commencer obligatoirement la **phase 1 par un concept visuel généré**, adapté à l'objet (pour un prop : objet isolé lisible, silhouette, matériaux, détails fonctionnels ; pour une scène : cadrage pertinent). S'appuyer sur le brief et la DA documentée, **une image principale par asset/itération**, sans générer des dizaines de variantes. Présenter ce concept comme proposition et attendre son approbation explicite avant la phase 2.
3. **Aucune image pertinente + pas de génération d'images disponible** : poursuivre avec une **référence textuelle structurée** ; si la description utilisateur est déjà précise, la conserver et la compléter seulement sur les points de fabrication manquants. Si elle est vague, **proposer une version textuelle plus complète** (fonction, zone, silhouette, proportions, dimensions estimées, construction, matériaux, couleurs motivées, vieillissement, habillage, fixations, lisibilité à distance de jeu, limites et hypothèses), clairement étiquetée `PROPOSITION À VALIDER`. Ne pas inventer d'image ni affirmer en avoir généré. Demander approbation de cette référence textuelle avant la phase 2.
- **L'image n'est pas obligatoire si l'outil est absent** : une spécification textuelle approuvée vaut référence principale pour les gates, à condition de détailler les éléments contrôlables ; comparer alors le vrai rendu à cette liste de critères plutôt que prétendre produire un côte-à-côte visuel impossible.
- Si l'utilisateur demande explicitement de **ne pas générer d'image**, respecter ce choix et utiliser la voie textuelle.
- Pour un lot, traiter les assets individuellement et limiter les générations aux éléments nécessaires ; préserver les concepts existants déjà validés.
- Ce routage appartient à la **phase 1**, et ne contourne jamais les validations entre phases ni les contraintes de temps réel.

## Fidélité aux références visuelles
- Être fidèle à une référence approuvée signifie reproduire **aussi son habillage** (props, textiles, végétation, signalétique, graffitis, salissures), pas uniquement la silhouette et les ouvertures.
- Avant de déclarer une phase prête, confronter son rendu réel à l'inventaire de référence ; toute omission visible et importante doit être justifiée.
- Un élément de blockout non finalisé ne doit jamais être présenté comme un asset terminé. La complexité doit rester proportionnée à la distance caméra et au budget temps réel.
- Préférer des graffitis abstraits ou illisibles ; ne pas inventer de texte lisible ni de marque non validée.

## Production par jalons
- Phase 1 : concept et spécification visuelle ; **aucun faux modèle 3D**.
- Phase 2 : modélisation 3D, UV, pivots, unités, modules éventuels, collisions éventuelles ; produire des preuves réellement rendues.
- Phase 3 : matériaux PBR, vieillissement motivé, éclairage, export, contrôles Godot 4.
- **Validation explicite requise** avant de passer à la phase suivante.
- Avant d'écrire dans un projet existant : lire `AGENTS.md`, `CLAUDE.md` et les contraintes du dépôt ; ne pas modifier silencieusement les zones validées.
- Ne pas prétendre avoir exécuté Blender, ouvert Godot, produit une image, inspecté un fichier ou testé des FPS sans preuve.
- Distinguer **créé / exécuté / vérifié / non vérifié / bloqué**.

## Sortie courte
Indiquer asset + zone + phase + hypothèses importantes. Livrer les fichiers, les preuves et un statut : PASS, BLOCKED ou NEEDS_USER_APPROVAL. Ne produire un long audit que si une anomalie le justifie.

## Étape finale obligatoire — Image et catalogue Notion
À la clôture de **chaque production d'asset** (concept approuvé, prototype ou asset final), suivre `references/NOTION_ASSET_CATALOG.md`.
1. Produire ou sélectionner **une vraie image représentative de l'asset** ; privilégier un rendu du mesh réel dès qu'il existe. Ne pas présenter un concept IA comme une capture 3D.
2. Créer ou **mettre à jour sans doublon** la fiche de cet asset dans la base officielle Notion « ⛩️ Assets Neon Ledger ».
3. Renseigner les champs disponibles, notamment `Nom`, `Catégorie`, `Type`, `Usage`, `Chemin projet`, `Lien`, `Auteur`, `Statut`, `Contrôle technique`, `Décision / remarques` et les informations de licence vérifiables.
4. **Renseigner la propriété fichier `Aperçu` avec l'image**, et conserver également une image visible dans le **contenu de la page** lorsque nécessaire pour la galerie configurée sur « Aperçu de la carte : Contenu ».
5. Aucun `Statut = Intégré` sans test d'intégration Godot effectivement réalisé ; aucune `Licence vérifiée` sans preuve ; ne pas deviner les valeurs.
6. Confirmer le lien de la fiche Notion et les champs réellement mis à jour. En cas d'absence d'accès Notion ou d'échec d'upload, signaler l'étape bloquée et garder les fichiers prêts, sans annoncer une synchronisation réussie.

Cette synchronisation ne remplace pas la validation humaine entre phases. Une fiche peut exister dès la phase concept avec `Statut = Nouvel asset`, puis être enrichie aux phases suivantes.
