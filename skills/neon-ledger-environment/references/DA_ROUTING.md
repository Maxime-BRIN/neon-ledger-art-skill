# Routage de direction artistique et concepts de base — V1.3

## Principe de sécurité créative

Ne jamais déduire une direction artistique du nom du Skill lui-même. La **racine du projet effectivement ciblé** (chemin, manifeste, documents et décisions), le prompt et les références approuvées gouvernent le rendu. À chaque nouveau projet, réévaluer les sources; ne pas recycler par inertie les goûts d'un projet antérieur.

## Algorithme obligatoire

1. **Identifier le projet réellement ouvert** à partir de ses documents ou du chemin de dépôt. Inscrire `project_identity = NEON_LEDGER | OTHER | UNKNOWN`. Si incertain, demander confirmation avant les concepts.
2. **Identifier la DA effective** : prompt explicite et références artistiques approuvées de l'utilisateur; bible et DA de zone si Neon Ledger confirmé; directives de projet externes si autre projet. Inscrire `da_source` et `da_status = KNOWN | MISSING | CONFLICT`. En cas de conflit, demander arbitrage ciblé.
3. **Neon Ledger confirmé** : privilégier la DA locale approuvée et ses références. À défaut de concept pertinent, pour un nouvel asset à créer (voie CRÉER autorisée) et si générateur d'images réellement disponible, **générer un concept de base** exprimant l'identité cyberpunk urbaine du projet, avec richesse technologique, superposition historique, contraste social et scène habitée **lorsque c'est cohérent avec la zone et l'objet**. Le niveau de détails recherché peut évoquer les environnements de *Cyberpunk 2077*, **sans copier ses assets, logos, typographies distinctives, scènes ou franchises**. Les matériaux, couleurs et degrés d'usure ne sont pas universels; conserver les caractéristiques spécifiques d'une zone riche, corporative, résidentielle ou pauvre.
4. **Autre projet + DA explicite** : suivre exclusivement cette DA, sans bible Neon Ledger ni palette cyberpunk par défaut. Si l'utilisateur a donné une image pertinente approuvée, la privilégier; sinon produire un concept de base au démarrage de la voie CRÉER autorisée si imagegen disponible.
5. **Autre projet + aucune DA** : **STOP, poser une question précise sur la DA** avant images, sourcings artistiques conclusifs ou modélisation. Ne pas proposer automatiquement un cyberpunk, réaliste, cartoon, fantasy, etc. Exemple : « Quelle direction artistique veux-tu pour ce projet (style, références ou image) ? ». Toute réponse créative non approuvée reste proposition, pas canon.
6. **Pas d'outil de génération d'image** : ne jamais prétendre avoir créé une image. Si DA connue, produire une spécification textuelle documentée et demander validation; si DA absente, demander la DA d'abord.
7. **Une référence approuvée prévaut** : le générateur ne doit pas émettre une nouvelle image simplement parce que le Skill est invoqué. Une image doit être créée lorsqu'un nouvel asset original nécessite un concept et qu'aucune référence d'asset pertinente approuvée n'existe, ou sur demande explicite. Une référence d'ambiance générale ne remplace pas automatiquement la vue d'asset, mais contraint la génération.
8. **Validation humaine** : tout concept généré est `PROPOSED` jusqu'à validation; aucun passage implicite vers Blender.

## Cas de contrôle

| Cas | Action attendue |
| --- | --- |
| `neon-ledger`, nouvel immeuble sans concept validé, génération disponible | Générer une image de base cyberpunk propre à la zone; demander approbation |
| `neon-ledger`, façade B18 avec deux images cyberpunk déjà approuvées | Réutiliser les références approuvées; pas de génération concurrente automatique |
| `neon-ledger`, tour corporative avec DA sobre approuvée | Respecter la DA corporative, pas d'usure ou néons par défaut |
| Projet fantasy externe, brief fantasy précis | Générer une image de base fantasy correspondant au brief (si création validée + outil disponible) |
| Projet externe sans DA | Demander DA; **aucune image générée** |
| Projet non identifié | Demander quel projet est visé |
| Génération d'images indisponible | Dire indisponible, référence textuelle seulement si DA connue |

## Sortie de cadrage

Avant création d'image ou modélisation, consigner brièvement :
- projet identifié et preuve;
- source de DA et version / approbation;
- images pertinentes existantes et statut;
- voie sourcing `REUSE / ADAPT / CREATE`;
- outil image réellement disponible ou non;
- décision `GENERATE / REUSE_REFERENCE / ASK_DA / TEXT_ONLY`;
- action requérant accord humain.

Ne pas créer un catalogue d'images superflues, ni convertir une ambition artistique en garantie de performance, réalisme ou qualité finale.
