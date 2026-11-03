# Set Dressing V0.2 — Structure-aware, asset-fit, visuel contrôlé

## Principe

L'habillage n'est pas « poser les assets disponibles ». Il est la traduction de la **fonction urbaine**, de l'architecture validée, de la direction artistique locale et des références utilisateur en une scène lisible et crédible. **Ne jamais atteindre artificiellement une impression de complétude en répétant les mêmes modèles.** Ne jamais modifier le masterplan, la greybox ou les zones gelées sans autorisation spécifique.

### Retours Weakland — exemple diagnostic (novembre 2026)

Les captures montrent quelques façades HLM fonctionnelles (fenêtres, climatiseurs, câbles) mais une composition majoritairement inachevée : grands pignons aveugles, chaussées et cour sans usages, lumière uniforme et faible, éléments provisoires visibles, silhouette répétitive. Les références visent une hiérarchie de niveaux de détail et des lieux habités : fronts commerciaux, seuils, toitures, canalisations, auvents, signalétique, éclairages orientés, points de vie et traces d'entretien. Ce **n'est pas** une exigence de copie exacte des références, ni un ordre de couvrir chaque mètre de néons, de déchets ou de mobilier. Un HLM résidentiel ne doit pas automatiquement devenir un marché commercial.

## Phase 3A — Références et objectifs observables

Avant d'ouvrir l'outil de placement :

1. Examiner les images de référence *et* les captures Godot existantes sous des angles comparables. Distinguer ce qui relève d'une **forme 3D**, d'une **texture/matériau**, de **l'éclairage**, de **l'atmosphère** et des **personnages/VFX**. Ne pas promettre de reproduire une référence de concept art photoréaliste sans assets, systèmes et budget adaptés.
2. Écrire un mini « look contract » de la zone : fonctions des lieux, identité, usage, niveaux de lumière, humeur, contraste, structures secondaires autorisées, détails prioritaires. L'utilisateur approuve les choix créatifs.
3. Délimiter les **hero views** (3 à 5 pour une petite cellule, davantage selon taille), à hauteur du joueur, avec positions/orientations/FOV reproductibles, plus 1 vue globale et 1 avant/après. Prendre les captures de départ et annoter les manques.
4. Déclarer les **zones d'intérêt visuel** et les zones volontairement calmes : la densité est pilotée par le sens de la scène, pas par un quota universel.

## Phase 3B — Analyse structure-aware obligatoire

Découper la zone de travail en sous-zones identifiées. Pour chaque bâtiment/facade/sol/toiture visible, remplir :

| Champ | Contenu exigé |
| --- | --- |
| `subzone_id` | ID stable, emprise/localisation |
| `function` | habitat, commerce, service, distribution, circulation, cour, maintenance, repos, etc. |
| `architectural_constraints` | type d'édifice, hauteur, accès, retraits, ouvertures, géométrie gelée |
| `human_activity` | qui utilise le lieu, pourquoi, à quelle heure, indices matériels |
| `visual_role` | focal / support / repos / transition |
| `needed_layers` | couches justifiées, chacune avec intention |
| `candidate_assets` | modèles disponibles et adaptation aux emprises |
| `gaps` | éléments absents et impact esthétique/fonctionnel |
| `protected_interfaces` | chemins et bâtiments interdits de modification |

Questions que l'agent doit traiter : qu'y a-t-il au pied du bâtiment ? comment entre-t-on ? où va le service de collecte ? pourquoi cet auvent ? où sont les réseaux ? quelle façade est vue de loin ? quelles surfaces doivent rester sobres ?

L'agent peut proposer des structures additionnelles **uniquement** si elles sont compatibles avec les emprises et géométries approuvées. Si elles nécessitent un changement de volume/accès, envoyer une demande de changement localisée et attendre l'accord.

## Phase 3C — Asset Coverage & Fit Audit (BLOQUANT)

Créer un inventaire de besoins **avant** tout placement final. L'inventaire local est une source de candidats, **pas une obligation d'utiliser ces candidats**.

Pour chaque **besoin**, tester les dimensions utiles, orientation, matériau, géométrie/montage, silhouette, usage plausible, DA, qualité LOD/performance, licence et capacité de variation. Une texture ne remplace pas un balcon, un store, un auvent ou une vitrine 3D lorsque la silhouette de référence en dépend.

Classification obligatoire :
- `FIT` : utilisable tel quel, preuves/aperçu;
- `ADAPT` : kitbash / adaptation non destructive possible dans la phase;
- `REJECT` : inadapté malgré disponibilité locale, avec raison;
- `MISSING` : pas de candidat utilisable;
- `PLACEHOLDER` : temporaire, **jamais final**.

Calcul par sous-zone : couverture **fonctionnelle** = besoins prioritaires `FIT` ou `ADAPT` prêt / total besoins prioritaires; une valeur quantitative n'est fournie que si le dénominateur est défini. L'agent doit aussi évaluer la couverture **visuelle** sur les hero views et les manques bloquants. Ne pas inventer un score précis sans données.

Si un besoin essentiel est `REJECT` ou `MISSING`, ne pas remplacer par un modèle générique répété : recherche gratuite autorisée seulement si les outils et permissions existent; sinon proposer la recherche et les demandes de création détaillées. L'approbation de DA/Assets **ne peut pas** valider une couverture insuffisante sans consentement explicite à un périmètre réduit ou un prototype inachevé.

## Phase 3D — Approvisionnement, priorité à l'adéquation

1. **Réutiliser** seulement les modèles locaux `FIT` et `ADAPT` effectivement pertinents.
2. **Chercher** des alternatives gratuites, licences compatibles, formats et qualité adaptés, URL source exacte et preuve de licence. Vérifier réellement les références; le nom d'un site n'est pas une preuve de licence. Demander l'autorisation spécifique avant de télécharger/intégrer ou d'écrire dans Notion; présenter des candidats si autorisation absente.
3. **Proposer** `neon-ledger-environment` (Skill de création d'assets du dépôt) pour les modèles narratifs spécifiques, modules sans équivalent libre ou objets trop singuliers. Fournir un brief et **attendre l'accord**; ne jamais invoquer le Skill automatiquement.
4. Si la couverture requise reste insuffisante : **stopper la phase**, donner une liste d'éléments bloquants, leur emplacement, coût relatif/impact et options à choisir. Aucun bricolage de remplacement silencieux.

Toute acquisition est traçable dans l'inventaire et dans Notion **si accès et autorisation réels**. Voir `ASSETS_NOTION.md`.

## Phase 4A — Placement par couches et sous-zones

Pour chaque sous-zone approuvée :

1. **Architecture de contact** : seuils/entrées, socles, retraits, vitrines (si autorisées), connexion bâtiment-sol.
2. **Infrastructure** : accès maintenance, alimentation, réseaux visibles, évacuation eau/pluie, ventilation, grilles, coffrets.
3. **Usage fonctionnel** : zones de livraison, circulation, réparation, collecte, repos, cuisine/vente, rangement.
4. **Commerce et signalétique** : points économiques seulement là où le quartier et le plan les justifient, enseignes ancrées dans un local.
5. **Occupation humaine** : linge, fenêtres individualisées, objets personnels, mobilier d'usage, petites traces de routine.
6. **Usure contextuelle** : salissures, corrosion, peinture et humidité selon exposition, drainage et maintenance; déchets aux endroits plausibles, pas partout.
7. **Éclairage et atmosphère** : sources traçables, contraste, orientation, lisibilité des accès; pluie/reflets/VFX optionnels si la technologie et la performance le permettent.

Ces couches sont **une grille d'analyse**, pas l'obligation d'ajouter sept objets à chaque endroit. Marquer explicitement `N/A + justification` pour une couche non applicable. Conserver des respirations et une hiérarchie visuelle.

### Micro-scènes narratives

Concevoir les micro-scènes **depuis les usages** : stand de restauration, réparation, point de collecte, hall d'immeuble, cour d'entraide, ruelle technique, dispensaire, etc. Chaque micro-scène décrit : fonction, sujet principal, accessoires compatibles, relation aux accès, lumière motivée, indices d'activité et angle(s) de contrôle. Proposer un hero spot et plusieurs micro-scènes **uniquement si l'échelle et la fonction de la zone le justifient**; ne pas forcer 1 hero + 4 scènes dans une petite transition résidentielle.

### Variété sans bruit

Éviter les clones contigus ou visibles en même temps qui trahissent une duplication non intentionnelle. Avant de réutiliser un mesh, vérifier distance perceptive, fonction, variété de silhouettes et détails, degré de saleté et matériaux. Rotation aléatoire et recoloration seules **ne suffisent pas** si la silhouette et l'usage sont inadaptés. Les répétitions architecturales HLM peuvent être réalistes, mais les traces d'occupation et les rez-de-chaussée demandent de la différenciation.

## Phase 4B — Boucle visuelle obligatoire (pas seulement une checklist)

1. Capturer au moins **3–5 hero views** cohérentes avec les vues de départ, une vue globale et des vues des jonctions. Les produire avec les outils Godot réellement accessibles.
2. Pour chaque vue, comparer à la **direction d'intention**, pas une exigence de reproduction pixel à pixel. Vérifier à la fois (a) silhouette, (b) activité perçue, (c) diversité cohérente, (d) éclairage et lisibilité, (e) surfaces/sols, (f) points d'attention et espaces calmes, (g) obstacles/performance.
3. Inscrire chaque écart : ID, capture, localisation, sévérité `BLOCKER/MAJOR/MINOR`, cause attribuée, correction minimale, catégorie d'asset manquant, autorisation requise.
4. Corriger **localement et non destructivement** les écarts des zones autorisées; reprendre les mêmes caméras et refaire les captures. N'arrêter l'itération qu'en l'absence de défauts bloquants ou après accord explicite de report/exception.
5. Si aucun outil de capture ou de test n'est disponible, **ne pas prétendre avoir validé le rendu**. Fournir les commandes et les obstacles, laisser le gate en `BLOCKED`.

## Interdictions explicites

- « On n'a pas l'asset, donc on réutilise le même HLM/facade/store partout ».
- Poser un objet incompatible avec la fonction ou les dimensions uniquement pour remplir un espace.
- Présenter un cube, une enseigne non lisible, une texture plate ou une façade factice comme asset final de qualité.
- Qualifier un screenshot trop sombre, des pignons nus ou des sols entièrement vides de « fini » sans justification de mise en scène approuvée.
- Modifier une zone verrouillée pour améliorer un point de vue voisin sans consentement explicite ciblé.
- Inventer un téléchargement, une licence, une entrée Notion, une capture Godot, une amélioration mesurée ou un appel au Skill de création.

## Rapport obligatoire

Produire le rapport selon `templates/dressing-report.md` avec, par sous-zone, couvertures, `FIT/ADAPT/REJECT/MISSING/PLACEHOLDER`, nouveautés et licences, écarts visuels, captures comparables, preuves de navigation/performance, zones protégées intactes et **demande de validation humaine**.
