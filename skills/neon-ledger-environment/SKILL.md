---
name: neon-ledger-environment
description: Skill de direction artistique, sourcing, adaptation et production d'assets 3D pour Neon Ledger OU un autre projet dont la DA est explicitement fournie. Modes FAST/STANDARD/FULL, concept, Blender, PBR et Godot 4.
---

# Environment Production Skill — V1.6

**Objectif :** produire vite un rendu fidèle à la DA approuvée et techniquement exploitable, sans multiplier les validations, scripts, rapports ou matériaux redondants. Choisir le **chemin de production le moins coûteux** qui conserve cette qualité. La fidélité **artistique** n'est pas garantie par la seule conformité métrique.

## 1. ROUTER AVANT de lire le reste

**D'abord identifier le projet, l'opération et le risque. Ne pas charger tous les documents pour une retouche mineure.**

| Situation | Mode / fichiers requis | Action |
| --- | --- | --- |
| Texture/roughness/decal/lumière d'un asset déjà approuvé, mêmes UV/meshes | **FAST** : `references/ITERATION_MODES.md`, éventuellement `WEATHERING.md` / `MATERIAL_PIPELINE.md` | Reprendre directement banc et preuves valides; 1 A/B utile, corrections autonomes, bilan très court. **Pas de nouveau sourcing, concept, rapport complet ni Notion à chaque passe.** |
| Nouvelle façade, adaptation de mesh/UV ou shader coûteux | **STANDARD** : docs techniques ciblées, `PHASES.md` | Témoin représentatif avec matériaux de niveau final, puis production incrémentale; tests impactés seulement |
| Nouvelle zone, asset final, intégration en jeu, modification géométrique importante | **FULL** : `QUALITY_GATES.md`, `VISUAL_FIDELITY.md`, références applicables | Contrôles complets, comparaison Godot et validation humaine finale |
| Nouvelle création / adaptation non évaluée | Sourcing via `ASSET_SOURCING.md`, puis projet/DA et concept | Rechercher/adapter avant de créer. Licence par ressource, permission avant acquisition |
| Identité du projet ou DA inconnue | `DA_ROUTING.md` | **Demander**, ne pas inventer de DA ni imposer Neon Ledger à un autre projet |

Si une opération FAST découvre un shader coûteux, UV modifiés ou de nouveaux risques, **escalader uniquement les contrôles touchés** à STANDARD. Une modification de zone protégée reste interdite sans accord, quel que soit le mode.

## Décision de fabrication : chercher le bon raccourci

Pour une **nouvelle production**, consulter `references/PRODUCTION_EFFICIENCY.md` si le choix des outils/sources/variantes n'est pas déjà tranché. Priorité : (1) ressource interne validée, (2) réemploi ou adaptation d'asset avec licence prouvée, y compris catalogue BlenderKit/Blendkit si accès disponible, (3) modules paramétriques, (4) création sur mesure. **Ne jamais ouvrir Blender pour une simple adaptation Godot si elle suffit.**

Après validation d'un **témoin artistique représentatif**, produire par petites familles réutilisables, pas un asset entièrement neuf par bâtiment. Réutiliser une même commande d'export/import/capture et un cache des tests si ces outils **existent réellement dans le projet**; le Skill n'est pas l'implémentation de ces scripts. Ne pas lancer un chantier d'outillage démesuré à la place d'une retouche FAST.

## 2. Direction artistique et références

1. Vérifier **l'identité réelle du projet** depuis le workspace, pas depuis le nom de ce Skill. Lire `references/DA_ROUTING.md` si contexte nouveau ou ambigu.
2. **Neon Ledger confirmé** : bible `references/NEON_LEDGER_ART_BIBLE.md` + DA locale `references/ZONES.md` + concepts explicitement approuvés. Style cyberpunk stratifié, habité et technologique lorsqu'il correspond au quartier, avec richesse comparable au niveau de détail voulu dans Cyberpunk 2077, **sans copier ses éléments propres**. Les décisions locales priment; pas de palette néon ou salissure universelle.
3. **Autre projet** : appliquer uniquement la DA fournie par ce projet/prompt. **Si absente, demander la DA avant toute image, modélisation ou choix artistique.**
4. **Création originale autorisée sans référence visuelle pertinente** : si un outil de génération d'image est disponible, créer d'abord **un concept de base** fidèle à cette DA, soumettre à validation humaine avant modélisation; sinon proposer un brief textuel approuvable. Une référence déjà approuvée **prévaut**, ne pas régénérer.
5. Une image générée reste un **concept**; seuls Blender/Godot fournissent la preuve d'un asset 3D produit.

## 3. Obtenir le bon rendu tôt

- Pour un nouvel ensemble architectural, réaliser **une baie / un module témoin** avec matériaux et éclairage représentatifs *avant* la multiplication de dizaines de modules.
- Fixer un **contrat visuel court** depuis la référence approuvée : `maintenance_state`, `coverage` (ponctuelle/étendue/dominante), `intensity`, distance TPP et exceptions mieux entretenues. Hériter des décisions déjà consignées plutôt que reposer les mêmes questions.
- Appliquer `references/WEATHERING.md` : **macro → moyen → micro**. Une dégradation dominante doit être évidente à 5–15 m; « saleté causale » ne veut pas dire patine timide. Les zones neuves/aisées restent propres si leur DA le demande.
- Réutiliser les presets et matériaux vérifiés avant de créer de nouvelles cartes. Lire `references/MATERIAL_PIPELINE.md` pour colorimétrie, UV, PBR, projection, VRAM et banc A/B.
- Comparer un **vrai rendu Godot** avec la référence approuvée aux caméras pertinentes, sous éclairage approprié. Un modèle techniquement correct mais générique ou trop propre = `VISUAL_INCOMPLETE`, pas `ART_READY`.
- Si une approche n'améliore pas le défaut visuel dominant, **changer de méthode** et non ajouter toujours plus de microdétails. Ne pas présenter des itérations manifestement sous la cible comme un résultat terminé.

## 4. Autonomie et protections

Après **approbation humaine du concept et autorisation explicite du périmètre de production**, enchaîner Blender, PBR, Godot, corrections et tests internes **sans arrêt entre micro-étapes**. Le mode supervisé reste possible sur demande.

**Accord préalable indispensable** pour changement de DA, nouvel asset/quartier hors périmètre, modification d'une zone validée (masterplan, greybox, accès, gabarits), téléchargement/acquisition non autorisé, service tiers ou distribution soumise à droits. Lire `AGENTS.md` et `CLAUDE.md` avant toute écriture dans le projet.

Réutiliser les vérifications encore valides. Ne tester de nouveau que les dépendances modifiées. **Aucun `PASS` hérité sans preuve**, aucun `ART_READY` avant gate final et validation humaine.

## 5. Livrables et réutilisation

- **FAST :** capture avant/après du vrai rendu, contrôle runtime ciblé, bref bilan; pas de dossier complet ni d'image Notion par micro-essai.
- **STANDARD :** témoins, vues ciblées, différences dominantes, tests de ce qui a changé.
- **FULL :** livrables source Blender et glTF/GLB selon pipeline, métriques utiles, contrôles Godot, comparatif concept/rendu, statut réel et validation finale.
- **Notion :** à la clôture d'un asset/jalon significatif, consulter `references/NOTION_ASSET_CATALOG.md`; conserver une fiche sans doublon et un aperçu dans le contenu pour la galerie. Vérifier licence, provenance, statut et écriture réellement effectuée. **Ne pas créer une fiche par variante cosmétique ou micro-itération**.
- **Faubourg des Traverses :** deux looks B18 validés (usé/entretenu et négligé/dominant) = références **locales**, à relier aux fichiers réels via `templates/material-profile.md` et `references/ZONES.md`. Leur valeur technique reste `REFERENCE_ONLY` tant que sources et paramètres exacts ne sont pas vérifiés.
- **Panachage :** City Builder décide de la distribution entretien/usage par façade; Environment produit les variantes cohérentes; pas de copie uniforme ni hasard pur. Ne jamais déclencher automatiquement le Skill City Builder.
- **B19 :** `references/B19_TRANSFER_TEST.md` spécifie le test de transfert local. Il reste `NOT_EXECUTED` tant que Godot n'a pas réellement été lancé.

**Ne pas confondre** `CREATED`, `TESTED`, `GEOMETRY_PASS`, `VISUAL_INCOMPLETE`, `ART_READY` et `BLOCKED`. Signaler clairement toute preuve inaccessible. Les guides techniques détaillés restent dans `references/`; ne les lire que pour la tâche concernée.
