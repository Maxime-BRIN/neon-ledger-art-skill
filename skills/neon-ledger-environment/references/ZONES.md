# Profils de zones (extensibles)

Les profils **décrivent uniquement les zones documentées**. Un profil absent ne justifie pas d'appliquer Weakland par défaut. Rechercher les docs officielles Neon Ledger avant toute invention.

## Weakland — Secteur Bas (profil initial)
Quartier résidentiel HLM pauvre, oppression verticale et densité humaine. Brutalisme social ancien colonisé par technologie low-cost et réparations improvisées.
- Silhouettes : béton préfabriqué, ajouts métalliques, câbles, évacuations, climatiseurs, supports fonctionnels.
- Matériaux : béton vieilli, peinture usée, métaux oxydés, vitrages irréguliers, humidité localisée.
- Éclairage : contrastes entre vie intérieure chaude, infrastructure publique froide et enseignes commerciales ponctuelles ; pas de surcharge gratuite.
- Storytelling : entretien inégal, habitation persistante, pauvreté non caricaturale.
- **Grille 6 × 3 m uniquement pour le kit de façades HLM concerné** ; aucune contrainte sur les autres objets.
- Risques : immeuble banal « + deux néons », répétitions procédurales, câbles flottants, faux trous de fenêtres.

## Faubourg des Traverses — zone spécifique Neon Ledger

**Statut :** DA et deux rendus B18 de vieillissement approuvés par l'utilisateur dans le projet; le Skill ne détient **pas** les fichiers sources locaux correspondants. Ne pas inventer de chemins/images SHA définitifs. Avant d'annoncer un preset `SOURCE_VERIFIED`, résoudre les chemins effectifs dans le workspace local avec `templates/material-profile.md`.

- Quartier d'ancien faubourg dense, organique, maintenu en activité, architecture stratifiée; avant/arrière, commerce/logements/technique avec états d'entretien différents.
- **Deux références de matière approuvées sur B18** : `FAUBOURG_WORN_PARTIALLY_MAINTAINED` et `FAUBOURG_NEGLECT_DOMINANT` dans `references/WEATHERING.md`. L'agent local doit pointer vers les captures Godot réellement approuvées (neutre, nocturne) et les paramètres exacts disponibles.
- **Mix souhaité** : panacher les deux états sur le quartier avec variabilité des assets, sans répétition mécanique ni hasard pur. Une façade commerçante peut être entretenue tandis que les parties résidentielles/techniques du même bâtiment sont très usées.
- **B18** : restaurant chaleureux et fonctionnel sous logements vieillis, contrastes entre commerce maintenu et structure dégradée.
- **B19** : silhouette plus verticale, panneaux métalliques sombres, commerce discret côté V07, réseaux techniques et réparations; ne pas recopier le matériau crème ou la devanture B18.
- **Règle de responsabilité** : City Builder décide de la distribution spatiale des états selon usages et composition du quartier; Environment construit et adapte les familles matière/asset; Godot vérifie. Le Skill ne décide pas de réaffecter arbitrairement les 31 bâtiments.
- Deux états ne sont **pas deux textures universelles**. Varier teintes, réparations, UV, intensité, chronologie et équipements. Une graine déterministe évite les changements au rechargement, mais un simple seed ne suffit pas pour une identité différente.
- Les concepts validés et les dimensions canoniques du projet font autorité. Aucun changement de masterplan/greybox ni saillies non autorisées.

## Autres secteurs / quartiers
**Non définis dans ce dépôt.** Charger les références officielles du projet ou rédiger une proposition à valider avant de la traiter comme canon.

### Modèle d'un nouveau profil
Nom, statut (canon/proposition), fonction, richesse, architecture, palette, matériaux, technologie, signalétique, éclairage, marqueurs iconiques, interdictions, contraintes dimensionnelles propres.
