#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBOOK 2/5 - La Patience du Trader Rentable"""
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
TITLE="La Patience du Trader Rentable"

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

def dq(text):
    t=Table([[Paragraph(text,st['dq'])]],colWidths=[CW])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),NOIR),('TOPPADDING',(0,0),(-1,-1),16),
        ('BOTTOMPADDING',(0,0),(-1,-1),16),('LEFTPADDING',(0,0),(-1,-1),22),('RIGHTPADDING',(0,0),(-1,-1),22)]))
    return KeepTogether([Spacer(1,8),t,Spacer(1,8)])

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
        [Paragraph('EBOOK 2 / 5',st['cn'])],[Spacer(1,20)],
        [Paragraph('LA PATIENCE',st['t1'])],[Paragraph('du Trader Rentable',st['t2'])],[Spacer(1,12)],
        [HRFlowable(width=70*mm,thickness=1.5,color=OR)],[Spacer(1,12)],
        [Paragraph('Attendre le bon setup sans devenir fou',st['cs'])],
        [Paragraph('La méthode des professionnels du trading',st['cs'])],[Spacer(1,20)],
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
        ('INTRODUCTION','Le Piège du Silence','Quand attendre devient insupportable'),
        ('CHAPITRE 1','La Patience Active','Une compétence tactique, pas une vertu passive'),
        ('CHAPITRE 2','Les Biais qui Sabotent','Pourquoi ton cerveau court-circuite ton plan'),
        ('CHAPITRE 3','La Méthode Kofi','Outils concrets pour attendre sans craquer'),
        ('CHAPITRE 4','Le Journal de Non-Trades','Transformer l\'inaction en données précieuses'),
        ('CHAPITRE 5','L\'Identité du Trader Patient','Devenir celui qui choisit de trader'),
        ('CONCLUSION','Le Super-Pouvoir Caché','L\'attente comme avantage compétitif ultime'),]:
        s+=[Paragraph(lbl,st['tl']),Paragraph(title,st['tt']),Paragraph(sub,st['ts']),Spacer(1,4)]
    return s

def content():
    P=lambda t:Paragraph(t,st['body'])
    PB=lambda t:Paragraph(t,st['bold'])
    H=lambda t:Paragraph(t,st['h2'])
    PI=lambda t:Paragraph(t,st['intro'])
    s=[]
    # INTRO
    s.append(ch('INTRODUCTION','Le Piège du Silence','Quand attendre devient insupportable'))
    s.append(PI("Tu t'es déjà senti piégé par le silence ? Ce moment exact. Celui où tes graphiques sont vides. Pas de setup clair. Pas de signal évident. Rien. Et pourtant, à l'intérieur, quelque chose crie. Une voix te pousse. 'Fais quelque chose. Ne reste pas là. Tu vas rater.'"))
    s.append(PI("Cette voix, c'est l'ennemi numéro un de ton compte de trading. Elle t'a déjà coûté combien ? Mille euros ? Cinq mille ? Ou pire, elle a érodé ta confiance, lentement, trade après trade. La plupart des traders appellent ça le manque de discipline. Des termes vagues. Comme un diagnostic qui ne t'aide pas."))
    s.append(sr([('80%','des traders échouent non par mauvaise stratégie, mais faute de savoir gérer l\'attente'),
                 ('73%','des trades pris hors plan sont perdants'),
                 ('1 400€','de pertes mensuelles moyennes dues à la fatigue décisionnelle')]))
    s.append(dq('"La patience, dans le trading, n\'est pas une vertu. C\'est une compétence tactique. Le muscle le plus puissant que tu puisses développer — et malheureusement, celui que personne n\'enseigne vraiment."'))
    s.append(grb(["<b>L'HISTOIRE DE KARIM</b>",
        "Karim a passé 8 mois à affiner sa stratégie sur les paires majeures du Forex. Win rate de 62%. Belle progression. Puis une semaine sans un seul trade validé. Le lundi, le mardi, le mercredi… Rien. Sa stratégie, froide et logique, lui disait d'attendre. Mais son ego lui chuchotait : 'Tu es un trader. Tu dois trader.'",
        "Le jeudi, il a pris un setup forcé. Un double top qui n'en était pas un. 300 euros perdus en 45 minutes. Le vendredi, 500 euros de plus. Et le lundi suivant, le setup parfait est apparu — clairement, évident. Mais Karim avait perdu sa confiance. Il n'a pas appuyé. Il a regardé 180 pips monter sans lui. Gain potentiel : 1 200 euros perdus par manque de patience.",
    ]))
    s.append(P("Ce n'était pas un problème de connaissance technique. Karim connaissait ses règles par cœur. Son problème était ailleurs. Un endroit bien plus profond. C'est l'histoire de 80% des traders qui échouent. Non pas parce qu'ils n'ont pas une bonne stratégie, mais parce qu'ils ne savent pas comment gérer le vide."))
    s.append(P("On te dit 'sois patient'. Mais comment ? Comment faire taire cette urgence qui te ronge quand le marché ne bouge pas ? Comment rester assis, calme, pendant que tes amis postent leurs gains ? Comment ne pas douter quand tu n'as pas pris un seul trade depuis deux jours ? Ce n'est pas de la force mentale brute. C'est une compréhension fine de la psychologie humaine."))
    s.append(P("Le trader rentable ne 'devient' pas patient. Il construit la patience, brique par brique. Il comprend que chaque seconde d'attente est un investissement — dans la qualité de son prochain trade et dans la préservation de son capital mental. Pense à cela : les traders amateurs se concentrent sur le 'meilleur setup'. Les professionnels, eux, se concentrent sur le 'meilleur moment pour ne rien faire'. Un gouffre entre les deux mondes."))

    # CH1
    s.append(ch('CHAPITRE 1','La Patience Active','Une compétence tactique, pas une vertu passive'))
    s.append(P("Beaucoup de traders pensent que la patience est une qualité passive. Qu'il suffit de ne rien faire. C'est une erreur coûteuse. La patience rentable est une action délibérée. C'est une décision consciente de ne pas appuyer sur le bouton. Une force active face à l'impulsion. Le cerveau humain déteste l'incertitude. Il déteste l'inaction. Il préfère une mauvaise décision à l'absence de décision."))
    s.append(P("C'est le piège de la fatigue décisionnelle. Après des heures à analyser, votre esprit est épuisé. Il cherche un soulagement. Souvent, ce soulagement est un trade précipité. Cette sensation coûte en moyenne 1 400 € aux traders particuliers chaque mois — pas des pertes énormes, mais des saignements constants."))
    s.append(grb(["<b>MARCUS — LA PRESSION DU SOIR</b>",
        "Marcus trade depuis dix-huit mois. Il a un emploi dans la logistique. Chaque soir, après avoir couché ses deux enfants, il se met devant ses graphiques. Sa stratégie est claire. Cinq critères précis doivent être remplis pour qu'un trade soit valide. Mais le marché est calme. Pas de setup parfait. Les heures passent.",
        "Il voit un mouvement. Pas parfait. Seulement trois critères sur cinq. Son cœur s'accélère. Il se dit 'c'est assez bon'. Il clique. Le trade tourne mal. Il perd 370 € en vingt-trois minutes. Cette nuit-là, Marcus a regardé le plafond pendant des heures. Il savait. Il savait que ce n'était pas le bon setup. Mais la pression de 'faire quelque chose' était trop forte.",
    ]))
    s.append(H("Amateurs vs Professionnels"))
    s.append(P("Les traders professionnels comprennent cette dynamique. Ils savent que 80% de leurs profits viennent de 20% de leurs trades. Ils ne sont pas constamment sur le marché. Ils attendent leur fenêtre. Le bon setup ne viendra pas quand ils le désirent. Il viendra quand le marché sera prêt à le donner. Les amateurs chassent le marché. Les professionnels attendent sa venue."))
    s.append(gb(["<b>VÉRITÉ FONDAMENTALE</b>",
        "◆  Amateurs : cherchent le 'meilleur setup' parmi 10 000 opportunités/jour",
        "◆  Professionnels : cherchent le 'meilleur moment pour ne rien faire'",
        "◆  La différence n'est pas dans l'analyse technique — elle est dans la gestion du silence.",
    ]))
    s.append(P("La vraie solution n'est pas de combattre l'impatience. C'est de changer ta relation avec l'attente elle-même. Transforme-la d'un fardeau en un avantage stratégique. Tu crois que le temps passé sans trader est du temps perdu ? C'est le temps le plus profitable de ta journée. C'est là que les gains se construisent, sans même avoir pris un trade."))
    s.append(grb(["<b>AISHA — LA CHECKLIST SACRÉE</b>",
        "Aisha, 36 ans, infirmière de nuit, a un compte de 8 000 €. Elle a développé une checklist rigoureuse : sept points à vérifier avant chaque entrée. Un soir, après une garde difficile, elle est épuisée. Elle voit une opportunité sur l'EUR/USD.",
        "Point 1, OK. Point 2, OK. Point 3, Manquant. Point 4, Manquant. Elle s'arrête. Ce n'est pas son setup. Elle ferme la fenêtre de trade. Le lendemain matin, elle voit que le trade aurait été un perdant de 250 €. Ce n'était pas un gain. Mais c'était une perte évitée. Une victoire. Aisha a gagné ce jour-là — non pas en argent, mais en discipline.",
    ]))

    # CH2
    s.append(ch('CHAPITRE 2','Les Biais qui Sabotent','Pourquoi ton cerveau court-circuite ton plan'))
    s.append(P("Notre cerveau n'est pas câblé pour l'attente. Nous sommes programmés pour l'action immédiate. C'est une relique de nos ancêtres chasseurs-cueilleurs. Quand une opportunité se présentait, il fallait agir. Vite. Aujourd'hui, cette pulsion nous pousse à cliquer. À entrer dans un trade. Même si le setup n'est pas parfait. C'est le piège le plus sournois du trading."))
    s.append(dq('"C\'est là que le fossé entre la connaissance et l\'exécution se creuse. La patience, cette qualité si souvent sous-estimée, devient le véritable gold standard du trader rentable."'))
    s.append(H("Le Biais d'Action"))
    s.append(grb(["<b>AMARA — 43 OUVERTURES PAR HEURE</b>",
        "Amara trade le Bitcoin depuis deux ans. Son téléphone vibre chaque minute. Elle sent une anxiété monter si elle ne regarde pas les graphiques. Amara ouvre son application 43 fois par heure. Même pendant les dîners de famille. Elle cherche des motifs qui n'existent pas.",
        "Ce n'est pas de la stratégie. C'est le biais d'action qui prend le dessus. Elle ne veut pas manquer le mouvement. Pourtant, c'est justement dans cette inaction que se cache l'or. Les 5% de traders rentables passent 80% de leur temps à attendre. Les 95% autres passent 80% de leur temps à trader. C'est là que le fossé se creuse.",
    ]))
    s.append(H("La Fatigue Décisionnelle"))
    s.append(P("La discipline est une ressource finie. Chaque décision que vous prenez dans la journée la consomme. Si vous passez des heures à fixer l'écran, à analyser des graphiques qui ne correspondent pas à votre plan, vous épuisez votre capacité à dire 'non' au bon moment. La fatigue décisionnelle vous rend vulnérable. Vous finissez par craquer. Vous prenez ce trade juste pour 'faire quelque chose'."))
    s.append(grb(["<b>DECLAN — LES COMPROMIS FATALS</b>",
        "Declan a une excellente stratégie de 'breakout' sur le Nasdaq. Règles claires : volume au-dessus de la moyenne 20 périodes, prix au-dessus d'une résistance majeure, bougie de clôture forte. Ces setups apparaissent 3 à 4 fois par semaine seulement.",
        "Declan veut trader tous les jours. Au bout de deux jours sans setup, il fait des compromis : 'Le volume est un peu faible, mais la bougie est quand même forte.' Ces petites déviations lui ont coûté 1 700 euros en un mois — non sur de mauvais trades, mais sur des trades qui n'auraient jamais dû être pris.",
    ]))
    s.append(H("Les Boucles de Dopamine"))
    s.append(P("Les boucles de dopamine s'activent à chaque trade. Gagnant ou perdant. L'excitation est une drogue puissante. Elle vous pousse à chercher la prochaine dose. Le prochain trade. Même si ce trade est objectivement mauvais. C'est le sophisme du joueur en pleine action. 'J'ai perdu trois fois, la prochaine doit être un gagnant.' Ces pensées nous forcent la main. Elles nous poussent à des trades que nous regrettons 30 minutes plus tard."))
    s.append(grb(["<b>INGRID — LA RAGE DE RATER</b>",
        "Ingrid a raté un mouvement de 12% sur l'Ethereum. Son setup n'était pas validé à 100%. Elle a regardé le mouvement avec rage et s'est jurée de ne plus jamais rater une telle opportunité.",
        "Le lendemain, elle a forcé un trade sur Solana qui ne respectait aucun de ses critères. Elle a perdu 850 euros en 30 minutes. Le prix de son impatience.",
        "Depuis, Ingrid a mis en place un système de points : trade non-pris qui aurait gagné = +1 point. Trade pris hors setup perdant = -2 points. Trade pris hors setup gagnant = -5 points. Les gains accidentels sont les plus dangereux — ils renforcent une mauvaise habitude.",
    ]))

    # CH3
    s.append(ch('CHAPITRE 3','La Méthode Kofi','Outils concrets pour attendre sans craquer'))
    s.append(P("Comment éviter de devenir fou en attendant ? La réponse est contre-intuitive. Ne fixez pas le marché. Kofi, un trader expérimenté, a une méthode radicale qui a transformé ses résultats."))
    s.append(grb(["<b>LA MÉTHODE KOFI — 30 MINUTES ET C'EST TOUT</b>",
        "Kofi passe 30 minutes chaque matin à identifier ses niveaux clés. Zones de support. Résistances. Niveaux de Fibonacci. Il marque les zones où son setup pourrait apparaître. Ensuite, il ferme sa plateforme. Il n'y revient qu'une fois par heure pour vérifier si le prix est dans une de ces zones.",
        "Si le prix n'est pas là, il ne fait rien. Il lit un livre. Il va marcher. Il travaille sur son autre activité. Kofi ne se sent plus obligé de 'faire quelque chose' juste parce qu'il est devant son écran. Il a appris que la patience est une forme d'action. La plus rentable.",
    ]))
    s.append(H("Le Pré-Mortem du Matin"))
    s.append(P("Chaque matin, avant d'ouvrir votre plateforme, regardez les graphiques de la veille. Identifiez les zones clés. Puis, définissez un ou deux setups précis que vous seriez prêt à prendre AUJOURD'HUI. Avec des points d'entrée, de stop loss et d'objectif clairs et mesurables. Écrivez-les sur un post-it. Votre travail pour la journée devient simple : vous êtes un exécutant, pas un analyste en temps réel."))
    s.append(gb(["<b>PROCESSUS DU PRÉ-MORTEM</b>",
        "◆  Étape 1 : Analyser les graphiques de la veille (30 minutes max)",
        "◆  Étape 2 : Identifier 1 à 2 setups précis pour la journée",
        "◆  Étape 3 : Écrire les critères exacts d'entrée, stop, objectif",
        "◆  Étape 4 : Si le setup se présente → exécuter. Sinon → ne rien faire.",
        "◆  Règle d'or : Pas d'improvisation. Pas de 'je pense que ça pourrait marcher'.",
    ]))
    s.append(grb(["<b>MALIK — DE 40 TRADES À 7 PAR SEMAINE</b>",
        "Malik travaillait 8 heures par jour comme développeur, puis rentrait pour trader la nuit. Il était épuisé. Il prenait des dizaines de trades par session, des crypto, du forex. Il a perdu 7 800 euros en 11 mois.",
        "Il a adopté le Pré-Mortem. Chaque soir, il passait 30 minutes à analyser et définissait UN setup pour le lendemain. Un seul. S'il ne se présentait pas, il allait se coucher sans trader. Les premières semaines furent difficiles.",
        "Au bout de trois mois : trades réduits de 40/semaine à 7. Taux de réussite : de 35% à 62%. Son compte a commencé à croître. Son secret ? Il ne tradait pas plus intelligemment. Il tradait beaucoup moins. Et beaucoup mieux.",
    ]))
    s.append(H("La Règle des Alertes"))
    s.append(P("Pose des alertes à tes niveaux d'entrée clés. Puis éloigne-toi de l'écran. Va vivre ta vie. Quand l'alerte se déclenche, tu reviens avec un regard frais. Tu n'as pas absorbé 4 heures de bruit émotionnel du marché. Tu peux évaluer calmement si l'entrée est toujours valide. Cette technique réduit la 'Fatigue Décisionnelle' et préserve ta discipline pour les moments qui comptent vraiment."))
    s.append(P("Paul Tudor Jones disait qu'il cherchait à minimiser son exposition aux marchés. Il ne trade pas constamment. Il attend les opportunités à forte probabilité. Il sait que le bon setup ne viendra pas quand il le désire — il viendra quand le marché sera prêt. C'est la distinction cruciale entre un chasseur et un pêcheur patient."))

    # CH4
    s.append(ch('CHAPITRE 4','Le Journal de Non-Trades','Transformer l\'inaction en données précieuses'))
    s.append(P("C'est aussi important qu'un journal de trades. Chaque fois que vous identifiez un setup qui ressemble à un bon setup — mais qui ne respecte pas toutes vos règles — écrivez-le. Notez les raisons pour lesquelles vous l'avez laissé passer. Et suivez ce trade virtuellement. Voyez ce qui se serait passé si vous l'aviez pris."))
    s.append(P("Vous découvrirez une vérité étonnante. La plupart de ces 'opportunités manquées' auraient été des perdants. Ou des trades à faible potentiel qui auraient immobilisé votre capital. Ce journal transforme une décision émotionnelle en une donnée factuelle. Et les données ne mentent jamais."))
    s.append(gb(["<b>CE QUE RÉVÈLE LE JOURNAL DE NON-TRADES</b>",
        "◆  La preuve chiffrée que votre patience a une valeur financière réelle",
        "◆  Les patterns de vos impulsions (heure, actif, état émotionnel)",
        "◆  Le coût exact de vos 'presque-setups' évités, en euros non perdus",
        "◆  La transformation de chaque 'non' en donnée quantifiable et motivante",
    ]))
    s.append(sr([('62%','win rate après journal de non-trades vs 35% avant'),
                 ('30j','d\'engagement à 100% de conformité pour reprogrammer les habitudes'),
                 ('85%','score de conformité cible pour valider un mois de trading discipliné')]))
    s.append(grb(["<b>MATEO — LA RÈGLE DES DEUX TRADES</b>",
        "Pendant deux ans, Mateo a lutté avec toutes les erreurs : revenge trading, stop-loss déplacés, sur-dimensionnements. Il a perdu 40% de son compte en six mois. Un soir, après avoir perdu 800 €, il a mis en place une règle simple : pas plus de deux trades par jour.",
        "Les premières semaines, il n'a pris qu'un ou zéro trade certains jours. Ce fut une lutte. Mais lentement, son esprit s'est apaisé. Il a arrêté de se sentir obligé. Il a commencé à voir le marché différemment — non pas comme une source d'argent à saisir, mais comme un partenaire avec qui danser, à son rythme.",
        "Cette transformation n'est pas magique. Elle est le résultat d'un travail acharné sur soi. La patience n'est pas innée. Elle est forgée dans la discipline.",
    ]))
    s.append(dq('"Chaque \'non\' à un setup médiocre est un \'oui\' à un futur plus clair. Un \'oui\' à un compte plus solide. Un \'oui\' à une paix intérieure que l\'argent seul ne peut acheter."'))
    s.append(P("Ne mesurez pas votre succès uniquement par les profits réalisés. Mesurez-le par le respect de votre plan. Par la qualité de vos décisions. La patience en est une — et c'est souvent la plus difficile à prendre. Pendant un mois entier, engagez-vous à ne prendre que des setups qui respectent 100% de vos règles. Pas 90%. Pas 95%. Cent pour cent."))

    # CH5
    s.append(ch('CHAPITRE 5',"L'Identité du Trader Patient",'Devenir celui qui choisit de trader'))
    s.append(P("L'identité du trader est en jeu ici. Êtes-vous un trader qui a besoin d'être constamment actif ? Ou un trader qui gagne de l'argent ? Ces deux identités sont souvent en conflit profond. La plupart des traders débutants associent 'être un trader' à 'prendre beaucoup de trades'. C'est une prophétie auto-réalisatrice destructrice."))
    s.append(P("Les traders professionnels se définissent par leur processus. Pas par leur activité. Ils voient le 'no trade' comme une décision de haute qualité. Comme une preuve de maîtrise. Chaque fois que vous refusez un setup imparfait, vous renforcez cette identité. Vous devenez le trader qui attend. Le trader qui gagne en attendant. Ce n'est pas passif. C'est une action délibérée."))
    s.append(H("La Patience comme Muscle"))
    s.append(P("La patience est une compétence qui se développe. Comme un muscle. Chaque fois que vous résistez à un trade non conforme, vous le renforcez. Cela commence par des petits gestes. Fermer votre écran pour quinze minutes quand vous sentez l'impatience monter. Rester à l'écart du marché les lundis matin si c'est là que vous faites vos pires erreurs. Réduire votre nombre de trades par jour à un maximum de trois. Ces actions construisent une nouvelle identité."))
    s.append(gb(["<b>EXERCICE — 30 JOURS DE PATIENCE ACTIVE</b>",
        "◆  Jours 1-7 : Identifiez vos critères d'entrée non-négociables (max 3)",
        "◆  Jours 8-14 : Journalisez TOUS les trades non-pris et leur résultat virtuel",
        "◆  Jours 15-21 : Appliquez le Pré-Mortem chaque matin (30 minutes max)",
        "◆  Jours 22-30 : Mesurez votre succès par votre % de respect du plan uniquement",
        "◆  Seuil de réussite : Score de conformité > 85% = mois réussi",
    ]))
    s.append(H("La Solitude de la Décision"))
    s.append(P("Personne ne vous tapera sur l'épaule pour vous féliciter d'avoir évité un mauvais trade. Personne ne verra la victoire silencieuse d'avoir fermé votre graphique plutôt que de cliquer sur un setup bancal. Mais vous le saurez. Et cette connaissance intérieure est la plus précieuse. C'est la fondation de la confiance en soi."))
    s.append(P("La confiance qui vous permet, le jour J, d'appuyer sur le bouton quand votre setup parfait se présente. Sans hésiter. C'est le pouvoir de dire non à cent opportunités. Pour dire oui à la seule qui compte. Cela s'apprend. Cela se développe. Ce n'est pas un don. C'est une compétence. La plus difficile. Et la plus gratifiante."))
    s.append(dq('"Jesse Livermore : L\'argent ne s\'est jamais fait en pensant. Il s\'est fait en attendant."'))
    s.append(P("Votre capacité à attendre est votre avantage le plus injuste. C'est votre super-pouvoir caché. Utilisez-le. Protégez-le. Cultivez-le avec la diligence d'un jardinier. Chaque fois que vous résistez à un trade médiocre, vous investissez dans votre succès à long terme. Ce n'est pas une quête pour l'argent. C'est une quête pour la maîtrise de soi. Et quand vous maîtrisez cela, les profits suivent naturellement. Ils ne sont qu'un sous-produit."))

    # CONCLUSION
    s.append(ch('CONCLUSION','Le Super-Pouvoir Caché','L\'attente comme avantage compétitif ultime'))
    s.append(P("Imaginez un sprinteur. Il ne court pas à chaque seconde de la journée. Il passe des heures à s'entraîner. À se reposer. À se préparer. Il conserve son énergie pour le moment précis où le coup de pistolet retentit. Dans le trading, le marché lance des milliers de 'coups de pistolet' chaque jour. La plupart sont des faux départs. Des distractions. Des pièges. Le maître sait quand ignorer le bruit."))
    s.append(P("La prochaine fois que vous êtes devant votre écran. Que vous sentez la pression monter. Que l'ennui vous guette. Que la peur de rater vous serre la gorge. Rappelez-vous : le marché sera toujours là demain. Les bonnes opportunités aussi. Votre capital, lui, est bien plus précieux. Protégez-le avec l'arme la plus puissante du trader — la patience."))
    s.append(grb(["<b>CHECKLIST DU TRADER PATIENT</b>",
        "✓  J'applique le Pré-Mortem chaque matin avant d'ouvrir ma plateforme",
        "✓  Je tiens un journal de non-trades avec les résultats virtuels",
        "✓  Je ne prends que des setups respectant 100% de mes critères",
        "✓  Je pose des alertes et m'éloigne de l'écran entre les sessions",
        "✓  Je ferme ma plateforme après 2 trades perdants consécutifs",
        "✓  Je mesure mon succès par mon % de conformité, pas par mon P&L",
    ]))
    s.append(gb(["<b>MES ENGAGEMENTS FINAUX</b>",
        "◆  Je définis mes setups la veille, jamais sous l'adrénaline du marché",
        "◆  Je traite chaque 'non-trade' comme une victoire de discipline",
        "◆  Je construis l'identité d'un trader patient, pas d'un trader actif",
        "◆  Je comprends que l'inaction bien choisie est souvent ma meilleure décision",
    ]))
    s.append(Spacer(1,16))
    s+=[Paragraph('TRADING ZONE',st['br']),Paragraph('Collection Le Code du Trader Élite — Ebook 2/5',st['br2']),Paragraph('www.tradingzone.fr',st['br3'])]
    return s

def build():
    out='02_Patience_TRADING_ZONE.pdf'
    frame=Frame(ML,MB,CW,PAGE_H-MT-MB,id='main')
    tpl=PageTemplate(id='main',frames=[frame],onPage=footer)
    doc=BaseDocTemplate(out,pagesize=A4,pageTemplates=[tpl],leftMargin=ML,rightMargin=MR,topMargin=MT,bottomMargin=MB)
    story=cover()+[PageBreak()]+cpright()+[PageBreak()]+toc()+[PageBreak()]+content()
    doc.build(story); print(f"✓ {out} généré")

if __name__=='__main__': build()
