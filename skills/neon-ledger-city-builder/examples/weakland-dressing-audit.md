# Weakland — exemple d'audit V0.2 (sur captures fournies)

> Exemple pédagogique issu d'un retour visuel, **pas** un audit de scènes Godot ni une autorisation de modifier la zone.

## Analyse comparative

**Observé :** les façades résidentielles ont des modules lisibles (fenêtres, unités de climatisation, tuyaux et fenêtres éclairées); cependant plusieurs murs latéraux sont nus, les surfaces au sol très abstraites, les accès peu contextualisés et les volumes fortement répétés. Le contraste lumineux local est faible et certaines fonctions du niveau sont difficilement identifiables.

**Références :** elles présentent plusieurs fonctions distinctes : bâtiment habité avec balcons/enseignes/commerces, ruelles techniques étroites, zones de street food, dispensaire, commerce au pied d'immeuble, réseaux, sols humides, lumière motivée. Elles ne constituent pas une liste d'assets à copier partout. Certaines sont plus réalistes et riches que le rendu Godot actuel.

**À vérifier dans Godot** : dimensions, modes d'éclairage, état d'avancement de chaque façade et accessibilité des zones. Impossible de conclure aux causes techniques uniquement depuis les captures.

| Sous-zone candidate | Besoin fonctionnel | Fit check attendu | Statut provisoire |
| --- | --- | --- | --- |
| Halls / pieds HLM | accès résidentiels identifiables, boîtes aux lettres, interphones, éclairage d'entrée | vérifier les portes, modules de socle et mobilier; ne pas inventer d'intérieurs | AUDIT_REQUIRED |
| Cour | fonction sociale/maintenance/commerciale à **faire confirmer** | bancs, éclairage, signalétique ou stand selon fonction choisie; ne pas imposer de marché | DESIGN_REQUIRED |
| Pignons et toitures | rupture de grandes surfaces neutres là où les volumes sont visibles | kits de façade/structure technique adaptés, ou mur sobre justifié | FIT_REQUIRED |
| Galeries / ruelles | plomberie, collecte, ventilation, signalétique fonctionnelle, gestion de l'eau | échelle, collisions et cohérence des éléments | FIT_REQUIRED |
| Commerces autorisés | vitrines/auvents/signage appropriés | architecture compatible avec réservations gelées; demander changement sinon | DESIGN_REQUIRED |

## Décision recommandée

1. **Ne pas reconstruire les HLM** sans accord : prioriser la composition et les éléments ajoutables sans toucher au greybox gelé.
2. Demander la fonction préférée de la cour et quels rez-de-chaussée sont commerciaux vs résidentiels, en proposant des options cohérentes avec le masterplan approuvé.
3. Établir une liste d'assets manquants **par fonction** avant le placement. Chercher des modèles gratuits compatibles avec vérification de licences; proposer `neon-ledger-environment` pour les modules clés.
4. Capturer 3–5 vues TPP dans Godot avec caméras mémorisées, puis itérer les sous-zones et comparer avant/après. Pas de `PASS` artistique sans nouvelles captures.

## Exemple de fiche de besoin

`WL-NEED-HALL-01` : kit d'entrée HLM compact (interphone, numérotation, boîte aux lettres, éclairage local); dimensions calculées **après inspection du bâtiment**, pas inventées. Priorité essentielle si hall visible. Réutilisation locale seulement si FIT. Recherche gratuite à proposer; sinon mini-brief de création sans lancer automatiquement le Skill.
