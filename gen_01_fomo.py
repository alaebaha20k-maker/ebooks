#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EBOOK 1/5 - FOMO : Maîtriser la Peur de Rater
Génère 01_FOMO_TRADING_ZONE.pdf
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.platypus.flowables import Flowable
import io

# ─── PALETTE ───────────────────────────────────────────────────────────────
NOIR    = HexColor('#0A0A0A')
OR      = HexColor('#C9A84C')
OR_PALE = HexColor('#FBF5E8')
OR_CLAIR= HexColor('#F5E6C8')
GRIS    = HexColor('#4A4A4A')
GRIS_BG = HexColor('#F5F5F5')
BLANC   = white

PAGE_W, PAGE_H = A4
ML, MR, MT, MB = 22*mm, 22*mm, 18*mm, 22*mm
CONTENT_W = PAGE_W - ML - MR

TITLE = "FOMO : Maîtriser la Peur de Rater"

# ─── STYLES ────────────────────────────────────────────────────────────────
def make_styles():
    s = {}
    s['intro_p']   = ParagraphStyle('intro_p',   fontName='Helvetica',      fontSize=13, textColor=GRIS, alignment=TA_JUSTIFY, leading=22, spaceAfter=10)
    s['body_p']    = ParagraphStyle('body_p',    fontName='Helvetica',      fontSize=11, textColor=GRIS, alignment=TA_JUSTIFY, leading=18.5, spaceAfter=8)
    s['body_bold'] = ParagraphStyle('body_bold', fontName='Helvetica-Bold', fontSize=11, textColor=NOIR, leading=18, spaceAfter=8)
    s['h2']        = ParagraphStyle('h2',        fontName='Helvetica-Bold', fontSize=15, textColor=OR,   leading=20, spaceBefore=16, spaceAfter=8)
    s['small_cap'] = ParagraphStyle('small_cap', fontName='Helvetica-Bold', fontSize=9,  textColor=OR,   leading=14, spaceAfter=4)
    s['stat_num']  = ParagraphStyle('stat_num',  fontName='Helvetica-Bold', fontSize=32, textColor=OR,   alignment=TA_CENTER, leading=38)
    s['stat_lbl']  = ParagraphStyle('stat_lbl',  fontName='Helvetica',      fontSize=8,  textColor=GRIS, alignment=TA_CENTER, leading=12)
    s['cover_badge']  = ParagraphStyle('cover_badge',  fontName='Helvetica-Bold', fontSize=9,  textColor=OR,      alignment=TA_CENTER, leading=14)
    s['cover_num']    = ParagraphStyle('cover_num',    fontName='Helvetica-Bold', fontSize=13, textColor=OR_CLAIR, alignment=TA_CENTER, leading=18)
    s['cover_t1']     = ParagraphStyle('cover_t1',     fontName='Helvetica-Bold', fontSize=44, textColor=BLANC,   alignment=TA_CENTER, leading=50)
    s['cover_t2']     = ParagraphStyle('cover_t2',     fontName='Helvetica-Bold', fontSize=30, textColor=OR,      alignment=TA_CENTER, leading=36)
    s['cover_sub']    = ParagraphStyle('cover_sub',    fontName='Helvetica',      fontSize=14, textColor=OR_CLAIR, alignment=TA_CENTER, leading=20)
    s['cover_tag']    = ParagraphStyle('cover_tag',    fontName='Helvetica',      fontSize=10, textColor=GRIS,    alignment=TA_CENTER, leading=14)
    s['cover_copy']   = ParagraphStyle('cover_copy',   fontName='Helvetica',      fontSize=9,  textColor=GRIS,    alignment=TA_CENTER, leading=12)
    s['copy_title']   = ParagraphStyle('copy_title',   fontName='Helvetica-Bold', fontSize=14, textColor=NOIR,    alignment=TA_CENTER, leading=20, spaceAfter=8)
    s['copy_body']    = ParagraphStyle('copy_body',    fontName='Helvetica',      fontSize=10, textColor=GRIS,    alignment=TA_CENTER, leading=16, spaceAfter=6)
    s['toc_label']    = ParagraphStyle('toc_label',    fontName='Helvetica-Bold', fontSize=9,  textColor=OR,      leading=14)
    s['toc_title']    = ParagraphStyle('toc_title',    fontName='Helvetica-Bold', fontSize=11, textColor=NOIR,    leading=16)
    s['toc_sub']      = ParagraphStyle('toc_sub',      fontName='Helvetica',      fontSize=9,  textColor=GRIS,    leading=13, spaceAfter=6)
    s['dq_text']      = ParagraphStyle('dq_text',      fontName='Helvetica-Oblique', fontSize=12, textColor=OR_CLAIR, alignment=TA_CENTER, leading=20)
    s['check_text']   = ParagraphStyle('check_text',   fontName='Helvetica', fontSize=11, textColor=GRIS, leading=18, spaceAfter=4)
    s['bullet_text']  = ParagraphStyle('bullet_text',  fontName='Helvetica', fontSize=11, textColor=GRIS, leading=18, spaceAfter=4)
    s['ch_label']     = ParagraphStyle('ch_label',     fontName='Helvetica-Bold', fontSize=9,  textColor=OR,   leading=14)
    s['ch_title']     = ParagraphStyle('ch_title',     fontName='Helvetica-Bold', fontSize=22, textColor=NOIR, leading=28, spaceAfter=4)
    s['ch_sub']       = ParagraphStyle('ch_sub',       fontName='Helvetica',      fontSize=13, textColor=GRIS, leading=20, spaceAfter=12)
    return s

ST = make_styles()

# ─── FOOTER ────────────────────────────────────────────────────────────────
def footer_cb(canvas, doc):
    canvas.saveState()
    y = MB - 8*mm
    canvas.setStrokeColor(GRIS)
    canvas.setLineWidth(0.3)
    canvas.line(ML, y + 5*mm, PAGE_W - MR, y + 5*mm)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(GRIS)
    canvas.drawString(ML, y, f"{TITLE}  ·  © TRADING ZONE")
    canvas.drawRightString(PAGE_W - MR, y, f"© TRADING ZONE  ·  {doc.page}")
    canvas.restoreState()

# ─── COMPONENTS ────────────────────────────────────────────────────────────
def dark_quote(text):
    inner = Paragraph(text, ST['dq_text'])
    tbl = Table([[inner]], colWidths=[CONTENT_W])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NOIR),
        ('TOPPADDING',    (0,0), (-1,-1), 16),
        ('BOTTOMPADDING', (0,0), (-1,-1), 16),
        ('LEFTPADDING',   (0,0), (-1,-1), 22),
        ('RIGHTPADDING',  (0,0), (-1,-1), 22),
    ]))
    return KeepTogether([Spacer(1, 8), tbl, Spacer(1, 8)])

def gold_box(items):
    rows = []
    for it in items:
        rows.append([Paragraph(it, ST['body_p'])])
    tbl = Table(rows, colWidths=[CONTENT_W - 32])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), OR_PALE),
        ('BOX',           (0,0), (-1,-1), 2.5, OR),
        ('TOPPADDING',    (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING',   (0,0), (-1,-1), 16),
        ('RIGHTPADDING',  (0,0), (-1,-1), 16),
    ]))
    outer = Table([[tbl]], colWidths=[CONTENT_W])
    outer.setStyle(TableStyle([
        ('LEFTPADDING',   (0,0), (-1,-1), 0),
        ('RIGHTPADDING',  (0,0), (-1,-1), 0),
        ('TOPPADDING',    (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    return KeepTogether([Spacer(1, 6), tbl, Spacer(1, 6)])

def grey_box(items):
    rows = []
    for it in items:
        rows.append([Paragraph(it, ST['body_p'])])
    inner = Table(rows, colWidths=[CONTENT_W - 24])
    inner.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), GRIS_BG),
        ('TOPPADDING',    (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING',   (0,0), (-1,-1), 16),
        ('RIGHTPADDING',  (0,0), (-1,-1), 8),
    ]))
    bar  = Table([['']],  colWidths=[3.5])
    bar.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), OR),
        ('TOPPADDING',    (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING',   (0,0), (-1,-1), 0),
        ('RIGHTPADDING',  (0,0), (-1,-1), 0),
    ]))
    combo = Table([[bar, inner]], colWidths=[3.5, CONTENT_W - 3.5])
    combo.setStyle(TableStyle([
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING',    (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING',   (0,0), (-1,-1), 0),
        ('RIGHTPADDING',  (0,0), (-1,-1), 0),
    ]))
    return KeepTogether([Spacer(1, 6), combo, Spacer(1, 6)])

def stats_row(data):
    cells = []
    for val, lbl in data:
        cells.append([Paragraph(val, ST['stat_num']), Paragraph(lbl, ST['stat_lbl'])])
    col_w = CONTENT_W / len(data)
    rows_t = [[Table([c], colWidths=[col_w]) for c in cells]]
    tbl = Table(rows_t, colWidths=[col_w]*len(data))
    tbl.setStyle(TableStyle([
        ('TOPPADDING',    (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING',   (0,0), (-1,-1), 4),
        ('RIGHTPADDING',  (0,0), (-1,-1), 4),
    ]))
    hr = HRFlowable(width=CONTENT_W, thickness=1, color=OR, spaceAfter=4)
    hr2= HRFlowable(width=CONTENT_W, thickness=1, color=OR, spaceBefore=4)
    return KeepTogether([Spacer(1,6), hr, tbl, hr2, Spacer(1,6)])

def check(text):
    return Paragraph(f'<font color="#2E7D32">✓</font>  {text}', ST['check_text'])

def bullet_or(text):
    return Paragraph(f'<font color="#C9A84C">◆</font>  {text}', ST['bullet_text'])

def ch_header(label, title, subtitle):
    elems = [
        Paragraph(label, ST['ch_label']),
        HRFlowable(width=CONTENT_W, thickness=1.5, color=OR, spaceAfter=6),
        Paragraph(title, ST['ch_title']),
        Paragraph(subtitle, ST['ch_sub']),
    ]
    return KeepTogether(elems)

# ─── COVER ─────────────────────────────────────────────────────────────────
def build_cover():
    story = []
    def row(p): return [p]
    rows = [
        [Paragraph('◆   COLLECTION LE CODE DU TRADER ÉLITE   ◆', ST['cover_badge'])],
        [Spacer(1, 12)],
        [Paragraph('EBOOK 1 / 5', ST['cover_num'])],
        [Spacer(1, 20)],
        [Paragraph('FOMO :', ST['cover_t1'])],
        [Paragraph('Maîtriser la Peur de Rater', ST['cover_t2'])],
        [Spacer(1, 12)],
        [HRFlowable(width=70*mm, thickness=1.5, color=OR, spaceAfter=0)],
        [Spacer(1, 12)],
        [Paragraph('La méthode complète pour ne plus jamais chasser le marché', ST['cover_sub'])],
        [Paragraph('et reprendre le contrôle de tes décisions', ST['cover_sub'])],
        [Spacer(1, 20)],
        [Paragraph('PSYCHOLOGIE DU TRADING · ÉDITION FRANÇAISE', ST['cover_tag'])],
        [Spacer(1, 12)],
        [Paragraph('© TRADING ZONE — Tous droits réservés', ST['cover_copy'])],
    ]
    tbl = Table(rows, colWidths=[170*mm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), NOIR),
        ('TOPPADDING',    (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING',   (0,0), (-1,-1), 20),
        ('RIGHTPADDING',  (0,0), (-1,-1), 20),
        ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(Spacer(1, 30*mm))
    story.append(tbl)
    return story

# ─── COPYRIGHT ─────────────────────────────────────────────────────────────
def build_copyright():
    story = [Spacer(1, 40*mm)]
    story.append(Paragraph('FOMO : Maîtriser la Peur de Rater', ST['copy_title']))
    story.append(HRFlowable(width=80*mm, thickness=1, color=OR, spaceAfter=16))
    for line in [
        '© 2024 TRADING ZONE — Tous droits réservés.',
        "Aucune partie de cet ouvrage ne peut être reproduite, distribuée ou transmise",
        "sous quelque forme que ce soit, sans l'autorisation écrite préalable de l'éditeur.",
        '',
        'Auteur : TRADING ZONE — Édition numérique PDF',
        '',
        'Avertissement légal :',
        "Cet ebook est destiné à un usage éducatif et informatif uniquement.",
        "Il ne constitue pas un conseil financier ou d'investissement.",
        "Le trading comporte des risques importants.",
        "Vous êtes seul responsable de vos décisions d'investissement.",
        '',
        'www.tradingzone.fr',
    ]:
        story.append(Paragraph(line, ST['copy_body']))
    return story

# ─── TABLE OF CONTENTS ─────────────────────────────────────────────────────
def build_toc():
    story = [Spacer(1, 10*mm)]
    story.append(Paragraph('TABLE DES MATIÈRES', ST['h2']))
    story.append(HRFlowable(width=CONTENT_W, thickness=1, color=OR, spaceAfter=12))
    entries = [
        ('INTRODUCTION', 'La Bougie Verte', 'Ce que tu ressens quand le marché monte sans toi'),
        ('CHAPITRE 1', "L'Ennemi Invisible", 'Pourquoi ton cerveau est câblé pour te faire rater'),
        ('CHAPITRE 2', 'Le Coût Réel', 'Ce que le FOMO détruit au-delà de l\'argent'),
        ('CHAPITRE 3', 'La Forteresse', 'Construire un système que le FOMO ne peut pas briser'),
        ('CHAPITRE 4', 'Le Recadrage Radical', 'Quand rater devient une victoire de discipline'),
        ('CHAPITRE 5', 'La Victoire Silencieuse', 'Devenir le trader qui choisit plutôt que celui qui chasse'),
        ('CONCLUSION', 'Le Trader que Tu Dois Devenir', 'Ton engagement final et ta feuille de route'),
    ]
    for lbl, title, sub in entries:
        story.append(Paragraph(lbl, ST['toc_label']))
        story.append(Paragraph(title, ST['toc_title']))
        story.append(Paragraph(sub, ST['toc_sub']))
        story.append(Spacer(1, 4))
    return story

# ─── CONTENT ────────────────────────────────────────────────────────────────
def build_content():
    story = []
    P = lambda t: Paragraph(t, ST['body_p'])
    PB = lambda t: Paragraph(t, ST['body_bold'])
    H2 = lambda t: Paragraph(t, ST['h2'])
    PI = lambda t: Paragraph(t, ST['intro_p'])

    # ── INTRODUCTION ──────────────────────────────────────────────────────
    story.append(ch_header('INTRODUCTION', 'La Bougie Verte', 'Ce que tu ressens quand le marché monte sans toi'))
    story.append(PI("La bougie verte ne s'arrête pas. Elle monte. +14%. Puis +18%. Ton doigt hésite au-dessus de la touche. Figé. Deux minutes plus tard, elle atteint +25%. Tu avais vu ce setup une heure avant. Tu l'avais ignoré. Et maintenant, cette nausée familière s'installe. Ce regret lourd, presque physique. Cette envie désespérée de rentrer avant qu'il ne soit trop tard."))
    story.append(PI("Tu connais ce nœud dans l'estomac. Ces battements accélérés dans les tempes. Tu viens d'expérimenter le rugissement primitif du FOMO — la peur de rater. Ce n'est pas juste une émotion passagère. C'est une douleur presque physique. Un sentiment profond d'être laissé pour compte. D'être invisible pendant que les autres s'enrichissent."))
    story.append(stats_row([
        ('83%', 'des traders retail sautent dans des trades par urgence perçue'),
        ('2x',  'plus intense : la douleur de rater vs une perte réelle'),
        ('95%', 'des traders particuliers n\'atteignent pas la rentabilité durable'),
    ]))
    story.append(dark_quote('"Il ne s\'agit pas de supprimer l\'émotion. Il s\'agit de comprendre pourquoi elle apparaît — et d\'avoir un système qui te protège d\'elle."'))
    story.append(P("Ce nœud dans l'estomac a un nom scientifique. Il a une mécanique précise. Et surtout, il a un antidote — pas basé sur la force de volonté, mais sur la compréhension profonde de ce qui se passe dans ton cerveau quand le marché bouge sans toi."))
    story.append(P("Ce livre va te montrer exactement comment faire ça. Pas avec des mantras vides. Pas avec des conseils génériques sur 'la discipline'. Mais avec des mécanismes précis, des histoires réelles, et des outils que tu peux appliquer dès ta prochaine session."))

    # ── CHAPITRE 1 ─────────────────────────────────────────────────────────
    story.append(ch_header('CHAPITRE 1', "L'Ennemi Invisible", 'Pourquoi ton cerveau est câblé pour te faire rater'))
    story.append(P("Imagine un mardi après-midi ordinaire. Bitcoin est en hausse. +3,7% en trente minutes. Tu avais décidé de prendre la journée plus détendue. Mais maintenant, chaque chiffre vert qui clignote ressemble à une insulte personnelle. Chaque tweet positif d'un autre trader brûle. Ils gagnent de l'argent. Toi, tu ne fais rien."))
    story.append(P("Ce n'est pas un manque de force mentale. C'est quelque chose de bien plus fondamental. C'est un mécanisme de survie millénaire, armé par le trading numérique."))
    story.append(H2('Le Câblage Ancestral'))
    story.append(P("Pendant des millénaires, les humains ont survécu en suivant le troupeau. Si tout le monde courait vers une nouvelle source de nourriture, tu courais aussi. L'hésitation signifiait la disette. En trading, ce même câblage ancien te dit de courir derrière le mouvement. De sauter dans ce trade en fusée. Même s'il est déjà à mi-chemin vers la lune."))
    story.append(grey_box([
        "<b>L'HISTOIRE D'ALEX</b>",
        "Alex a vu le graphique Solana exploser. +21% en 45 minutes. Il n'était pas à son bureau — il récupérait ses enfants à l'école. Rentré chez lui, il a vérifié son téléphone. Vu le vert. Ressenti ce sentiment d'enfoncement familier.",
        "Le lendemain matin, toujours vibrant de regret, il a repéré un petit altcoin grimper modestement de 3%. Il a foncé. Pas parce que sa stratégie indiquait une entrée. Parce qu'il ne pouvait pas supporter de rater encore une fois. Une heure plus tard, il était en baisse de 6%. Il avait transformé son regret initial en une perte fraîche et inutile.",
    ]))
    story.append(H2('La Nature Insidieuse du FOMO'))
    story.append(P("C'est là que réside le vrai danger. Le FOMO ne te fait pas seulement rater des trades. Il te pousse activement dans de mauvais trades. Il te fait abandonner tes règles soigneusement construites. Il te fait chasser des opportunités fugaces qui s'évaporent souvent au moment précis où tu sautes dedans."))
    story.append(gold_box([
        "<b>VÉRITÉ BRUTALE N°1</b>",
        "Le FOMO ne concerne pas le trade que tu as manqué. Il concerne le trade stupide que tu vas prendre à cause du trade que tu as manqué.",
    ]))
    story.append(H2("L'Effet de Wagon — Bandwagon Effect"))
    story.append(P("Cette impulsion porte un nom en psychologie comportementale : l'Effet de Wagon. Tout le monde le fait, donc ça doit être correct. Ton cerveau interprète l'activité collective comme un signal de sécurité. Mais sur les marchés financiers, c'est souvent exactement le contraire : le moment où tout le monde parle d'un mouvement est souvent le moment où ce mouvement est sur le point de s'inverser."))
    story.append(grey_box([
        "<b>MARCUS ET SOLANA — UNE RÈGLE BRISÉE</b>",
        "Marcus observait Solana depuis des semaines. Il avait un setup solide identifié à 105€. Il avait posé une alerte. Mais le marché a bougé pendant qu'il était en réunion. Quand il a regardé, Solana était déjà à 118€.",
        "Sa règle était claire : ne jamais chasser un mouvement déjà à +10% de son entrée prévue. Mais l'écran était un kaléidoscope de vert. Il s'est dit : 'C'est différent cette fois. Ça va à 150€.' Il a cliqué achat à 119€.",
        "En une heure, Solana a retracé à 112€. Marcus a clôturé. -700€. Il savait mieux que ça. Il n'avait simplement pas pu résister.",
    ]))
    story.append(H2("L'Heuristique de Disponibilité"))
    story.append(P("Ton cerveau se souvient des gains massifs que tu as vus postés par d'autres traders. Il ignore les pertes silencieuses. Cette asymétrie de mémoire crée une vision déformée de la réalité — une réalité où tout le monde gagne sauf toi. C'est l'Heuristique de Disponibilité à l'œuvre. Elle amplifie le danger du FOMO en te faisant croire que les opportunités manquées sont la règle, non l'exception."))
    story.append(P("Comprendre ce mécanisme n'est pas juste académique. C'est la première étape pour le désamorcer. Quand tu sais que ton cerveau exagère la douleur de rater, tu peux commencer à questionner cette douleur. À te demander : est-ce que cette urgence est réelle ? Ou est-ce simplement mon câblage ancestral qui fait son travail millénaire ?"))

    # ── CHAPITRE 2 ─────────────────────────────────────────────────────────
    story.append(ch_header('CHAPITRE 2', 'Le Coût Réel', "Ce que le FOMO détruit au-delà de l'argent"))
    story.append(P("La plupart des traders pensent que le FOMO concerne l'argent. Les euros qu'ils auraient pu gagner sur un trade manqué. Mais le vrai coût est beaucoup plus insidieux. Il touche quelque chose de bien plus profond : l'identité."))
    story.append(P("Tu as commencé à trader parce que tu voulais du contrôle. Tu imaginais être un décideur intelligent, calculé, maître de tes finances. Puis le FOMO frappe. Tu fais un trade stupide. Tu perds peut-être 17% de ton compte en une impulsion d'après-midi. Soudain, cette image de toi-même s'effondre."))
    story.append(dark_quote('"Les dommages émotionnels sont bien plus dangereux que toute perte financière. Les pertes financières peuvent se récupérer. Une image de soi brisée peut faire dérailler toute une carrière."'))
    story.append(H2('Le Capital Mental'))
    story.append(P("Chaque décision prise sous l'influence du FOMO grignote ton capital mental. Ce n'est pas une métaphore. La recherche en neurosciences montre que les décisions émotionnelles épuisent les ressources cognitives de la même façon qu'un effort physique intense épuise les muscles."))
    story.append(P("Quand ton capital mental est épuisé, tu prends de pires décisions. Tu es plus susceptible aux biais. Tu es plus lent à détecter les signaux réels. Le cercle vicieux s'auto-alimente. Chaque trade FOMO prépare le terrain pour le prochain. C'est une spirale que seule la conscience peut briser."))
    story.append(grey_box([
        "<b>AISHA ET SON SYSTÈME SOLIDE</b>",
        "Aisha trade le Forex. Elle a méticuleusement backtesté un système de suivi de tendance pendant six mois. Win rate de 62%. R moyen de 1,4. Un système solide.",
        "Un mardi matin, elle fait défiler un forum de trading. Tout le monde parle d'un short sur EUR/USD. 'Grosse cassure en approche.' '200 pips faciles.' Son système n'a aucun signal. En fait, il penche long.",
        "Mais l'excitation collective est écrasante. Elle doute de son propre processus : 'Est-ce que je rate quelque chose d'évident ?' Elle prend une petite position short. EUR/USD choppe pendant une heure, puis remonte. Petite perte.",
        "L'erreur d'Aisha n'était pas la perte en euros. C'était l'érosion de sa confiance dans son propre système. Son bord statistique — construit en six mois — a été mis en doute à cause d'un forum.",
    ]))
    story.append(H2("L'Effet de Contagion Émotionnelle"))
    story.append(P("Les réseaux sociaux amplifient cette contagion. Les screenshots de gains massifs inondent ton fil d'actualité. Chaque témoignage de succès déclenche une comparaison douloureuse. Mateo, un trader d'options, passait des heures à lire des forums. Il achetait sur la base du buzz. Il perdait 60% de son compte en six mois. Son FOMO était alimenté par une communauté entière."))
    story.append(P("Sa solution ? Il s'est désabonné de tous les forums de trading. Il a supprimé les réseaux sociaux de son téléphone pendant les heures de trading. Il a réduit son temps d'écran de 75%. Ses résultats ont commencé à se stabiliser. Les gains petits mais constants ont remplacé les montagnes russes émotionnelles."))
    story.append(gold_box([
        "<b>LES 3 NIVEAUX DE COÛT DU FOMO</b>",
        "◆  Coût 1 — Financier : Les trades de FOMO ont en moyenne un ratio risque/récompense 40% moins favorable que les trades planifiés.",
        "◆  Coût 2 — Mental : Chaque décision émotionnelle épuise les ressources cognitives et réduit la qualité des décisions suivantes.",
        "◆  Coût 3 — Identitaire : L'accumulation de trades FOMO érode la confiance en soi et crée une prophétie auto-réalisatrice d'échec.",
    ]))

    # ── CHAPITRE 3 ─────────────────────────────────────────────────────────
    story.append(ch_header('CHAPITRE 3', 'La Forteresse', 'Construire un système que le FOMO ne peut pas briser'))
    story.append(P("La solution n'est pas la force de volonté. On ne peut pas simplement décider de ne pas ressentir le FOMO. C'est une réponse physiologique. C'est le cortisol et l'adrénaline qui font leur travail millénaire. La vraie solution, c'est de construire des structures. Un système si robuste que le FOMO ne peut pas le briser."))
    story.append(H2('Outil 1 — La Liste de Surveillance Proactive'))
    story.append(P("Ne réagis pas au marché. Anticipe-le. Identifie les actifs qui correspondent à tes critères bien avant qu'ils ne bougent. Pré-analyse leurs graphiques chaque soir. Marque les niveaux clés. Identifie les setups potentiels. Cette seule habitude fait passer ton état d'esprit de 'chasser' à 'attendre'."))
    story.append(P("Quand un actif de ta liste commence à bouger, ce n'est pas un signal de panique — c'est un signal de vérification. Est-ce que ça correspond à mon plan ? Si non, tu regardes. Tu ne bouges pas."))
    story.append(H2('Outil 2 — La Zone de Non-Trade'))
    story.append(P("Après un mouvement parabolique, le marché entre dans une zone à haut risque. Les mains fortes prennent leurs profits. Le retail afflue, pensant que le mouvement va continuer. Ta règle : si un actif a bougé de plus de X% en moins de Y heures, tu ne prends aucune nouvelle entrée pendant une période définie."))
    story.append(grey_box([
        "<b>JULIAN — UNE RÈGLE QUI A TOUT CHANGÉ</b>",
        "Julian trade les small caps américaines. Il se faisait piéger dans chaque pump-and-dump. Il achetait à l'ouverture des actions qui montaient de 50% en pré-marché. La moitié du temps, il était en baisse de 20% avant midi.",
        "Maintenant, Julian a une règle simple mais inviolable : toute action à +25% en pré-marché, il ne considère que des positions short. Et seulement si elle montre des signes clairs de faiblesse à l'ouverture. Cette seule règle lui a économisé des milliers d'euros. Elle a transformé sa perspective du marché.",
    ]))
    story.append(H2('Outil 3 — Les Alertes de Prix'))
    story.append(P("Pose des alertes à tes niveaux d'entrée clés. Puis éloigne-toi de l'écran. Va vivre ta vie. Quand l'alerte se déclenche, tu reviens avec un regard frais. Tu n'as pas absorbé 4 heures de bruit émotionnel du marché. Tu peux évaluer calmement si l'entrée est toujours valide."))
    story.append(P("Cette technique simple réduit ce qu'on appelle la 'Fatigue Décisionnelle'. Chaque fois que tu surveilles ton écran, même passivement, tu consommes de l'énergie cognitive. Chaque fois que tu résistes à l'envie d'entrer sur un mauvais setup, tu utilises une partie de ta réserve de discipline. Les alertes automatisent l'observation — et préservent ta discipline pour les moments qui comptent vraiment."))
    story.append(H2('Outil 4 — Le Journal Anti-FOMO'))
    story.append(P("Lucie, une trader sur futures, a commencé à tout journaliser avec une précision médicale. Pas seulement les entrées et les sorties. Elle notait son état émotionnel avant chaque trade. Elle documentait les trades qu'elle avait failli prendre mais qu'elle avait évités."))
    story.append(gold_box([
        "<b>LES DONNÉES DE LUCIE — 3 MOIS DE JOURNAL</b>",
        "◆  Trades FOMO détectés : 23",
        "◆  Pertes sur ces trades : 78% des cas",
        "◆  Perte moyenne FOMO : 1,8x la perte moyenne sur trades planifiés",
        "◆  Conclusion : Chaque trade FOMO lui coûtait en moyenne le double d'un trade normal. Voir ce chiffre noir sur blanc a changé sa relation au FOMO — la douleur de rater était devenue moins forte que la certitude de perdre.",
    ]))

    # ── CHAPITRE 4 ─────────────────────────────────────────────────────────
    story.append(ch_header('CHAPITRE 4', 'Le Recadrage Radical', 'Quand rater devient une victoire de discipline'))
    story.append(P("Qu'est-ce que 'rater' signifie vraiment dans le trading ? C'est la peur de laisser de l'argent sur la table. La croyance que chaque mouvement profitable est ton argent. Mais c'est une illusion profondément destructrice."))
    story.append(P("Les marchés financiers opèrent depuis des centaines d'années. Ils continueront bien après nous. La croyance que 'ceci est la dernière opportunité' est le mensonge fondamental du FOMO. Il y a toujours un autre setup. Toujours une autre opportunité."))
    story.append(dark_quote('"L\'argent ne t\'appartient pas tant qu\'il n\'est pas dans ton compte. Et il n\'est dans ton compte que si tu as suivi ton processus."'))
    story.append(H2('La Redéfinition du Succès'))
    story.append(P("La plupart des traders mesurent le succès par leur P&L. Chaque jour. Chaque trade. Cette boucle de rétroaction immédiate est la source principale du FOMO. Elle connecte ton estime de soi à un résultat aléatoire à court terme."))
    story.append(P("Les traders professionnels mesurent quelque chose de différent. Ils mesurent l'adhésion à leur processus. La qualité de leur exécution. La cohérence de leur comportement. Les profits sont la conséquence de ce processus — pas la mesure directe."))
    story.append(grey_box([
        "<b>LE PRÉ-MORTEM DE DÉCLAN</b>",
        "Déclan, un trader de devises, passait 8 heures par jour devant ses graphiques. Il prenait 15 à 20 trades par jour. La plupart étaient des entrées FOMO ou des trades de vengeance. Sa performance chutait de 40% après la première heure.",
        "Il a mis en place un plan rigide : chaque soir, il définissait exactement 1 à 3 setups possibles pour le lendemain. Les conditions d'entrée précises. Le stop. L'objectif. S'ils ne se présentaient pas, il ne faisait rien.",
        "Résultat en 6 mois : nombre de trades passé de 15+ à 3 par jour. Win rate de 38% à 55%. Son niveau de stress : réduit drastiquement. Il était enfin en contrôle.",
    ]))
    story.append(H2('Le Recadrage Pratique'))
    story.append(P("Voici l'exercice de recadrage le plus puissant que tu puisses pratiquer. La prochaine fois que tu rates un trade, dis-toi exactement ceci :"))
    story.append(gold_box([
        "<b>LE SCRIPT DE RECADRAGE</b>",
        "Ce trade ne respectait pas mes critères d'entrée définis. Ne pas le prendre était la décision correcte, indépendamment du résultat. Mon travail est d'exécuter mon plan. Pas de prédire quels trades vont monter.",
    ]))
    story.append(P("Ce script semble simple. Il l'est. Mais sa répétition systématique reprogramme ton association mentale entre 'rater un trade' et 'échec'. Tu commences à vivre ce recadrage comme une vérité — parce que c'en est une."))
    story.append(H2('Le Sophisme du Joueur'))
    story.append(P("Après avoir raté un trade profitable, ton cerveau te murmure que tu es 'dû' pour un gain. Que le prochain mouvement doit être le tien. C'est le Sophisme du Joueur appliqué au trading. Chaque trade est un événement indépendant. Le marché ne sait pas que tu as raté le précédent. Il ne te 'doit' rien."))
    story.append(P("Cette vérité est à la fois libératrice et exigeante. Libératrice parce qu'elle te décharge de la pression artificielle de 'récupérer'. Exigeante parce qu'elle t'oblige à évaluer chaque trade sur ses propres mérites, pas sur ta situation émotionnelle du moment."))
    story.append(stats_row([
        ('40%', 'moins favorable : ratio risque/récompense des trades FOMO vs planifiés'),
        ('78%', 'des trades FOMO de Lucie se terminaient en perte'),
        ('1.8x', 'la perte moyenne d\'un trade FOMO vs un trade planifié'),
    ]))

    # ── CHAPITRE 5 ─────────────────────────────────────────────────────────
    story.append(ch_header('CHAPITRE 5', 'La Victoire Silencieuse', 'Devenir le trader qui choisit plutôt que celui qui chasse'))
    story.append(P("Clara a commencé comme beaucoup d'autres traders. Elle regardait le marché monter. Elle ressentait cette douleur familière de regret. Elle entrait dans des trades en retard. Elle sortait trop tôt quand elle gagnait, trop tard quand elle perdait. Après 14 mois de montagnes russes émotionnelles, elle était épuisée."))
    story.append(P("Elle a décidé de changer l'objectif fondamental de son trading. Pour 90 jours, elle ne regarderait plus son P&L chaque soir. Son unique métrique serait son score de respect des règles. Une coche verte pour chaque règle suivie. Un X rouge pour chaque déviation."))
    story.append(grey_box([
        "<b>CLARA — 90 JOURS DE PROCESSUS PUR</b>",
        "Semaines 1-2 : score de conformité à 60%. Elle luttait encore avec les sorties prématurées et les entrées tardives.",
        "Semaine 6 : conformité à 85%. Les données remplaçaient les émotions dans ses journaux.",
        "Semaine 12 : conformité dépassant 92% de façon consistante.",
        "Bilan à 90 jours : performance améliorée de 18% versus la période précédente. Mais surtout — son niveau de stress réduit de moitié. Elle se sentait enfin en contrôle de ses décisions.",
    ]))
    story.append(H2('Le Stop Loss Mental'))
    story.append(P("Tout comme tu définis un prix où tu sors d'un trade perdant, définis un état mental où tu arrêtes de trader. Si tu ressens cette urgence familière. Si ta respiration s'accélère. Si tu commences à chercher des excuses pour un mauvais setup. C'est ton signal. Lève-toi. Éloigne-toi de l'écran."))
    story.append(P("Ce Stop Loss Mental préserve quelque chose de bien plus précieux que l'argent : ton capital décisionnel. Si tu le draines en courant après chaque mouvement, tu n'auras plus rien en réserve pour les setups à haute probabilité."))
    story.append(H2("L'Identité du Trader Discipliné"))
    story.append(P("Haruki, un trader d'options sur actions, a identifié son déclencheur précis : les rallyes soudains de +15% en une heure sur des meme stocks. Son journal montrait que 7 fois sur 7, quand il entrait sur ce type de mouvement, il perdait entre 200 et 500 euros."))
    story.append(P("Il a créé une règle simple : si un actif a bougé de plus de 5% en moins de 15 minutes, il ne touche pas cet actif pendant les 30 minutes suivantes. Pas parce qu'il prédisait un retournement. Parce qu'il prédisait sa propre réaction — et il choisissait de ne pas lui faire confiance."))
    story.append(grey_box([
        "<b>LE RÉSULTAT D'HARUKI</b>",
        "En quatre semaines, ses pertes dues au FOMO : zéro.",
        "A-t-il raté des mouvements explosifs ? Oui.",
        "A-t-il évité 100% des retournements violents qui lui avaient coûté des milliers d'euros ? Oui.",
        "Son choix : la paix plutôt que le potentiel. Ses règles plutôt que le bruit. Lui-même plutôt que le marché.",
    ]))
    story.append(dark_quote('"Tu n\'es pas le trader qui chasse chaque pump. Tu es le trader qui attend patiemment son setup. Celui qui exécute son plan avec précision. Ce changement d\'identité — c\'est la vraie victoire sur le FOMO."'))

    # ── CONCLUSION ─────────────────────────────────────────────────────────
    story.append(ch_header('CONCLUSION', 'Le Trader que Tu Dois Devenir', 'Ton engagement final et ta feuille de route'))
    story.append(P("La prochaine fois que ce nœud familier se forme dans ton estomac. La prochaine fois que tu vois un graphique partir en fusée sans toi. La prochaine fois que ton fil d'actualité est inondé de screenshots de gains que tu n'as pas faits."))
    story.append(PB("Souviens-toi de ceci : Tu n'es pas en train de rater un trade. Tu es en train de choisir de ne pas participer à quelque chose qui ne respecte pas tes règles. Et c'est une victoire."))
    story.append(grey_box([
        "<b>LES 5 OUTILS DE TA FORTERESSE</b>",
        "✓  La Liste de Surveillance Proactive — anticiper, pas réagir",
        "✓  La Zone de Non-Trade — des règles spécifiques après les mouvements paraboliques",
        "✓  Les Alertes de Prix — automatiser l'observation, préserver la discipline",
        "✓  Le Journal Anti-FOMO — transformer les données en conscience",
        "✓  Le Script de Recadrage — reprogrammer l'association rater = échec",
    ]))
    story.append(P("Le FOMO ne disparaîtra jamais complètement. Ce n'est pas l'objectif. L'objectif, c'est de construire un système si solide que quand le FOMO se manifeste — et il se manifestera — il frappe un mur. Un mur fait de règles claires, de données concrètes, et d'une identité de trader que tu as choisie consciemment."))
    story.append(gold_box([
        "<b>TES ENGAGEMENTS FINAUX</b>",
        "◆  Je construis et maintiens ma liste de surveillance proactive chaque soir.",
        "◆  Je pose des alertes de prix — et je m'éloigne de l'écran.",
        "◆  Je tiens mon journal anti-FOMO avec précision et honnêteté.",
        "◆  Je récite le Script de Recadrage chaque fois que je rate un trade.",
        "◆  Je mesure mon succès par mon adhésion au processus, pas par mon P&L.",
    ]))
    story.append(dark_quote('"Tu ne contrôles pas le marché. Tu ne contrôles pas les mouvements. Tu contrôles une seule chose : ta réponse. Et c\'est suffisant."'))
    story.append(Spacer(1, 16))
    story.append(Paragraph('TRADING ZONE', ParagraphStyle('brand', fontName='Helvetica-Bold', fontSize=14, textColor=OR, alignment=TA_CENTER, leading=20)))
    story.append(Paragraph('Collection Le Code du Trader Élite — Ebook 1/5', ParagraphStyle('brand2', fontName='Helvetica', fontSize=10, textColor=GRIS, alignment=TA_CENTER, leading=16)))
    story.append(Paragraph('www.tradingzone.fr', ParagraphStyle('brand3', fontName='Helvetica', fontSize=10, textColor=OR, alignment=TA_CENTER, leading=16)))
    return story

# ─── MAIN ───────────────────────────────────────────────────────────────────
def build_pdf():
    from reportlab.platypus import PageBreak
    output = '01_FOMO_TRADING_ZONE.pdf'
    frame = Frame(ML, MB, CONTENT_W, PAGE_H - MT - MB, id='main')
    template = PageTemplate(id='main', frames=[frame], onPage=footer_cb)
    doc = BaseDocTemplate(output, pagesize=A4, pageTemplates=[template],
                          leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB)
    story = []
    story += build_cover()
    story.append(PageBreak())
    story += build_copyright()
    story.append(PageBreak())
    story += build_toc()
    story.append(PageBreak())
    story += build_content()
    doc.build(story)
    print(f"✓ {output} généré avec succès")

if __name__ == '__main__':
    build_pdf()
