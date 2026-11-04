# Phase 3 V0.4 — Asset Coverage 100 % / résolution des besoins

## Objectif absolu

À partir d'un registre stable d'IDs de besoins essentiels, obtenir **N/N ressources prêtes** sur le périmètre approuvé (Faubourg des Traverses : **50/50**, sauf modification explicite du brief par l'utilisateur). Le diagnostic 15/50 ou le sourcing de neuf candidats n'est pas la fin de la phase : c'est une liste de travail à résoudre.

## Unité de comptage : besoin, pas modèle

- **Besoin essentiel** : composant fonctionnel et artistique nécessaire à une sous-zone définie, avec ID immuable et critères d'acceptation précis. Exemple : entrée résidentielle B18, auvent commercial B19, kit de signalétique pour S02.
- **Modèle unique** : un fichier ou une famille d'assets local/externe, peut satisfaire plusieurs besoins si fit testé individuellement.
- **Évaluation** : relation entre un modèle candidat et un besoin; peut être plus nombreuse que le nombre de modèles uniques.
- **Solutions identifiées** : candidat concret, adaptable, licence potentiellement vérifiable, ou création sur mesure entièrement spécifiée mais *non réalisée*. Une intention vague « chercher » ne compte pas. Un brief approuvé ne devient pas un asset.
- **Ressources prêtes** : existant FIT vérifié, ADAPT effectivement adapté/vérifié, ou asset obtenu légalement avec permission, import/test dans Godot réussi et adéquation à l'usage prouvée; aucune ambiguïté de licence. Une commande de téléchargement non exécutée, un achat non conclu, un modèle non importé ou un placeholder ne comptent pas.

Reporter deux chiffres séparés : **solutions identifiées X/N** et **ressources prêtes Y/N**. Demander `APPROUVER_DA_ASSETS` uniquement lorsque **Y=N** et que les preuves existent. Une ressource peut servir à plusieurs besoins, mais chaque affectation doit avoir ses tests de FIT distincts.

## Boucle obligatoire : NE PAS ABANDONNER LES MANQUES

1. Lire tous les besoins essentiels, y compris ceux rejetés ou sans modèle, et figer la liste d'IDs du périmètre.
2. Contrôler les candidats locaux pour les besoins encore ouverts; rejeter avec motif ceux qui ne conviennent pas.
3. **Chercher activement**, avec les outils disponibles, des modèles gratuits adaptés pour **tous** les besoins manquants; vérifier URL exacte, licence à la source, auteur, format, dimensions, usage commercial/attribution, qualité et réutilisabilité. Privilégier les kits modulaires couvrant plusieurs besoins sans incohérence esthétique.
4. Pour tout manque persistant, produire un **brief sur mesure précis** et proposer l'usage de `neon-ledger-environment` avec le lot minimal de kits à créer; ne jamais lancer le Skill automatiquement.
5. Regrouper dans un tableau de décisions les téléchargements, adaptations, créations et alternatives par besoin, avec coûts d'effort, risques et autorisations. Demander l'accord humain **sur les actions spécifiques**, non une approbation générale de la phase.
6. Après autorisation : effectuer uniquement les opérations autorisées, vérifier effectivement les licences/imports/dimensions/rendu dans Godot, tenir à jour le registre et les éventuelles entrées Notion si autorisé. Si le projet n'est pas accessible, rester en attente de vérification. Si l'utilisateur refuse un asset, proposer une autre solution ou demander un changement de brief.
7. Recalculer la couverture et continuer jusqu'à **N/N READY**, ou rester `BLOCKED` avec liste précise des approbations et dépendances. **Ne pas déclencher la phase 4** si N/N n'est pas atteint.

## Trois statuts de progression (ne pas confondre)

- `AUDITED` : besoin classé, manque connu, pas nécessairement de solution.
- `SOLUTION_IDENTIFIED` : candidat concret ou kit spécifié, encore non disponible/validé.
- `READY` : ressource utilisable, vérifiée, légalement documentée, et prête pour l'intégration dans la sous-zone. Un asset n'est pas READY du seul fait qu'une fiche a été créée.

Un besoin `MISSING`, `REJECT` ou `PLACEHOLDER` ne doit jamais être READY. Un statut `FIT` ou `ADAPT` seul n'est pas une preuve d'import et de fonctionnement. Distinguer modèle prêt à l'emploi et scène déjà habillée : la **mise en place dans le quartier appartient à la phase 4**, pas à la phase 3.

## Règle anti-triche

- Pas de suppression ou déclassement d'un besoin essentiel pour améliorer le pourcentage.
- Pas de réduction automatique de 50 à 15; un pilote limité **nécessite l'accord humain explicite** et tous les autres besoins restent visibles en backlog.
- Aucun modèle incompatible recyclé pour plusieurs besoins.
- Ne pas appeler « couvert » un modèle seulement trouvé en ligne ou un brief de création.
- Reporter les compteurs indépendants : modèle unique, évaluation, besoin unique, nombre prêt.
- Indiquer les capacités non disponibles (recherche Web, import Godot, Notion, génération), les besoins bloqués et les actions nécessaires sans inventer les succès.
- Ne pas forcer des téléchargements ou la création de dizaines de modèles peu réutilisables; proposer kits mutualisés et variantes pertinentes, sur accord.

## Demande de validation

Produire `templates/asset-coverage-register.md` et les preuves de contrôle. Si Y < N, la sortie attendue est **DEMANDER_AUTORISATIONS_ASSETS** ou **BLOCKED**, et non `APPROUVER_DA_ASSETS`.

La revue humaine de la DA et des choix artistiques peut avoir lieu avant Y=N, mais ne déverrouille pas la phase 4. Les approbations techniques et artistiques restent explicites.
