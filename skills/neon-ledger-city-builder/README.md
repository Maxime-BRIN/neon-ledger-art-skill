# Neon Ledger City Builder — Skill unique (V0.4)

Skill d'orchestration pour Claude Code / Codex : cadrage créatif guidé par l'utilisateur, masterplan JSON + SVG, extensions nommées avec registre global, construction greybox Godot, plan d'assets, habillage, qualité et protections.

**La V0.4 conserve des règles opérationnelles, des schémas, un validateur géométrique et un générateur SVG.** Elle ne contient pas de générateur automatique de scènes Godot ni d'intégration Notion : ces actions sont réalisées par l'agent avec les outils et autorisations disponibles, puis contrôlées. Les validations humaines sont obligatoires entre les phases.

## V0.4 — 100 % des besoins essentiels avant habillage

La phase 3 doit poursuivre les recherches et propositions d'acquisition/création **pour chaque besoin essentiel**, plutôt que clôturer le travail avec un diagnostic incomplet. Il faut distinguer `solutions identifiées X/N` de `ressources réellement prêtes Y/N`. L'entrée en phase 4 et la demande d'`APPROUVER_DA_ASSETS` nécessitent **Y=N**, soit **50/50** sur le périmètre actuellement défini pour le Faubourg des Traverses. Les recherches sont actives, les téléchargements et créations demandent une autorisation spécifique, et toute impossibilité conduit à `BLOCKED` plutôt qu'à un succès fictif.

Références : `references/ASSET_COVERAGE_100.md` et `templates/asset-coverage-register.md`.

## V0.3 — Masterplan et habillage vérifiables

Le Skill intègre désormais une **revue urbanistique indépendante** : morphologie, hiérarchie des espaces, logique des implantations, asymétrie seulement si le brief la justifie, fonctions des espaces libres, progression TPP prévue, et conformité JSON/SVG. Les plans « bâtiments en grille autour d'une place centrale » doivent être critiqués lorsqu'ils contredisent le caractère organique demandé, même si la géométrie est valide. Voir `references/MASTERPLAN.md` et `templates/masterplan-design-review.md`.

## V0.2 — Habillage vérifiable\n\nL'agent doit analyser les références visuelles et les sous-zones, qualifier les assets existants FIT/ADAPT/REJECT/MISSING/PLACEHOLDER, rechercher des alternatives adaptées (avec autorisation et vérification des licences), proposer sans lancer automatiquement `neon-ledger-environment`, puis créer des micro-scènes fonctionnelles et vérifier le résultat par captures TPP avant/après. Un rendu insuffisant ou non testé ne doit pas être déclaré final. Voir `references/SET_DRESSING.md`, `references/QUALITY_GATES.md`, `templates/dressing-report.md` et `examples/weakland-dressing-audit.md`.\n\nCette version renforce les **instructions et critères d'acceptation**. Elle ne fournit pas de moteur autonome de recherche d'assets, de plugin Godot ni de reconnaissance d'image; ces capacités nécessitent les outils de l'agent.\n\n## Installer

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
