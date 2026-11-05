# Weathering & maintenance intent — V1.5

## Définir le résultat AVANT les détails

La DA / les références validées du projet et de la zone décident du niveau d'entretien. **« Vieillissement causal et non uniforme » ne signifie JAMAIS « petites taches localisées »** : une façade longtemps négligée peut être dégradée sur la majorité de sa surface, par exposition générale, pluie, pollution, entretien irrégulier et accumulations. Inversement, les matériaux neufs ou les zones prospères peuvent rester propres. Ne pas imposer un vieillissement à un autre projet ou une autre zone sans DA appropriée.

Contrat visuel minimal : `maintenance_state` (entretien), `coverage` (ponctuelle/étendue/dominante), `intensity` (faible/modérée/forte), `view_distance` (5–15 m TPP par défaut si pertinent) et `clean_exceptions` (objets/zones volontairement préservés). Ces valeurs viennent d'abord des références approuvées; ne pas re-questionner l'utilisateur si déjà déterminées. Les pourcentages, s'ils sont précisés par l'utilisateur, sont des cibles perceptives, pas des mesures automatiques certifiées.

## Presets validés dans Faubourg des Traverses

- **FAUBOURG_WORN_PARTIALLY_MAINTAINED (A)** : bâtiment usé avec vieillissement visible, reprises, corrosion en périphérie des métaux, mais entretien partiel lisible.
- **FAUBOURG_NEGLECT_DOMINANT (B)** : encrassement et pollution dominants sur les enduits, humidité générale avec couches crédibles, métal ancien significativement corrodé, interventions hétérogènes. Les façades conservent des exceptions entretenues, notamment certains commerces en service.
- Les captures B18 validées par l'utilisateur sont les **références artistiques**, pas une garantie que tous les fichiers techniques sont récupérés. Charger les matériaux et paramètres **réellement disponibles dans le projet**, puis qualifier `SOURCE_VERIFIED` / `REFERENCE_ONLY`. Ne jamais inventer un identifiant de texture, hash ou fichier.
- Les deux presets sont **locaux au Faubourg**. B19 conserve son langage métallique, sombre, vertical et le commerce discret côté V07. Ne pas dupliquer la teinte de B18 sur B19.

## Ordre d'exécution obligatoire : macro → moyen → micro

1. **MACRO (à 5–15 m)** : répartition globale du vieillissement, masses de pollution, teinte et décoloration, entretien perçu. Tester sous éclairage neutre et nocturne si nécessaire. Si un mur demandé négligé ressemble encore à du neuf, NE PAS passer au microdétail.
2. **MOYEN** : ruissellement sous bords et appareils, dépôts autour des grilles, pluies, remontées d'humidité, peintures et enduits d'époques différentes, traces de réparations, corrosion plausible.
3. **MICRO** : normal/height, grain, fines fissures, roughness, rayures et écaillage. Rien de cela ne remplace une composition macro manquante.

## Couches combinables

- Support d'origine (plâtre, béton, métal, peinture, béton peint) avec réponse PBR plausible.
- Décoloration et lessivage.
- Pollution / suie / poussière déposée selon exposition et circulations d'air.
- Humidité, capillarité, sels, crasse aux pieds de murs et zones abritées.
- Perte d'enduit / écaillage (sur le **bon matériau** : le plâtre ne rouille pas).
- Corrosion des éléments ferreux, migrations de rouille sur supports adjacents.
- Réparations de générations différentes et patchs.
- Pièces remplacées, nettoyage partiel, commerces encore exploités.

La causalité existe à **plusieurs échelles** : la pollution urbaine généralisée ou l'abandon expliquent une dégradation dominante; chaque tache n'a pas besoin de partir d'une vis. Ajuster distinctement les surfaces par type de matériau.

## Interdictions visuelles, à contrôler dans Godot

- Pas d'aplats orange uniformes (rouille cuivrée ou simple peinture), ni de métal de rouille entièrement brillant : peindre métal, oxyde, dépôt et roughness selon leur physique.
- Pas de taches géantes floues sans structure ou visibles comme du bruit procédural plaqué; introduire strates de formes et variations réelles.
- Pas de répétition trop régulière du masque sur les modules, ni de même vieillissement sur tous les matériaux.
- Pas de fissures sinusoïdales ou traitées comme crayon; fissures et reprises doivent paraître intégrées dans la matière.
- Pas d'usage indiscriminé des décals qui empile inutilement les appels de rendu et la VRAM.

## Gate visuel : résultat avant preuve administrative

Avant la livraison, inspecter la **vue de jeu** à distance cible : le niveau d'entretien est-il évident immédiatement, et le delta perceptible par rapport à la variante initiale ? En absence de progrès substantiel, faire une correction macro interne ou changer de méthode; ne pas livrer « encore un peu trop propre » quand la commande autorisait explicitement une dégradation dominante.

Conserver les accès, les gabarits et la DA officielle; une correction de shader ne donne jamais le droit de changer le canon.
