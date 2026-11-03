# Quality Gates — V0.2

**Principe :** une phase ne passe pas simplement parce qu'un script est vert ou que quelques modèles sont placés. Les décisions esthétiques restent humaines. Les preuves d'exécution doivent être vérifiables.

| Gate | Critères techniques minimum | Décision |
| --- | --- | --- |
| 0 Cadrage | Besoins imposés, hypothèses, variantes pertinentes, contradictions révélées | APPROUVER_CADRAGE |
| 1 Masterplan | JSON cohérent, SVG généré depuis JSON, géométrie/flux/raccordements contrôlés | APPROUVER_MASTERPLAN |
| 2 Greybox | Emprises mesurées dans la scène chargée, caméra TPP, collisions/parcours réels testés | APPROUVER_GREYBOX |
| 3A Intention | Style guide, références commentées, sous-zones, usages et hero views identifiés | Intégré au gate DA/Assets |
| 3B Asset-fit | Matrice de besoins/fonctions, fit géométrique et artistique, `FIT/ADAPT/REJECT/MISSING/PLACEHOLDER`, sources et licences traçables | APPROUVER_DA_ASSETS uniquement si couverture acceptable |
| 4 Habillage | Toutes les sous-zones essentielles traitées, pas de substitutions non approuvées, captures avant/après, problèmes suivis, navigation/performance, zones gelées intactes | APPROUVER_HABILLAGE |
| 5 Gel | Approbation phase 4 explicite, registre/diff/rapports alignés | Passage `locked` |

## Nouvelle classification V0.2 des défauts

- **BLOCKER** : asset de fonction essentielle absent et remplacé trompeusement; zone validée modifiée sans autorisation; passage bloqué; scène/captures non vérifiables alors que la validation dépend du rendu; impossibilité de respecter un aspect central du brief; licence inconnue pour un asset effectivement intégré; substitution placeholder présentée comme finale.
- **MAJOR** : plusieurs hero views sans composition/occupation crédible; géométrie des assets incompatible avec les façades; uniformité visible abusive; grandes zones d'usage laissées génériques sans intention approuvée; éclairage rendant les parcours ou intentions invisibles; sous-zones importantes non traitées.
- **MINOR** : variation secondaire, détail matériel, désalignement local sans enjeu d'accès, petit défaut de salissure ou d'ambiance.

Un `BLOCKER` empêche la demande de validation finale. Un `MAJOR` doit être résolu ou présenté au client comme **exception explicite à accepter**; cette exception ne vaut pas « rendu conforme aux références ». Une `MINOR` peut être suivie dans la liste de finition.

## Asset Coverage Gate (obligatoire avant Phase 4)

- Couverture = nombre de besoins prioritaires disposant d'une solution réellement `FIT` ou `ADAPT` prête / nombre total de besoins prioritaires, par sous-zone et globalement. Tous les besoins essentiels doivent être classés; ne pas utiliser les quantités de meshes bruts comme mesure de couverture.
- `ADAPT` signifie adaptation réalisable et autorisée, **pas** simplement « peut-être possible ».
- Les objets `MISSING`, `REJECT`, `PLACEHOLDER` ne sont jamais comptés comme couverts.
- Une zone volontairement sobre peut être `COMPLETE` avec peu d'objets si sa fonction/DA justifient cette sobriété et si l'utilisateur l'a approuvée.
- Si des éléments essentiels sont absents, **STOP** : proposer sourcing gratuit, adaptation, création sur mesure **sur accord**, ou livrable partiel explicitement approuvé. Ne jamais maquiller le manque par de la duplication.

## Visual Acceptance Gate (obligatoire après Phase 4)

Créer 3 à 5 hero views pour une petite cellule (adapter au contexte), une vue globale et des comparatifs avant/après à des positions de caméra reproduisibles. Évaluer visuellement et tracer :

| Dimension | Questions de vérification |
| --- | --- |
| Structure | Est-ce que l'asset est monté au bon endroit, à la bonne échelle, sur le bon support ? |
| Usage | Les entrées, commerces, zones techniques et sols ont-ils une logique identifiable ? |
| Composition | Existe-t-il des points focaux, des profondeurs et des respirations intentionnelles ? |
| Variété | Les répétitions flagrantes sont-elles justifiées et différenciées lorsque nécessaire ? |
| Références | Qu'est-ce qui manque dans les éléments artistiques *réalisables* approuvés ? |
| Lumière | Sources plausibles, contrastes, visibilité du cheminement, absence de zones involontairement illisibles ? |
| Technique | Collisions, capsule/caméra TPP, performance cible réellement mesurée, fichiers protégés inchangés ? |

Captures absentes, Godot indisponible ou état non exécuté = `NOT_TESTED/BLOCKED`, jamais `PASS`. La comparaison concept-art / jeu doit distinguer matériaux, éclairage, VFX et modèles 3D; ne pas prétendre égaler une référence photoréaliste sans les ressources appropriées.

## Rapport et preuves

Utiliser `templates/dressing-report.md`. Par sous-zone indiquer :
- exigences satisfaites, non satisfaites, non applicables et justifications;
- modèles réutilisés / écartés / nouveaux / manquants, provenance et licence;
- défauts de répétition et de fit;
- hero views avant/après et liste d'écarts classés;
- épreuves de navigation et mesures de performance réellement exécutées;
- liste exacte des fichiers modifiés et preuve que les zones `locked` sont intactes;
- validation humaine requise et exceptions éventuelles.

Un `WARNING` exige explication; un `ERROR/BLOCKER` stoppe. Le succès du validateur JSON ne suffit jamais pour certifier une scène Godot ou une direction artistique.
