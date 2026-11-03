# Neon Ledger — Environment Art Skill

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
