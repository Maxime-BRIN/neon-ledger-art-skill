# Production efficiency — V1.6 (guide de décision, pas nouvel outil livré)

## Priorité : résultat visuel par unité de travail

Avant d'ouvrir Blender, rechercher la **voie la plus courte compatible avec la qualité, les droits et la DA approuvée**. Le bon objectif est un rendu exploitable en Godot, pas le nombre de modèles créés. Ne pas ajouter de nouveau projet d'automatisation ou d'asset sur une petite demande FAST.

| Besoin | Préférer | Quand passer à plus coûteux |
| --- | --- | --- |
| Simple prop existant et licencié | Import direct dans Godot si format/matériaux compatibles | Blender seulement si géométrie/UV/rig/collision/transformation l'exigent |
| Prop ressemblant à un asset catalogué | Adaptation ciblée de mesh/matériau | Modélisation neuve si adaptation est plus coûteuse ou contraire à la DA |
| Matériau d'enduit/métal ancien | Preset approuvé + masque/paramètres | Nouvelle texture uniquement si le preset ne permet pas le look |
| Façade dans kit compatible | Assemblage de modules existants + variations | Nouveaux modules si silhouette, accès et usage sont réellement différents |
| Asset singulier / identité forte | Conception et mesh dédiés | Ne pas sacrifier la DA à une économie artificielle |

## Décision sourcing courte et à rendement limité

Ordre : (1) fichiers locaux + presets validés, (2) catalogue Notion déjà renseigné, (3) quelques candidats externes pertinents, dont **BlenderKit/Blendkit**, Poly Haven, Kenney, Quaternius, autres selon licence réelle; (4) adapter ou créer. **BlenderKit est une source possible, non une obligation, et non une garantie d'automatisation officielle.**

Sur un asset courant : ne pas passer plus de temps à comparer des catalogues que le coût raisonnable de l'adaptation ou création. Chercher 1 à 3 candidats maximum au départ; arrêter si trouvé et conforme, ou si recherche manifestement non rentable. La recherche/licence déjà vérifiée peut être réutilisée uniquement si même fichier/version/droits.

**Exigences avant acquisition :** disponibilité exacte (gratuit ou abonnement), accès/connecteur fonctionnel, licence exacte de l'asset et de chaque texture, usage commercial, attribution et redistribution (notamment dépôt Git public), compatibilité et coûts. Ne pas télécharger, installer d'addon, créer de compte ou appeler une API externe sans autorisation nécessaire. Ne pas appeler un téléchargement « automatisé » si l'intégration n'existe pas ou si un humain doit le faire.

## Production par familles et lots

- Regrouper des besoins compatibles (ex. 4 coffrets avec géométrie commune, variantes de matériau; équipements de climatisation; devantures), **pas par contrainte de quota**.
- D'abord produire **un exemplaire témoin à qualité finale**, puis décliner en variantes utiles. Ne pas lancer 10 nouveaux assets/365 variantes avant d'avoir vérifié le témoin.
- La variation est multidimensionnelle : géométrie réellement différente quand nécessaire, fonction, pose, matériaux, teintes, saleté, réparations, accessoires, enseignes. Une seed ou rotation de texture seule ne crée pas un nouveau bâtiment crédible.
- Faire un lot seulement dans le périmètre déjà approuvé; pas d'extension tacite à un autre bâtiment ou quartier.
- Prévoir l'instanciation Godot ou MultiMesh uniquement pour des répétitions convenables, en tenant compte des limites de culling, matériaux, collisions et interactions; ne pas le rendre obligatoire.

## Outil de production réutilisable (spécification, non exécuté ici)

**Ne pas créer un nouveau script à chaque asset.** Si projet déjà équipé, réutiliser l'existant. Sinon, proposer une **unique entrée de commande** couvrant au besoin : validation dépendances → export Blender ciblé → import Godot ciblé → capture mêmes caméras/lumières → tests touchés → statut.

Interface logique d'exemple : `asset_pipeline --asset <ID> --mode fast|standard|full --views neutral,night --output <dossier>`.
**Cette commande est une interface cible et N'EXISTE PAS automatiquement.** L'implémenter/tester dans le dépôt de jeu seulement lorsque le projet est disponible et que les écritures sont autorisées. Ne jamais en annoncer la réussite depuis le seul Skill.

### Cache de validation déterministe

Index léger par asset : IDs de fichiers et empreintes versionnées pour mesh, UV, shader, textures, scène/caméra, licence/source, version de Godot/Blender et contrôles réellement passés. Si un fichier dépendant change, invalider **uniquement** les contrôles correspondants; si identité incertaine, contrôler plutôt que supposer. Ne pas créer une base de données supplémentaire sans besoin.

## Assembleur de façades : investissement conditionnel

- Repartir du kit modulaire existant et des **données de bâtiments canoniques** (JSON) pour placer baies, étages, accès et éléments compatibles, **sans toucher au masterplan ou à la greybox**.
- Autoriser des variantes déterministes par façade/étage, mais ne pas changer la silhouette, les collisions, les gabarits ni la topologie d'accès approuvés.
- Tester l'outil sur un **petit nombre de façades distinctes**, juger qualité, temps réel économisé et répétition perceptible. Ne pas construire un générateur complet pour un seul besoin.
- City Builder définit l'emplacement et la logique socio-fonctionnelle d'entretien; Environment définit kits et matériaux; l'assembleur **exécute**, mais ne décide pas la DA.

## Critères de succès / arrêt

Mesurer au moins pour le pilote : nombre de cycles artistiques, interactions humaines non nécessaires, opérations rejouées, temps de calcul si journal disponible, défauts artistiques majeurs restants, nombre de ressources réellement réutilisées, résultat Godot. Aucune promesse de pourcentage d'accélération sans comparaison.

**Critère d'arrêt :** la qualité approuvée en vue TPP est atteinte sans régression métrique, technique et juridique; éviter le perfectionnisme de micro-détail invisible. Si 2 stratégies raisonnables n'améliorent pas l'image, changer de levier (macro-texturing, autre source, projection, lumière, géométrie) et signaler le véritable blocage, au lieu de demander 50 validations.

**Ne pas dériver** la mission vers une infrastructure d'automatisation disproportionnée. Les opérations importantes/irréversibles exigent accord, et le résultat final reste soumis à validation humaine.
