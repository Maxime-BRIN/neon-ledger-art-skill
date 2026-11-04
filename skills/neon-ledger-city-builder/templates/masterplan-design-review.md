# Masterplan — Revue de conception urbaine

**Zone / version :** [ID / Vx]  
**Cadrage approuvé (référence) :** [date + texte / preuve]  
**Modèle canonique :** [JSON path / SHA]  
**SVG dérivé du JSON :** [fichier ouvrable / lien]  
**État :** DRAFT / NEEDS_REVISION / READY_FOR_HUMAN_REVIEW / APPROVED_BY_USER

## 1. Brief et invariants

| Exigence imposée | Données du plan | Respect ? | Justification |
| --- | --- | --- | --- |
| [exigence] | [dimensions / IDs] | PASS/FAIL/UNKNOWN | [preuve] |

## 2. Concept morphologique

- **Pourquoi le quartier a cette forme :** […]
- **Hiérarchie spatiale :** axe principal → seuils → espaces d'activité → ruelles/espaces calmes → sorties
- **Usages et parcelles :** […]
- **Variantes étudiées et compromis :** […]
- **Symétries ou répétitions intentionnelles :** […]
- **Points de vue TPP prévus (hypothèses, pas tests Godot) :** […]

## 3. Design Quality Gate

| Critère | PASS / MAJOR / BLOCKER / NOT_TESTED | Preuve/lieu/raison | Correction proposée |
| --- | --- | --- | --- |
| Morphologie conforme au brief | […] | […] | […] |
| Implantation et retraits justifiés | […] | […] | […] |
| Absence de quadrillage générique non souhaité | […] | […] | […] |
| Marché/cour/espaces libres fonctionnels | […] | […] | […] |
| Séquence de marche TPP et repères | […] | […] | […] |
| Hiérarchie boulevard → seuils → ruelles | […] | […] | […] |
| Densité et gabarits sans réduction implicite | […] | […] | […] |
| Réalisme des accès, livraisons et largeur utile | […] | […] | […] |
| Registre / frontières / raccordements | […] | […] | […] |
| Cohérence JSON/SVG et limites du schéma | […] | […] | […] |

## 4. Revue métrique indépendante

- Commandes réellement exécutées et résultats : […]
- Largeurs utiles aux virages / points de conflit : […]
- Emprises/hauteurs vérifiées : […]
- Contraintes que le validateur ne sait pas vérifier : […]
- **Ce qui reste NOT_TESTED dans Godot :** caméra TPP réelle, collisions, visibilité, scène chargée

## 5. Changements V1 → V2 (si révision)

| ID / zone | Ancien plan | Nouveau plan | Pourquoi | Impact sur contraintes approuvées |
| --- | --- | --- | --- | --- |
| […] | […] | […] | […] | […] |

## 6. Décision

- Erreurs bloquantes : […]
- Défauts majeurs : […]
- Arbitrages soumis à l'utilisateur : […]
- **Validation attendue :** APPROUVER_MASTERPLAN / DEMANDER_CORRECTIONS / REFUSER
- **Aucune greybox autorisée avant une réponse explicite de l'utilisateur.**
