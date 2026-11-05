# V1.4 — Production rapide et contrôles proportionnels

## Objectif

Accélérer les petites modifications de matériaux, textures, éclairage ou détails sans supprimer la sécurité des fichiers ni la fidélité aux références. **Un changement mineur ne doit pas déclencher une nouvelle chaîne complète de sourcing, audits UV, rapports et validations.** Réutiliser les bancs et les preuves existants si leurs dépendances sont inchangées.

## Routage prioritaire V1.5

**Le mode doit être choisi à l'entrée du SKILL.md avant toute lecture ou tâche lourde.** Une petite retouche sur asset/DA et licences approuvés en FAST ne déclenche pas le sourcing, la phase concept, la matrice complète, un nouveau banc ou une mise à jour Notion à chaque micro-correction. Lire seulement les références touchées et conserver les preuves dont les dépendances sont inchangées.

La production du nouveau lookdev de façade/kit est STANDARD jusqu'à premier témoin convaincant; les petites itérations de paramètres sur ce témoin passent en FAST. La livraison finale en jeu est FULL.

## Choisir le mode d'après le risque réel, pas selon la taille du prompt

| Mode | Déclencheurs | Minimum attendu |
| --- | --- | --- |
| **FAST** | Matériau, roughness, texture déjà autorisée, decal, couleur, paramètre lumière, détail visuel local dans un banc approuvé; pas d'édition des volumes, UV, collisions, entrées ni DA | Reuse du banc, diff ciblé, contrôle d'import/runtime, **1 vue principale A/B**, une vue neutre seulement si l'appréciation du matériau l'exige, vérification légère des fichiers protégés, 3 lignes de bilan |
| **STANDARD** | Nouvelle façade/kit, adaptation de mesh, plusieurs matériaux ou sources, nouveau shader à coût significatif, changement d'UV, variations architecturales locales compatibles | Inventaire ciblé, captures comparaison concept/rendu, tests ciblés selon les changements, performance représentative et rapport bref |
| **FULL** | Nouvelle zone, changement d'emprises/ouvertures, kit final livré, validation ART_READY, intégration définitive, optimisation globale, nouvelle source externe ou situation à risque | Tous les gates applicables : métriques, collision/navigation si impactée, licences, provenance, rendu Godot, performance/LOD et revue humaine |

La gravité prévaut : changement de géométrie protégée ou de sécurité = arrêt/autorisation, même si l'utilisateur parle d'une « petite retouche ». **Un nouveau shader complexe qui ajoute de la VRAM ou modifie le pipeline peut relever de STANDARD.** Ne pas forcer FAST au détriment de l'exactitude.

## Politique d'autonomie

- Le mode par défaut est **SUPERVISÉ** avant concept approuvé ou autorisation de production. **Après validation explicite du concept et autorisation d'un périmètre de production**, utiliser **AUTONOME DANS CE PÉRIMÈTRE** par défaut : modélisation, PBR, import, captures, corrections, retests itératifs sans re-demander l'accord entre missions 2 et 3. Les gates internes restent appliqués, mais ne constituent plus des interruptions humaines.
- L'utilisateur peut demander le mode **SUPERVISÉ** pour imposer des validations aux jalons internes; respecter ce choix.
- L'autonomie ne permet jamais d'élargir le périmètre à un autre kit/quartier, changer DA approuvée, télécharger sans autorisation, transférer vers un service tiers ou modifier zone/géométrie protégée.
- En cas de conflit, de licence absente, d'action externe nécessitant accord ou de correction irréalisable sans toucher au canon : arrêter **seulement l'opération bloquée** et présenter la décision précise.
- Conserver la validation humaine du **concept initial** et du **livrable final**. Un utilisateur peut demander une pause intermédiaire.

## Invalidation sélective des preuves (cache de validation)

Réutiliser une preuve précédente **uniquement** si les fichiers/paramètres dont elle dépend n'ont pas changé et si son périmètre reste valable. Noter les dépendances sans recréer un audit complet.

| Changement | Contrôles à reprendre | Contrôles généralement réutilisables |
| --- | --- | --- |
| Roughness / couleur / texture sur même UV | rendu ciblé, chargement shader/material, résultat visuel | géométrie, collision, navigation, UV et licence déjà vérifiée |
| Nouvelle source de texture | licence/provenance de **cette source**, import et rendu | autres licences, géométrie |
| UV modifiés | densité/unwrap sur pièces touchées + rendu | navigation si collision inchangée |
| Nouveau mesh/saillie | dimensions/collision/clearance pertinentes + vues | provenance des textures inchangées |
| Nouveau shader gourmand | rendu, erreurs Godot, mémoire/temps représentatifs | géométrie et licences inchangées |
| Intégration en scène de jeu | interactions, caméra/navigation et performance en contexte | preuve de licence existante si identique |

**Jamais de cache aveugle :** une preuve ancienne incompatible, manquante ou liée à une version différente = NOT_TESTED et contrôle nécessaire.

## Réutilisation des outils

- Privilégier un **banc de validation réutilisable** par asset/kit, avec scènes, caméras, lumières et commande de rendu stables; créer un nouveau banc seulement si aucune base appropriée n'existe ou si le précédent est techniquement corrompu/incompatible.
- Ne pas créer systématiquement un dossier de 9 captures, scripts de reconstruction, fichiers JSON et rapports Markdown à chaque ajustement mineur.
- Si comparaison A/B, conserver A comme référence immuable et capturer B depuis le même environnement; on peut faire plusieurs essais internes avant l'unique résultat présenté.
- Réutiliser les états de licences/provenances et dossiers consultés, sauf modification des ressources ou doute réel; pas de nouvelle recherche Web obligatoire pour chaque roughness.
- Ne pas recharger intégralement les fichiers d'instructions à chaque sous-commande interne; relecture au changement de scope, de version de Skill ou de risque.
- Pour une correction locale, utiliser un **delta** dans le rapport de fidélité existant plutôt que créer une matrice complète nouvelle.

## Preuves et sortie au bon format

**FAST :** une capture A/B (+ neutre uniquement utile), résultat test, fichiers changés, écart artistique encore dominant. **STANDARD :** 2–4 vues pertinentes, contrôle fonctionnel ciblé, coût approximatif/mesuré si pertinent, rapport concis. **FULL :** livrables détaillés du Skill.

La documentation, les CREDITS/Notion et les audits complets sont actualisés à la **clôture de l'asset ou de la phase de production**, ou immédiatement si une nouvelle source/licence exige d'être tracée; pas de fiche/galerie Notion par micro-itération. Ne pas prétendre avoir synchronisé sans autorisation et preuve.

Le résultat FAST ou STANDARD n'est **pas ART_READY automatiquement**; la revue finale FULL reste nécessaire. Une capture concept IA ne remplace jamais une capture du vrai modèle.

## Boucle de convergence V1.5

1. Comparer le rendu réel avec le contrat visuel et classer le principal écart selon **MACRO / MOYEN / MICRO / STRUCTURE / LUMIÈRE**.
2. Pour une façade trop propre, agir en priorité sur couverture/intensité à l'échelle de l'image, pas sur les seules normales ni petites fixations.
3. Itérer plusieurs fois **en interne sur le même banc**, sans nouveaux rapports et validations pour chaque micro-essai; archiver seulement le résultat pertinent et les sources reproductibles.
4. Si deux approches raisonnables n'apportent pas d'amélioration visible, changer de technique (textures, masques, decals, projection, calibrage) plutôt que forcer le même réglage. Ne pas inventer de satisfaction humaine.
5. Si le besoin de la prochaine correction sort du périmètre approuvé ou exige une licence/ressource externe, demander **seulement cette décision**.
6. Réaliser un seul bilan court sur le résultat consolidé; gates FULL et synchronisation documentaire au jalon final.

## Exemples pratiques

- B18_ART_V2, ajustement d'enduit, roughness et peinture à géométrie/UV inchangés : **FAST**. Réutiliser le banc; 1 comparaison + rendu neutre au besoin; pas de recherche web, de 9 vues ou d'audit UV complet.
- Remplacement complet du matériau via un ShaderMaterial personnalisé avec nouvelles cartes 3K, effets mémoire : **STANDARD** ciblé pour performance/VRAM; pas de re-test navigation si mesh intact.
- Nouveau passage de câbles avec saillie affectant la caméra : **STANDARD + test clearance**, et autorisation si dépassement.
- B18 entier déployé dans Faubourg des Traverses : **FULL**, test en scène et accord humain.
