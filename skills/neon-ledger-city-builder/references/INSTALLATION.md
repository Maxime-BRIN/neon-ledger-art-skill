# Installation

Copier **le même dossier** `neon-ledger-city-builder` (tout son contenu, y compris les scripts) dans :

- Codex : `.agents/skills/neon-ledger-city-builder/`
- Claude Code : `.claude/skills/neon-ledger-city-builder/`

Si les deux outils travaillent sur le même dépôt, choisir une source unique et créer des liens symboliques/jonctions ou une synchronisation contrôlée; vérifier la prise en charge sous Windows. Ne pas entretenir deux copies divergentes.

Le Skill ne fournit **pas** à lui seul Godot, un MCP, une capture d'écran, Blender, GitHub ou le connecteur Notion. Leurs outils doivent être installés et disponibles dans l'environnement de l'agent. Les validations humaines sont des actions dans la conversation, pas des valeurs que l'agent peut inventer dans un fichier.

Commandes de vérification après copie :

```sh
python -m unittest discover -s tests -v
python scripts/validate_city.py examples/city_master_index.json
python scripts/render_masterplan_svg.py examples/zone_masterplan.json -o examples/zone_masterplan.svg
```

Exécuter à la racine du dossier Skill. Pour un vrai projet, utiliser ses chemins `data/city/...`. Le fichier `examples` est **fictif** et ne doit pas remplacer Weakland ou le registre réel.

Déclenchement : « Utilise neon-ledger-city-builder pour concevoir un nouveau quartier d'affaires... » ou « Propose une extension de Weakland ... ». Le Skill commence par vérifier le registre et établir le cadrage, **sans commencer Godot avant les validations humaines**.
