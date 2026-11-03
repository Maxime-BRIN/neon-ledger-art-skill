# Assets, sourcing, licences et Notion — V0.2

BDD Notion cible : https://app.notion.com/p/ns-group/5dc0caa5658e48499bb87bcf0d9be012?v=40a79de523e180268e68000ceb50e47f

## Priorité réelle : fit avant réemploi

La disponibilité locale n'est **pas** un critère suffisant. L'agent doit prendre chaque besoin décrit dans l'audit `SET_DRESSING.md` et rechercher une réponse fonctionnellement, géométriquement et artistiquement compatible. Si le modèle local est inadapté, **REJECT**, même si aucun autre modèle n'existe.

Pour chaque besoin, le registre `asset-needs` inclut :
- `need_id`, `subzone_id`, `priority` (essential/support/optional), `function`, `placement_constraints`, `visual_reference`;
- `candidate_asset_id`, `fit_status` (`FIT/ADAPT/REJECT/MISSING/PLACEHOLDER`), `fit_reason`, `adaptation_work`;
- `source_type` (local/external/proposed_custom), `license_verified`, `source_url`, `author`, `attribution`, `status`;
- `next_action`, `human_approval_needed`, `godot_path` uniquement si réellement intégré.

Ne jamais confondre quantité d'objets instanciés et couverture des fonctions. Dix copies du même immeuble ne couvrent pas un besoin de devanture, d'auvent, de stand, de sas d'entrée ou de réseau technique.

## Modes de résolution des manques

1. **Asset existant** : inspecter géométrie, dimensions, usage, qualité, couleurs, variations possibles; adopter uniquement si `FIT` ou `ADAPT` réellement faisable.
2. **Sourcing gratuit** : effectuer une recherche ciblée lorsque les outils web sont disponibles, avec mots-clés qui décrivent fonction, encombrement, qualité et style. Présenter les candidats précis (URL source, capture/preview lorsque disponible, format, licence, créateur, attribution, adaptation). Vérifier sur la page source, pas sur une page de résultat. Gratuit ≠ libre d'usage commercial. Vérifier restrictions de redistribution, attribution, modifications et intégration au jeu. Sourcing/recherche ≠ téléchargement ni intégration.
3. **Kitbash non destructif** : assembler des modules existants seulement si silhouette, échelle, stabilité et usage sont corrects; documenter les sources de chaque composant.
4. **Création sur mesure** : proposer uniquement, **jamais lancer automatiquement**, le Skill réellement présent `neon-ledger-environment` dans `skills/neon-ledger-environment/` (bibliothèque GitHub). Fournir un brief avec références visuelles autorisées, dimensions, matériaux, LOD, pivots, usage et interface Blender→GLB→Godot; attendre validation explicite.
5. **Blocage** : si l'asset est essentiel et aucune solution approuvée n'est disponible, laisser la sous-zone `BLOCKED/INCOMPLETE` et proposer le meilleur arbitrage utilisateur. Aucune duplication dissimulée et aucune promesse d'achèvement.

Pour une recherche de nouveaux assets, si l'outil n'est pas accessible, expliquer que la recherche n'a pas été faite. Ne jamais inventer d'URL ou de licence.

## Approvals distinctes et Notion

La validation `APPROUVER_DA_ASSETS` autorise le plan artistique, **pas automatiquement** le téléchargement, l'intégration externe ou les modifications Notion. Demander une permission spécifique avant ces actions; les autorisations peuvent être groupées par liste de candidats identifiés si l'utilisateur l'accepte. Aucune création automatique sur mesure.

Pour tout nouvel asset intégré avec autorisation :
- nom exact, identifiant, URL origine et téléchargement, créateur, licence, attribution, preuves et date de vérification;
- catégorie/type/format, dimensions, preview réellement accessible, chemin Godot, zone affectée, statut (candidat/téléchargé/importé/validé) et adaptations;
- vérifier la structure et les propriétés réelles de la BDD Notion, insérer une entrée avec contenu/aperçu utilisable, **ne pas créer de doublons**, puis confirmer le succès avec lien ou ID réel;
- si la connexion Notion est absente : préparer la fiche d'import, marquer `NOT_SYNCED`, ne jamais prétendre à une mise à jour.

## Rapport utilisateur obligatoire

Toujours communiquer les 4 sections :
1. **Assets existants retenus** et raisons `FIT/ADAPT`.
2. **Assets existants rejetés** et raisons précises.
3. **Assets gratuits identifiés / nouveaux intégrés** avec URLs, licences et état Notion vérifiés.
4. **Assets sur mesure proposés** avec mini-brief + problèmes bloquants et approbations nécessaires.

Si aucune acquisition externe n'a été faite, indiquer `aucun nouvel asset téléchargé`. Si les besoins essentiels restent ouverts, **le rendu final est non approuvable** sauf accord explicite pour un livrable partiel.
