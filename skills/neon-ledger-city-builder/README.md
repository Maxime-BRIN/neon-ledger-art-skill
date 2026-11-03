# Neon Ledger City Builder — Skill unique (V0.1)

Skill d'orchestration pour Claude Code / Codex : cadrage créatif guidé par l'utilisateur, masterplan JSON + SVG, extensions nommées avec registre global, construction greybox Godot, plan d'assets, habillage, qualité et protections.

**La V0.1 contient des règles opérationnelles, des schémas, un validateur géométrique et un générateur SVG.** Elle ne contient pas de générateur automatique de scènes Godot ni d'intégration Notion : ces actions sont réalisées par l'agent avec les outils et autorisations disponibles, puis contrôlées. Les validations humaines sont obligatoires entre les phases.

## Installer

Décompresser le dossier `neon-ledger-city-builder` dans :
- `.agents/skills/` (Codex)
- `.claude/skills/` (Claude Code)

Voir `references/INSTALLATION.md` pour détails et contrôle.

## Tester

À la racine du Skill :

```bash
python -m unittest discover -s tests -v
python scripts/validate_city.py examples/city_master_index.json
python scripts/render_masterplan_svg.py examples/zone_masterplan.json -o examples/zone_masterplan.svg
```

## Utiliser

> Utilise `neon-ledger-city-builder`. Je veux un grand quartier d'affaires avec trois gratte-ciel centraux, une place et des bureaux autour. Consulte le registre de ville, pose-moi les questions structurantes avec des propositions cohérentes, puis attends ma validation du cadrage avant le masterplan.

**Ne jamais remplacer les masterplans réels par les fichiers `examples/`** (démonstration fictive).
