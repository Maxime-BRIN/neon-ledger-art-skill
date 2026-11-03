# Protection des zones déjà validées

## Règle principale

Toute zone au statut `locked` est **non modifiable**, même pour des changements jugés anodins. Toute phase intermédiaire approuvée (cadrage/masterplan/greybox/DA) est gelée pour les aspects validés.

En cas de besoin de raccord : produire une **demande de changement** indiquant exactement les objets/fichiers, la raison, les solutions évitant le changement, les impacts, les captures avant, et la plus petite modification possible. Attendre une autorisation explicite de l'utilisateur, portant sur ces éléments précis. Une approbation générale d'une extension n'autorise pas une modification d'un quartier voisin.

## Procédure

1. Identifier les zones touchées en se basant sur le registre, les chemins de scène et le diff Git.
2. Définir la liste blanche d'IDs d'objets/fichiers autorisés **après** consentement.
3. Avant de modifier, créer un point de retour Git (selon règles projet) et prendre le relevé des fichiers concernés.
4. Appliquer le changement minimal, ne pas reconstruire tout le quartier. Contrôler une deuxième fois les chemins modifiés, déplacements des bâtiments et connexions.
5. Restituer un diff et des tests ciblés; la zone doit être revalidée pour les aspects impactés. En cas de dépassement : arrêter, annuler/revenir à l'état précédent sans écraser un travail tiers.

Les statuts JSON ne sont **pas** une barrière d'accès suffisante. Pour une protection réelle, combiner revue de diff, séparation des scènes/branches, permissions OS lorsque pertinent, Git et contrôles CI. L'agent ne doit jamais enregistrer lui-même une approbation humaine fictive.
