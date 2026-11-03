# Gates bloquants et preuves

| Gate | Critères avant présentation à l'utilisateur | Critères hors portée du validateur JSON |
| --- | --- | --- |
| Cadrage | Besoin et contraintes explicités, conflits détectés, defaults identifiés comme propositions | Arbitrage artistique et choix humains |
| Masterplan | JSON valide, IDs uniques, emprises dans la zone, emprises bâties dans réservations, pas de collision bâti/voirie, routes définies, raccords plausibles, SVG dérivé du JSON | Réalisme urbanistique, lisibilité du plan |
| Greybox | Contrat approuvé, tailles et coordonnées extraites de la scène Godot réelle, collisions, cheminements TPP, captures | Confort, perception, impossibilité d'un accès bloqué hors des chemins testés |
| DA/Assets | Guide local cohérent, inventaire, statut/provenance/licence vérifiée de chaque nouveau modèle, plan d'habillage | Qualité artistique et capacité de lecture |
| Habillage | Zones verrouillées intactes, circulation réelle, vues comparées, rapport performance/tests | Jugement esthétique humain |
| Gel | Autorisation humaine finale, sauvegarde/trace, registre aligné, état locked | Permissions Git, sécurité ou authenticité cryptographique de l'approbation |

Un contrôle `WARNING` exige explication; un `ERROR` bloque le passage. La réussite du script est insuffisante à elle seule pour déclarer le gate réussi. Les résultats de Godot doivent être testés avec les outils réellement disponibles.

## Matrice de preuve de zone

- références canoniques et version/hachage;
- liste des contrôles et leurs résultats;
- captures réelles et positions caméra pour permettre comparaison;
- statut de l'accord humain + formulation explicite;
- inventaire diff de fichiers et de zones touchées;
- anomalies résiduelles et plan de correction.
