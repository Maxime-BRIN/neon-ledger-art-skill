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
