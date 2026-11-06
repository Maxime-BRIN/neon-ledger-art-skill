# Masterplan 2D — urbanisme crédible et composition spatiale (V0.3)

## Mission

Un plan peut être **géométriquement valide et artistiquement raté**. Le JSON, le SVG et les tests de collisions sont nécessaires, **mais ne prouvent ni le réalisme urbain ni l'intérêt du quartier à hauteur de joueur**. Le Skill doit traduire la demande de l'utilisateur en composition urbaine argumentée, sans imposer un style architectural, une densité, une symétrie ou une forme « cyberpunk » universelle.

**Principe anti-template :** ne jamais placer les bâtiments en grille uniquement parce que leurs emprises sont rectangulaires dans le schéma. Ne pas confondre lisibilité des données et alignement systématique des bâtiments.

## Étape 1 — intention et morphologie (avant toute emprise)

1. Lire les exigences **approuvées** : taille, bâtiment(s), usages, densité, style, accessibilité, liens aux voisins. En cas d'absence de directive sur la composition, proposer 1 à 2 concepts morphologiques avec recommandation motivée; soumettre les décisions majeures à l'utilisateur.
2. Définir l'**histoire spatiale** : pourquoi le quartier a pris cette forme (construction initiale, densification, extensions, occupation informelle, contraintes topographiques, services) et quelle différence existe entre les lieux.
3. Définir une **hiérarchie** concrète : axe primaire, accès, seuils, circulation secondaire, passages de service, lieux d'activité, retraits, espaces calmes. Une place n'est pas automatiquement centrée.
4. Construire une **séquence de marche TPP** : arrivée → seuil → virage/resserrement → révélation d'un lieu → choix de sortie. Indiquer les perspectives, éléments qui masquent/ouvrent une vue, points de repère, alternatives et zones de repos; limiter les angles morts inutiles.
5. Nommer des **sous-espaces distincts** et leurs relations (marché, cour, pignon technique, zone résidentielle, accès service...), avec leur caractère. Les accès doivent servir leurs usages.
6. Proposer les emprises seulement après avoir vérifié la profondeur utile, l'échelle humaine, l'accès des secours/livraisons quand pertinent et les contraintes des bâtiments. Si tout ne tient pas, **remonter l'arbitrage** au lieu de réduire silencieusement les dimensions, largeurs ou nombres imposés.

## Étape 2 — anti-symétrie non dogmatique

La symétrie peut être souhaitée pour une place civique ou un quartier corporatif. **L'irrégularité n'est pas une fin en soi** : elle doit découler de l'histoire, du relief, des accès, de l'usage et de la DA que l'utilisateur a validés.

Si la demande vise un quartier organique / bricolé / dense (comme Neon-Gutter), rejeter l'effet « six tours rangées en 2 × 3 autour d'un rectangle central ». Vérifier particulièrement :

- **Implantation** : diversité justifiée d'orientations, retraits, gabarits, profondeurs, trames et rapports à la rue; ne pas tricher sur les emprises imposées.
- **Tissu et vides** : alternance de passages étroits et élargissements; séquences d'espaces interconnectés; parcelles ou fronts qui se poursuivent à différentes profondeurs; pas de « vide générique » faute de programme.
- **Marché ou place** : implantation liée au flux et aux fonctions, limites nuancées, accès non systématiquement opposés; étals comme occupations, non obstacles à la largeur libre. Forme simple acceptée si **justifiée**, pas seulement par facilité.
- **Réseau** : connexions fonctionnelles, ruelles secondaires et cheminements de secours adaptés aux usages; perspectives parfois brisées, sans multiplier artificiellement les zigzags.
- **Variété de silhouettes** : éviter le copier-coller d'îlots; prévoir les façades et pignons réellement exposés. Les répétitions HLM peuvent être voulues, mais doivent être composées et contextualisées.
- **Lecture TPP** : depuis des positions de caméra plausibles, vérifier l'effet de confinement, le repérage, les séquences de découverte, les seuils et la navigation; ne pas assimiler une vue SVG agréable à une preuve en jeu.

**Ne jamais appliquer un quota fixe d'irrégularité ou imposer des rotations décoratives.** Une composition rationnelle peut être excellente si elle répond au brief; une composition organique doit rester constructible, mesurable et jouable.

## Règle de constructibilité — organicité urbaine ≠ complexité géométrique

**Une ville organique peut être composée majoritairement de bâtiments géométriquement simples.** L'agent doit rechercher la diversité dans le réseau des rues, les orientations, les retraits, les longueurs de façades, la profondeur des parcelles, les variations de hauteur, les cours, les annexes et l'histoire des transformations, **pas en multipliant des polygones à angles arbitraires**.

- **Par défaut** privilégier les rectangles, les formes en L, U, cour ou assemblages lisibles de volumes simples et modulaires. Les bâtiments aux plans très découpés, pointus ou à angles aigus ne sont pas une preuve d'organicité.
- **Exceptions justifiées** : parcelle réellement contrainte, angle de rue particulier, topographie, bâtiment iconique, adaptation historique ou fonction vérifiable. Documenter pour chaque exception la justification, le coût de construction et sa relation aux accès.
- **Audit de faisabilité 3D anticipé** : vérifier surfaces réellement exploitables, trame de façade et ouvertures, accès au rez-de-chaussée, épaisseur du bâtiment, toitures, collisions, modularité Blender/GLB/Godot et réutilisation raisonnable des assets. Ne pas créer 30 architectures uniques lorsque des kits réutilisables répondent à la demande.
- **Ne pas surcorriger** vers une grille symétrique : des bâtiments simples peuvent être décalés, légèrement réorientés si le modèle géométrique le permet, différenciés en hauteur, en retraits et en relations à l'espace public. La forme des parcelles et les espaces intermédiaires peuvent rester irréguliers.
- **Lors d'une révision ciblée** d'un masterplan trop polygonal, conserver autant que possible les voies et la hiérarchie déjà appréciées; proposer les corrections **bâtiment par bâtiment** sans modifier le cadrage approuvé et fournir un comparatif avant/après.
- **Ne pas inventer une métrique universelle** (« au moins 80 % de rectangles », « 5 côtés maximum »). Juger par la crédibilité architecturale et le coût réel de production. Un bâtiment complexe explicitement demandé reste légitime.

Une emprise anormalement complexe **sans cause urbaine démontrable** est un défaut `MAJOR` dans la revue de conception; si elle compromet un accès, la constructibilité ou le contrat géométrique, elle peut devenir `BLOCKER`.

## Étape 3 — faisabilité et représentation

1. Formaliser la morphologie retenue dans le contrat de données canonique. Attention : la V0.1 du schéma ne représente que des **rectangles axis-alignés** pour chaque bâtiment. Pour une emprise complexe, ne pas la remplacer silencieusement par un rectangle approximatif faisant croire que la forme est représentée. Proposer une représentation par éléments identifiés compatibles avec le schéma (et documenter que c'est une approximation) ou demander une évolution de schéma approuvée. Une rotation architecturale réelle requiert un support explicite du modèle et des validateurs avant construction.
2. Les voies complexes peuvent être décrites par ensembles de segments rectangulaires **avec contrôle des largeurs utiles réelles**, y compris aux angles. Ne pas prétendre reproduire une courbe si la représentation ne le permet pas.
3. Vérifier emprises, collisions, voiries, portes, retraits, continuité des parcours, usages et liaisons. Une largeur de ruelle annoncée ne doit pas cacher un rétrécissement au virage.
4. Générer le SVG **du même JSON** et vérifier sa lisibilité : échelle, nord, circulation, fonctions, légende, hauteurs, repères, identifiants, portes/accès quand les données les portent. Si le schéma ne stocke pas certaines de ces données, le signaler au lieu de les dessiner à la main sans source.
5. Afficher ou fournir le **fichier SVG réellement ouvrable** à l'utilisateur, pas seulement une annonce de création ou un chemin Windows non ouvrable pour lui. L'approbation `APPROUVER_CADRAGE` autorise la génération du JSON/SVG, pas la greybox.

## Étape 4 — revue urbanistique indépendante (Design Quality Gate)

Avant toute demande `APPROUVER_MASTERPLAN`, utiliser `templates/masterplan-design-review.md` et produire une revue **distincte** du validateur géométrique :

| Contrôle | Question déterminante |
| --- | --- |
| Morphologie | Le plan répond-il vraiment à la forme / au caractère demandé, plutôt qu'à un schéma générique ? |
| Structure | Les blocs ont-ils des rapports variés et plausibles à la rue ? Si répétitifs, est-ce intentionnel ? |\n| Constructibilité | Les empreintes individuelles restent-elles simples/modulaires sauf justification précise, sans polygones artificiels ni perte d'organicité globale ? |
| Espaces publics | Chaque place, cour et espace libre a-t-il un rôle et un accès lisible ? |
| Navigation TPP | Les séquences et perspectives sont-elles intéressantes sans rendre le parcours confus ou impraticable ? |
| Densité | Les usages et gabarits tiennent-ils sans réduction cachée ? |
| Transition | Boulevard, seuil, cœur, ruelles et bordures forment-ils une hiérarchie ? |
| Cohérence | Les décisions sont-elles reliées à l'histoire locale, la DA et le tissu voisin ? |
| Source canonique | Le JSON peut-il représenter fidèlement le plan, sans décorations SVG contradictoires ? |

Classer chaque constat en `PASS`, `MAJOR`, `BLOCKER`, `NOT_TESTED`. Une symétrie non désirée, un quadrillage générique ou un marché posé au centre sans raison peuvent être `MAJOR` **si contraires au brief**; pas s'ils sont explicitement demandés et cohérents. Corriger avant présentation ou demander un arbitrage si la correction touche aux contraintes approuvées. `BLOCKER` ou `MAJOR` non assumé = ne pas présenter le plan comme prêt à être approuvé.

## Exemple de contre-audit : Neon-Gutter 60 × 80 m

Le cadrage approuvé exige six HLM, boulevard ouest de 14 m, deux accès, ruelles secondaires, place de marché, identité cyberpunk vivante. Le premier plan place les six bâtiments en trois rangées de deux autour d'un marché rectangulaire centré, avec plusieurs axes droits alignés : **c'est géométriquement lisible mais trop rigide pour l'intention organique exprimée**.

Dans la phase de révision :
- préserver les contraintes **approuvées**, les six HLM tant qu'une décision contraire n'est pas obtenue, les gabarits/largeurs minimales et les accès essentiels;
- proposer une implantation hiérarchisée moins systématique (ex. trois ou quatre groupes bâtis plutôt que deux colonnes), des retraits dépendant des usages, une place légèrement désaxée avec accès contrastés et des ruelles réellement motivées; **ce sont des options, pas des modifications pré-approuvées**;
- fournir une justification des vues TPP et des fonctions par sous-espace;
- produire **une V2 JSON + SVG** et un rapport d'écarts (V1 → V2), sans aucune construction 3D avant `APPROUVER_MASTERPLAN`.

## Livrables de phase 1

Le dossier doit comprendre : le JSON canonique et sa version, le SVG ouvert/lien vérifié, la liste des emprises et accès, les vérifications techniques, la revue morphologique, les arbitrages ouverts, et la demande **explicite** d'approbation humaine. Seule une validation humaine autorise la phase 2.

## SVG : outil et orientation

- Utiliser le script de rendu **du projet** (`tools/render_masterplan_svg.py`) quand il existe : celui de ce skill (`scripts/render_masterplan_svg.py`) suit le schéma d'exemple et peut échouer (`KeyError: 'segments'`) sur le schéma 2.0 d'un projet. Ne jamais lancer `git checkout` sur un SVG pour « tester » : il peut contenir du travail non commité.
- Orienter les SVG dans le sens de la **vue de dessus du moteur** (Godot : X vers la droite, +Z vers le bas, flèche du nord en conséquence). Un plan en miroir est pris pour une erreur de la scène.
- Après tout retrait ou ajout d'objet, régénérer le SVG de zone et la carte globale depuis le JSON, et vérifier qu'aucun identifiant retiré n'y figure.
