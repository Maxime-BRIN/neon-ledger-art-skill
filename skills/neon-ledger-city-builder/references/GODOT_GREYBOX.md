# Godot 4 — construction métrique et vérification

## Avant écriture

- Lire la version réelle de Godot, les scènes chargées, caméra actuelle, contrôleur, capsule, collision layers/masks, données de terrain et conventions de coordonnées.
- Vérifier que le masterplan a une approbation humaine courante, pas uniquement un champ `status` modifié par l'agent.
- Créer une zone/scène isolée et des groupes identifiés; ne pas ajouter directement des noeuds à un quartier gelé.

## Conversion rectangulaire (pour les primitives)

Pour une emprise locale `(min_x,max_x,min_z,max_z)` et une origine globale `(ox,oz)` :

- taille du BoxMesh `(max_x-min_x, hauteur, max_z-min_z)`;
- centre global `(ox + (min_x+max_x)/2, terrain_y + hauteur/2, oz + (min_z+max_z)/2)`;
- `scale=(1,1,1)` pour éviter une double multiplication accidentelle;
- mesures de la BoxMesh et de la CollisionShape cohérentes; ne pas supposer qu'un visuel prouve une collision correcte.

## Contrôles

- À partir du **scène réellement exécutée**, extraire positions mondiales, bounding boxes et tailles; comparer aux références, en mètres. Tester les façades/retraits et limites de circulation.
- Nav: tester spawn → sortie + embranchements avec la capsule réelle, virages, marches, passages couverts et caméra à la troisième personne. Contrôler occultations, points d'intérêt et cadrage. Le FOV n'est pas un remède à une implantation erronée.
- Capturer vue orthographique exacte et vues TPP de spawn, sorties, intersections et points de repère. Ne jamais dire avoir capturé la scène si l'outil n'était pas disponible.
- Exécuter les tests sans téléchargement automatique, sans scripts destructifs, sans toucher aux zones verrouillées. Si Godot/MCP est indisponible : rapport de blocage et étape non approuvable pour la partie réelle.

## Retours d'expérience (Faubourg V3, 6 novembre 2026)

- **Outils paramétrés par la zone :** ne pas copier-coller audit, capture et navigation d'une zone à l'autre. Les écrire une fois, avec l'identifiant de la zone et le chemin du masterplan en paramètres (origine, sol et masterplan lus dans `City.zone`).
- **Scène réellement chargée :** les scènes hébergées dans la scène de jeu ne construisent leur sol qu'après l'entrée en jeu. Appeler la méthode d'entrée du menu (`Menu.enter_game()`) et attendre environ 60 images physiques avant tout tir de rayon. Sans cela, l'audit signale à tort « pas de sol ».
- **Scène générée :** produire la scène d'une zone par un script de génération rejouable (CityBuilder + nœuds de jeu conservés), jamais à la main. Garder la sauvegarde de la version précédente.
- **Tolérance :** une tolérance de test (par exemple une image sur dix mille où la caméra frôle un angle) se documente dans le test et dans le dossier, avec la classe MINOR.
- **Sol des espaces :** les espaces posés 5 cm au-dessus du sol sans collision propre sont un MINOR connu ; ne pas le redécouvrir.
