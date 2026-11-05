---
name: neon-ledger-environment
description: Direction artistique et production 3D cohérente avec Neon Ledger pour tous types d'assets, props, bâtiments, rues et environnements, avec phases concept, Blender, PBR et Godot 4. À utiliser dès qu'une création visuelle ou 3D doit respecter la DA du jeu.
---

# Neon Ledger Environment Art

Objectif : produire des visuels distinctifs et des assets techniquement exploitables, **sans uniformiser les quartiers ni confondre rendu séduisant et asset validé**.

## Démarrage V1.5 — routeur minimal, avant tout audit

1. **Identifier le projet et le type d'opération** (nouvelle création / adaptation / retouche sur asset approuvé / livraison) à partir du dépôt et du brief. Si projet inconnu, demander. Lire `references/DA_ROUTING.md` seulement pour une DA à déterminer / un nouveau projet; ne pas imposer Neon Ledger ailleurs.
2. **Choisir FAST / STANDARD / FULL avant de charger les étapes** — lire `references/ITERATION_MODES.md`. Une correction d'un matériau approuvé FAST **saute sourcing, concept, nouvel inventaire et synchronisation Notion**; réutiliser sources et validations inchangées. Ne pas charger tous les fichiers pour une micro-itération.
3. **DA** : pour Neon Ledger confirmé, lire la DA de zone dans `references/ZONES.md`, la bible globale et les références approuvées si nécessaires; pour un autre projet, seulement sa DA; **sans DA externe, demander, ne pas inventer**.
4. **Nouveau modèle** : lire `references/ASSET_SOURCING.md` puis `references/PHASES.md` pour l'étape pertinente. Concept image si création et absence de référence approuvée et outil disponible; demander validation avant Blender.
5. **Matériaux / weathering** : charger `references/WEATHERING.md` et `references/MATERIAL_PIPELINE.md` lorsque nécessaires; **qualité macro à 5–15 m avant microdétails**. Consulter `references/VISUAL_FIDELITY.md` et `references/QUALITY_GATES.md` seulement pour les contrôles réellement applicables.
6. **Livraison** : contrôles finaux du mode FULL, validation humaine, catalogue Notion si asset livré; pas une fiche Notion par correction de roughness. Utiliser les templates existants sans nouveaux rapports redondants.

**Règle de convergence :** l'état de finition requis est une **cible initiale**, pas une patine minimale qu'on augmente sur dix itérations. Dès le témoin, reproduire l'intensité de la référence approuvée; si une forte négligence paraît propre à distance de jeu, reprendre les grandes masses visuelles en interne.

## Routage de direction artistique selon le projet — V1.3 (obligatoire)

**Déterminer le projet depuis le dépôt réellement ouvert (racine, manifeste, documentation), et non depuis le nom du Skill.** Appliquer `references/DA_ROUTING.md` **avant** toute image, proposition de design ou production.

1. **Projet Neon Ledger confirmé** : utiliser la bible globale + la **DA de zone et les décisions visuelles approuvées**, lorsqu'elles existent. En l'absence de concept pertinent déjà approuvé, pour une création originale autorisée, **générer une image concept de base** si l'outil image est réellement accessible, avec l'identité cyberpunk dystopique dense, stratifiée, vécue et technologique définie pour Neon Ledger, dans l'esprit de richesse visuelle recherché par l'utilisateur dans *Cyberpunk 2077*, **sans recopier des lieux, signes ou marques du jeu**. L'image doit illustrer le vrai type d'asset, pas uniquement une ambiance. Soumettre le concept à approbation humaine avant Blender. Si la zone a une DA propre, **elle prévaut sur les conventions générales** : ne pas imposer néons, pauvreté ou saleté à une zone prospère ou sobre.
2. **Autre projet avec DA explicite** : respecter **uniquement la DA et les références du projet / du prompt**. Ne pas importer la bible Neon Ledger, une palette cyberpunk ou la référence à *Cyberpunk 2077*. Produire une image de base pour les créations originales autorisées, si outil accessible et image appropriée absente, fidèle à la DA indiquée.
3. **Autre projet sans DA identifiable** : **STOP et demander explicitement à l'utilisateur quelle direction artistique il souhaite**, avec une question concise; ne générer aucun concept, ne modéliser et **ne jamais inventer une DA par défaut**. L'absence de DA n'est pas une autorisation d'appliquer Neon Ledger. Si l'appartenance du projet à Neon Ledger est incertaine, demander confirmation plutôt que l'inférer du Skill.
4. **Références prioritaires** : une image pertinente déjà approuvée, fournie ou présente dans le projet, prime sur une nouvelle génération. Ne pas régénérer des images à chaque appel sans nécessité : produire un nouveau concept seulement pour une nouvelle création, une DA explicitement révisée ou une comparaison demandée. Respecter les décisions humaines, l'accord de sourcer/créer et l'absence éventuelle d'outil de génération.
5. **Aucun outil image accessible** : signaler `IMAGE_GENERATION_NOT_AVAILABLE`, proposer une spécification textuelle contrôlable fondée sur la DA **connue et validée**, soumise à approbation. Pour un projet externe dont la DA est absente, demander la DA avant cette étape.

## Routage du brief
Identifier : **type d'asset, zone, usage gameplay, échelle/dimensions, distance caméra, phase, contraintes disponibles, références existantes**.
- Ne pas inventer de lore ou de décisions de DA « officielles » pour une zone non documentée. Distinguer faits, hypothèses et propositions.
- Si une information manque sans bloquer : poser une hypothèse explicite et réversible ; si elle bloque réellement, demander uniquement le détail nécessaire.
- Les bâtiments modulaires demandent une grille ; les props uniques, véhicules et personnages **n'héritent pas** d'une grille de façade.
- Weakland ≠ tout Neon Ledger. Ne pas appliquer « HLM délabré, béton humide, néon magenta » par défaut à chaque asset.
- Préserver une identité commune : stratification urbaine, contrastes socio-économiques, technologies intégrées à leurs fonctions, signalétique diégétique, composition lisible à hauteur de joueur.
- Adapter le niveau de détails à la cible et à la distance caméra ; AAA est une ambition de rendu, pas une garantie.
- Prioriser **une sortie visuelle principale** par itération ; produire planches techniques et variantes après validation si elles sont utiles au type d'asset.
- Corriger les **3 défauts majeurs** plutôt que réécrire tout le prompt.

## Recherche et réutilisation avant génération — étape 0 obligatoire
Pour tout **nouvel asset 3D ou adaptation non encore évaluée**, appliquer `references/ASSET_SOURCING.md` **avant** le routage des images : (1) rechercher les assets déjà présents dans le projet et le catalogue Notion, (2) chercher des modèles externes gratuits réellement téléchargeables, (3) vérifier l'adéquation artistique/technique **et la licence de la fiche précise**, (4) comparer réutilisation, adaptation et création.
- Un asset déjà adapté et exploitable est à **réutiliser**, pas à recréer. Un asset proche est à **adapter**, si l'effort est raisonnable ; sinon proposer la création.
- Prioriser la qualité finale, le coût d'intégration et la traçabilité ; « gratuit », « CC0 » ou « libre de droits » ne se déduisent pas d'un site entier. Vérifier le droit d'usage commercial, de modification, les attributions et les restrictions de redistribution pour l'asset concerné. Sans preuve, ne pas annoncer « licence vérifiée » et ne pas incorporer le fichier.
- Pour un lot, garder une liste courte de candidats par asset, sans téléchargement massif ni doublons. Respecter l'accord de l'utilisateur avant toute acquisition/import qui écrit dans le projet.
- Si la recherche externe n'est pas disponible, consigner **NOT_TESTED**, ne pas prétendre avoir cherché et proposer une décision provisoire.
- **Ne déclencher la création de concept IA que pour la voie CRÉER validée**, jamais simplement parce qu'il manque une image. Une image utilisateur utile peut aider à choisir ou à adapter un asset existant, sans imposer une reconstruction.
- Les assets réutilisés ou adaptés passent les contrôles artistiques, techniques et de licences pertinents. Conserver les validations humaines et la synchronisation Notion.

## Routage obligatoire des références — avant la phase 1
**Après le routage DA `references/DA_ROUTING.md` et le choix documenté RÉUTILISER / ADAPTER / CRÉER**, déterminer pour **chaque asset**, avant tout concept ou modélisation, si une référence visuelle pertinente est fournie (image jointe, image de projet ou concept déjà approuvé), si l'agent dispose **réellement** d'un outil de génération d'images, et si le brief textuel est suffisamment précis. Une image générique d'ambiance n'est pas automatiquement une référence d'asset.
1. **Image pertinente fournie** : l'utiliser prioritairement, sans la remplacer ni régénérer par défaut. Identifier ses éléments visibles, son statut (proposée/approuvée) et ses limites. Si la référence est ambiguë, proposer une interprétation et solliciter validation ; ne pas traiter une image non approuvée comme canon.
2. **Voie CRÉER validée, aucune image pertinente + génération d'images disponible** : commencer obligatoirement la **phase 1 par un concept visuel généré**, adapté à l'objet (pour un prop : objet isolé lisible, silhouette, matériaux, détails fonctionnels ; pour une scène : cadrage pertinent). S'appuyer sur le brief et la DA documentée **(ou sur l'identité Neon Ledger confirmée, sous réserve des choix spécifiques de zone)**, **une image principale par asset/itération**, sans générer des dizaines de variantes. Présenter ce concept comme proposition et attendre son approbation explicite avant la phase 2.
3. **Voie CRÉER validée, aucune image pertinente + pas de génération d'images disponible** : poursuivre avec une **référence textuelle structurée** ; si la description utilisateur est déjà précise, la conserver et la compléter seulement sur les points de fabrication manquants. Si elle est vague **mais que la DA est déjà connue**, **proposer une version textuelle plus complète** (fonction, zone, silhouette, proportions, dimensions estimées, construction, matériaux, couleurs motivées, vieillissement, habillage, fixations, lisibilité à distance de jeu, limites et hypothèses), clairement étiquetée `PROPOSITION À VALIDER`. Ne pas inventer d'image ni affirmer en avoir généré. Demander approbation de cette référence textuelle avant la phase 2.
- **L'image n'est pas obligatoire si l'outil est absent** : une spécification textuelle approuvée vaut référence principale pour les gates, à condition de détailler les éléments contrôlables ; comparer alors le vrai rendu à cette liste de critères plutôt que prétendre produire un côte-à-côte visuel impossible.
- Si l'utilisateur demande explicitement de **ne pas générer d'image**, respecter ce choix et utiliser la voie textuelle.
- Pour un lot, traiter les assets individuellement et limiter les générations aux éléments nécessaires ; préserver les concepts existants déjà validés.
- **Jamais de génération ni d'hypothèse de DA pour un autre projet sans DA : poser d'abord la question.**
- Ce routage appartient à la **phase 1**, et ne contourne jamais les autorisations humaines applicables selon le mode supervisé/autonome et les contraintes de temps réel.

## Fidélité aux références visuelles
- Être fidèle à une référence approuvée signifie reproduire **aussi son habillage** (props, textiles, végétation, signalétique, graffitis, salissures), pas uniquement la silhouette et les ouvertures.
- Avant de déclarer une phase prête, confronter son rendu réel à l'inventaire de référence ; toute omission visible et importante doit être justifiée.
- Un élément de blockout non finalisé ne doit jamais être présenté comme un asset terminé. La complexité doit rester proportionnée à la distance caméra et au budget temps réel.
- Préférer des graffitis abstraits ou illisibles ; ne pas inventer de texte lisible ni de marque non validée.

## Visual Fidelity & Detail Gate — V1.2 (obligatoire)

**Critère principal :** un modèle techniquement conforme mais visuellement banal **ne passe pas** lorsqu'il manque les familles de détails majeures d'une référence artistique approuvée. Le nombre de modules, de triangles ou de tests réussis n'est pas une preuve de fidélité.

1. **Contrat visuel avant production.** Pour chaque concept approuvé (ou spécification textuelle), décomposer par bâtiment, façade et zone visible les familles de détails : architecture secondaire, commerces/entrées, réseaux techniques et ancrages, occupation humaine, enseignes, usure causale, matériaux, éclairage, éléments de toiture. Associer importance perceptive, distance caméra, contrainte métrique, responsable de kit et critères d'acceptation. Utiliser `templates/visual-fidelity-matrix.md` et `references/VISUAL_FIDELITY.md`.
2. **Statuts explicites par détail :** `EXISTING / ADAPT / SOURCE / CREATE / GODOT_EFFECT / INCOMPATIBLE`; états de réalisation distincts `PLANNED / PRODUCED / INTEGRATED / VERIFIED / DEFERRED_APPROVED`. Une proposition de sourcing ou un concept IA ne signifie jamais « produit ». Les détails transférés à K02/K03/K04 restent ouverts, avec propriétaire et gate de phase; ils ne sont pas tacitement attribués à K01.
3. **Fidélité de l'ambiance voulue :** si la référence cyberpunk approuvée présente une stratification marquée (câbles et gaines avec attaches, coffrets, ventilations, reprises, vitrines profondes, signalétique diégétique, lumière et traces de vie), **ne pas la réduire** à une façade classique + quelques néons. Ce langage visuel dépend de la référence **locale** : ne pas imposer ces détails à toutes les zones.
4. **Validation par image réelle.** Pour chaque gate de production **pertinent au mode choisi**, comparer le concept approuvé au **rendu du vrai mesh** depuis Blender et, à l'étape d'intégration, Godot, avec caméras et conditions d'éclairage aussi proches que possible; au jalon FULL fournir aussi une capture neutre et une capture TPP contextuelle. Identifier `BLOCKER / MAJOR / MINOR`, les 3 écarts dominants et un plan de correction. Ne jamais présenter un paintover ou une image générée séparément comme preuve de modélisation.
5. **Construction mesurée et performante.** Les images de concept ne sont **pas** des plans cotés : positions, ouvertures, emprises, 1,50 m de passage, clearance, hauteurs, saillies et toitures restent gouvernés par le JSON/contrat technique. Les ajouts hors enveloppe doivent être classés `INCOMPATIBLE` et soumis à arbitrage; jamais placés par défaut. Géométrie réelle pour relief/silhouette/ombre; trim sheets, normal maps, decals et éclairage pour microdétail, avec budgets mesurés.
6. **Gate sans faux succès :** un asset peut être `GEOMETRY_PASS / VISUAL_INCOMPLETE` : autoriser les tests d'intégration isolés, mais **pas** `ART_READY` ou validation finale tant que les écarts majeurs de sa **portée approuvée** restent ouverts. Un kit architectural K01 peut être accepté comme base sans que la façade enrichie K01+K02+K03+K04 soit déclarée terminée.

## Modes d'itération FAST / STANDARD / FULL — V1.4

Après sélection du mode dès le routeur V1.5, appliquer `references/ITERATION_MODES.md` et **choisir le niveau de contrôle selon le risque réel** :

- **FAST :** correction locale de matériau, roughness, texture, lumière ou decal avec géométrie et UV inchangés; réutiliser banc/provenance/licences/audits antérieurs, produire 1 vue A/B pertinente (vue neutre si utile), contrôle runtime ciblé et bilan concis. **Pas de nouvel audit complet, de neuf captures, de recherche externe ou de validation entre micro-itérations par défaut.**
- **STANDARD :** nouveau module/façade, changement UV/mesh local, shader ou texture avec impact mémoire significatif; contrôles sélectifs des éléments modifiés, quelques captures, performance ciblée si pertinente.
- **FULL :** livraison `ART_READY`, intégration définitive dans le quartier, zone complète, modification du canon ou risque élevé; appliquer tous les quality gates pertinents et demander validation humaine.

**Production autonome après approbation du concept et autorisation explicite du périmètre :** les missions Blender, PBR, tests Godot et corrections itératives s'enchaînent sans validation humaine à chaque petite étape. La validation humaine demeure obligatoire pour concept initial et livrable final, ainsi que changement de DA, extension du périmètre, modification de zones protégées, acquisition/source externe soumise à permission ou conflit majeur. Mode supervisé disponible sur demande.

Ne jamais confondre **moins d'interruptions** et **moins de qualité** : les preuves obsolètes sont invalidées sélectivement, non réutilisées sans contrôle. Conserver les résultats dans les fichiers existants; ne pas fabriquer un nouveau rapport pour chaque modification.

## Production par jalons
- Étape 0 : diagnostic réutiliser / adapter / créer et vérification de licence ; aucune génération d'image inutile.
- Phase 1 : concept et spécification visuelle **pour la création originale** ; en réutilisation/adaptation, revue et approbation de la source et des modifications prévues ; **aucun faux modèle 3D**.
- Phase 2 : modélisation 3D, UV, pivots, unités, modules éventuels, collisions éventuelles ; produire des preuves réellement rendues.
- Phase 3 : matériaux PBR, vieillissement motivé, éclairage, export, contrôles Godot 4.
- **Validation explicite requise** pour le concept initial et la livraison finale; en mode supervisé, également entre missions. En mode autonome expressément autorisé par le périmètre de production, les missions 2 et 3 et leurs itérations internes s'enchaînent sans interrompre l'utilisateur. Voir `references/ITERATION_MODES.md`.
- Avant d'écrire dans un projet existant : lire `AGENTS.md`, `CLAUDE.md` et les contraintes du dépôt ; ne pas modifier silencieusement les zones validées.
- Ne pas prétendre avoir exécuté Blender, ouvert Godot, produit une image, inspecté un fichier ou testé des FPS sans preuve.
- Distinguer **créé / exécuté / vérifié / non vérifié / bloqué**.

## Sortie courte
Indiquer asset + zone + phase + hypothèses importantes. Livrer les fichiers, les preuves et un statut : PASS, BLOCKED ou NEEDS_USER_APPROVAL. Ne produire un long audit que si une anomalie le justifie.

## Étape finale obligatoire — Image et catalogue Notion
À la clôture de **chaque jalon d'asset livré à l'utilisateur** (concept approuvé, prototype livré ou asset final), **et non pour chaque micro-itération FAST/STD**, suivre `references/NOTION_ASSET_CATALOG.md`.
1. Produire ou sélectionner **une vraie image représentative de l'asset** ; privilégier un rendu du mesh réel dès qu'il existe. Ne pas présenter un concept IA comme une capture 3D.
2. Créer ou **mettre à jour sans doublon** la fiche de cet asset dans la base officielle Notion « ⛩️ Assets Neon Ledger ».
3. Renseigner les champs disponibles, notamment `Nom`, `Catégorie`, `Type`, `Usage`, `Chemin projet`, `Lien`, `Auteur`, `Statut`, `Contrôle technique`, `Décision / remarques` et les informations de licence vérifiables.
4. **Renseigner la propriété fichier `Aperçu` avec l'image**, et conserver également une image visible dans le **contenu de la page** lorsque nécessaire pour la galerie configurée sur « Aperçu de la carte : Contenu ».
5. Aucun `Statut = Intégré` sans test d'intégration Godot effectivement réalisé ; aucune `Licence vérifiée` sans preuve ; ne pas deviner les valeurs.
6. Confirmer le lien de la fiche Notion et les champs réellement mis à jour. En cas d'absence d'accès Notion ou d'échec d'upload, signaler l'étape bloquée et garder les fichiers prêts, sans annoncer une synchronisation réussie.

Cette synchronisation ne remplace pas les validations humaines applicables au concept, au périmètre et au livrable final (ou aux jalons intermédiaires du mode supervisé). Une fiche peut exister dès la phase concept avec `Statut = Nouvel asset`, puis être enrichie aux phases suivantes.
