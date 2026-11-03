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
