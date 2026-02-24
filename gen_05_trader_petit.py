#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBOOK 5/5 - Trader Petit pour Gagner Grand"""
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
TITLE="Trader Petit pour Gagner Grand"

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
        [Paragraph('EBOOK 5 / 5',st['cn'])],[Spacer(1,20)],
        [Paragraph('TRADER PETIT',st['t1'])],[Paragraph('pour Gagner Grand',st['t2'])],[Spacer(1,12)],
        [HRFlowable(width=70*mm,thickness=1.5,color=OR)],[Spacer(1,12)],
        [Paragraph('La psychologie et la méthode pour faire croître',st['cs'])],
        [Paragraph('un petit capital avec discipline et précision',st['cs'])],[Spacer(1,20)],
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
        ('INTRODUCTION','Le Poids de 700 Euros','Quand chaque euro compte double'),
        ('CHAPITRE 1','La Psychologie du Petit Compte','Comprendre pourquoi ça brûle si vite'),
        ('CHAPITRE 2','La Règle du 1%','Risquer 5€ pour construire tout le reste'),
        ('CHAPITRE 3','Le Cadre des 3 Règles','Le système concret pour un petit capital'),
        ('CHAPITRE 4','La Transformation Aisha','Du compte qui stagne au comportement rentable'),
        ('CHAPITRE 5','La Compétence Transférable','Prouver à 500€ ce qui sera vrai à 50 000€'),
        ('CONCLUSION','Le Vrai Gain','La maîtrise de soi comme premier profit'),]:
        s+=[Paragraph(lbl,st['tl']),Paragraph(title,st['tt']),Paragraph(sub,st['ts']),Spacer(1,4)]
    return s

def content():
    P=lambda t:Paragraph(t,st['body'])
    PB=lambda t:Paragraph(t,st['bold'])
    H=lambda t:Paragraph(t,st['h2'])
    PI=lambda t:Paragraph(t,st['intro'])
    s=[]

    # INTRO
    s.append(ch('INTRODUCTION','Le Poids de 700 Euros','Quand chaque euro compte double'))
    s.append(PI("Tu as ouvert ton compte de trading avec 700 euros. Tu sens une pression énorme. Chaque trade est un test. Pas seulement du marché. Mais de toi-même. De ta capacité à transformer ce petit capital. Tu rêves de milliers d'euros. De liberté financière. Et tu as déjà essayé de prendre un trade trop gros. Tu as déjà laissé courir une perte bien au-delà de ton stop."))
    s.append(PI("92% des traders particuliers qui démarrent avec moins de 1 000 euros brûlent leur compte en moins de six mois. Ce n'est pas un secret. C'est une statistique brutale. Une réalité que tu connais peut-être déjà. Mais voici ce que la plupart ne comprennent pas. Ce n'est pas la taille de ton capital qui est le problème. C'est ta psychologie."))
    s.append(sr([('92%','des traders avec moins de 1 000€ brûlent leur compte en moins de 6 mois'),
                 ('95%','des traders particuliers n\'atteignent pas la rentabilité durable'),
                 ('2x','plus intense : la douleur d\'une perte de 2% sur 500€ vs 50 000€')]))
    s.append(dq('"La taille de ton capital est moins importante que la taille de ton engagement envers ton processus. Et ta capacité à penser comme un professionnel — même avec 500 euros."'))
    s.append(grb(["<b>L'HISTOIRE D'AISHA — 650 EUROS ET UN RÊVE</b>",
        "Aisha a commencé avec 650 euros. Son objectif était simple : 50 euros par jour. Un gain modeste. Mais elle n'y est jamais parvenue. Le lundi, elle gagnait 30 euros. Une petite victoire. Mais son biais de récence prenait le dessus. Elle se sentait invincible.",
        "Le mardi matin, elle voyait une configuration 'parfaite' sur l'EUR/USD. Son plan disait 1% de risque. Soit 6,50 euros. Elle a cliqué sur 5% de risque — 32,50 euros. Cinq fois trop. Ce trade a commencé à monter. Plus 20 euros. Plus 35 euros. Mais la peur l'a envahie. Elle a fermé. Plus 38 euros. Puis la frustration est montée : le trade a continué à son objectif. 70 euros. Pas 38.",
        "C'est l'effet de disposition à l'œuvre. Tu coupes tes gagnants trop tôt. Tu laisses courir tes perdants trop longtemps. Un revenge trade un jeudi a anéanti 120 euros. Son compte est passé de 650 euros à 530 euros en une semaine. Puis à 480 euros.",
    ]))
    s.append(P("Ce n'est pas un manque d'intelligence. Tu as lu les livres. Tu as suivi des formations. Tu connais les indicateurs. Les bougies japonaises. Les zones de support et résistance. Mais quelque chose bloque. Et cette croyance — que la prochaine configuration magique transformera tes 850 euros en 8 500 euros — c'est elle qui te tue à petit feu. Trade après trade."))

    # CH1
    s.append(ch('CHAPITRE 1','La Psychologie du Petit Compte','Comprendre pourquoi ça brûle si vite'))
    s.append(P("Avec seulement 500 euros, chaque euro perdu est un coup de massue. Chaque gain est une bouffée d'oxygène qui te pousse à prendre le risque suivant. C'est l'aversion aux pertes qui s'amplifie. La douleur de perdre 10 euros n'est pas juste le double du plaisir d'en gagner 10. Sur un compte de 500 euros, cette perte représente 2% de ton capital. Une somme qui te semble énorme. Ce 2% te paralyse. Ou pire, il te pousse à la vengeance."))
    s.append(P("Ton cerveau ne fait pas la différence entre 1% de 500 euros et 1% de 50 000 euros. Il ressent la pression. Il voit la taille relative de la perte. Et il panique. Il te pousse à agir de manière irrationnelle. C'est le détournement amygdalien qui prend le contrôle. Ton cerveau émotionnel court-circuite ta logique."))
    s.append(grb(["<b>MARCO — LE COMPTE QUI IMPLOSE</b>",
        "Marco avait commencé avec 700 euros. Il s'était juré de suivre ses règles. Il avait un plan clair. Le premier mois, il a fait de petits gains. Son compte est passé à 750 euros.",
        "Puis, un jeudi après-midi, il a pris une perte de 15 euros sur une paire Forex. Ce n'était que 2% de son compte. Mais il a ressenti une colère froide. Il a voulu récupérer ces 15 euros. Rapidement. Il a pris un trade sur-dimensionné. Sans stop loss. Convaincu que le marché allait se retourner.",
        "En moins de 30 minutes, il a perdu 180 euros. Son compte était à 555 euros. Il m'a dit : 'C'est comme si une autre personne était aux commandes.' C'est la réalité de l'épuisement de l'ego. Chaque décision, chaque perte, diminue ta discipline.",
    ]))
    s.append(H("Voir le Capital Différemment"))
    s.append(P("Les traders professionnels ne voient pas un petit compte comme une contrainte. Ils le voient comme un laboratoire. Un endroit où l'on peut affiner ses réflexes. Sans que la pression financière ne vienne tout gâcher. Un compte de 500 euros est parfait pour ça. Tu peux y développer ton identité de trader. Pas l'identité d'un joueur qui cherche le gros coup. Mais l'identité d'un gestionnaire de risque discipliné."))
    s.append(dq('"Imagine que chaque euro sur ton compte est un soldat. Un soldat loyal. Dont la mission est de te servir. De générer plus de soldats. Pas de mourir au combat sans raison."'))
    s.append(P("Ce n'est pas une question de chance. Ni de talent inné. C'est une question de système. De psychologie inversée. De chiffres précis que personne ne t'a montrés. Et ce secret est à ta portée. Même avec un compte de 800 euros."))
    s.append(grb(["<b>AISHA — LE REGARD QUI CHANGE TOUT</b>",
        "Son compte est passé de 650 euros à 480 euros. Elle a commencé à douter de tout. De ses compétences. De sa stratégie. De sa valeur. Ce n'était pas juste de l'argent. C'était un coup à son identité.",
        "Elle regardait d'autres traders sur les réseaux sociaux. Tous semblaient faire des gains incroyables. Des pourcentages fous. Elle se sentait perdue. Complètement déconnectée de la réalité du trading rentable.",
        "Tu as peut-être connu ce sentiment. Ce regard fixé sur l'écran. Cette boule au ventre. Cette question silencieuse : 'Qu'est-ce qui ne va pas chez moi ?'. La réponse : ce n'est pas un manque de stratégie. C'est un problème de cadre mental.",
    ]))

    # CH2
    s.append(ch('CHAPITRE 2','La Règle du 1%','Risquer 5€ pour construire tout le reste'))
    s.append(P("Voici un cadre simple et puissant pour transformer ton approche. La première règle est la plus critique. Risque un maximum de 1% de ton capital par trade. Sur 500 euros, ça fait 5 euros. Oui, 5 euros. Cela peut sembler ridicule. Tu te dis : 'Je ne vais jamais faire fortune avec 5 euros par trade.' Et c'est exactement le point. Tu n'es pas là pour faire fortune avec ces 5 euros. Tu es là pour prouver à toi-même que tu peux être un trader."))
    s.append(P("Avec 5 euros de risque, tu peux prendre 100 trades perdants d'affilée avant de vider ton compte. Cela te donne une marge d'erreur colossale. Cela enlève la pression du 'tout ou rien'. Et cette pression disparue — c'est de la clarté mentale retrouvée. De la discipline retrouvée."))
    s.append(gb(["<b>LES 3 RÈGLES DU CADRE DE BASE</b>",
        "◆  Règle 1 — Risque Maximum : 1% de ton capital par trade (5€ sur 500€)",
        "◆  Règle 2 — Limite de Trades : maximum 2-3 trades par jour, jamais plus",
        "◆  Règle 3 — Journal Obligatoire : chaque trade + l'émotion avant, pendant, après",
    ]))
    s.append(grb(["<b>MARCO — LA RÈGLE SAUVE-COMPTE</b>",
        "Imagine un instant. Tu as pris un trade, une petite perte de 5 euros. Ce n'est rien sur un compte de 10 000 euros. Mais sur 500 euros, ces 5 euros, c'est déjà 1% de ton solde. Ton cerveau crie. Il te dit : 'Récupère-le vite.'",
        "C'est là que la spirale commence. Tu commences à chercher un nouveau trade. Pas basé sur ton plan. Basé sur l'émotion. C'est le sophisme du joueur qui te murmure. La prochaine fois, ce sera la bonne. Avec la règle du 1%, ce danger est éliminé. 5 euros perdus ne déclenchent plus la réponse de panique.",
    ]))
    s.append(H("Redéfinir 'Gagner'"))
    s.append(P("Pour y arriver, tu as besoin de redéfinir ce que 'gagner' signifie au début. Ce n'est pas une question de profits en euros. C'est une question de preuves. De preuves que tu peux suivre tes règles. Que tu peux maîtriser tes émotions. Que tu peux exécuter ton plan. Même quand ton cerveau te supplie de faire le contraire."))
    s.append(P("La deuxième règle : limite ton nombre de trades par jour. Pas plus de deux ou trois trades. Si tu as atteint ton nombre, tu fermes la plateforme. Peu importe si tu as gagné ou perdu. La fatigue décisionnelle est réelle. Plus tu prends de décisions, plus la qualité de ces décisions diminue."))

    # CH3
    s.append(ch('CHAPITRE 3','Le Cadre des 3 Règles','Le système concret pour un petit capital'))
    s.append(P("La troisième règle : journalise absolument tout. Chaque trade. La raison de l'entrée. La raison de la sortie. L'émotion que tu as ressentie avant, pendant, et après le trade. Une note sur ton respect du plan. Ce n'est pas pour trouver la stratégie parfaite. C'est pour identifier tes schémas émotionnels."))
    s.append(P("C'est pour voir où l'aversion aux pertes te frappe le plus fort. Ou quand le biais de surconfiance t'amène à prendre trop de risques. Le marché ne se soucie pas de la taille de ton compte. Il se soucie de tes actions. Il récompense la discipline. Il punit l'impulsivité."))
    s.append(grb(["<b>AISHA — LA TRANSFORMATION EN 2 MOIS</b>",
        "Aisha a commencé avec 600 euros. Elle était frustrée par des mois de trading erratique. Elle a décidé d'appliquer ces règles strictes. 1% de risque par trade. Maximum 3 trades par jour. Journal de trading obligatoire.",
        "Pendant les trois premières semaines, son compte a très peu bougé. Il était à 605 euros. Puis à 598 euros. Puis à 612 euros. Elle a failli abandonner. Elle se sentait idiote de risquer seulement 6 euros.",
        "Mais elle a persévéré. Au bout de deux mois, son compte n'avait augmenté que de 7%. Mais son win rate était passé de 38% à 56%. Et plus important encore, elle avait arrêté les revenge trades. Elle avait développé une discipline. Elle était devenue une trader. Pas encore profitable en euros, mais profitable en comportement.",
    ]))
    s.append(H("La Dépersonnalisation de l'Argent"))
    s.append(P("Ne regarde pas tes gains ou tes pertes en pourcentage du compte. Regarde-les comme des points. Chaque trade est un point sur un graphique. Un point de données pour ton apprentissage. Tu gagnes 5 points. Tu perds 3 points. Ce n'est pas de l'argent. C'est de l'information. Cette dépersonnalisation de l'argent est une technique puissante. Elle te libère de la pression émotionnelle."))
    s.append(gb(["<b>SYSTÈME COMPLET DU PETIT CAPITAL</b>",
        "◆  Règle 1 : 1% de risque max par trade",
        "◆  Règle 2 : 2-3 trades max par jour, fermeture de la plateforme après",
        "◆  Règle 3 : Journal complet (émotions incluses) pour chaque trade",
        "◆  Règle 4 : Voir les trades comme des 'points', pas comme de l'argent",
        "◆  Règle 5 : Succès = respect du plan à 100%, jamais P&L en euros",
    ]))
    s.append(sr([('1%','de risque max — 100 trades perdants consécutifs avant de vider le compte'),
                 ('56%','win rate d\'Aisha après 2 mois vs 38% avant les 3 règles'),
                 ('7%','de croissance en 2 mois : petit mais constant, sans revenge trades')]))

    # CH4
    s.append(ch('CHAPITRE 4','La Transformation Aisha','Du compte qui stagne au comportement rentable'))
    s.append(P("C'est cette transformation comportementale qui est le vrai gain. C'est ça, 'gagner grand' avec un petit capital. La valeur de 500 euros ne réside pas dans sa capacité à te rendre riche. Elle réside dans sa capacité à te forcer à la discipline. À te forcer à apprendre les leçons fondamentales."))
    s.append(P("Ce que tu construis avec 500 euros, ce n'est pas un portefeuille. C'est une compétence. Et la compétence est transférable. Si tu arrives à être consistent et profitable avec un risque de 1% sur 500 euros, tu pourras faire la même chose avec 1% de 50 000 euros. Les chiffres seront différents, mais le processus, la psychologie, la discipline resteront identiques."))
    s.append(grb(["<b>MARCO — DE 555€ À LA CLARTÉ</b>",
        "Marco, après avoir perdu 180 euros en un après-midi de rage, a décidé de tout recommencer. Pas une nouvelle stratégie. Pas un nouvel indicateur. Un nouveau cadre mental.",
        "Il a appliqué les 3 règles strictement pendant 6 semaines. Les premières semaines, il ne faisait qu'un ou deux trades par jour. Parfois zéro. C'était difficile. Son ancien cerveau voulait 'faire quelque chose'.",
        "Mais lentement, quelque chose a changé. Il a commencé à voir chaque euro préservé comme une victoire. Chaque 'non' à une impulsion comme un progrès. Son compte a grimpé de 555 euros à 630 euros. Pas spectaculaire. Mais constant. Et surtout, fait avec discipline.",
    ]))
    s.append(H("Les Boucles de Dopamine Saines"))
    s.append(P("Les boucles de dopamine sont un concept puissant ici. Quand tu prends un trade risqué et que tu gagnes gros, ton cerveau libère de la dopamine. C'est une sensation incroyable. Mais cette sensation est addictive. Elle te pousse à répéter le comportement risqué. Même si c'est mauvais pour toi à long terme."))
    s.append(P("Avec un risque de 5 euros, les gains sont petits. La libération de dopamine est moins intense. Mais les gains constants, même petits, créent des boucles de dopamine plus saines. Des boucles qui récompensent la discipline. Pas le risque insensé. Et ces boucles saines sont le fondement d'une carrière de trader durable."))
    s.append(dq('"Le marché est un miroir. Il reflète tes peurs, tes espoirs, tes impatiences. Avec un petit compte, ces reflets sont amplifiés. Mais c\'est justement pour ça que le petit capital est ta meilleure opportunité de te connaître."'))

    # CH5
    s.append(ch('CHAPITRE 5','La Compétence Transférable','Prouver à 500€ ce qui sera vrai à 50 000€'))
    s.append(P("Pourquoi la grande majorité des traders particuliers — environ 95% selon les études — ne parviennent-ils pas à une rentabilité durable ? Ce n'est presque jamais une lacune technique. Ce n'est pas que leur stratégie est fondamentalement mauvaise. C'est l'exécution, pure et simple."))
    s.append(P("C'est l'incapacité à rester fidèle à un plan éprouvé lorsque la pression monte. C'est la peur viscérale de perdre une petite somme d'argent. C'est l'attrait irrésistible de gagner une somme importante, rapidement. Ces deux forces émotionnelles — la peur et la cupidité — dominent. Et elles dominent d'autant plus fort que le capital est petit."))
    s.append(grb(["<b>AISHA — 90 JOURS PLUS TARD</b>",
        "Trois mois après avoir appliqué les 3 règles, Aisha me contacte. Son compte est maintenant à 710 euros, en partant de 600. Une croissance de 18%. Petite, mais réelle.",
        "Mais ce qui a vraiment changé, c'est sa façon de se voir. Elle ne se décrit plus comme 'quelqu'un qui essaie de trader'. Elle se décrit comme 'un trader qui construit ses compétences'. Elle a demandé comment passer à un compte de 2 000 euros. Ma réponse : 'Pas encore. Prouve ton edge pendant 6 mois de plus. Ensuite, on en parle.'",
        "Elle a compris. Elle a souri. Elle a dit : 'Je comprends maintenant. Je ne veux pas plus d'argent. Je veux plus de compétence.' C'est ça, le vrai changement. C'est ça, 'Trader Petit pour Gagner Grand'.",
    ]))
    s.append(H("La Preuve avant l'Échelle"))
    s.append(P("C'est la preuve dont tu as besoin. La preuve pour toi-même. Le marché est indifférent à la taille de ton compte. Il est sensible à la cohérence de tes décisions. Un trader qui gère 500 euros avec discipline aura les mêmes principes pour gérer 50 000 euros. C'est la transférabilité de la compétence."))
    s.append(gb(["<b>LE CHEMIN EN 5 ÉTAPES</b>",
        "◆  Étape 1 : Appliquer les 3 règles strictement pendant 30 jours",
        "◆  Étape 2 : Atteindre un win rate > 50% sur au moins 50 trades",
        "◆  Étape 3 : Montrer une croissance positive (même 2-3%) sur 3 mois",
        "◆  Étape 4 : Démontrer ZÉRO revenge trade sur 2 mois consécutifs",
        "◆  Étape 5 : Seulement alors — envisager d'augmenter le capital",
    ]))
    s.append(P("Penses-y un instant. Si tu arrives à être consistant avec 500 euros — si tu respectes ta règle de 1%, si tu fermes la plateforme après tes 3 trades, si ton journal montre une amélioration constante — alors tu as prouvé quelque chose d'inestimable. Tu as prouvé que tu peux faire confiance à toi-même. Et cette preuve est transférable. À n'importe quel montant."))

    # CONCLUSION
    s.append(ch('CONCLUSION','Le Vrai Gain','La maîtrise de soi comme premier profit'))
    s.append(P("Alors, la prochaine fois que tu regardes ton compte de 500 euros et que tu ressens cette frustration, cette envie de tout risquer pour 'enfin faire quelque chose', rappelle-toi ceci. Ce petit compte est ta meilleure opportunité. Pas pour devenir millionnaire en un mois. Mais pour devenir un maître de toi-même."))
    s.append(P("Pour prouver que tu as la discipline. L'humilité. La patience. Les qualités que possèdent les vrais traders. Ceux qui ont duré. Ceux qui ont réussi. Ceux qui ont transformé 500 euros en bien plus. Mais d'abord, en une meilleure version d'eux-mêmes. Une version capable de gérer le marché. Et surtout, de se gérer soi-même."))
    s.append(grb(["<b>CHECKLIST DU PETIT CAPITAL</b>",
        "✓  Je risque maximum 1% de mon capital par trade, jamais plus",
        "✓  Je prends maximum 2-3 trades par jour — je ferme ensuite la plateforme",
        "✓  Je tiens un journal complet avec mes émotions pour chaque trade",
        "✓  Je mesure mon succès par mon win rate et mon respect du plan",
        "✓  Je vois mon capital comme un laboratoire, pas comme une source de richesse rapide",
        "✓  Je ne passe à un capital supérieur qu'après avoir prouvé mon edge pendant 6 mois",
    ]))
    s.append(gb(["<b>MES ENGAGEMENTS FINAUX</b>",
        "◆  Je comprends que la taille de mon capital est moins importante que ma discipline",
        "◆  Chaque euro préservé est une victoire autant que chaque euro gagné",
        "◆  Je construis une compétence transférable, pas un portefeuille",
        "◆  Je suis un gestionnaire de risque discipliné — même avec 500 euros",
        "◆  Ma liberté financière se construit brique par brique, trade discipliné après trade discipliné",
    ]))
    s.append(dq('"Ce n\'est pas une quête pour l\'argent rapide. C\'est une quête pour la maîtrise de soi. Et quand tu maîtrises ça — les profits suivent naturellement. C\'est là que le vrai travail commence. Et c\'est là qu\'il vaut la peine d\'être fait."'))
    s.append(Spacer(1,16))
    s+=[Paragraph('TRADING ZONE',st['br']),Paragraph('Collection Le Code du Trader Élite — Ebook 5/5',st['br2']),Paragraph('www.tradingzone.fr',st['br3'])]
    return s

def build():
    out='05_Trader_Petit_Grand_TRADING_ZONE.pdf'
    frame=Frame(ML,MB,CW,PAGE_H-MT-MB,id='main')
    tpl=PageTemplate(id='main',frames=[frame],onPage=footer)
    doc=BaseDocTemplate(out,pagesize=A4,pageTemplates=[tpl],leftMargin=ML,rightMargin=MR,topMargin=MT,bottomMargin=MB)
    story=cover()+[PageBreak()]+cpright()+[PageBreak()]+toc()+[PageBreak()]+content()
    doc.build(story); print(f"✓ {out} généré")

if __name__=='__main__': build()
