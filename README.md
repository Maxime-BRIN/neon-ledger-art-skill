# Neon Ledger — Bibliothèque de Skills IA

Ce dépôt regroupe les Skills spécialisés du projet **Neon Ledger** pour Claude Code et Codex. Les Skills sont indépendants et utilisent des procédures à validation humaine.

## Catalogue

| Skill | Répertoire | Fonction |
| --- | --- | --- |
| **neon-ledger-environment** | [skills/neon-ledger-environment](skills/neon-ledger-environment/) | Conception et production d'assets 3D avec contrôle de la DA, Blender et intégration Godot |
| **neon-ledger-city-builder** | [skills/neon-ledger-city-builder](skills/neon-ledger-city-builder/) | Cadrage urbain, masterplans JSON/SVG, extensions, greybox, habillage, protections et contrôles |

## Installation

Copier individuellement le dossier du Skill choisi dans `.agents/skills/` (Codex) ou `.claude/skills/` (Claude Code). Le dossier du Skill doit contenir son `SKILL.md` et ses ressources.

Le **City Builder** peut recommander l'utilisation de **neon-ledger-environment** pour produire un modèle absent, mais **ne l'appelle pas automatiquement** : accord humain spécifique requis.

## Documentation historique — Skill d'assets

Skill réutilisable pour concevoir et produire **tout type d'asset** de Neon Ledger : architecture, rues, props, véhicules, intérieurs éventuels, signalétique et environnements.

## Principe
Une direction artistique globale cohérente ; des **profils par zone** ; un **brief par asset** ; trois phases à validation explicite.

1. Concept / art direction — un hero shot ou une planche adaptée à l'objet.
2. Modélisation / géométrie — Blender, UV, modularité **si pertinente**.
3. Textures PBR / lookdev / intégration Godot 4.

Aucune dimension, palette ou densité propre à Weakland ne doit être imposée à l'ensemble du monde.

## Utilisation
Copier `skills/neon-ledger-environment/` dans un chemin de skills pris en charge par l'agent utilisé, ou demander explicitement de lire son `SKILL.md`.

Exemple :
> Utilise `neon-ledger-environment`. Conçois un terminal de paiement pour le Secteur Haut, phase 1 seulement. Propose une DA cohérente avec Neon Ledger et signale les éléments de zone non définis.

Autre exemple :
> Utilise `neon-ledger-environment` pour une façade HLM Weakland 6 × 3 m ; mission 1, une image d'abord.

## Structure
- `SKILL.md` : déclenchement, routage, règles.
- `references/NEON_LEDGER_ART_BIBLE.md` : invariants transversaux.
- `references/ZONES.md` : profils de zones (Weakland initialement, autres à compléter).
- `references/PHASES.md` : missions 1 à 3.
- `references/QUALITY_GATES.md` : critères de validation.
- `templates/asset-brief.md` : brief minimal.
- `templates/validation-report.md` : rapport de preuve.
- `examples/requests.md` : exemples.

Ce dépôt contient des instructions, **pas** un générateur automatique d'assets 3D. Les licences des ressources externes sont à documenter individuellement.

## Environment V1.5 — production artistique accélérée (5 novembre 2026)

- **FAST / STANDARD / FULL à l'entrée** du Skill : contrôles proportionnés, banc réutilisé, pas de sourcing/Notion par micro-retouche.
- **Lookdev représentatif tôt** : une baie avec les matériaux de qualité finale avant la multiplication des modules.
- **Weathering selon DA** : vieillissement ponctuel, étendu ou dominant, grande échelle d'abord; aucune saleté universelle.
- **Faubourg des Traverses** : deux références de qualité matière approuvées (usé entretenu / négligé fortement dégradé), à relier aux vraies sources Godot locales. `REFERENCE_ONLY` tant que les presets ne sont pas vérifiés dans le workspace.
- **B19** : protocole de test de transfert dans `skills/neon-ledger-environment/references/B19_TRANSFER_TEST.md` ; pas de test Blender/Godot local prétendu.
- **City Builder** : décide où répartir les états d'entretien, Environment produit les variantes, sans lancement automatique.

Fichiers détaillés : `skills/neon-ledger-environment/references/WEATHERING.md`, `MATERIAL_PIPELINE.md`, `ITERATION_MODES.md` et `ZONES.md`.

## Environment V1.6 — sourcing et fabrication plus efficaces (5 novembre 2026)

- Routeur de production **réemploi → adaptation / import direct Godot → assemblage modulaire → création**, selon qualité artistique et coût total.
- **BlenderKit/Blendkit** intégré comme catalogue candidat de modèles et de matériaux, **sans téléchargement automatique ni licence présumée**.
- Petits lots d'assets cohérents, témoin de lookdev avant variantes, variations déterministes et respect des plans validés.
- Guide `skills/neon-ledger-environment/references/PRODUCTION_EFFICIENCY.md` : stratégie de pipeline unique, cache de validation, assembleur de façades, mesure du gain et critères d'arrêt.
- Aucun script du pipeline de jeu, plugin externe ou fichier Godot n'a été installé par cette modification du Skill. La mise en place doit être testée dans le workspace du jeu.
