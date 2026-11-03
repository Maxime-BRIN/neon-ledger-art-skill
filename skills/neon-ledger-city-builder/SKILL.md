---
name: neon-ledger-city-builder
description: "Workflow unique pour cadrer, planifier, étendre, construire et habiller des zones urbaines de Neon Ledger sous Godot 4. Utiliser pour toute demande de création/extension de quartier, masterplan, SVG métrique, greybox, set dressing ou validation de zone. Exige des validations humaines aux jalons, protège les zones existantes et privilégie une source JSON canonique."
---

# Neon Ledger — City Builder

## Mission

Transformer **la demande créative de l'utilisateur** en quartiers urbains crédibles, raccordés, jouables et techniquement vérifiés, sans imposer une direction artistique préfabriquée. Ce Skill constitue **un seul workflow** (et non quatre skills à installer). Il est utilisable par Claude Code et Codex. La description et la composition du quartier sont définies par l'utilisateur; l'agent propose des valeurs par défaut seulement en cas de manque.

## Ordre de priorité

1. Demandes explicites de l'utilisateur et autorisations spécifiques **dans la session courante**.
2. Interdiction de toucher à une zone approuvée sans autorisation humaine spécifique, localisée et documentée.
3. Contrats validés de la phase en cours; index de ville, masterplans canoniques, guides artistiques approuvés.
4. `AGENTS.md`, `CLAUDE.md`, conventions techniques et paramètres réels du projet Godot.
5. Recommandations de ce Skill, jamais substituées aux décisions créatives de l'utilisateur.

Si ces sources se contredisent, **arrêter les opérations concernées**, exposer le conflit et demander un arbitrage; ne pas choisir discrètement.

## Préalables obligatoires

1. Inspecter le dépôt et l'arborescence existants, `AGENTS.md`, `CLAUDE.md`, la version réelle de Godot, les scènes, le contrôleur de joueur, la caméra, les assets locaux et la zone ciblée. Ne pas inventer une installation, un outil ou une donnée.
2. Charger `data/city/city_master_index.json` s'il existe. Identifier les zones voisines, leurs connexions et leur statut; ne jamais réinitialiser un registre peuplé.
3. Rechercher les décisions approuvées et les documents du projet. Si un fichier manque, l'indiquer clairement; proposer une création/migration **sans écraser l'existant**.
4. Classer la demande : nouvelle zone / extension / révision autorisée / reprise / audit. Une extension est une **opération**, pas nécessairement un nouveau district.
5. Lire les références nécessaires, en premier `references/WORKFLOW.md`, `references/DATA_CONTRACT.md`, `references/QUALITY_GATES.md` et `references/PROTECTION.md`.

## Workflow à validations humaines obligatoires

| Phase | Production agent | Validation humaine avant progression |
| --- | --- | --- |
| 0 — Cadrage | Cahier des charges avec contraintes imposées, hypothèses et propositions par défaut; géographie et intentions | **APPROUVER_CADRAGE** |
| 1 — Masterplan | Modèle JSON canonique, **SVG lisible dérivé du JSON**, audit des raccords/flux/emprises, rapport | **APPROUVER_MASTERPLAN** |
| 2 — Greybox | Volumes Godot fidèles, mesures de scènes, tests de navigation avec personnage et caméra réels, captures | **APPROUVER_GREYBOX** |
| 3 — Direction artistique et assets | Guide d'ambiance local, plan d'habillage, inventaire, besoins et licences vérifiées | **APPROUVER_DA_ASSETS** |
| 4 — Habillage et vérification | Placement d'assets, éclairage, vues TPP, validation technique et artistique, corrections locales | **APPROUVER_HABILLAGE** |
| 5 — Gel | Finaliser index, version, preuve et état `locked`; publier le bilan | Validation de phase 4 requise; le gel ne peut être auto-approuvé |

L'agent peut travailler, vérifier et corriger **à l'intérieur de la phase autorisée**, sans franchir un jalon. Un silence, une absence de réponse ou une validation d'une autre phase **ne vaut jamais approbation**. Si le dialogue se coupe, reprendre au dernier jalon humain enregistré, pas plus loin. Les approbations ne sont pas des mécanismes de sécurité informatique : la protection requiert aussi revue de diff, permissions et Git.

## Questions de cadrage : initiative sans autoritarisme

- Séparer **imposé par l'utilisateur**, **inféré des quartiers existants**, **hypothèses** et **inconnues bloquantes**.
- Poser des questions ciblées **seulement** sur les choix majeurs dont la réponse peut substantiellement changer le quartier (taille, identité, nombre de tours, accès, densité, rapport au voisinage). Toujours proposer un **défaut concret et justifié** et permettre de le modifier.
- Les paramètres mineurs peuvent recevoir des valeurs de travail réversibles, présentées pour contrôle au jalon; **ne jamais présenter un défaut comme approuvé**.
- En cas de demande « grand quartier d'affaires, trois tours centrales, place et bureaux », conserver ces exigences; **ne jamais forcer** les dimensions, les matériaux ou une esthétique de Weakland. Recommander seulement des solutions compatibles avec le monde et les quartiers voisins.
- Si l'utilisateur demande une comparaison, proposer au plus 2–3 variantes réellement distinctes avant de choisir.

## Source de vérité et visualisation

- Un masterplan `zone_masterplan.json` contient les coordonnées **métriques locales X/Z**, origine mondiale X/Z, Y vertical dans Godot, gabarits, voies, points de raccord et parcours.
- Le SVG est une **vue de contrôle**, obligatoirement générée depuis le **même JSON** (script `scripts/render_masterplan_svg.py`). Il doit rester compréhensible : nord, échelle, limites, routes, IDs, emprises, hauteurs, repères, légende et, si besoin, vues partielles. Toute modification demandée sur le SVG se traduit d'abord en modification JSON, puis en régénération.
- Une donnée « emprise réservée » n'est pas une « emprise bâtie » : définir séparément `reserved_footprint` et `built_footprint`. Les retraits n'autorisent pas l'occupation des circulations.
- Ne pas déclarer « mathématiquement garanti » sans validation numérique et contrôle de la scène Godot réelle. Le SVG et la scène ne doivent pas être deux réalisations artistiques indépendantes.

## Registre central et extensions

- Maintenir `data/city/city_master_index.json`, avec un **ID immuable** pour chaque district et chaque zone, un nom lisible, une origine globale, dimensions, état, chemin de masterplan et profil DA. Ne jamais recycler un ID supprimé.
- Une extension reçoit un nouvel ID, un nom, un lien explicite vers les zones adjacentes et des connecteurs X/Z mesurés et testés; la même procédure de phases 0–5 s'applique.
- Avant de créer, rechercher chevauchements, coutures entre zones, évolution des routes, horizon visuel, continuité de styles et transitions raisonnables. Les transitions ne signifient pas uniformiser les quartiers.
- Une zone approuvée est **read-only par défaut**, y compris ses fichiers, géométries, scènes et connexions; se référer à `references/PROTECTION.md`.

## Godot et habillage

- Respecter Godot 4: **X/Z horizontal, Y vertical, 1 unité = 1 mètre**, sans réinterprétation des axes.
- Mesurer positions, tailles et collisions des instances **réellement chargées**. Exécuter des tests de navigation avec capsule/caméra existantes; une droite entre deux points n'est pas un test de parcours. Fournir des captures TPP et orthographiques réelles, ou dire explicitement qu'elles n'ont pas pu être produites.
- L'habillage doit raconter un usage plausible, et non disperser des props arbitraires; conserver lignes de vue, accès, dégagements et budget GPU. Le style vient de la fiche DA **approuvée du quartier**, pas d'une recette cyberpunk universelle.
- Pour les assets, réutiliser les modèles locaux; chercher si nécessaire des assets gratuits avec **licences et provenances vérifiées**; ne télécharger/intégrer des éléments externes ou écrire dans Notion que lorsque l'autorisation correspondante a été accordée. Tenir la liste « existants / nouveaux + source/licence / manquants ».
- Si un asset sur mesure est justifié, **proposer** `neon-ledger-art-skill` avec une mini-spécification; **ne jamais le déclencher automatiquement**. Voir `references/ASSETS_NOTION.md`.

## Livrables et transparence à chaque jalon

À chaque étape, afficher : (a) exigences satisfaites, (b) fichiers créés/modifiés, (c) preuves de contrôles, (d) erreurs/incertitudes, (e) **ce qui reste strictement inchangé**, (f) décision demandée (approuver / demander corrections / refuser). Ne jamais annoncer un test, téléchargement, écriture Notion, capture ou approbation non réalisés.

## Outils fournis

- `python scripts/validate_city.py examples/city_master_index.json` : contrôle local de cohérence sur les données d'exemple.
- `python scripts/render_masterplan_svg.py examples/zone_masterplan.json -o plan.svg` : plan SVG depuis le JSON, sans dépendance externe.
- `python -m unittest discover -s tests -v` : tests des validateurs.

Ces scripts valident une **partie des invariants géométriques**; ils ne remplacent pas les tests dans Godot, une validation de licence ou la décision humaine.

## Références à charger selon la tâche

- `references/WORKFLOW.md` — questions, livrables, jalons, reprise.
- `references/DATA_CONTRACT.md` — conventions, registre, IDs, données métriques.
- `references/MASTERPLAN.md` — urbanisme, SVG et mesures.
- `references/EXTENSIONS.md` — raccords, continuité, transitions.
- `references/GODOT_GREYBOX.md` — Godot et contrôle de proportions.
- `references/SET_DRESSING.md` — art direction et rendu.
- `references/ASSETS_NOTION.md` — sourcing, licences, Notion, Skill art externe.
- `references/QUALITY_GATES.md` — critères bloquants.
- `references/PROTECTION.md` — verrouillage et changement minimal.
- `references/INSTALLATION.md` — installation Claude Code et Codex.
