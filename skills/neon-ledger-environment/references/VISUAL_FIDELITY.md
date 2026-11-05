# Visual Fidelity & Detail Gate — V1.2

## Pourquoi

Un kit peut être correct métriquement, modulaire et importable dans Godot, tout en produisant un bâtiment générique ne ressemblant pas au concept artistique approuvé. **L'acceptation technique ne certifie pas l'identité visuelle.** Le gate empêche la validation artistique prématurée, sans exiger d'un kit K01 tous les ajouts spécialisés destinés à K02/K03/K04.

## 1. Décomposer les références approuvées AVANT Blender

Pour chaque bâtiment / façade / angle important, analyser les détails visibles à 5–15 m (TPP), et le plan plus lointain si pertinent. Séparer :

1. Architecture secondaire : dormants, vitrages en profondeur, stores, volets, bandeaux, éléments d'angle, seuils, supports.
2. Commerce et usages : vitrines, comptoirs, signalétique, menus, rideaux, appuis, accessoires, distribution des activités.
3. Stratification technique : câbles, chemins de câbles, conduites, raccords, boîtiers, climatisations, ventilation, extraction, fixations; relier l'équipement à sa fonction, sans câbles flottants.
4. Occupation et histoire : modifications successives, reprises d'enduit, plaques rivetées, usure causale, traces de ruissellement, objets d'usage.
5. Lumière et matière : fenêtres inégalement éclairées, sources diégétiques, indices colorés, métal, béton, verre, variation de roughness, traces d'humidité.
6. Couronnements/toits : silhouette et équipements seulement dans la hauteur/enveloppe autorisées; un concept peut proposer des éléments incompatibles.
7. Contexte : sol humide, enseignes, ambiance, silhouettes et VFX. Identifier ce qui relève de la scène Godot et non d'un mesh.

Une image est une **intention artistique**, jamais une preuve métrique, ni une autorisation de changer le masterplan.

## 2. Suivre l'exécution à la bonne granularité

Remplir `templates/visual-fidelity-matrix.md` avec les colonnes : ID de référence, source, bâtiment/façade, famille, détail observable, importance (HERO/MAJOR/SUPPORT), rôle, distance, solution (EXISTING/ADAPT/SOURCE/CREATE/GODOT_EFFECT/INCOMPATIBLE), kit propriétaire, état (PLANNED/PRODUCED/INTEGRATED/VERIFIED/DEFERRED_APPROVED), contrainte métrique, preuves et acceptation.

Une ligne peut renvoyer à un kit ultérieur **avec autorisation explicite de report**; elle n'est pas marquée produite. Les concepts proposés, images IA et éléments sourcés non vérifiés ne valent pas `VERIFIED`.

## 3. Comparaisons obligatoires

À la fin de chaque phase utile, produire :
- référence approuvée et capture du **vrai modèle** sur des angles comparables;
- une vue éclairage neutre pour juger volume, relief et vrais matériaux;
- une vue TPP contextuelle dans Godot à l'intégration (ou `NOT_TESTED` explicite);
- pour chaque détail majeur, emplacement et état réel; 3 écarts dominants, action, responsable, gravité et preuve après correction.

La différence d'éclairage, de focale ou de perspective doit être mentionnée. **Ne jamais substituer une image concept IA / paintover à une capture Blender ou Godot.** Ne pas inventer une métrique « 90 % visuellement identique »; la fidélité est une décision argumentée et révisable.

## 4. Richesse cyberpunk — uniquement si demandée et approuvée

Pour des concepts urbains cyberpunk riches, préserver l'intention de **construction stratifiée** : une architecture d'origine réutilisée, puis adaptations commerciales, réseaux apparents, réparations, interfaces et lumière contemporaine. Ne pas réduire ce langage à « immeuble classique + enseigne néon ». Les détails sont positionnés selon le fonctionnement et les contraintes, pas distribués aléatoirement.

Cas de référence Neon Ledger / Faubourg des Traverses :
- **B18** : restaurant actif et chaleureux au socle; menuiseries lisibles, vitrines et profondeur, éclairage commercial, écrans/menus et réseau de service; façades résidentielles à traces d'occupation, reprises, câbles attachés, climatiseurs localisés; contrastes cyan/magenta/ambre motivés.
- **B19** : commerce plus discret côté V07; enveloppe métallique sombre reprise, réparations, coffrets et gaines, ventilation, fenêtres éclairées de façon irrégulière, accents lumineux ponctuels; identité distincte de B18.
- Les deux restent des immeubles constructibles, dans leurs dimensions/portes de 1,50 m et enveloppes validées, sans saillie ou équipement de toiture ajouté hors volume par défaut.
- Les images enrichies sont **concepts non modélisés**. Vérifier qu'elles sont accessibles dans le projet et enregistrer leur statut d'approbation, sans les prétendre déjà produites.

Le Skill s'applique aux autres styles : ne jamais imposer la saturation technique, l'usure, les néons ou des enseignes à une zone qui ne les demande pas.

## 5. Partager correctement K01 / K02 / K03 / K04

- **K01** : structure et enveloppe modulaire, ouvertures, profondeur des fenêtres, cadre/socle, interfaces de fixation et toitures autorisées.
- **K02** : fonctionnement commercial, comptoirs, accessoires, usages et scénographie commerciale.
- **K03** : réseaux, HVAC/extraction, supports, traversées techniques compatibles.
- **K04** : signalétique, vieillissement, traces d'usage et identité graphique.
- **Godot / L01 / H01–H02** : sources lumineuses dynamiques, effets d'ambiance, personnage et animations; ne pas les attribuer mensongèrement aux kits de Blender.

Une façade finale doit réunir les couches nécessaires, mais **on ne bloque pas l'acceptation géométrique K01** pour les accessoires K02–K04 expressément différés. On bloque en revanche sa déclaration `ART_READY` à l'échelle du bâtiment complet tant que les écarts majeurs restent ouverts.

## 6. Go / No-Go

- `GEOMETRY_PASS` : dimensions et assemblage satisfaisants, indépendamment de la DA.
- `VISUAL_INCOMPLETE` : familles majeures absentes ou non vérifiées.
- `ART_READY` : richesses et identité attendues pour le **périmètre approuvé du livrable**, comparées au vrai rendu, sans `MAJOR` caché.
- `NOT_TESTED` : preuves Godot / Blender ou référence absentes.
- `BLOCKED` : conflit avec un contrat approuvé, absence d'autorisation, usage illicite ou impossibilité de respecter un impératif.

**Mode V1.4 :** sur une petite correction FAST, corriger les écarts utiles, réutiliser la matrice existante, capturer une vue A/B réelle et actualiser uniquement les lignes modifiées; **ne pas exiger une revue humaine à chaque micro-itération**. En mode STANDARD, contrôler les composants modifiés. En mode FULL (livraison / ART_READY), comparer l'ensemble des vues majeures et demander validation humaine. Les droits d'acquisition et les protections restent inchangés. Voir `ITERATION_MODES.md`. Aucune création massive hors périmètre autorisé.
