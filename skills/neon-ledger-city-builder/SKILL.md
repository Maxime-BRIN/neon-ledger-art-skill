---
name: neon-ledger-city-builder
description: "Workflow unique pour cadrer, planifier, étendre, construire et habiller des zones urbaines de Neon Ledger sous Godot 4. Utiliser pour toute demande de création/extension de quartier, masterplan, SVG métrique, greybox, set dressing ou validation de zone. Exige des validations humaines aux jalons, protège les zones existantes et privilégie une source JSON canonique."
---

# Neon Ledger — City Builder (V0.4)

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
| 1 — Masterplan | JSON canonique, **SVG lisible réellement présenté**, contrôles métriques **et Design Quality Gate indépendant** : morphologie urbaine, hiérarchie, variété de composition conforme au brief, usages des vides, parcours TPP prévus | **APPROUVER_MASTERPLAN** seulement après revue urbanistique documentée |
| 2 — Greybox | Volumes Godot fidèles, mesures de scènes, tests de navigation avec personnage et caméra réels, captures | **APPROUVER_GREYBOX** |
| 3 — Direction artistique et assets | Guide local, références étudiées, hero views initiales, **audit de couverture et d'adéquation des assets par sous-zone** (FIT/ADAPT/REJECT/MISSING), sourcing proposé ou manques bloquants | **APPROUVER_DA_ASSETS** seulement à 100 % de besoins essentiels couverts par des ressources réellement disponibles/validées sur le périmètre approuvé |
| 4 — Habillage et vérification | Placement **par sous-zone et par couches**, micro-scènes justifiées, **comparatifs avant/après aux mêmes caméras TPP**, itérations et suivi des défauts BLOCKER/MAJOR/MINOR | **APPROUVER_HABILLAGE** après gate visuel documenté |
| 5 — Gel | Finaliser index, version, preuve et état `locked`; publier le bilan | Validation de phase 4 requise; le gel ne peut être auto-approuvé |

L'agent peut travailler, vérifier et corriger **à l'intérieur de la phase autorisée**, sans franchir un jalon. Un silence, une absence de réponse ou une validation d'une autre phase **ne vaut jamais approbation**. Si le dialogue se coupe, reprendre au dernier jalon humain enregistré, pas plus loin. Les approbations ne sont pas des mécanismes de sécurité informatique : la protection requiert aussi revue de diff, permissions et Git.

## Questions de cadrage : initiative sans autoritarisme

- Séparer **imposé par l'utilisateur**, **inféré des quartiers existants**, **hypothèses** et **inconnues bloquantes**.
- Poser des questions ciblées **seulement** sur les choix majeurs dont la réponse peut substantiellement changer le quartier (taille, identité, nombre de tours, accès, densité, rapport au voisinage). Toujours proposer un **défaut concret et justifié** et permettre de le modifier.
- Les paramètres mineurs peuvent recevoir des valeurs de travail réversibles, présentées pour contrôle au jalon; **ne jamais présenter un défaut comme approuvé**.
- En cas de demande « grand quartier d'affaires, trois tours centrales, place et bureaux », conserver ces exigences; **ne jamais forcer** les dimensions, les matériaux ou une esthétique de Weakland. Recommander seulement des solutions compatibles avec le monde et les quartiers voisins.
- Si l'utilisateur demande une comparaison, proposer au plus 2–3 variantes réellement distinctes avant de choisir.

## Conception urbaine — gate anti-template V0.3

- **La validation géométrique n'est pas la validation urbanistique.** Un plan de six HLM rangés en deux colonnes autour d'un marché rectangle peut passer les tests JSON et rester incompatible avec un brief de ruelles organiques. L'agent doit composer le quartier selon ses usages et son histoire, et non remplir une grille de rectangles.
- Avant les emprises, développer **une morphologie motivée** : hiérarchie boulevard/seuils/ruelles/lieux de vie, accès, densité et fonctions; proposer si pertinent des alternatives de composition. Pour une demande de ville organique, tester décalages crédibles, séquences de marche TPP, lieux resserrés/ouverts, changement de perspectives et diversité de rapports à la rue. **Ne jamais imposer l'asymétrie** si l'utilisateur veut un quartier ordonné.
- Le format actuel de rectangles axis-alignés ne sait pas représenter fidèlement des rotations ou emprises irrégulières. Ne pas promettre des géométries qu'il ne peut pas exprimer : proposer une décomposition claire ou une extension de schéma/validateur soumise à approbation.
- **Organicité urbaine ≠ polygones complexes :** privilégier les bâtiments simples (rectangles, L, U, assemblages modulaires); produire l'irrégularité par l'implantation, les retraits, les hauteurs, les voies et l'histoire du tissu. Toute forme fortement découpée doit avoir une justification de parcelle/usage/architecture, et être jugée constructible avec les assets et modules 3D. Éviter les deux excès : grille répétitive comme composition par défaut et formes polygonales arbitraires comme fausse organicité.\n- Avant d'appeler `APPROUVER_MASTERPLAN`, **lire obligatoirement** `references/MASTERPLAN.md`, remplir `templates/masterplan-design-review.md` et corriger les `BLOCKER` et `MAJOR` non assumés. Si le SVG est symétrique/générique contrairement aux exigences, le considérer comme un défaut de conception même si les chiffres passent. Ne pas commencer Godot.
- L'agent doit fournir **le SVG lui-même dans un fichier effectivement ouvrable** et une synthèse de conception. L'approbation du cadrage n'est pas celle du masterplan; garder le jalon humain.

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
- L'habillage doit raconter un usage plausible, et non disperser des props arbitraires; conserver lignes de vue, accès, dégagements et budget GPU. Le style vient de la fiche DA **approuvée du quartier**, pas d'une recette cyberpunk universelle.\n- **Gate V0.2 avant placement :** inspecter les références et captures de départ, décomposer les façades/sols/toitures par fonction, identifier 3–5 vues héroïques adaptées, remplir la matrice Asset Fit `FIT/ADAPT/REJECT/MISSING/PLACEHOLDER`, calculer la couverture des besoins prioritaires et signaler les manques bloquants. **Un asset existant mais inadapté doit être rejeté, jamais répété pour remplir l'espace.** Voir `references/SET_DRESSING.md`.\n- **Gate V0.2 après placement :** preuves des couches appliquées ou justifiées N/A pour chaque sous-zone, micro-scènes d'usage plausibles, captures comparables avant/après, défauts classés et corrections itératives. **Aucune validation finale en présence de BLOCKER, et pas de MAJOR caché.** Une scène inachevée peut être présentée comme prototype partiel, jamais comme rendu final. Utiliser `templates/dressing-report.md`.
- Pour les assets, **réutiliser uniquement les candidats réellement adaptés**; si une catégorie essentielle manque, proposer une recherche d'alternatives gratuites (source/licence vérifiées), une adaptation ou la création sur mesure. **Sourcing à proposer et réaliser avec des outils disponibles**; téléchargements, intégrations et écritures Notion nécessitent les autorisations correspondantes. Tenir les listes « retenus / rejetés / nouveaux / manquants » et leurs preuves.
- Si un asset sur mesure est justifié, **proposer** `neon-ledger-environment` (répertoire `skills/neon-ledger-environment` de la bibliothèque) avec une mini-spécification; **ne jamais le déclencher automatiquement**. Voir `references/ASSETS_NOTION.md`.

## Phase 3 — Obligation de résolution de 100 % des besoins essentiels (V0.4)

- Un diagnostic « 15/50 couverts » est un **point de départ, jamais une fin de phase**. L'agent continue la recherche et la planification des solutions pour **chaque besoin essentiel** à l'échelle du périmètre défini (par défaut, toute la zone approuvée).
- Suivre deux compteurs **distincts et auditables** : **solutions identifiées N/N** (candidat concret avec preuve de fit et accès réaliste, ou création sur mesure précisément spécifiée et soumise à autorisation) et **ressources prêtes N/N** (asset existant validé, adapté et testé, ou acquisition/création autorisée effectivement obtenue, licence vérifiée et import Godot validé). Une piste de recherche, une URL non contrôlée, un devis, un brief ou une simple intention **ne compte jamais comme prêt**.
- Pour chaque besoin non couvert : chercher des alternatives **réellement pertinentes**; étudier les assets locaux, catalogues gratuits et kitbash; si aucune solution existante satisfaisante n'est trouvée, proposer un **brief de création sur mesure** via `neon-ledger-environment`, sans déclenchement automatique. **Ne jamais arrêter l'analyse après neuf liens si 35 besoins restent sans solution.**
- Si l'utilisateur n'a pas encore autorisé l'acquisition ou la création, présenter **un lot de décisions d'approvisionnement** (candidats, preuves/licences, coûts/effort, réemploi, besoins résolus) puis **rester en Phase 3**. Demander la permission, reprendre ensuite jusqu'à atteindre N/N ressources prêtes; ne pas solliciter `APPROUVER_DA_ASSETS` prématurément.
- **Pas de contournement** en réduisant artificiellement le dénominateur, en reclassant des essentiels en optionnels, en inventant des licences ou en comptant une référence pour plusieurs besoins incompatibles. Tout changement de périmètre ou de besoin essentiel exige arbitrage humain explicite et traçable.
- Vérifier les compteurs : **modèles uniques ≠ évaluations candidat/besoin ≠ besoins essentiels**. Si 51 modèles produisent 56 jugements, indiquer clairement les deux populations et les affectations multiples.
- Les autorisations restent distinctes : sourcing/recherche, téléchargement, intégration, écriture Notion, lancement de `neon-ledger-environment`, modification d'une zone verrouillée. Aucune action nécessitant un accord ne peut être devinée. Une impossibilité externe est un **BLOCKED** expliqué, jamais un 100 % fictif.
- Lire `references/ASSET_COVERAGE_100.md` et livrer `templates/asset-coverage-register.md` avant de soumettre la phase 3.

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
- `references/MASTERPLAN.md` — composition morphologique V0.3, anti-grille générique, parcours TPP, SVG et mesures.\n- `templates/masterplan-design-review.md` — contrôle de conception urbain indépendant du validateur JSON.
- `references/EXTENSIONS.md` — raccords, continuité, transitions.
- `references/GODOT_GREYBOX.md` — Godot et contrôle de proportions.
- `references/SET_DRESSING.md` — protocole V0.2 structure-aware, audit asset-fit, sous-zones et itérations visuelles.\n- `templates/dressing-report.md` — rapport de contrôle avant validation humaine.\n- `examples/weakland-dressing-audit.md` — analyse pédagogique du rendu Weakland et exemples de besoins.
- `references/ASSETS_NOTION.md` — sourcing, licences, Notion, Skill art externe.
- `references/QUALITY_GATES.md` — critères bloquants.
- `references/PROTECTION.md` — verrouillage et changement minimal.
- `references/INSTALLATION.md` — installation Claude Code et Codex.
