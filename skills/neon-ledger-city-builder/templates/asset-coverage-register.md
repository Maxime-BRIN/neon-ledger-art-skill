# Registre de couverture des assets — [Zone, version, date]

**Périmètre approuvé :** [zone complète ou sous-zone explicitement approuvée]  
**Référence des besoins :** [fichier + hash, IDs]  
**Objectif :** [N/N besoins essentiels, ex. 50/50]  
**Solutions identifiées :** [X/N, preuve]  
**Ressources réellement prêtes :** [Y/N, preuve]  
**Phase 3 :** AUDIT / SOURCING / AWAITING_APPROVAL / ACQUISITION / VALIDATION / READY / BLOCKED

## Inventaire par besoin essentiel (une ligne par ID)

| Need ID | Sous-zone | Critères de FIT | Candidat / provenance | FIT/ADAPT/REJECT/MISSING | Solution identifiée (oui/non) | READY (oui/non + preuve) | Licence / statut import | Action suivante / autorisation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ID] | […] | […] | […] | […] | […] | […] | […] | […] |

## Actions à autoriser

| Lot | Besoins résolus | Action précise (recherche / téléchargement / adaptation / génération / Notion) | Sources, licences, coûts/efforts | Permission demandée |
| --- | --- | --- | --- | --- |
| […] | […] | […] | […] | […] |

## Compteurs anti-confusion

- Besoins essentiels uniques du périmètre : [N]
- Besoins avec solution identifiée : [X]
- Besoins avec ressource READY : [Y]
- Modèles uniques audités : [A]
- Évaluations modèle × besoin : [B]
- Modèles rejetés / placeholders : [détails]
- Besoins essentiels sans solution : [IDs]
- Besoins avec solution mais pas READY : [IDs]
- IDs exclus par **changement de périmètre explicitement approuvé** : [IDs + preuve + backlog] ou aucun

## Validation du gate

- [ ] Tous les IDs essentiels du référentiel présentés, sans suppression cachée
- [ ] 100 % READY (Y=N), avec preuves individuelles
- [ ] Licences/provenances vérifiées, adaptations terminées
- [ ] Imports/tests Godot exécutés et prouvés
- [ ] Périmètre approuvé et autres zones gelées inchangés
- [ ] Demande `APPROUVER_DA_ASSETS` possible **seulement si tout ce qui précède est vrai**

**Si Y < N :** rester en Phase 3 et demander les actions/permissions nécessaires. Ne jamais cocher les preuves non obtenues.
