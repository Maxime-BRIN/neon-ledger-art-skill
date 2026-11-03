# Extension urbaine contrôlée

- Déterminer si la demande agrandit un district existant ou crée un district nouveau. Ne pas transformer systématiquement toute nouvelle cellule en district.
- Réserver un ID nouveau et unique et un nom descriptif. Avant de numéroter, inspecter `city_master_index.json` et l'historique des IDs, y compris archivés.
- Analyser limites physiques et visuelles, dénivelés, bâtiments adjacents, connexions routières et piétonnes, styles, services techniques et skyline.
- Le raccord doit avoir des positions mondiales identiques (ou des segments de franchissement compatibles) et des largeurs utiles adaptées. Le validateur détecte certains décalages, mais pas les obstacles 3D.
- Définir une transition architecturale/logistique **justifiée**. Éviter la répétition d'un même vocabulaire partout; une transition peut être volontairement abrupte si le monde et la demande le justifient.
- Préparer deux variantes si un compromis majeur est nécessaire; proposer une solution localisée qui n'altère pas les zones approuvées.
- **Ne pas modifier l'ancienne zone** pour faire correspondre la nouvelle. En cas d'impossibilité, arrêter et produire une demande de dérogation selon `PROTECTION.md`.
- Relancer le workflow masterplan → greybox → DA → habillage sur la seule extension, avec jalons humains.
