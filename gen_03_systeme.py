#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBOOK 3/5 - Le Système Complet du Trader"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame,
    Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether, PageBreak)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

NOIR=HexColor('#0A0A0A'); OR=HexColor('#C9A84C'); OR_PALE=HexColor('#FBF5E8')
OR_CLAIR=HexColor('#F5E6C8'); GRIS=HexColor('#4A4A4A'); GRIS_BG=HexColor('#F5F5F5')
PAGE_W,PAGE_H=A4; ML=MR=22*mm; MT=18*mm; MB=22*mm; CW=PAGE_W-ML-MR
TITLE="Le Système Complet du Trader"

def S(n,**k):
    d=dict(fontName='Helvetica',fontSize=11,textColor=GRIS,leading=18.5,spaceAfter=8,alignment=TA_JUSTIFY)
    d.update(k); return ParagraphStyle(n,**d)

st={'body':S('b'),'bold':S('bd',fontName='Helvetica-Bold',textColor=NOIR,leading=18),
 'intro':S('i',fontSize=13,leading=22,spaceAfter=10),
 'h2':S('h2',fontName='Helvetica-Bold',fontSize=15,textColor=OR,leading=20,spaceBefore=16,spaceAfter=8),
 'dq':S('dq',fontName='Helvetica-Oblique',fontSize=12,textColor=OR_CLAIR,alignment=TA_CENTER,leading=20),
 'sn':S('sn',fontName='Helvetica-Bold',fontSize=32,textColor=OR,alignment=TA_CENTER,leading=38),
 'sl':S('sl',fontSize=8,textColor=GRIS,alignment=TA_CENTER,leading=12),
 'cb':S('cb',fontName='Helvetica-Bold',fontSize=9,textColor=OR,alignment=TA_CENTER,leading=14),
 'cn':S('cn',fontName='Helvetica-Bold',fontSize=13,textColor=OR_CLAIR,alignment=TA_CENTER,leading=18),
 't1':S('t1',fontName='Helvetica-Bold',fontSize=44,textColor=white,alignment=TA_CENTER,leading=50),
 't2':S('t2',fontName='Helvetica-Bold',fontSize=30,textColor=OR,alignment=TA_CENTER,leading=36),
 'cs':S('cs',fontSize=14,textColor=OR_CLAIR,alignment=TA_CENTER,leading=20),
 'ct':S('ct',fontSize=10,textColor=GRIS,alignment=TA_CENTER,leading=14),
 'cc':S('cc',fontSize=9,textColor=GRIS,alignment=TA_CENTER,leading=12),
 'cp':S('cp',fontName='Helvetica-Bold',fontSize=14,textColor=NOIR,alignment=TA_CENTER,leading=20,spaceAfter=8),
 'cb2':S('cb2',fontSize=10,textColor=GRIS,alignment=TA_CENTER,leading=16,spaceAfter=6),
 'tl':S('tl',fontName='Helvetica-Bold',fontSize=9,textColor=OR,leading=14),
 'tt':S('tt',fontName='Helvetica-Bold',fontSize=11,textColor=NOIR,leading=16),
 'ts':S('ts',fontSize=9,textColor=GRIS,leading=13,spaceAfter=6),
 'hl':S('hl',fontName='Helvetica-Bold',fontSize=9,textColor=OR,leading=14),
 'ht':S('ht',fontName='Helvetica-Bold',fontSize=22,textColor=NOIR,leading=28,spaceAfter=4),
 'hs':S('hs',fontSize=13,textColor=GRIS,leading=20,spaceAfter=12),
 'br':S('br',fontName='Helvetica-Bold',fontSize=14,textColor=OR,alignment=TA_CENTER,leading=20),
 'br2':S('br2',fontSize=10,textColor=GRIS,alignment=TA_CENTER,leading=16),
 'br3':S('br3',fontSize=10,textColor=OR,alignment=TA_CENTER,leading=16),
}

def footer(c,doc):
    c.saveState(); y=MB-8*mm
    c.setStrokeColor(GRIS); c.setLineWidth(0.3)
    c.line(ML,y+5*mm,PAGE_W-MR,y+5*mm)
    c.setFont('Helvetica',8); c.setFillColor(GRIS)
    c.drawString(ML,y,f"{TITLE}  ·  © TRADING ZONE")
    c.drawRightString(PAGE_W-MR,y,f"© TRADING ZONE  ·  {doc.page}"); c.restoreState()

def dq(t):
    tb=Table([[Paragraph(t,st['dq'])]],colWidths=[CW])
    tb.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),NOIR),('TOPPADDING',(0,0),(-1,-1),16),
        ('BOTTOMPADDING',(0,0),(-1,-1),16),('LEFTPADDING',(0,0),(-1,-1),22),('RIGHTPADDING',(0,0),(-1,-1),22)]))
    return KeepTogether([Spacer(1,8),tb,Spacer(1,8)])

def gb(items):
    t=Table([[Paragraph(i,st['body'])] for i in items],colWidths=[CW-32])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),OR_PALE),('BOX',(0,0),(-1,-1),2.5,OR),
        ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),16),('RIGHTPADDING',(0,0),(-1,-1),16)]))
    return KeepTogether([Spacer(1,6),t,Spacer(1,6)])

def grb(items):
    inner=Table([[Paragraph(i,st['body'])] for i in items],colWidths=[CW-24])
    inner.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),GRIS_BG),('TOPPADDING',(0,0),(-1,-1),8),
        ('BOTTOMPADDING',(0,0),(-1,-1),8),('LEFTPADDING',(0,0),(-1,-1),16),('RIGHTPADDING',(0,0),(-1,-1),8)]))
    bar=Table([['']],colWidths=[3.5])
    bar.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),OR),('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
    combo=Table([[bar,inner]],colWidths=[3.5,CW-3.5])
    combo.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
    return KeepTogether([Spacer(1,6),combo,Spacer(1,6)])

def sr(data):
    cw=CW/len(data)
    cells=[[Paragraph(v,st['sn']),Paragraph(l,st['sl'])] for v,l in data]
    t=Table([[Table([c],colWidths=[cw]) for c in cells]],colWidths=[cw]*len(data))
    t.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4)]))
    hr=HRFlowable(width=CW,thickness=1,color=OR,spaceAfter=4)
    return KeepTogether([Spacer(1,6),hr,t,HRFlowable(width=CW,thickness=1,color=OR,spaceBefore=4),Spacer(1,6)])

def ch(lbl,title,sub):
    return KeepTogether([Paragraph(lbl,st['hl']),HRFlowable(width=CW,thickness=1.5,color=OR,spaceAfter=6),
        Paragraph(title,st['ht']),Paragraph(sub,st['hs'])])

def cover():
    rows=[[Paragraph('◆   COLLECTION LE CODE DU TRADER ÉLITE   ◆',st['cb'])],[Spacer(1,12)],
        [Paragraph('EBOOK 3 / 5',st['cn'])],[Spacer(1,20)],
        [Paragraph('LE SYSTÈME',st['t1'])],[Paragraph('Complet du Trader',st['t2'])],[Spacer(1,12)],
        [HRFlowable(width=70*mm,thickness=1.5,color=OR)],[Spacer(1,12)],
        [Paragraph('Comment construire des règles que tu respecteras vraiment',st['cs'])],
        [Paragraph('La méthode pour passer de la connaissance à l\'exécution',st['cs'])],[Spacer(1,20)],
        [Paragraph('PSYCHOLOGIE DU TRADING · ÉDITION FRANÇAISE',st['ct'])],[Spacer(1,12)],
        [Paragraph('© TRADING ZONE — Tous droits réservés',st['cc'])]]
    t=Table(rows,colWidths=[170*mm])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),NOIR),('TOPPADDING',(0,0),(-1,-1),10),
        ('BOTTOMPADDING',(0,0),(-1,-1),10),('LEFTPADDING',(0,0),(-1,-1),20),
        ('RIGHTPADDING',(0,0),(-1,-1),20),('ALIGN',(0,0),(-1,-1),'CENTER')]))
    return [Spacer(1,30*mm),t]

def cpright():
    s=[Spacer(1,40*mm),Paragraph(TITLE,st['cp']),HRFlowable(width=80*mm,thickness=1,color=OR,spaceAfter=16)]
    for l in ['© 2024 TRADING ZONE — Tous droits réservés.',
        "Aucune partie ne peut être reproduite sans autorisation écrite.",'',
        'Auteur : TRADING ZONE — Édition numérique PDF','',
        "Avertissement : Cet ebook est destiné à un usage éducatif uniquement.",
        "Il ne constitue pas un conseil financier.",
        "Le trading comporte des risques importants.",'','www.tradingzone.fr']:
        s.append(Paragraph(l,st['cb2']))
    return s

def toc():
    s=[Spacer(1,10*mm),Paragraph('TABLE DES MATIÈRES',st['h2']),
       HRFlowable(width=CW,thickness=1,color=OR,spaceAfter=12)]
    for lbl,title,sub in [
        ('INTRODUCTION','Le Fossé Fatal','Entre ce que tu sais et ce que tu fais'),
        ('CHAPITRE 1','La Vérité Brutale','Tes règles ne sont pas faites pour être suivies'),
        ('CHAPITRE 2','Les Biais Cognitifs','Les ennemis invisibles de ton système'),
        ('CHAPITRE 3','Spécificité Extrême','Comment rendre tes règles inviolables'),
        ('CHAPITRE 4','La Ritualisation','Transformer les règles en automatismes'),
        ('CHAPITRE 5','Le Journal Inflexible','Mesurer ce qui compte vraiment'),
        ('CONCLUSION','La Vraie Liberté','Construire un système qui te libère'),]:
        s+=[Paragraph(lbl,st['tl']),Paragraph(title,st['tt']),Paragraph(sub,st['ts']),Spacer(1,4)]
    return s

def content():
    P=lambda t:Paragraph(t,st['body'])
    PB=lambda t:Paragraph(t,st['bold'])
    H=lambda t:Paragraph(t,st['h2'])
    PI=lambda t:Paragraph(t,st['intro'])
    s=[]

    # INTRO
    s.append(ch('INTRODUCTION','Le Fossé Fatal','Entre ce que tu sais et ce que tu fais'))
    s.append(PI("Tu connais ce silence. Pas le silence du marché endormi, mais celui qui s'installe en toi. Juste après avoir cliqué. Après avoir fait l'exact opposé de ton plan. Le plan que tu as passé des heures à construire. Chaque niveau, chaque ligne, chaque règle. Écrits noir sur blanc. Immuables. Pourtant, tes doigts ont tremblé. Ta pensée s'est embrouillée. Et maintenant, cette lourdeur. Cette déception envers toi-même. Ce n'est pas une perte d'argent. C'est bien pire. C'est une perte de confiance."))
    s.append(PI("Tu t'es dit que cette fois, ce serait différent. Vraiment différent. Tu as juré. À toi-même, devant l'écran éteint. Plus jamais un revenge trade. Plus jamais de stop loss déplacé. Plus jamais de clôture prématurée d'un gagnant. Tu te sens fort, résolu. Pendant 24 heures. Peut-être 48. Puis le marché s'anime. Et la vieille habitude revient. Comme un fantôme tenace."))
    s.append(sr([('95%','des traders échouent à cause du fossé connaissance-exécution, pas de mauvaises stratégies'),
                 ('5%','seulement comprennent qu\'un système doit contourner les biais, pas les défier'),
                 ('73%','des pertes majeures viennent de la violation d\'une seule règle bien identifiée')]))
    s.append(dq('"Ce n\'est pas un problème de stratégie. C\'est un problème de système. Un système qui ne prend pas en compte le facteur le plus volatile de tous — toi. Ton cerveau. Tes émotions humaines."'))
    s.append(P("Tu as lu tous les livres. Regardé toutes les vidéos. Suivi des formations coûteuses. Tu connais les indicateurs. Les bougies. Les structures de marché. Tu peux réciter les principes de gestion des risques. Un pourcent par trade. Trois trades par jour. Tu sais tout ça. Intellectuellement. Mais ce fossé. Entre ce que tu sais. Et ce que tu fais. Il s'élargit chaque semaine."))
    s.append(P("Imagine un instant. Si tes règles étaient si profondément ancrées. Si elles étaient si naturellement intégrées à ton être. Que les suivre te paraissait plus simple, plus facile, moins coûteux que de les briser. Ce n'est pas une question de discipline brute. Car la discipline seule s'épuise. Elle est comme un muscle. Elle fatigue. Surtout quand elle est en lutte constante contre tes propres pulsions."))

    # CH1
    s.append(ch('CHAPITRE 1','La Vérité Brutale','Tes règles ne sont pas faites pour être suivies'))
    s.append(P("Tu as des règles, n'est-ce pas ? Bien sûr que oui. Tu as noté ton plan quelque part. Tu as défini des points d'entrée, des stops, des objectifs. Des règles de gestion de risque. Et pourtant. Combien de fois as-tu regardé ces règles s'évaporer en direct ? En 17 minutes, parce qu'une bougie s'est montrée plus agressive que prévu. Ou en 45 secondes, juste après avoir cliqué sur 'acheter'."))
    s.append(P("Ce n'est pas ta discipline qui est cassée. C'est la façon dont tes règles sont construites. C'est la première vérité brutale. Tes règles ne sont pas faites pour être suivies par un être humain. Elles sont écrites par la partie rationnelle de ton cerveau. Mais elles sont brisées par la partie la plus primitive. La partie qui réagit à la peur et à l'avidité."))
    s.append(grb(["<b>L'HISTOIRE DE MATEO — LE BIAIS DE SURCONFIANCE</b>",
        "Mateo trade depuis 18 mois. Son bureau est impeccable. Son journal de trading, détaillé. Il s'est juré de ne jamais risquer plus de 0,5% de son capital par trade. Jamais. Une règle claire, presque parfaite sur papier.",
        "Un jeudi matin, il repère une configuration sur le pétrole. Elle semble infaillible. Il entre. Le trade monte. Puis consolide. Et Mateo commence à transpirer. Il ne peut pas laisser passer ça. Il ajoute. Il double. Puis il ajoute encore. En 28 minutes, il risquait 4,2% de son compte.",
        "Pourquoi Mateo, si discipliné en apparence, a-t-il pulvérisé sa règle la plus sacrée ? Ce n'est pas un manque de volonté. C'est le 'biais de surconfiance'. Quelques victoires passées lui ont donné une fausse certitude — une conviction alimentée par la dopamine des gains précédents.",
    ]))
    s.append(H("Ce que les Pros ont Compris"))
    s.append(P("Ce que les traders professionnels ont compris, et que les amateurs ignorent, c'est que les règles doivent anticiper la faiblesse humaine. Pas la défier. Un pro sait qu'il va être tenté de déplacer son stop. Il sait qu'il va être tenté d'ajouter à un perdant. Alors, il ne fait pas que se l'interdire. Il rend l'action physiquement difficile. Ou psychologiquement impossible. C'est la différence fondamentale."))
    s.append(gb(["<b>LA RÈGLE D'OR DES PROS</b>",
        "◆  Les amateurs écrivent des règles pour un robot. Pas pour eux-mêmes.",
        "◆  Ton système complet doit être une armure contre toi-même — conçue sur mesure.",
        "◆  Une règle n'est pas une suggestion. C'est un automatisme.",
        "◆  Les pros utilisent des stops automatiques : taux de respect 3x plus élevé.",
    ]))
    s.append(H("La Fatigue Décisionnelle"))
    s.append(P("Considère la 'fatigue décisionnelle'. Chaque décision que tu prends dans une journée épuise une partie de ta force mentale. Ton travail. Tes choix personnels. Tes interactions sociales. Chaque trade que tu places est une décision. À la fin de la journée, ton réservoir de discipline est vide. Et c'est là que tes belles règles s'effondrent."))
    s.append(grb(["<b>CAMILLE — LA SIMPLICITÉ QUI LIBÈRE</b>",
        "Camille trade le forex. Elle avait un système très sophistiqué. Moyennes mobiles, RSI, stochastiques, niveaux de fibonacci. Tout y était. Elle passait des heures à analyser avant chaque trade. Puis, une fois en position, l'anxiété montait. Elle vérifiait son trade 38 fois par heure.",
        "Après 6 mois de stagnation, elle a jeté son système. Elle a gardé une seule règle d'entrée : attendre une cassure de structure claire sur le graphique 4 heures. Et une seule règle de sortie : un stop fixe de 50 pips.",
        "Son taux de réussite n'a pas explosé. Mais son stress a chuté de 80%. Et ses pertes ont diminué. Pourquoi ? Parce qu'elle a réduit sa 'fatigue décisionnelle'. La simplicité a libéré son esprit.",
    ]))

    # CH2
    s.append(ch('CHAPITRE 2','Les Biais Cognitifs','Les ennemis invisibles de ton système'))
    s.append(P("Pense à l''effet de disposition'. C'est une bête insidieuse. Elle te pousse à vendre tes gagnants trop tôt. Tu prends tes profits rapidement parce que le gain est agréable. Il valide ton intelligence. Mais elle te fait garder tes perdants trop longtemps. Tu refuses de couper une perte. Parce que la douleur d'avoir tort est insupportable."))
    s.append(P("La douleur de perdre est deux fois plus intense que le plaisir de gagner. C'est une réalité psychologique. C'est pourquoi 73% des traders particuliers gardent leurs perdants plus longtemps que leurs gagnants. Même s'ils ont une règle de stop-loss. Ils le déplacent. Ils l'ignorent. Parce qu'ils cherchent à éviter la douleur immédiate."))
    s.append(dq('"L\'aversion aux pertes te frappe deux fois plus fort que la joie de gagner. Un gain de 100 € est moins impactant qu\'une perte de 100 €. C\'est pourquoi tu gardes les trades perdants — c\'est l\'Effet de Disposition à l\'œuvre."'))
    s.append(H("La Mécanisation comme Solution"))
    s.append(P("Comment combattre cet 'effet de disposition' avec des règles ? Par la mécanisation. Si ton trade atteint ton stop-loss, que se passe-t-il ? Si tu dois cliquer pour fermer, tu vas hésiter. Tu vas chercher un prétexte. Et si la plateforme le faisait pour toi, automatiquement ? Le stop-loss n'est pas une ligne dans le sable. C'est un mur de béton."))
    s.append(gb(["<b>BIAIS À CONNAÎTRE ET DÉSAMORCER</b>",
        "◆  Biais de surconfiance : victoires passées → fausse certitude sur le trade actuel",
        "◆  Effet de disposition : couper les gagnants trop tôt, garder les perdants trop longtemps",
        "◆  Sophisme du joueur : croire qu'après des pertes, un gain est 'dû'",
        "◆  Biais de récence : les pertes récentes occultent les statistiques long terme",
        "◆  Fatigue décisionnelle : réservoir de discipline vidé → décisions impulsives",
    ]))
    s.append(H("L'Identité du Trader"))
    s.append(P("Un autre point crucial : ton identité de trader. Qui penses-tu être ? Un trader impulsif ? Un trader qui doute ? Tes actions suivront toujours l'image que tu as de toi-même. Si tu te vois comme quelqu'un qui 'ne peut pas suivre ses règles', alors tu ne les suivras pas. C'est une prophétie auto-réalisatrice."))
    s.append(grb(["<b>YUSUF — UNE PHOTO ET UNE PHRASE</b>",
        "Yusuf a lutté pendant des années avec l'impulsivité. Il se voyait comme un 'chasseur d'opportunités'. Ce qui, en trading, était une catastrophe. Ses 'opportunités' étaient des trades de vengeance. Il perdait 1 200 euros en moyenne par mois.",
        "Un jour, il a affiché une photo de lui-même à son bureau. Avec une seule phrase manuscrite : 'Yusuf est un trader patient. Il attend son setup.' Chaque fois qu'il était tenté d'entrer sur une impulsion, il regardait cette photo. Il se demandait : 'Est-ce que le Yusuf patient ferait ça ?'",
        "En 3 mois, ses pertes ont diminué de 60%. Pas par une nouvelle stratégie. Mais par une nouvelle identité.",
    ]))

    # CH3
    s.append(ch('CHAPITRE 3','Spécificité Extrême','Comment rendre tes règles inviolables'))
    s.append(P("Tes règles doivent être testables. Mesurables. Si tu ne peux pas quantifier si tu as suivi une règle, ce n'est pas une règle. C'est une vague intention. 'Coupe tes pertes rapidement' n'est pas une règle. C'est une intention. Une règle, c'est : 'Si le prix atteint X% de ma taille de position initiale, je ferme 50% de la position, peu importe le setup.' Ça, c'est une instruction. Sans interprétation possible."))
    s.append(grb(["<b>MATEO — DES RÈGLES CHIRURGICALES</b>",
        "Mateo a refait ses règles après avoir brûlé deux petits comptes. Ses anciennes règles : 'Évite le revenge trading.' De bonnes intentions. Mais quand il était à -300 € sur la journée, il se disait : 'Bon, ce n'est pas vraiment du revenge trading, c'est juste une opportunité.'",
        "Il a écrit : 'Si mon compte est en négatif de plus de 1% à 15h00, je ferme la plateforme jusqu'au lendemain. Sans exception. Pas de \"dernière chance\".' Et aussi : 'Je ne prendrai pas plus de 3 trades par session. Même si les 3 premiers sont gagnants.'",
        "Les premières semaines ont été dures. Son corps l'implorait de reprendre un trade. Mais parce que la règle était si spécifique, si binaire, il ne pouvait pas la tordre. Et lentement, une nouvelle identité a commencé à se former.",
    ]))
    s.append(H("Rendre les Règles Inviolables"))
    s.append(P("La deuxième étape est de rendre tes règles inviolables. Pas juste importantes. Inviolables. Imagine que chaque règle est un contrat avec ton futur toi. Le toi qui sera profitable. Le toi qui sera libre. Si tu brises ce contrat, tu trahis non pas la règle, mais la personne que tu veux devenir."))
    s.append(P("C'est là que l'ancrage psychologique entre en jeu. La plupart des traders perçoivent une règle brisée comme une simple 'erreur technique'. Non. C'est une rupture de ton engagement personnel. C'est un acte de sabotage. Et chaque fois que tu le fais, tu renforces l'Impuissance Apprise — tu apprends à ton cerveau que tu ne peux pas faire confiance à toi-même."))
    s.append(grb(["<b>LUCIA — LA CONSÉQUENCE COMPORTEMENTALE</b>",
        "Lucia avait du mal avec les stops-loss. Elle les déplaçait toujours. Sa nouvelle règle : 'Si je déplace mon stop-loss de plus de 5 pips après l'entrée, je ne trade pas pendant 24 heures.' C'était brutal. Pour une trader active, 24 heures sans trading, c'est une punition.",
        "La première fois, la tentation était forte de 'juste oublier' la règle. Mais elle s'est souvenue du sentiment de trahison. Elle a fermé son ordinateur. La douleur du manque à gagner sur une opportunité potentielle était plus forte que la douleur d'une petite perte.",
        "Cette approche utilise le concept de 'punition comportementale' pour recâbler la réponse. Ce n'est pas agréable, mais c'est efficace. Le cerveau apprend : 'Si je fais X, il y a une conséquence Y.' Ce n'est plus une question de volonté. C'est du conditionnement.",
    ]))
    s.append(H("Ancrer chaque Règle dans une Douleur Passée"))
    s.append(P("Chaque règle doit être la cicatrice d'une leçon durement apprise. Ne dis pas : 'Je coupe mes pertes rapidement.' Dis plutôt : 'Je coupe mes pertes à 1% de mon capital maximum par trade parce qu'en mars dernier, j'ai perdu 2 300 € en espérant un retournement qui n'est jamais venu.' Quand tu connectes une règle à la brûlure d'une perte spécifique, le coût de l'ignorer devient palpable. C'est le biais de récence mis à ton service."))

    # CH4
    s.append(ch('CHAPITRE 4','La Ritualisation','Transformer les règles en automatismes'))
    s.append(P("La troisième étape est la Ritualisation. Tes règles ne doivent pas être des exceptions. Elles doivent devenir des rituels. Des actions automatiques. Avant d'entrer dans un trade, as-tu un checklist ? Pas un mental. Un vrai checklist. Sur papier. Avant chaque trade, lis tes 3 règles à voix haute. Juste avant d'appuyer sur le bouton. Ça prend 15 secondes. Mais ces 15 secondes te sortent de l'urgence émotionnelle."))
    s.append(grb(["<b>HARUKI — LE RITUEL DES 15 SECONDES</b>",
        "Haruki, un trader de Tokyo, avait 3 règles cruciales. Une pour la taille de position. Une pour la confirmation de setup. Une pour la gestion du stop. Avant chaque trade, il lisait ces 3 règles à voix haute. Juste avant d'appuyer sur le bouton. Ça prend 15 secondes.",
        "Mais ces 15 secondes le sortaient de l'urgence émotionnelle. Ça activait son cortex préfrontal. Ça ramenait le rationnel au premier plan. C'est le contraste entre l'amateur et le professionnel.",
        "L'amateur se jette dans le trade. Le professionnel ritualise son entrée. Il crée une barrière délibérée entre l'impulsion et l'action. Il transforme la décision émotionnelle en une exécution mécanique. Ce n'est pas de la rigidité. C'est de l'efficacité.",
    ]))
    s.append(H("Externaliser son Engagement"))
    s.append(P("La discipline est difficile à maintenir seul. Partage tes règles avec une personne de confiance. Pas pour qu'elle te juge. Mais pour qu'elle soit le témoin de ton intention. Clara a commencé à envoyer un résumé quotidien de son respect des règles à son frère. Non pas ses profits, juste son score d'adhérence. Le simple fait de savoir que quelqu'un allait lire ses chiffres a transformé sa concentration."))
    s.append(gb(["<b>LES 5 ÉTAPES POUR BÂTIR UN SYSTÈME SOLIDE</b>",
        "◆  Étape 1 — Spécificité Extrême : chaque règle est binaire, pas interprétable",
        "◆  Étape 2 — Règles Inviolables : les lier à une conséquence comportementale",
        "◆  Étape 3 — Ritualisation : checklist lu à voix haute avant chaque trade",
        "◆  Étape 4 — Journal Inflexible : mesurer le respect des règles, pas le profit",
        "◆  Étape 5 — Flexibilité Rigide : réviser les règles une fois par mois, jamais sous stress",
    ]))
    s.append(sr([('57%','win rate de Marcus sur 100 backtests — solide système initial'),
                 ('3x','plus élevé : taux de respect des stops automatiques vs manuels'),
                 ('90%','de respect du plan atteint par Aisha après 2 semaines de ritualisation')]))

    # CH5
    s.append(ch('CHAPITRE 5','Le Journal Inflexible','Mesurer ce qui compte vraiment'))
    s.append(P("Ce n'est pas juste pour suivre tes résultats financiers. C'est pour suivre ton respect des règles. Chaque jour. Chaque trade. Tu dois évaluer non pas 'ai-je gagné ou perdu ?', mais 'ai-je suivi mes règles à 100% ?'. Pour chaque trade, tu dois noter : la règle violée, l'émotion ressentie au moment de la violation, la conséquence financière directe, et la conséquence comportementale appliquée."))
    s.append(grb(["<b>AMARA — LE MIROIR IMPITOYABLE</b>",
        "Amara avait l'habitude de se sentir coupable après un trade mal géré. Une culpabilité vague. Mais quand elle a commencé à journaliser, elle a vu un schéma. Presque toutes ses pertes importantes venaient de la violation de la même règle : 'Ne jamais trader sur un range incertain.'",
        "En six semaines, elle a accumulé 27 violations. Le chiffre l'a choquée. Ce n'était pas 'quelques erreurs'. C'était un comportement récurrent. Ce niveau de spécificité a créé un déclic. Elle a commencé à se concentrer non pas sur gagner de l'argent, mais sur ne pas violer la règle.",
        "La douleur de voir le nombre de violations monter était plus forte que la douleur d'une petite perte. Le journal n'était plus un simple outil. C'était un miroir impitoyable.",
    ]))
    s.append(H("Changer ce que tu Mesures"))
    s.append(P("Arrête de ne mesurer que le profit et la perte. C'est la boucle de dopamine la plus dangereuse. Elle te rend dépendant du résultat aléatoire d'un trade. Mesure ton respect des règles. C'est la seule variable que tu contrôles à 100%. Concentre-toi sur le processus."))
    s.append(grb(["<b>OMAR — 90 JOURS DE PROCESSUS PUR</b>",
        "Omar a passé 90 jours à ne se soucier que de son score de respect des règles. Il visait 85%. Ses profits étaient secondaires. Au bout de 90 jours, non seulement il avait dépassé 90% de respect, mais son compte avait augmenté de 17%. Pour la première fois de sa carrière.",
        "Le marché récompense le processus. Pas la chance.",
    ]))
    s.append(H("La Flexibilité Rigide"))
    s.append(P("La cinquième étape est la Flexibilité Rigide. Ça paraît contradictoire, non ? Mais c'est essentiel. Tes règles ne sont pas gravées dans le marbre pour l'éternité. Le marché évolue. Tu évolues. Tes règles doivent pouvoir s'adapter. Mais cette adaptation doit être intentionnelle. Pas émotionnelle."))
    s.append(grb(["<b>FARAH — LA RÈGLE DES 50 TRADES</b>",
        "Farah était obsédée par la recherche de 'l'indicateur parfait'. Elle passait des heures à tester de nouvelles stratégies. Chaque fois, elle écrivait de nouvelles règles. Puis elle les abandonnait. Elle était prise dans le sophisme du joueur.",
        "Sa règle de flexibilité est devenue : 'Je ne modifierai aucune règle de ma stratégie active avant d'avoir exécuté 50 trades selon ces règles.' Cette règle l'a forcée à donner une chance réelle à son système. À lui faire confiance, même quand ça faisait mal.",
    ]))

    # CONCLUSION
    s.append(ch('CONCLUSION','La Vraie Liberté','Construire un système qui te libère'))
    s.append(P("Le marché est un miroir. Il reflète tes forces et tes faiblesses. Il ne te ment jamais. Quand tu échoues, ce n'est pas le marché qui t'a trahi. C'est toi qui as trahi ton propre système. La bonne nouvelle ? Tu peux changer ça. Dès aujourd'hui. Dès la prochaine session."))
    s.append(P("Le plus grand secret du trading n'est pas un secret caché dans une formule complexe. C'est une vérité simple. Le succès ne vient pas de la découverte du bon système. Le succès vient de ta capacité à devenir le bon trader. Le trader qui respecte son système. Le trader qui se respecte lui-même."))
    s.append(grb(["<b>CHECKLIST DU SYSTÈME COMPLET</b>",
        "✓  Mes règles sont spécifiques, binaires, non interprétables",
        "✓  Chaque règle est liée à une conséquence comportementale précise",
        "✓  J'ai un rituel pré-trade : checklist lu à voix haute",
        "✓  Je tiens un journal de respect des règles, pas seulement de P&L",
        "✓  Je révise mes règles une fois par mois, jamais sous l'emprise d'une émotion",
        "✓  Mes stops sont automatiques — pas manuels",
    ]))
    s.append(gb(["<b>MES ENGAGEMENTS FINAUX</b>",
        "◆  Je construis des règles pour l'être humain imparfait que je suis",
        "◆  Je mesure mon succès par mon respect du plan, pas par mes profits",
        "◆  Je traite chaque violation comme une donnée précieuse, pas un échec",
        "◆  Je construis mon identité de 'trader qui respecte ses règles'",
    ]))
    s.append(dq('"Ce système n\'est pas un carcan. C\'est une libération. C\'est la structure qui te permet de prospérer. Tu as les outils. Tu as la capacité. Il te reste une seule chose à faire. Faire confiance. Non pas au marché. Mais à toi."'))
    s.append(Spacer(1,16))
    s+=[Paragraph('TRADING ZONE',st['br']),Paragraph('Collection Le Code du Trader Élite — Ebook 3/5',st['br2']),Paragraph('www.tradingzone.fr',st['br3'])]
    return s

def build():
    out='03_Systeme_Complet_TRADING_ZONE.pdf'
    frame=Frame(ML,MB,CW,PAGE_H-MT-MB,id='main')
    tpl=PageTemplate(id='main',frames=[frame],onPage=footer)
    doc=BaseDocTemplate(out,pagesize=A4,pageTemplates=[tpl],leftMargin=ML,rightMargin=MR,topMargin=MT,bottomMargin=MB)
    story=cover()+[PageBreak()]+cpright()+[PageBreak()]+toc()+[PageBreak()]+content()
    doc.build(story); print(f"✓ {out} généré")

if __name__=='__main__': build()
