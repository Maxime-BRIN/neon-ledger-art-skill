# Extension urbaine contrôlée

- Déterminer si la demande agrandit un district existant ou crée un district nouveau. Ne pas transformer systématiquement toute nouvelle cellule en district.
- Réserver un ID nouveau et unique et un nom descriptif. Avant de numéroter, inspecter `city_master_index.json` et l'historique des IDs, y compris archivés.
- Analyser limites physiques et visuelles, dénivelés, bâtiments adjacents, connexions routières et piétonnes, styles, services techniques et skyline.
- Le raccord doit avoir des positions mondiales identiques (ou des segments de franchissement compatibles) et des largeurs utiles adaptées. Le validateur détecte certains décalages, mais pas les obstacles 3D.
- Définir une transition architecturale/logistique **justifiée**. Éviter la répétition d'un même vocabulaire partout; une transition peut être volontairement abrupte si le monde et la demande le justifient.
- Préparer deux variantes si un compromis majeur est nécessaire; proposer une solution localisée qui n'altère pas les zones approuvées.
- **Ne pas modifier l'ancienne zone** pour faire correspondre la nouvelle. En cas d'impossibilité, arrêter et produire une demande de dérogation selon `PROTECTION.md`.
- Relancer le workflow masterplan → greybox → DA → habillage sur la seule extension, avec jalons humains.

## Intégration à l'existant : inventaire et contrôles obligatoires (retour du 2026-11-10)

Origine : un quartier v3 dense et organique posé au nord de la Rue de la Dernière-Relance « n'avait aucun sens » avec elle. Il était 3 fois plus large que la rue, orienté en biais sans rapport avec elle, avec des tours corpo de 37 à 90 m face à des immeubles de 7 à 13 m. Il touchait la rue par un seul raccord, et les décors de fond restaient en place alors qu'ils ne cachaient plus rien. La composition doit **partir de l'existant**, pas lui être juxtaposée.

**Avant toute esquisse**, lire la source de vérité du projet (ex. `world/layout.gd`, `world/street.gd`, `world/collision.gd`) et produire un **inventaire de l'existant** chiffré :

- rues : axe, orientation, largeurs (chaussée, trottoirs), cotes, extrémités ;
- bâtiments : emprise, profondeur, hauteur, l'arrière de chaque façade (ce qui est derrière doit exister) ;
- ruelles, passerelles, escaliers, places : où elles mènent aujourd'hui, ce qui doit les prolonger ;
- ouvrages traversants (viaduc, piles), et leurs dégagements ;
- **décors de fond / façades plates** : quelle vue ils ferment, et ce qu'ils deviennent si la vue s'ouvre ;
- lignes de vue joueur depuis la caméra réelle : ce qu'on voit au bout et au-dessus de la rue.

**Règles de composition**

1. **Continuité des tracés** : les nouvelles voies prolongent ou recoupent les tracés existants (même axe, ou angle justifié au point de rencontre). Une ruelle existante en impasse vers la zone est prolongée ou reçoit une fin justifiée. Le nouveau tissu est d'abord **orthogonal ou parallèle** à la rue existante sur sa frange ; les biais ne viennent qu'au-delà, et chaque changement d'orientation doit avoir un motif (relief, ancien tracé, place).
2. **Frange de transition** : sur une profondeur d'au moins un îlot, l'échelle et les gabarits de l'existant sont repris (largeur de parcelle, hauteur à ±1 niveau, profondeur). Les dos des bâtiments existants sont adossés à un bâti ou à une cour réelle, jamais à un vide résiduel. Les grands gabarits (corpo, tours) restent au loin et sont justifiés par la skyline vue depuis la rue.
3. **Échelle relative** : la nouvelle zone se dimensionne d'après l'existant (rapport de surfaces, nombre de rues à traverser), pas d'après un rectangle libre. Donner le rapport et le justifier. Une zone beaucoup plus grande se découpe en extensions successives.
4. **Plusieurs raccords** : au moins autant d'accès que la rue existante offre de débouchés vers la zone (placette, ruelle, escaliers, passerelle), chacun à cotes identiques.
5. **Décors devenus caducs** : tout décor de fond qui fermait une vue désormais ouverte est listé, avec une décision proposée (retirer, remplacer par du bâti réel, garder pour une vue qui reste fermée). Ne jamais le modifier sans autorisation (zone protégée).
6. **Ouvrages traversants** : piles et emprises du viaduc gardent leur dégagement ; le bâti s'y rapporte (dessous, en appui, ou à distance), jamais à cheval sur une pile.

**Contrôles avant présentation** (dans le SVG de contexte et dans le tableau de revue) :

| Contrôle | Attendu |
| --- | --- |
| Tracés prolongés | chaque débouché existant vers la zone → raccord ou fin justifiée |
| Orientation de frange | bâti de la première bande ∥ ou ⟂ à la rue existante, à ±5° |
| Gabarits de frange | hauteur ≤ hauteur existante voisine + 1 niveau |
| Dos des bâtiments existants | adossé à du bâti ou à une cour nommée |
| Décors de fond | chacun listé avec une décision proposée |
| Échelle | rapport surface nouvelle / existante affiché et justifié |
| Raccords | nombre ≥ nombre de débouchés, cotes identiques |
