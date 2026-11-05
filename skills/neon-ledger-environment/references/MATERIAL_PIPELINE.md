# Material pipeline & reusable lookdev — V1.5

## Ce que doit produire un preset validé

Une fiche légère : ID stable, projet/zone, capture Godot réelle neutre + nuit, variante de référence et statut humain, sources textures + licences, fichiers matériaux/shaders, repères UV, paramètres des masques, coût observé et limites connues. **Les deux looks B18 ne deviennent reproductibles que si les sources/paramètres exacts sont retrouvés dans le projet local.** Une capture seule = `REFERENCE_ONLY`.

Réutiliser un preset existant par adaptation paramétrique plutôt que recomposer un shader et toutes ses cartes pour chaque façade. Séparer matériaux géométriquement identiques des variantes d'albedo/masque/roughness. Un atlas de démonstration ou override Godot n'est pas présumé prêt pour 31 bâtiments.

## Contrôles techniques à l'introduction d'un mécanisme, pas à chaque retouche

- **Colorimétrie :** albedo/emission sRGB selon import, roughness/metallic/normal/masques en données linéaires, conversions explicites et vérification du risque de double sRGB.
- **UV/projection :** tester orientation/échelle sur quelques repères connus; ne pas placer un masque de rouille décalé sur une armoire ou à travers un cadre par erreur.
- **Texel density :** inspecter la résolution réelle de chaque source, pas le nom du dossier; suréchantillonner un atlas ne crée pas du détail.
- **PBR métal/oxyde :** distinguer acier nu, peinture, oxyde rugueux, salissures et coulures; la rouille n'est pas un cuivre métallisé brillant.
- **Canaux :** déclarer explicitement le rôle de chaque canal. Un masque de corrosion empaqueté dans une texture ne devient pas un ORM standard sans remapping validé.
- **Mémoire :** mesurer séparément textures référencées par la variante, images résidentes du banc, cache/overrides et vraie mémoire d'un paquet final isolé; le delta d'un A/B avec les deux variantes chargées n'est pas le coût d'une release.
- **Perf :** sampler des points pertinents, distinguer GPU median/p95, draw calls, VRAM, LOD et affichage. N'en déduire aucun FPS de quartier complet sur un banc isolé.

## Banc A/B réutilisable : contrat d'interface

Le Skill demande la réutilisation de la **scène et des scripts existants du projet**. Si aucun banc n'existe, en concevoir un une seule fois avec une interface logique :

`compare_materials --before <variant_A> --after <variant_B> --views neutral,night --out <dir>`

La commande ci-dessus est une **interface cible illustrative**, pas un exécutable déjà livré. Adapter au moteur et aux outils réels; ne pas afficher un succès si aucun runner n'existe ou n'a été exécuté.

- Les caméras, lights, post-processing et temps de rendu sont figés entre A/B.
- Le variant B change un **ensemble déclaré de ressources/paramètres**, pas une branche de code par ajustement.
- Captures produites hors des répertoires importés/observés par Godot, lorsque c'est compatible avec la configuration.
- Masques et matériaux non modifiés : pas de régénération.
- Vérification des dépendances et contrôles invalidés seulement.

## Conversion du témoin B18 en ressources réutilisables

1. Retrouver dans le projet local les sources et paramètres de A/B approuvés; consigner les chemins réels et versions. Si absents, classer `BLOCKED_MISSING_SOURCE` : ne pas inventer.
2. Contrôler que les variantes qui utilisent des overrides Godot rendent correctement en scène de jeu; conserver l'original Blender si son export GLB ne sait pas représenter un shader spécifique Godot.
3. Définir un paquet de matériaux Godot réutilisables avec variantes paramétrées et masques, sans garder l'ancien et le nouveau chargés en production.
4. Conserver les sources Blender, les textures d'origine et les contraintes de licence; tester aller-retour Blender/GLB uniquement là où le pipeline l'exige.
5. Mesurer le coût du paquet en contexte isolé puis en intégration réelle; documenter la différence.
6. Enregistrer un preset de zone dans le manifeste de matériaux et la fiche d'asset existante, **sans nouvelle BDD**.

## Réutilisation et variation

Les sous-familles `maintained` / `worn` / `neglected` sont des paramètres logiques, pas trois copies de chaque mesh. Utiliser masks, tiled PBR, vertex colors, decals peu nombreux ou shader params au niveau du module. Les variantes sont déterministes (ID stable / seed déclaré) pour que la régénération du quartier ne change pas leur apparence sans contrôle.

Le matériau final doit rester compatible avec le mode de rendu Godot en usage; les coûts de shaders/VRAM d'un banc RTX 5080 ne prouvent pas un budget cible universel.
