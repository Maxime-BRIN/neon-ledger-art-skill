# Test de transfert V1.5 — B19 / Faubourg des Traverses

## Statut réel

**PLAN / NOT_EXECUTED** : la scène Blender/Godot et les variantes récentes B18/B19 du Faubourg n'ont pas été accessibles dans cette session via le dépôt du jeu. Ce document ne vaut donc **pas** preuve d'une modélisation ou d'une validation Godot sur B19. Le test doit être réalisé par l'agent local qui a accès au workspace Windows.

## Mission locale, sans nouvelle DA

- Projet : Neon Ledger ; zone Faubourg des Traverses ; cible B19 et commerce V07.
- Références : concepts cyberpunk approuvés, B19 vertical et discret, mobilier commercial plus sobre, surfaces métalliques sombres reprises, réseaux apparents. Deux niveaux d'entretien approuvés sur B18 servent de **qualité de rendu et de méthode**, pas de copie de couleurs B18.
- Respecter dimensions/portes/gabarits canoniques, K01, greybox et masterplan. Pas de modification de protections sans accord.
- Mode : STANDARD pour la première transposition de familles de matériaux, FAST pour les micro-corrections internes; FULL uniquement à la livraison finale ou intégration réelle.
- Réutiliser la bibliothèque de matériaux validés + banc existant; ne pas re-sourcer les ressources déjà contrôlées.
- **Première action** : vérifier que les deux presets B18 approuvés sont disponibles comme ressources réelles. Sinon consigner fichiers absents et résoudre ce seul blocage avant de poursuivre; ne pas prétendre avoir reproduit le matériau.

## Contrat artistique B19

1. Conserver la dominante sombre, verticalité et personnalité privée/discrète.
2. Séparer commerce plus maintenu, panneaux industriels différemment vieillis, réseaux et coffrets corrodés et arrière-façade potentiellement négligée **selon emplacement réel**.
3. Différenciation des matériaux à grande échelle d'abord : l'état « usé » ou « négligé » doit être évident à 5–15 m, sans uniformité ni rouille de cuivre.
4. Réparer les symptômes techniques connus : colorimétrie, projections UV, rouille trop orange, masques répétitifs.
5. Ne pas générer de concept B19 concurrent; conserver l'image approuvée.

## Test de convergence minimal

- Produire un témoin de façade B19 + commerce V07 avec le matériau adapté dans le banc existant.
- Comparer **1 capture neutre et 1 nocturne** au concept B19 et à l'état précédent.
- Vérifier l'absence de régression en dimensions/clearance/erreurs Godot; mesures de coût ciblées si shader nouveau, sinon héritage de preuves valides.
- Livrer un compte rendu bref des écarts, ressources modifiées et nombre d'itérations internes.
- Si le rendu est encore trop propre par rapport au contrat, **corriger le macro-weathering en interne avant de soumettre**.
- Arrêter si décision humaine nécessaire (nouvelle DA, asset externe, dérogation gabarit ou nouveau périmètre). Ne pas appeler `ART_READY` sur un témoin tant que le lot final n'est pas vérifié.

**Critère de succès V1.5 :** un premier témoin B19 stylistiquement convaincant, sans succession d'approbations mineures et sans accumulation de scripts/rapports jetables. Observer les durées et nombre de corrections sans promettre une réduction quantifiée.
