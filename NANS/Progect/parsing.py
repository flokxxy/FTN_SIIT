# Словарь с городами и соответствующими странами
city_to_country = {
    "Paris": "France",
    "New York": "United States",
    "London": "United Kingdom",
    "Berlin": "Germany",
    "Rome": "Italy",
    "Madrid": "Spain",
    "Amsterdam": "Netherlands",
    "Vienna": "Austria",
    "Moscow": "Russia",
    "Tokyo": "Japan",
    "Beijing": "China",
   
}

def get_country_from_city(author_info):
    """
    Извлекает страну по городу, указанному в скобках у автора.
    :param author_info: строка с именем автора и дополнительной информацией (например, год и город).
    :return: название страны или 'Unknown', если город не найден.
    """
    city_match = re.search(r"\(([^,)]+)", author_info)  # Извлечение текста из скобок до первой запятой
    if city_match:
        city = city_match.group(1).strip()
        return city_to_country.get(city, "Unknown")
    return "Unknown"


def get_style_and_genre(artist_name):
    artist_info = artist_styles_genres.get(artist_name.upper())  # Преобразуем имя к верхнему регистру
    if artist_info:
        return artist_info
    else:
        return {"style": "Unknown", "genre": "Unknown"}


artist_styles_genres = {
    "ABD AL-HADI EL-GAZZAR": {"style": "Social Realism", "genre": "Figurative"},
    "ABDULHAY MUSALLAM ZARARA": {"style": "Naive Art", "genre": "Folk"},
    "ADAM HENEIN": {"style": "Modernism", "genre": "Sculptural"},
    "AHMED MATER": {"style": "Contemporary", "genre": "Conceptual"},
    "AMMAR FARHAT": {"style": "Modernism", "genre": "Figurative"},
    "AREF EL RAYESS": {"style": "Modernism", "genre": "Abstract"},
    "ASIM ABOU SHAKRA": {"style": "Modernism", "genre": "Expressionist"},
    "BAHMAN MOHASSES": {"style": "Modernism", "genre": "Surrealist"},
    "BAYA": {"style": "Folk Art", "genre": "Figurative"},
    "CHAÏBIA TALAL": {"style": "Folk Art", "genre": "Naive"},
    "DIA AL-AZZAWI": {"style": "Contemporary", "genre": "Abstract"},
    "ETEL ADNAN": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "FARID BELKAHIA": {"style": "Modernism", "genre": "Abstract"},
    "HAFIDH AL DROUBI": {"style": "Modernism", "genre": "Cubism"},
    "HAMED NADA": {"style": "Social Realism", "genre": "Figurative"},
    "HAYV KAHRAMAN": {"style": "Contemporary", "genre": "Figurative"},
    "HELEN KHAL": {"style": "Modernism", "genre": "Abstract"},
    "HUSSEIN BICAR": {"style": "Realism", "genre": "Portrait"},
    "IBRAHIM EL-SALAHI": {"style": "Modernism", "genre": "Abstract"},
    "INJI EFFLATOUN": {"style": "Social Realism", "genre": "Figurative"},
    "KAMAL BOULLATA": {"style": "Geometric Abstraction", "genre": "Abstract"},
    "LAILA SHAWA": {"style": "Contemporary", "genre": "Conceptual"},
    "MAHMOUD HAMMAD": {"style": "Modernism", "genre": "Abstract"},
    "MAHMOUD SABRI": {"style": "Social Realism", "genre": "Figurative"},
    "MAHMOUD SAÏD": {"style": "Modernism", "genre": "Figurative"},
    "MANOUCHER YEKTAI": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "MARWAN": {"style": "Modernism", "genre": "Expressionist"},
    "MOHAMED MELEHI": {"style": "Hard-edge Abstraction", "genre": "Geometric"},
    "MOHAMMED AL SALEEM": {"style": "Modernism", "genre": "Abstract"},
    "MOHAMMED CHABÂA": {"style": "Modernism", "genre": "Abstract"},
    "MOHAMMED KACIMI": {"style": "Social Realism", "genre": "Figurative"},
    "MOHAMMED SAMI": {"style": "Contemporary", "genre": "Figurative"},
    "MONIR SHAHROUDY FARMANFARMAIAN": {"style": "Geometric Abstraction", "genre": "Sculptural"},
    "PAUL GUIRAGOSSIAN": {"style": "Expressionism", "genre": "Figurative"},
    "SAFIA FARHAT": {"style": "Modernism", "genre": "Decorative"},
    "SAMIA HALABY": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "SHAFIC ABBOUD": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "SHAKER HASSAN AL SAID": {"style": "Modernism", "genre": "Abstract"},
    "SLIMAN MANSOUR": {"style": "Social Realism", "genre": "Figurative"},
    "SOHRAB SEPEHRI": {"style": "Modernism", "genre": "Minimalist"},
    "TAHIA HALIM": {"style": "Social Realism", "genre": "Figurative"},
    "YVETTE ACHKAR": {"style": "Modernism", "genre": "Abstract"},
    "ZIAD DALLOUL": {"style": "Contemporary", "genre": "Figurative"},
    "ABD AL-HADI EL-GAZZAR": {"style": "Social Realism", "genre": "Figurative"},
    "ABDELAZIZ GORGI": {"style": "Modernism", "genre": "Abstract"},
    "ABDUL HALIM RADWI": {"style": "Contemporary", "genre": "Conceptual"},
    "ABDULNASSER GHAREM": {"style": "Contemporary", "genre": "Conceptual"},
    "ADAM HENEIN": {"style": "Modernism", "genre": "Sculpture"},
    "ADHAM WANLY": {"style": "Impressionism", "genre": "Figurative"},
    "ALFRED BASBOUS": {"style": "Modernism", "genre": "Sculpture"},
    "DIA AL-AZZAWI": {"style": "Contemporary", "genre": "Abstract"},
    "EMILY JACIR": {"style": "Conceptual Art", "genre": "Photography"},
    "ETEL ADNAN": {"style": "Contemporary", "genre": "Abstract"},
    "FAHRELNISSA ZEID": {"style": "Modernism", "genre": "Abstract"},
    "FARHAD MOSHIRI": {"style": "Pop Art", "genre": "Mixed Media"},
    "GEORGES HANNA SABBAGH": {"style": "Modernism", "genre": "Figurative"},
    "HAFIDH AL-DROUBI": {"style": "Modernism", "genre": "Figurative"},
    "HAYV KAHRAMAN": {"style": "Contemporary", "genre": "Figurative"},
    "HELEN KHAL": {"style": "Modernism", "genre": "Abstract"},
    "HIMAT MOHAMMED ALI": {"style": "Contemporary", "genre": "Abstract"},
    "HUSSEIN MADI": {"style": "Modernism", "genre": "Sculpture"},
    "JAMIL MOLAEB": {"style": "Modernism", "genre": "Abstract"},
    "JULIANA SERAPHIM": {"style": "Surrealism", "genre": "Figurative"},
    "JUMANA EL HUSSEINI": {"style": "Modernism", "genre": "Abstract"},
    "LAILA SHAWA": {"style": "Contemporary", "genre": "Political Art"},
    "MAHMOUD OBAIDI": {"style": "Contemporary", "genre": "Conceptual"},
    "MAHMOUD SABRI": {"style": "Modernism", "genre": "Figurative"},
    "MANAL AL DOWAYAN": {"style": "Contemporary", "genre": "Conceptual"},
    "MARC GUIRAGOSSIAN": {"style": "Modernism", "genre": "Figurative"},
    "MARWAN": {"style": "Expressionism", "genre": "Figurative"},
    "MARWAN SAHMARANI": {"style": "Contemporary", "genre": "Figurative"},
    "MASSOUD ARABSHAHI": {"style": "Modernism", "genre": "Abstract"},
    "MOHAMMED GHANI HIKMAT": {"style": "Modernism", "genre": "Sculpture"},
    "MONIR SHAHROUDY FARMANFARMAIAN": {"style": "Modernism", "genre": "Geometric"},
    "NABIL ANANI": {"style": "Contemporary", "genre": "Figurative"},
    "NEZIHA SELIM": {"style": "Modernism", "genre": "Figurative"},
    "PAUL GUIRAGOSSIAN": {"style": "Expressionism", "genre": "Figurative"},
    "SHAKER HASSAN AL SAID": {"style": "Modernism", "genre": "Abstract"},
    "SUAD AL-ATTAR": {"style": "Surrealism", "genre": "Figurative"},
    "TAGREED DARGHOUTH": {"style": "Contemporary", "genre": "Figurative"},
    "TALA MADANI": {"style": "Contemporary", "genre": "Figurative"},
    "TIMO NASSERI": {"style": "Contemporary", "genre": "Geometric"}
}



# Словарь художников и их стран
artists_countries = {
    "ALEC EGAN": "United States",
    "ALEX GARDNER": "United States",
    "ALEX KATZ": "United States",
    "ALINA PEREZ": "United States",
    "ANDY WARHOL": "United States",
    "BRIAN CALVIN": "United States",
    "CHRIS OFILI": "United Kingdom",
    "CHUN KWANG YOUNG": "South Korea",
    "CLAIRE TABOURET": "France",
    "COSIMA VON BONIN": "Germany",
    "DAVID HAMMONS": "United States",
    "DAVID SALLE": "United States",
    "DEBORAH KASS": "United States",
    "DEBORAH ROBERTS": "United States",
    "DONALD BAECHLER": "United States",
    "DOROTHEA ROCKBURNE": "Canada",
    "ED RUSCHA": "United States",
    "ERIC FISCHL": "United States",
    "ESTEBAN VICENTE": "Spain",
    "FRANCESCO CLEMENTE": "Italy",
    "FRIEDEL DZUBAS": "Germany",
    "GENESIS TRAMAINE": "United States",
    "GEORGE CONDO": "United States",
    "HANS HOFMANN": "Germany",
    "HARLAND MILLER": "United Kingdom",
    "JAMIAN JULIANO-VILLANI": "United States",
    "JAMMIE HOLMES": "United States",
    "JAUME PLENSA": "Spain",
    "JEAN-MICHEL BASQUIAT": "United States",
    "JENNIFER GIUDI": "United States",
    "JIM DINE": "United States",
    "JOHN KACERE": "United States",
    "JOSH SMITH": "United States",
    "KATHERINE BERNHARDT": "United States",
    "KIKI SMITH": "United States",
    "LORNA SIMPSON": "United States",
    "LOUISA MATTHÍASDÓTTIR": "Iceland",
    "LYNNE DREXLER": "United States",
    "MANOLO VALDES": "Spain",
    "MARGARET KILGALLEN": "United States",
    "MEL BOCHNER": "United States",
    "MICHAEL KAGAN": "United States",
    "MICKALENE THOMAS": "United States",
    "NNENNA OKORE": "Nigeria",
    "NORMAN BLUHM": "United States",
    "PHILIP PEARLSTEIN": "United States",
    "RACHEL HARRISON": "United States",
    "RAYMOND PETTIBON": "United States",
    "REGGIE BURROWS HODGES": "United States",
    "RICHARD PETTIBONE": "United States",
    "ROMARE BEARDEN": "United States",
    "ROSS BLECKNER": "United States",
    "SAM FRANCIS": "United States",
    "SCOTT KAHN": "United States",
    "STANLEY WHITNEY": "United States",
    "STERLING RUBY": "United States",
    "THOMAS HOUSEAGO": "United Kingdom",
    "TOM WESSELMANN": "United States",
    "TOMOO GOKITA": "Japan",
    "URS FISCHER": "Switzerland",
    "WADE GUYTON": "United States",
    "WANGECHI MUTU": "Kenya",
    "WILLIAM KENTRIDGE": "South Africa",
    "ZANELE MUHOLI": "South Africa",
    "ABRAHAM WILLAERTS": "Netherlands",
    "ALBERT-ERNEST CARRIER-BELLEUSE": "France",
    "ANTHONY CLAESZ. LE JEUNE": "Netherlands",
    "ANTOINE DIEU": "France",
    "ANTONIO FRILLI": "Italy",
    "ANTONIO GARELLA": "Italy",
    "ATTRIBUÉ À CHARLES LEPEINTRE": "France",
    "ATTRIBUÉ À GIUSEPPE GAVAGNIN": "Italy",
    "ATTRIBUÉ À JACOPINO DEL CONTE": "Italy",
    "ATTRIBUÉ À ÉRASME QUELLIN LE JEUNE": "Belgium",
    "CARL AUGUST WILHELM SOMMER": "Germany",
    "CERCLE DE FRANÇOIS GIRARDON": "France",
    "CHARLES LE BRUN": "France",
    "CHARLES-ANDRÉ VAN LOO DIT CARLE VAN LOO": "France",
    "CHARLES-THÉODORE FRÈRE": "France",
    "CORNELIS CORNELISZ. VAN HAARLEM": "Netherlands",
    "D'APRÈS FRANÇOIS DUQUESNOY": "Belgium",
    "D'APRÈS FÉLIX LECOMTE": "France",
    "D'APRÈS JEAN-LOUIS LEMOYNE": "France",
    "D'APRÈS L'ANTIQUE, FIN DU XVIIIe OU XIXe SIÈCLE": "Italy",
    "D'APRÈS L'ANTIQUE, ITALIE, FIN DU XIXE OU DÉBUT DU XXE SIÈCLE": "Italy",
    "D'APRÈS LORENZO BARTOLINI": "Italy",
    "D'APRÈS TIZIANO VECELLIO, DIT TITIEN": "Italy",
    "D'APRÈS UN MODÈLE ATTRIBUÉ À SIMON DUGUET": "France",
    "DANS LE GOÛT DE JEAN-ANTOINE WATTEAU": "France",
    "DANS LE GOÛT DE L'ÉCOLE DE FRANKENTHAL": "Germany",
    "ECOLE ANVERSOISE DU XVIIe SIECLE, ATELIER DE JAN BRUEGHEL LE JEUNE": "Belgium",
    "ENTOURAGE DE FRANÇOIS BOUCHER": "France",
    "FILIPPO PALIZZI": "Italy",
    "FRANCOIS RUDE": "France",
    "FRANÇOIS BOUCHER": "France",
    "GABRIEL-FRANÇOIS DOYEN": "France",
    "GASPARE TRAVERSI": "Italy",
    "GILLIAM DANDOY": "Belgium",
    "GIOVANNI DOMENICO TIEPOLO": "Italy",
    "GIOVANNI GRUBACS": "Italy",
    "GIOVANNI PANEALBO": "Italy",
    "HENRY BOUVET": "France",
    "HUBERT ROBERT": "France",
    "JACOB ADRIAENSZ. BACKER": "Netherlands",
    "JACOBUS STORCK": "Netherlands",
    "JACOPO PALMA IL GIOVANE": "Italy",
    "JAN VAN KESSEL L'ANCIEN": "Belgium",
    "JEAN DE SAINT-IGNY": "France",
    "JEAN-BAPTISTE CARPEAUX": "France",
    "JEAN-BAPTISTE LEPRINCE": "France",
    "JEAN-HIPPOLYTE FLANDRIN": "France",
    "JEAN-HONORÉ FRAGONARD": "France",
    "JOHAN BARTHOLD JONGKIND": "Netherlands",
    "JOHN BRIDGES": "United Kingdom",
    "JOHN JAMES MASQUERIER": "United Kingdom",
    "JOOS DE MOMPER LE JEUNE": "Belgium",
    "JULIUS PORCELLIS": "Netherlands",
    "LEV TCHISTOVSKY": "Russia",
    "LOUIS DE BOULLOGNE LE JEUNE": "France",
    "LUDOVICO CARRACCI": "Italy",
    "MARCUS DE BYE": "Netherlands",
    "MARIUS-JEAN-ANTONIN MERCIÉ": "France",
    "MICHEL CORNEILLE II": "France",
    "NICOLAES ELIASZ. PICKENOY": "Netherlands",
    "NICOLAS-FRANÇOIS DUN": "France",
    "PHILIP DE LÁSZLÓ": "Hungary",
    "PIERRE ARISTIDE ANDRÉ BROUILLET": "France",
    "PIERRE GUSMAN": "France",
    "PIERRE JOSEPH WALLAERT": "France",
    "RAYMOND LAFAGE": "France",
    "RINSE VERZIJL": "Netherlands",
    "ROBERT LE VRAC DE TOURNIÈRES": "France",
    "ROSA BONHEUR": "France",
    "SIR JOSEPH EDGAR BOEHM": "United Kingdom",
    "ÉCOLE ANGLAISE DU XVIe SIÈCLE, SUIVEUR DE GEORGE GOWER": "United Kingdom",
    "ÉCOLE ESPAGNOLE DU XVIIe SIÈCLE": "Spain",
    "ÉCOLE FLAMANDE DU XVIIe SIÈCLE": "Belgium",
    "ÉCOLE FRANÇAISE DU XVIIIe SIÈCLE": "France",
    "ÉCOLE ITALIENNE DU XVIIIe SIÈCLE": "Italy",
    "ÉCOLE HOLLANDAISE DU XVIIe SIÈCLE": "Netherlands",
    "Alexander Calder": "United States",
    "Raoul Dufy": "France",
    "Moïse Kisling": "Poland",
    "Sonia Delaunay": "Ukraine",
    "ALBERT GLEIZES": "France",
    "Albert Gleizes": "France",
    "Georges Valmier": "France",
    "André Lhote": "France",
    "Auguste Herbin": "France",
    "Léopold Survage": "Russia",
    "Ossip Zadkine": "Belarus",
    "Sam Szafran": "France",
    "Marino Marini": "Italy",
    "Tamara de Lempicka": "Poland",
    "Etel Adnan": "Lebanon",
    "Karel Appel": "Netherlands",
    "František Kupka": "Czech Republic",
    "Serge Poliakoff": "Russia",
    "Marc Chagall": "Belarus",
    "Zao Wou-Ki": "China",
    "Kazuo Shiraga": "Japan",
    "Chu Teh-Chun": "China",
    "Enrico Donati": "Italy",
    "Jacqueline Lamba": "France",
    "Leonor Fini": "Argentina",
    "Pablo Picasso": "Spain",
    "D'après Pablo Picasso": "Spain",
    "Henri Matisse": "France",
    "Egon Schiele": "Austria",
    "Joan Miró": "Spain",
    "Anselm Kiefer": "Germany",
    "Michel Parmentier": "France",
    "Simon Hantaï": "Hungary",
    "Helmut Newton": "Germany",
    "Antonio Saura": "Spain",
    "Antoni Tàpies": "Spain",
    "Paul Delvaux": "Belgium",
    "Jean Dubuffet": "France",
    "Günther Förg": "Germany",
    "Gérard Schneider": "Switzerland",
    "Hans Hartung": "Germany",
    "Maria Helena Vieira da Silva": "Portugal",
    "Bernard Buffet": "France",
    "Henri Laurens": "France",
    "Félix Vallotton": "Switzerland",
    "Bernard Frize": "France",
    "Josef Albers": "Germany",
    "Victor Vasarely": "Hungary",
    "Carlos Cruz-Diez": "Venezuela",
    "Alighiero Boetti": "Italy",
    "Mimmo Rotella": "Italy",
    "Mario Schifano": "Italy",
    "Luciano Fabro": "Italy",
    "Vettor Pisani": "Italy",
    "Mario Merz": "Italy",
    "Giuseppe Penone": "Italy",
    "Gilberto Zorio": "Italy",
    "Jannis Kounellis": "Greece",
    "Giovanni Anselmo": "Italy",
    "Emilio Prini": "Italy",
    "Fausto Melotti": "Italy",
    "Philippe Hiquily": "France",
    "ALBRECHT DÜRER": "Germany",
    "ANTHONY VAN DYCK": "Flanders (modern Belgium)",
    "ANTONIO CANAL, CALLED CANALETTO": "Italy",
    "ARSHILE GORKY": "Armenia / United States",
    "AUGUSTIN HIRSCHVOGEL": "Germany",
    "BENTON M. SPRUANCE": "United States",
    "BERNARDO BELLOTTO": "Italy",
    "BLANCHE LAZZELL": "United States",
    "BROR JULIUS OLSSON NORDFELDT": "United States",
    "CAMILLE PISSARRO": "France",
    "CHARLES MERYON": "France",
    "CHARLES SHEELER": "United States",
    "CHILDE HASSAM": "United States",
    "CHRISTOFFEL JEGHER AFTER PETER PAUL RUBENS": "Flanders (modern Belgium)",
    "CLARE LEIGHTON": "England",
    "DIEGO RIVERA": "Mexico",
    "EDGAR DEGAS": "France",
    "EDVARD MUNCH": "Norway",
    "EDWARD HOPPER": "United States",
    "ELIZABETH CATLETT": "United States",
    "EMIL NOLDE": "Germany",
    "ERICH HECKEL": "Germany",
    "ERNST LUDWIG KIRCHNER": "Germany",
    "ETHEL MARS": "United States",
    "FRANCES H. GEARHART": "United States",
    "FRANCISCO DE GOYA Y LUCIENTES": "Spain",
    "FÉLIX BRACQUEMOND": "France",
    "FÉLIX VALLOTTON": "Switzerland",
    "GEORGE WESLEY BELLOWS": "United States",
    "GEORGES BRAQUE": "France",
    "GIOVANNI BATTISTA TIEPOLO": "Italy",
    "GUSTAVE BAUMANN": "United States",
    "HANNS LAUTENSACK": "Germany",
    "HEINRICH CAMPENDONCK": "Germany",
    "HENDRICK GOLTZIUS": "Netherlands",
    "HENDRIK GOUDT AFTER ADAM ELSHEIMER": "Netherlands / Germany",
    "HENRI DE TOULOUSE-LAUTREC": "France",
    "HENRI MATISSE": "France",
    "HONORÉ DAUMIER": "France",
    "HOWARD COOK": "United States",
    "JACQUES BELLANGE": "France",
    "JACQUES CALLOT": "France",
    "JACQUES VILLON": "France",
    "JAMES ABBOTT MCNEILL WHISTLER": "United States / United Kingdom",
    "JAN MATULKA": "United States",
    "JEAN DUVET": "France",
    "JOAN MIRÓ": "Spain",
    "JOANNES VAN DOETECUM THE ELDER AND LUCAS VAN DOETECUM AFTER PIETER BRUEGEL THE ELDER": "Netherlands",
    "JOHN MARIN": "United States",
    "JOHN SINGER SARGENT": "United States",
    "JOHN STEUART CURRY": "United States",
    "KARL SCHMIDT-ROTTLUFF": "Germany",
    "KÄTHE KOLLWITZ": "Germany",
    "LOUIS LOZOWICK": "United States",
    "LUCAS VAN LEYDEN": "Netherlands",
    "LYONEL FEININGER": "United States / Germany",
    "MABEL HEWIT": "United States",
    "MARC CHAGALL": "Belarus / France",
    "MARTIN LEWIS": "United States",
    "MARTIN SCHONGAUER": "Germany",
    "MAURICE BRAZIL PRENDERGAST": "United States",
    "MAX BECKMANN": "Germany",
    "ODILON REDON": "France",
    "PABLO PICASSO": "Spain",
    "PAUL KLEE": "Switzerland / Germany",
    "PETER PAUL RUBENS": "Flanders (modern Belgium)",
    "PIERRE BONNARD": "France",
    "RAPHAEL SOYER": "United States",
    "REGINALD MARSH": "United States",
    "REMBRANDT HARMENSZ. VAN RIJN": "Netherlands",
    "RODOLPHE BRESDIN": "France",
    "SAMUEL MARGOLIES": "United States",
    "STOW WENGENROTH": "United States",
    "STUART DAVIS": "United States",
    "THOMAS GAINSBOROUGH": "England",
    "THOMAS HART BENTON": "United States",
    "WINSLOW HOMER": "United States",
    "ÉDOUARD MANET": "France",
    "ABD AL-HADI EL-GAZZAR": "Egypt",
    "ABDULHAY MUSALLAM ZARARA": "Palestine",
    "ADAM HENEIN": "Egypt",
    "AHMED MATER": "Saudi Arabia",
    "AMMAR FARHAT": "Tunisia",
    "AREF EL RAYESS": "Lebanon",
    "ASIM ABOU SHAKRA": "Israel/Palestine",
    "BAHMAN MOHASSES": "Iran",
    "BAYA": "Algeria",
    "CHAÏBIA TALAL": "Morocco",
    "DIA AL-AZZAWI": "Iraq",
    "ETEL ADNAN": "Lebanon",
    "FARID BELKAHIA": "Morocco",
    "HAFIDH AL DROUBI": "Iraq",
    "HAMED NADA": "Egypt",
    "HAYV KAHRAMAN": "Iraq",
    "HELEN KHAL": "Lebanon",
    "HUSSEIN BICAR": "Egypt",
    "IBRAHIM EL-SALAHI": "Sudan",
    "INJI EFFLATOUN": "Egypt",
    "KAMAL BOULLATA": "Palestine",
    "LAILA SHAWA": "Palestine",
    "MAHMOUD HAMMAD": "Syria",
    "MAHMOUD SABRI": "Iraq",
    "MAHMOUD SAÏD": "Egypt",
    "MANOUCHER YEKTAI": "Iran",
    "MARWAN": "Syria",
    "MOHAMED MELEHI": "Morocco",
    "MOHAMMED AL SALEEM": "Saudi Arabia",
    "MOHAMMED CHABÂA": "Morocco",
    "MOHAMMED KACIMI": "Morocco",
    "MOHAMMED SAMI": "Iraq",
    "MONIR SHAHROUDY FARMANFARMAIAN": "Iran",
    "PAUL GUIRAGOSSIAN": "Lebanon",
    "SAFIA FARHAT": "Tunisia",
    "SAMIA HALABY": "Palestine",
    "SHAFIC ABBOUD": "Lebanon",
    "SHAKER HASSAN AL SAID": "Iraq",
    "SLIMAN MANSOUR": "Palestine",
    "SOHRAB SEPEHRI": "Iran",
    "TAHIA HALIM": "Egypt",
    "YVETTE ACHKAR": "Lebanon",
    "ZIAD DALLOUL": "Syria",
    "ABD AL-HADI EL-GAZZAR": "Egypt",
    "ABDELAZIZ GORGI": "Tunisia",
    "ABDUL HALIM RADWI": "Saudi Arabia",
    "ABDULNASSER GHAREM": "Saudi Arabia",
    "ADAM HENEIN": "Egypt",
    "ADHAM WANLY": "Egypt",
    "ALFRED BASBOUS": "Lebanon",
    "DIA AL-AZZAWI": "Iraq",
    "EMILY JACIR": "Palestine",
    "ETEL ADNAN": "Lebanon",
    "FAHRELNISSA ZEID": "Turkey",
    "FARHAD MOSHIRI": "Iran",
    "GEORGES HANNA SABBAGH": "Lebanon",
    "HAFIDH AL-DROUBI": "Iraq",
    "HAYV KAHRAMAN": "Iraq",
    "HELEN KHAL": "Lebanon",
    "HIMAT MOHAMMED ALI": "Iraq",
    "HUSSEIN MADI": "Lebanon",
    "JAMIL MOLAEB": "Lebanon",
    "JULIANA SERAPHIM": "Lebanon",
    "JUMANA EL HUSSEINI": "Palestine",
    "LAILA SHAWA": "Palestine",
    "MAHMOUD OBAIDI": "Iraq",
    "MAHMOUD SABRI": "Iraq",
    "MANAL AL DOWAYAN": "Saudi Arabia",
    "MARC GUIRAGOSSIAN": "Lebanon",
    "MARWAN": "Syria",
    "MARWAN SAHMARANI": "Lebanon",
    "MASSOUD ARABSHAHI": "Iran",
    "MOHAMMED GHANI HIKMAT": "Iraq",
    "MONIR SHAHROUDY FARMANFARMAIAN": "Iran",
    "NABIL ANANI": "Palestine",
    "NEZIHA SELIM": "Iraq",
    "PAUL GUIRAGOSSIAN": "Lebanon",
    "SHAKER HASSAN AL SAID": "Iraq",
    "SUAD AL-ATTAR": "Iraq",
    "TAGREED DARGHOUTH": "Lebanon",
    "TALA MADANI": "Iran",
    "TIMO NASSERI": "Iran"
}


# Добавление жанра по ключевым словам
def extract_genre(description):
    genre_keywords = {
       "portrait": "Portrait",
        "self-portrait": "Self-Portrait",
        "landscape": "Landscape",
        "seascape": "Seascape",
        "abstract": "Abstract",
        "still life": "Still Life",
        "figurative": "Figurative",
        "conceptual": "Conceptual",
        "modern": "Modern Art",
        "contemporary": "Contemporary Art",
        "historical": "Historical",
        "religious": "Religious Art",
        "mythological": "Mythological",
        "nude": "Nude",
        "cubism": "Cubism",
        "impressionism": "Impressionism",
        "expressionism": "Expressionism",
        "pop art": "Pop Art",
        "surrealism": "Surrealism",
        "minimalism": "Minimalism",
        "baroque": "Baroque",
        "renaissance": "Renaissance",
        "romanticism": "Romanticism",
        "symbolism": "Symbolism",
        "abstract expressionism": "Abstract Expressionism",
        "realism": "Realism",
        "fauvism": "Fauvism",
        "photography": "Photography",
        "installation": "Installation",
        "video art": "Video Art",
    
    }

    for keyword, genre in genre_keywords.items():
        if keyword in description.lower():
            return genre
    return "Unknown"  # Если жанр не удалось определить

def extract_style(description):
    style_keywords = {
        "cubism": "Cubism",
        "impressionism": "Impressionism",
        "expressionism": "Expressionism",
        "pop art": "Pop Art",
        "surrealism": "Surrealism",
        "minimalism": "Minimalism",
        "baroque": "Baroque",
        "renaissance": "Renaissance",
        "romanticism": "Romanticism",
        "abstract expressionism": "Abstract Expressionism",
        "realism": "Realism",
        "fauvism": "Fauvism",
        "modern": "Modern Art",
        "contemporary": "Contemporary Art",
        "symbolism": "Symbolism",
        "conceptual": "Conceptual Art",
        "neoclassicism": "Neoclassicism",
        "art deco": "Art Deco",
        "art nouveau": "Art Nouveau",
        "post-impressionism": "Post-Impressionism",
        "figurative": "Figurative Art",
        "classicism": "Classicism",
        "gothic": "Gothic",
        "constructivism": "Constructivism",
    }

    for keyword, style in style_keywords.items():
        if keyword in description.lower():
            return style
    return "Unknown"  # Если стиль не удалось определить

# Функция для конвертации размеров в сантиметры
def convert_to_cm(dimensions):
    try:
        match = re.match(r"([\d.,]+)\s*x\s*([\d.,]+)\s*(mm|cm|in)", dimensions, re.IGNORECASE)
        if match:
            width, height, unit = match.groups()
            width = float(width.replace(",", "."))
            height = float(height.replace(",", "."))
            if unit.lower() == "mm":
                # Конвертируем миллиметры в сантиметры
                width /= 10
                height /= 10
            elif unit.lower() == "in":
                # Конвертируем дюймы в сантиметры (1 дюйм = 2.54 см)
                width *= 2.54
                height *= 2.54
            # Возвращаем строку в формате "ширина x высота см"
            return f"{width:.1f} x {height:.1f} cm"
        else:
            return "Размер не найден"
    except Exception as e:
        return "Ошибка конвертации"



# import json
# import re
# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.edge.service import Service

# edge_options = Options()
# # edge_options.add_argument("--headless")

# driver_path = "D:\\project on python\\msedgedriver.exe"
# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=edge_options)

# url = "https://www.christies.com/en/auction/british-and-european-art-29994/browse-lots"
# driver.get(url)

# driver.implicitly_wait(10)

# scripts = driver.find_elements(By.TAG_NAME, "script")
# lots_json = None

# for script in scripts:
#     text = script.get_attribute("innerHTML")
#     if "window.chrComponents.lots" in text:
#         match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", text, re.DOTALL)
#         if match:
#             json_str = match.group(1)
#             lots_data = json.loads(json_str)
#             lots_json = lots_data["data"]["lots"]
#         break

# if not lots_json:
#     print("Не удалось найти данные о лотах.")
#     driver.quit()
#     exit()

# results = []
# for lot in lots_json:
#     artist = lot.get("title_primary_txt", "")
#     title = lot.get("title_secondary_txt", "")
#     price = lot.get("price_realised_txt", "")
#     estimate = lot.get("estimate_txt", "")
#     description = lot.get("description_txt", "")

#     # Удаляем все содержимое в скобках из имени художника
#     # Например, было: "GUSTAVE COURBET (FRENCH, 1819-1877)"
#     # Станет: "GUSTAVE COURBET"
#     artist_clean = re.sub(r"\([^)]*\)", "", artist).strip()

#     # Парсинг страны и периода из имени художника.
#     # Формат ожидается: ARTIST NAME (COUNTRY, YYYY-YYYY)
#     country = ""
#     period = ""
#     style = extract_style(description)
#     genre = extract_genre(description)
#     artist_match = re.search(r"\(([^,]+),\s*([^)]+)\)", artist)
#     if artist_match:
#         country = artist_match.group(1).strip()
#         period = artist_match.group(2).strip()

#     lines = description.split("<br>")
#     material = ""
#     dimensions = ""
#     for l in lines:
#         line = l.strip()
#         # Ищем материал
#         if "oil on" in line.lower() or "watercolor" in line.lower() or "bronze" in line.lower():
#             material = line

#         # Ищем размеры в см
#         cm_match = re.search(r"\(([\d.,]+)\s*x\s*([\d.,]+)\s*cm\.\)", line)
#         if cm_match:
#             width_cm = cm_match.group(1)
#             height_cm = cm_match.group(2)
#             dimensions = f"{width_cm} x {height_cm} cm"

#     results.append({
#         "название": title,
#         "имя_художника": artist_clean ,
#         "стоимость": price,
#         "примерная_оценка": estimate,
#         "материал": material,
#         "размер": dimensions,
#         "страна": country,    
#         "период": period,    
#         "стиль": "Realism", 
#         "жанр": genre    
#     })

# driver.quit()

# # Записываем в CSV
# csv_file = "British and European Art_14dec.csv"
# fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль", "жанр"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     # Используем точку с запятой как разделитель полей
#     # Отключаем кавычки вовсе
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writeheader()
#     writer.writerows(results)


# print(f"Данные сохранены в {csv_file}")

#-----------------------------------------------------------------------------

# import json
# import re
# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.edge.service import Service

# edge_options = Options()
# # edge_options.add_argument("--headless")

# driver_path = "D:\\project on python\\msedgedriver.exe"
# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=edge_options)

# url = "https://www.christies.com/en/auction/the-sam-josefowitz-collection-graphic-masterpieces-by-rembrandt-van-rijn-part-ii-30288/?page=2&sortby=lotnumber"
# driver.get(url)

# driver.implicitly_wait(10)

# scripts = driver.find_elements(By.TAG_NAME, "script")
# lots_json = None

# for script in scripts:
#     text = script.get_attribute("innerHTML")
#     if "window.chrComponents.lots" in text:
#         match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", text, re.DOTALL)
#         if match:
#             json_str = match.group(1)
#             lots_data = json.loads(json_str)
#             lots_json = lots_data["data"]["lots"]
#         break

# if not lots_json:
#     print("Не удалось найти данные о лотах.")
#     driver.quit()
#     exit()


# results = []
# for lot in lots_json:
#     artist = lot.get("title_primary_txt", "")
#     title = lot.get("title_secondary_txt", "")
#     price = lot.get("price_realised_txt", "")
#     estimate = lot.get("estimate_txt", "")
#     description = lot.get("description_txt", "")

#     # Извлекаем период из скобок
#     period = ""
#     period_match = re.search(r"\(([^)]+)\)", artist)
#     if period_match:
#         period = period_match.group(1).strip()

#     # Удаляем скобки с периодом из имени художника
#     artist_clean = re.sub(r"\([^)]*\)", "", artist).strip()

#     # Страна отсутсвует
#     country = ""
#     dimensions = ""

#     lines = description.split("<br>")


#     for l in lines:
#         line = l.strip()
#          # Ищем материал
#         if "oil on" in line.lower() or "watercolor" in line.lower() or "bronze" in line.lower():
#              material = line
#     # Ищем размеры в см
#         if re.search(r"\d+\s*x\s*\d+", l):
#             dimensions = l.strip()

    

#     results.append({
#         "название": title,
#         "имя_художника": artist_clean,
#         "стоимость": price,
#         "примерная_оценка": estimate,
#         "материал": "",   # Если нужно, добавьте логику определения материала
#         "размер": dimensions,
#         "страна": "",
#         "период": period,
#         "стиль": "Graphic",
#         "жанр": "Portrait"
        
#     })

# driver.quit()

# # Записываем в CSV без кавычек
# csv_file = "Graphic Masterpieces by Rembrandt van Rijn - Part II.csv"
# fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль","жанр"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     # Используем точку с запятой как разделитель полей, без кавычек
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writeheader()
#     writer.writerows(results)

# print(f"Данные сохранены в {csv_file}")




#---------------------------------------------------------------
# import requests
# import re
# import json
# import csv

# # URL страницы
# url = "https://www.christies.com/en/auction/fine-chinese-modern-and-contemporary-ink-paintings-30363?page=3&sortby=lotnumber"

# # Заголовки для запроса
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
# }

# # Отправляем запрос
# response = requests.get(url, headers=headers)

# # Проверяем статус ответа
# if response.status_code != 200:
#     print(f"Ошибка: сервер вернул статус {response.status_code}")
#     exit()

# # Ищем JSON в HTML-коде
# match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", response.text, re.DOTALL)
# if match:
#     json_str = match.group(1)
#     lots_data = json.loads(json_str).get("data", {}).get("lots", [])
# else:
#     print("Не удалось найти JSON-данные в HTML.")
#     exit()

# # Обрабатываем данные
# results = []
# for lot in lots_data:
#     title = lot.get("title_secondary_txt", "")
#     artist = lot.get("title_primary_txt", "")
#     price = lot.get("price_realised_txt", "")
#     estimate = lot.get("estimate_txt", "")
#     description = lot.get("description_txt", "")

#     # Извлечение периода из имени художника
#     period = ""
#     artist_clean = artist
#     artist_match = re.search(r"\(([^)]+)\)", artist)
#     if artist_match:
#         artist_clean = artist[:artist_match.start()].strip()
#         period = artist_match.group(1).strip()


#     # Парсинг размера
#     dimensions = ""
#     dimension_match = re.search(r"(\d+\.?\d*)\s*x\s*(\d+\.?\d*)\s*cm", description, re.IGNORECASE)
#     if dimension_match:
#         dimensions = f"{dimension_match.group(1)} x {dimension_match.group(2)} cm"

#     results.append({
#         "название": title,
#         "имя_художника": artist_clean,
#         "стоимость": price,
#         "примерная_оценка": estimate,
#         "материал": "",  # Можно доработать для извлечения материала
#         "размер": dimensions,
#         "страна": "Китай",  # Страна фиксированная
#         "период": period,
#         "стиль": "Traditional Chinese Style",  # Фиксированный стиль
#         "жанр": "Traditional Chinese Painting" 
#     })

# # Записываем в CSV
# csv_file = "Fine_Chinese_Modern_and_Contemporary_Ink_Paintings.csv"
# fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль","жанр"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writeheader()
#     writer.writerows(results)

# print(f"Данные сохранены в {csv_file}")





#------------------------------------------------------------------------

# import requests
# import re
# import json
# import csv

# # URL страницы
# url = "https://onlineonly.christies.com/s/exquisite-eye-chinese-paintings-online/lots/3828?page=2&sortby=LotNumber"

# # Заголовки для HTTP-запроса
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
# }

# # Отправляем запрос к странице
# response = requests.get(url, headers=headers)

# if response.status_code != 200:
#     print(f"Ошибка загрузки страницы: {response.status_code}")
#     exit()

# # Ищем скрипт с JSON-данными на странице
# page_content = response.text
# match = re.search(r"window\.chrComponents\s*=\s*(\{.*?\});", page_content, re.DOTALL)

# if not match:
#     print("Не удалось найти данные о лотах на странице.")
#     exit()

# # Извлекаем JSON-данные
# json_str = match.group(1)
# chr_components = json.loads(json_str)

# # Проверяем наличие данных о лотах
# lots_data = chr_components.get("lots", {}).get("data", {}).get("lots", [])
# if not lots_data:
#     print("Данные о лотах отсутствуют в JSON.")
#     exit()

# # Обрабатываем данные
# results = []
# for lot in lots_data:
#     title = lot.get("title_secondary_txt", "")
#     artist = lot.get("title_primary_txt", "")
#     price = lot.get("price_realised_txt", "")
#     estimate = lot.get("estimate_txt", "")
#     description = lot.get("description_txt", "")

#     # Удаление HTML-тегов из описания
#     description_clean = re.sub(r"<.*?>", " ", description)

#     # Извлечение размера
#     size_match = re.search(r"([\d.,]+ x [\d.,]+ cm)", description_clean)
#     size = size_match.group(1) if size_match else ""

#     # Извлечение страны и периода из имени художника
#     country = "CHINA"
#     period = ""
#     artist_clean = re.sub(r"<.*?>", " ", artist)
#     artist_name = artist_clean.strip()
#     artist_match = re.search(r"(.*?)\(([^,]+)\)", artist_clean)
#     if artist_match:
#         artist_name = artist_match.group(1).strip()  # Имя автора
#         period = artist_match.group(2).strip()  # Период
    

#     results.append({
#         "Название": title,
#         "Имя художника": artist_name,
#         "Стоимость": price,
#         "Примерная оценка": estimate,
#         "Размер": size,
#         "Страна": country,
#         "Период": period,
#         "Стиль": "Traditional Chinese Art"
#     })

# # Записываем в CSV
# csv_file = "Exquisite_Eye_hinese_Paintings.csv"
# fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Размер", "Страна", "Период","Стиль"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writeheader()
#     writer.writerows(results)

# print(f"Данные сохранены в {csv_file}")


#-----------------------------------------------------------------------------------------


# import requests
# import re
# import json
# import csv

# # URL страницы
# url = "https://www.christies.com/en/auction/vivre-la-couleur-hommage-jean-fournier-30660/"

# # Заголовки для HTTP-запроса
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
# }

# # Отправляем запрос к странице
# response = requests.get(url, headers=headers)

# if response.status_code != 200:
#     print(f"Ошибка загрузки страницы: {response.status_code}")
#     exit()

# # Ищем скрипт с JSON-данными на странице
# page_content = response.text
# match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", page_content, re.DOTALL)

# if not match:
#     print("Не удалось найти данные о лотах на странице.")
#     exit()

# # Извлекаем JSON-данные
# json_str = match.group(1)
# chr_components = json.loads(json_str)

# # Проверяем наличие данных о лотах
# lots_data = chr_components.get("data", {}).get("lots", [])
# if not lots_data:
#     print("Данные о лотах отсутствуют в JSON.")
#     exit()

# # Обрабатываем данные
# results = []
# for lot in lots_data:
#     title = lot.get("title_secondary_txt", "").strip()  # Название произведения
#     artist = lot.get("title_primary_txt", "").strip()   # Имя художника
#     price = lot.get("price_realised_txt", "").strip()   # Стоимость
#     estimate = lot.get("estimate_txt", "").strip()      # Примерная оценка
#     description = lot.get("description_txt", "").strip()  # Описание

#     # Извлечение периода из имени художника
#     period = ""
#     artist_clean = artist
#     artist_match = re.search(r"\(([^)]+)\)", artist)
#     if artist_match:
#         artist_clean = artist[:artist_match.start()].strip()
#         period = artist_match.group(1).strip()
#     # Удаляем фразы "né en" и другие ненужные выражения
#         period = re.sub(r"né en\s*", "", period, flags=re.IGNORECASE)
#         period = period.strip()

#         style = extract_style(description)
#         genre = extract_genre(description)

    
#      # Извлечение размера
#     dimensions = ""
#     description_match = re.search(r"(\d+\s*x\s*\d+\s*cm)", description, re.IGNORECASE)
#     if not description_match:
#         description_match = re.search(r"\((\d+\s*x\s*\d+\s*cm)\)", description, re.IGNORECASE)
#         if not description_match:
#             description_match = re.search(r"(\d+\s*x\s*\d+\s*in)", description, re.IGNORECASE)
#     if description_match:
#         dimensions = description_match.group(1)

#     # Извлечение материала
#     material = ""
#     material_match = re.search(r"(oil on canvas|acrylic|mixed media|gouache|watercolor|bronze)", description, re.IGNORECASE)
#     if material_match:
#         material = material_match.group(1).capitalize()

#     results.append({
#         "название": title,
#         "имя_художника": artist_clean,
#         "стоимость": price,
#         "примерная_оценка": estimate,
#         "материал": material,
#         "размер": dimensions,
#         "страна": "FRENCH",  # Можно добавить логику извлечения
#         "период": period,
#         "стиль": "Abstractus",
#         "жанр": genre
#     })

# # Записываем в CSV
# csv_file = "Vivre_la_couleur.csv"
# fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль", "жанр"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writeheader()
#     writer.writerows(results)

# print(f"Данные сохранены в {csv_file}")

#-----------------------------------------------------------------------------------

# import requests
# import re
# import json
# import csv

# # URL страницы
# url = "https://www.christies.com/en/auction/old-masters-part-i-30289/"

# # Заголовки для HTTP-запроса
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
# }

# # Отправляем запрос к странице
# response = requests.get(url, headers=headers)

# if response.status_code != 200:
#     print(f"Ошибка загрузки страницы: {response.status_code}")
#     exit()

# # Ищем скрипт с JSON-данными на странице
# page_content = response.text
# match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", page_content, re.DOTALL)

# if not match:
#     print("Не удалось найти данные о лотах на странице.")
#     exit()

# # Извлекаем JSON-данные
# json_str = match.group(1)
# chr_components = json.loads(json_str)

# # Проверяем наличие данных о лотах
# lots_data = chr_components.get("data", {}).get("lots", [])
# if not lots_data:
#     print("Данные о лотах отсутствуют в JSON.")
#     exit()

# # Обрабатываем данные
# results = []
# for lot in lots_data:
#     title = lot.get("title_secondary_txt", "").strip()  # Название произведения
#     artist = lot.get("title_primary_txt", "").strip()   # Имя художника
#     price = lot.get("price_realised_txt", "").strip()   # Стоимость
#     estimate = lot.get("estimate_txt", "").strip()      # Примерная оценка
#     description = lot.get("description_txt", "").strip()  # Описание

#     # Извлечение периода из имени художника
#     period = ""
#     artist_clean = artist
#     artist_match = re.search(r"\(([^)]+)\)", artist)
#     if artist_match:
#         artist_clean = artist[:artist_match.start()].strip()
#         period = artist_match.group(1).strip()
#     # Удаляем фразы "né en" и другие ненужные выражения
#         period = re.sub(r"né en\s*", "", period, flags=re.IGNORECASE)
#         period = period.strip()

    
#      # Извлечение размера
#     dimensions = ""
#     description_match = re.search(r"(\d+\s*x\s*\d+\s*cm)", description, re.IGNORECASE)
#     if not description_match:
#         description_match = re.search(r"\((\d+\s*x\s*\d+\s*cm)\)", description, re.IGNORECASE)
#         if not description_match:
#             description_match = re.search(r"(\d+\s*x\s*\d+\s*in)", description, re.IGNORECASE)
#     if description_match:
#         dimensions = description_match.group(1)

#     # Извлечение материала
#     material = ""
#     material_match = re.search(r"(oil on canvas|acrylic|mixed media|gouache|watercolor|bronze)", description, re.IGNORECASE)
#     if material_match:
#         material = material_match.group(1).capitalize()

#     results.append({
#         "название": title,
#         "имя_художника": artist_clean,
#         "стоимость": price,
#         "примерная_оценка": estimate,
#         "материал": material,
#         "размер": dimensions,
#         "страна": "",  # Можно добавить логику извлечения
#         "период": period,
#         "стиль": "Abstractus",
#         "жанр": "религиозная живопись"
#     })

# # Записываем в CSV
# csv_file = "Old_Masters_Part_I.csv"
# fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль", "жанр"]

# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
#     writer.writeheader()
#     writer.writerows(results)

# print(f"Данные сохранены в {csv_file}")


#--------------------------------------------------------------------------


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import re
# import json
# import csv



# # Путь к WebDriver
# driver_path = "D:\\project on python\\msedgedriver.exe"  # Укажите путь к вашему WebDriver

# # Настройка WebDriver
# edge_options = Options()
# edge_options.add_argument("--headless")  # Запуск в фоновом режиме
# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=edge_options)

# # URL страницы
# url = "https://onlineonly.christies.com/s/first-open-post-war-contemporary-art/lots/3847?page=5&sortby=LotNumber"

# try:
#     # Загружаем страницу
#     driver.get(url)

#     # Ищем все скрипты на странице
#     scripts = driver.find_elements(By.TAG_NAME, "script")

#     lot_data = None

#     # Ищем JSON с лотами в скриптах
#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents" in script_content:
#             match = re.search(r"window\.chrComponents\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_str = match.group(1)
#                 lot_data = json.loads(json_str)
#             break

#     if not lot_data:
#         print("Не удалось найти данные о лотах.")
#         exit()

#     # Извлекаем информацию о лотах
#     lots = lot_data.get("lots", {}).get("data", {}).get("lots", [])
#     if not lots:
#         print("Данные о лотах отсутствуют в JSON.")
#         exit()


#     results = []
#     for lot in lots:
#         title = lot.get("title_secondary_txt", "N/A")
#         artist = lot.get("title_primary_txt", "N/A")
#         price_realised = lot.get("price_realised_txt", "N/A")
#         estimate = lot.get("estimate_txt", "N/A")
#         description = lot.get("description_txt", "")

#          # Извлекаем размер из описания
#         dimensions_match = re.search(r"\(([\d.,]+\s*x\s*[\d.,]+\s*cm\.)\)", description)
#         dimensions = dimensions_match.group(1) if dimensions_match else "N/A"

#         material = re.search(r"(oil on canvas|acrylic|mixed media|gouache|watercolor|bronze)", lot.get("description_txt", ""), re.IGNORECASE)
#         material = material.group(1) if material else "N/A"

#     # Удаляем любые скобки с содержимым (например, годы жизни художника)
#         artist_clean = re.sub(r"\([^)]*\)", "", artist).strip()

#         # Получаем страну из словаря
#         artist_clean = artist.split("(")[0].strip().upper()  # Убираем возможные скобки и переводим в верхний регистр
#         country = artists_countries.get(artist_clean, "Unknown")

#         period_match = re.search(r"\(([^)]+)\)", artist)
#         period = period_match.group(1) if period_match else "N/A"
        
#         # Добавляем жанр и стиль
#         # Определяем жанр
#         genre = extract_genre(description)
#         #genre = "Contemporary Art"  # Пример жанра (можно заменить на логику извлечения)
#         style = "Contemporary Art"  
#         #style = extract_style(description)

#         results.append({
#             "название": title,
#             "имя_художника": artist_clean,
#             "стоимость": price_realised,
#             "примерная_оценка": estimate,
#             "материал": material,
#             "размер": dimensions,
#             "страна": country,
#             "период": period,
#             "стиль": style,
#             "жанр": genre
#         })


#     # Сохраняем результаты в CSV
#     csv_file = "Post-War_and_Contemporary_Art.csv"
#     fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль", "жанр"]

#     with open(csv_file, "w", newline="", encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(results)

#     print(f"Данные успешно сохранены в {csv_file}")


# finally:
#     driver.quit()

# -------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import re
# import json
# import csv



# # Путь к WebDriver
# driver_path = "D:\\project on python\\msedgedriver.exe"  # Укажите путь к вашему WebDriver

# # Настройка WebDriver
# edge_options = Options()
# edge_options.add_argument("--headless")  # Запуск в фоновом режиме
# edge_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")


# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=edge_options)

# # URL страницы
# url = "https://onlineonly.christies.com/s/maitres-anciens-peintures-dessins-sculptures-online/lots/3527?page=2&sortby=LotNumber"

# try:
#     #Загружаем страницу
#     driver.get(url)

#     # Ищем все скрипты на странице
#     scripts = driver.find_elements(By.TAG_NAME, "script")

#     lot_data = None

#     # Ищем JSON с лотами в скриптах
#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents" in script_content:
#             match = re.search(r"window\.chrComponents\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_str = match.group(1)
#                 lot_data = json.loads(json_str)
#             break

#     if not lot_data:
#         print("Не удалось найти данные о лотах.")
#         exit()

#     # Извлекаем информацию о лотах
#     lots = lot_data.get("lots", {}).get("data", {}).get("lots", [])
#     if not lots:
#         print("Данные о лотах отсутствуют в JSON.")
#         exit()



#     results = []
#     for lot in lots:
#         title = lot.get("title_secondary_txt", "N/A")
#         artist = lot.get("title_primary_txt", "N/A")
#         price_realised = lot.get("price_realised_txt", "N/A")
#         estimate = lot.get("estimate_txt", "N/A")
#         description = lot.get("description_txt", "")

#          # Извлекаем размер из описания
#         dimensions_match = re.search(r"([\d.,]+\s*x\s*[\d.,]+\s*cm)", description)
#         dimensions = dimensions_match.group(1) if dimensions_match else "N/A"

#         material = re.search(r"(oil on canvas|acrylic|mixed media|gouache|watercolor|bronze)", lot.get("description_txt", ""), re.IGNORECASE)
#         material = material.group(1) if material else "N/A"

#     # Удаляем любые скобки с содержимым (например, годы жизни художника)
#         artist_clean = re.sub(r"\([^)]*\)", "", artist).strip()

#         # Получаем страну из словаря
#         artist_clean = artist.split("(")[0].strip().upper()  # Убираем возможные скобки и переводим в верхний регистр
#         country = artists_countries.get(artist_clean, "Unknown")

#         period_match = re.search(r"\(([^)]+)\)", artist)
#         period = period_match.group(1) if period_match else "N/A"
        
#         # Добавляем жанр и стиль
#         style = extract_style(description)
#         genre = extract_genre(description)  

#         results.append({
#             "название": title,
#             "имя_художника": artist_clean,
#             "стоимость": price_realised,
#             "примерная_оценка": estimate,
#             "материал": material,
#             "размер": dimensions,
#             "страна": country,
#             "период": period,
#             "стиль": style,
#             "жанр": genre
#         })


#     # Сохраняем результаты в CSV
#     csv_file = "Maîtres_Anciens.csv"
#     fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль", "жанр"]

#     with open(csv_file, "w", newline="", encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(results)

#     print(f"Данные успешно сохранены в {csv_file}")



# finally:
#     driver.quit()


##############################################################################################################

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import re
# import json



# # Путь к WebDriver
# driver_path = "D:\\project on python\\msedgedriver.exe"  # Укажите путь к вашему WebDriver

# # Настройка WebDriver
# edge_options = Options()
# edge_options.add_argument("--headless")  # Запуск в фоновом режиме
# edge_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")
# edge_options.add_argument("--disable-blink-features=AutomationControlled")

# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=edge_options)

# # URL страницы
# url = "https://onlineonly.christies.com/s/maitres-anciens-peintures-dessins-sculptures-online/lots/3527?page=2&sortby=LotNumber"

# try:
#     # Загружаем страницу
#     driver.get(url)

#     # Ищем все скрипты на странице
#     scripts = driver.find_elements(By.TAG_NAME, "script")


    

#     lot_data = None

#     # Ищем JSON с лотами в скриптах
#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents" in script_content:
#             print("Найден скрипт с данными:")
#             print(script_content[:1000])  # Для проверки содержимого
#             match = re.search(r"window\.chrComponents\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_str = match.group(1)
#                 lot_data = json.loads(json_str)
#                 break

    
    

#     if not lot_data:
#         print("Не удалось найти данные о лотах.")
#         exit()

#     # Извлекаем информацию о лотах
#     lots = lot_data.get("lots", {}).get("data", {}).get("lots", [])
#     if not lots:
#         print("Данные о лотах отсутствуют в JSON.")
#         exit()

#     # Список для хранения уникальных имен художников
#     authors = set()

#     # Извлекаем имена художников
#     for lot in lots:
#         artist = lot.get("title_primary_txt", "").split("(")[0].strip()
#         if artist:
#             authors.add(artist)

#     # Преобразуем в отсортированный список
#     authors = sorted(authors)

#     # Выводим всех авторов
#     for author in authors:
#         print(author)

# finally:
#     driver.quit()

##############################################################################################################

# -------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import re
# import json
# import csv

# # Настройки WebDriver
# driver_path = "D:\\project on python\\msedgedriver.exe"  # Укажите путь к вашему WebDriver
# options = Options()
# options.add_argument("--headless")  # Запуск браузера в фоновом режиме
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")
# # Настройка WebDriver
# edge_options = Options()
# edge_options.add_argument("--headless")  # Запуск в фоновом режиме
# edge_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=options)

# # URL для парсинга
# url = "https://www.christies.com/en/auction/20-21-century-art-day-sale-30415/?page=2&sortby=lotnumber"

# try:
#     # Открываем страницу
#     driver.get(url)

#     # Находим все скрипты на странице
#     scripts = driver.find_elements(By.TAG_NAME, "script")

#     lot_data = None

#     # Ищем нужный скрипт с JSON
#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents" in script_content:  # Проверяем, есть ли нужная структура
#             match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_str = match.group(1)
#                 lot_data = json.loads(json_str)  # Преобразуем JSON в словарь Python
#                 break

#     if not lot_data:
#         print("Не удалось найти данные о лотах.")
#         driver.quit()
#         exit()

#     # Извлекаем данные о лотах
#     lots = lot_data.get("data", {}).get("lots", [])
#     if not lots:
#         print("Данные о лотах отсутствуют.")
#         driver.quit()
#         exit()

#     # Создаем CSV
#     results = []
#     for lot in lots:
#         title = lot.get("title_secondary_txt", "N/A")
#         artist = lot.get("title_primary_txt", "N/A")
#         price_realised = lot.get("price_realised_txt", "N/A")
#         estimate = lot.get("estimate_txt", "N/A")
#         description = lot.get("description_txt", "N/A")

#         # Размер
#         dimensions_match = re.search(r"([\d.,]+\s*x\s*[\d.,]+\s*(?:cm|in))", description)
#         dimensions = dimensions_match.group(1) if dimensions_match else "N/A"

#         material_match = re.search(r"(oil on canvas|acrylic|mixed media|gouache|watercolor|bronze)", description, re.IGNORECASE)
#         material = material_match.group(1) if material_match else "N/A"

#         # Удаляем скобки и извлекаем период
#         artist_cleaned = re.sub(r'\(.*?\)', '', artist).strip()
#         # Извлечение периода из имени художника (например, данные в скобках)
#         period_match = re.search(r'\((.*?)\)', artist)
#         period = period_match.group(1) if period_match else "N/A"

#         # Страна
#         country = artists_countries.get(artist_cleaned, "Unknown")

#         # Извлекаем стиль и жанр
#         style = extract_style(description)
#         genre = extract_genre(description)

        

#         # Добавляем данные в список
#         results.append({
#             "Название": title,
#             "Имя художника": artist_cleaned,
#             "Стоимость": price_realised,
#             "Примерная оценка": estimate,
#             "Материал": material,
#             "Размер": dimensions,
#             "Страна": country,
#             "Период": period,
#             "Стиль": "Abstract Expressionism",
#             "Жанр": "Abstract"
#         })

#     # Сохраняем в CSV
#     csv_file = "20_21_CENTURY_ART.csv"
#     fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Материал", "Размер", "Страна", "Период", "Стиль", "Жанр"]

#     with open(csv_file, "w", newline="", encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(results)

#     print(f"Данные успешно сохранены в {csv_file}")

# finally:
#     driver.quit()

#-------------------------------------------------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import re
# import json
# import csv


# # Укажите путь к вашему WebDriver
# driver_path = "D:\\project on python\\msedgedriver.exe"

# # Настройки WebDriver
# options = Options()
# options.add_argument("--headless")  # Запуск браузера в фоновом режиме (если необходимо)
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

# # Настройка службы WebDriver
# service = Service(driver_path)

# # Создание экземпляра WebDriver
# driver = webdriver.Edge(service=service, options=options)


# # URL страницы
# url = "https://onlineonly.christies.com/s/marc-chagall-entre-ciel-et-terre-oeuvres-provenant-de-la-succession-de/lots/3732"



# try:
#     # Открываем страницу
#     driver.get(url)

#     # Ищем теги <script>, содержащие данные
#     scripts = driver.find_elements(By.TAG_NAME, "script")
#     lot_data = None

#     # Ищем JSON в одном из скриптов
#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents" in script_content:
#             match = re.search(r"window\.chrComponents\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_data = match.group(1)
#                 lot_data = json.loads(json_data)
#                 break

#     if not lot_data:
#         print("Данные не найдены.")
#     else:
#         # Парсим лоты
#         lots = lot_data.get("lots", {}).get("data", {}).get("lots", [])
#         results = []

#         for lot in lots:
#             artist = lot.get("title_primary_txt", "N/A")
#             title = lot.get("title_secondary_txt", "N/A")
#             price_realised = lot.get("price_realised_txt", "N/A")
#             estimate = lot.get("estimate_txt", "N/A")
#             description = lot.get("description_txt", "N/A")

#             # Извлекаем материал и размеры
#             dimensions_match = re.search(r"([\d.,]+\s*x\s*[\d.,]+\s*(cm|in))", description)
#             dimensions = dimensions_match.group(1) if dimensions_match else "N/A"

#             material_match = re.search(r"(oil on canvas|acrylic|mixed media|gouache|watercolor|bronze)", description, re.IGNORECASE)
#             material = material_match.group(1) if material_match else "N/A"

#             # Удаляем скобки и извлекаем период
#             artist_cleaned = re.sub(r'\(.*?\)', '', artist).strip()
#             period_match = re.search(r"\\(([^)]+)\\)", artist)
#             period = period_match.group(1) if period_match else "N/A"

#             # Страна
#             country = "FRENCH"  # Можно заменить на словарь стран по художникам

#             # Извлекаем стиль и жанр
#             style = "Surrealism"
#             genre = "Fantasy Compositions"

#             # Добавляем данные в список
#             results.append({
#                 "Название": title,
#                 "Имя художника": artist_cleaned,
#                 "Стоимость": price_realised,
#                 "Примерная оценка": estimate,
#                 "Материал": material,
#                 "Размер": dimensions,
#                 "Страна": country,
#                 "Период": "1887-1985",
#                 "Стиль": style,
#                 "Жанр": genre
#         })
            
        
#         csv_file = "Marc_Chagall.csv"
#         fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Материал", "Размер", "Страна", "Период", "Стиль", "Жанр"]

#         with open(csv_file, "w", newline="", encoding="utf-8") as file:
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(results)

#         print(f"Данные успешно сохранены в файл {csv_file}")

# finally:
#     # Закрываем браузер
#     driver.quit()



#-----------------------------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import re
# import json
# import csv

# url = "https://www.christies.com/en/auction/exceptional-impressions-the-alan-and-marianne-schwartz-collection-30738/?page=2&sortby=lotnumber"
# # Укажите путь к вашему WebDriver
# driver_path = "D:\\project on python\\msedgedriver.exe"

# # Настройки WebDriver
# options = Options()
# options.add_argument("--headless")  # Запуск браузера в фоновом режиме (если необходимо)
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

# # Настройка службы WebDriver
# service = Service(driver_path)

# # Создание экземпляра WebDriver
# driver = webdriver.Edge(service=service, options=options)

# try:
#     # Открываем страницу
#     driver.get(url)

#     # Ищем теги <script>, содержащие данные
#     scripts = driver.find_elements(By.TAG_NAME, "script")
#     lot_data = None

#     # Ищем JSON в одном из скриптов
#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents.lots" in script_content:
#             match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_data = match.group(1)
#                 lot_data = json.loads(json_data)
#                 break

#     if not lot_data:
#         print("Данные не найдены.")
#     else:
#         # Парсим лоты
#         lots = lot_data.get("data", {}).get("lots", [])
#         filters = lot_data.get("data", {}).get("filters", {}).get("groups", [])
        
#         results = []
#         for lot in lots:
#             artist = lot.get("title_primary_txt", "N/A")
#             title = lot.get("title_secondary_txt", "N/A")
#             price_realised = lot.get("price_realised_txt", "N/A")
#             estimate = lot.get("estimate_txt", "N/A")
#             description = lot.get("description_txt", "N/A")
            

#             # Извлекаем размер
#             dimensions_match = re.search(r"([\d.,]+\s*x\s*[\d.,]+\s*(mm|cm|in))", description, re.IGNORECASE)
#             dimensions = dimensions_match.group(1) if dimensions_match else "Размер не найден"

#             material_match = re.search(r"(oil on canvas|acrylic|mixed media|gouache|watercolor|bronze)", description, re.IGNORECASE)
#             material = material_match.group(1) if material_match else "N/A"

           
#             # Удаляем скобки и извлекаем период
#             artist_cleaned = re.sub(r'\(.*?\)', '', artist).strip()
#             # Извлечение периода
#             period_match = re.search(r"\((?:CIRCA\s*)?(\d{4}-\d{4})\)", artist, re.IGNORECASE)
#             period = period_match.group(1) if period_match else "Период не найден"

#             # Добавляем страну, период, жанр
#             country = artists_countries.get(artist_cleaned, "Unknown")
            
#             genre = ""

#             results.append({
#                 "Название": title,
#                 "Имя художника": artist_cleaned,
#                 "Стоимость": price_realised,
#                 "Примерная оценка": estimate,
#                 "Материал": material,
#                 "Размер": dimensions,
#                 "Страна": country,
#                 "Период": period,
#                 "Стиль": "Engraving",  # Пока данных о стиле нет
#                 "Жанр": "Engraving"
#             })

#         # Сохраняем данные в CSV
#         csv_file = "Alan_and_Marianne_Schwartz.csv"
#         fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Материал", "Размер", "Страна", "Период", "Стиль", "Жанр"]

#         with open(csv_file, "w", newline="", encoding="utf-8") as file:
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(results)

#         print(f"Данные успешно сохранены в файл {csv_file}")

# finally:
#     # Закрываем браузер
#     driver.quit()

#---------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import re
# import json
# import csv

# # Функция для получения стиля и жанра
# def get_style_and_genre(artist_name):
#     artist_info = artist_styles_genres.get(artist_name.upper())  # Преобразуем имя к верхнему регистру
#     if artist_info:
#         return artist_info
#     else:
#         return {"style": "Unknown", "genre": "Unknown"}


# url = "https://www.christies.com/en/auction/modern-and-contemporary-middle-eastern-art-including-highlights-from-the-dalloul-collection-30564/"
# # Укажите путь к вашему WebDriver
# driver_path = "D:\\project on python\\msedgedriver.exe"

# # Настройки WebDriver
# options = Options()
# options.add_argument("--headless")  # Запуск браузера в фоновом режиме (если необходимо)
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

# # Настройка службы WebDriver
# service = Service(driver_path)

# # Создание экземпляра WebDriver
# driver = webdriver.Edge(service=service, options=options)

# try:
#     # Открываем страницу
#     driver.get(url)

#     # Ищем теги <script>, содержащие данные
#     scripts = driver.find_elements(By.TAG_NAME, "script")
#     lot_data = None

#     # Ищем JSON в одном из скриптов
#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents.lots" in script_content:
#             match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_data = match.group(1)
#                 lot_data = json.loads(json_data)
#                 break

#     if not lot_data:
#         print("Данные не найдены.")
#     else:
#         # Парсим лоты
#         lots = lot_data.get("data", {}).get("lots", [])
#         filters = lot_data.get("data", {}).get("filters", {}).get("groups", [])
        
#         results = []
#         for lot in lots:
#             artist = lot.get("title_primary_txt", "N/A")
#             title = lot.get("title_secondary_txt", "N/A")
#             price_realised = lot.get("price_realised_txt", "N/A")
#             estimate = lot.get("estimate_txt", "N/A")
#             description = lot.get("description_txt", "N/A")
            

#             # Попытка извлечь размер и конвертировать в сантиметры
#             dimensions_match = re.search(r"([\d.,]+\s*x\s*[\d.,]+\s*(mm|cm|in))", description, re.IGNORECASE)
#             dimensions = convert_to_cm(dimensions_match.group(0)) if dimensions_match else "Размер не найден"

#             material_match = re.search(r"(oil on canvas|acrylic|mixed media|gouache|watercolor|bronze)", description, re.IGNORECASE)
#             material = material_match.group(1) if material_match else "N/A"

           
#             # Удаляем скобки и извлекаем период
            
#             artist_cleaned = re.sub(r'\(.*?\)', '', artist).strip()
#             # Извлечение периода (всё, что в скобках)

#             period_match = re.search(r"\((.*?)\)", artist)
#             period = period_match.group(1) if period_match else "Период не найден"
#             artist = re.sub(r"\s*\(.*?\)", "", artist).strip().upper()


#             # Добавляем страну, период, жанр
#             country = artists_countries.get(artist_cleaned, "Unknown")
#             style_genre = get_style_and_genre(artist)
#             genre = ""

#             results.append({
#                 "Название": title,
#                 "Имя художника": artist_cleaned,
#                 "Стоимость": price_realised,
#                 "Примерная оценка": estimate,
#                 "Материал": material,
#                 "Размер": dimensions,
#                 "Страна": country,
#                 "Период": period,
#                 "Стиль": style_genre["style"],
#                 "Жанр": style_genre["genre"]
#             })

#         # Сохраняем данные в CSV
#         csv_file = "Modern_and_Contemporary_Middle.csv"
#         fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Материал", "Размер", "Страна", "Период", "Стиль", "Жанр"]

#         with open(csv_file, "w", newline="", encoding="utf-8") as file:
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(results)

#         print(f"Данные успешно сохранены в файл {csv_file}")

# finally:
#     # Закрываем браузер
#     driver.quit()


#---------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import re
# import json
# import csv

# # Укажите путь к WebDriver
# driver_path = "D:\\project on python\\msedgedriver.exe"

# # Настройки WebDriver
# options = Options()
# options.add_argument("--headless")  # Запуск в фоновом режиме
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

# # Создаем экземпляр WebDriver
# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=options)

# # URL страницы
# url = "https://onlineonly.christies.com/s/modern-contemporary-middle-eastern-art-including-highlights-dalloul/lots/3403"

# # Функция для извлечения данных
# def extract_lot_data(driver, url):
#     driver.get(url)

#     # Находим скрипты на странице
#     scripts = driver.find_elements(By.TAG_NAME, "script")
#     lot_data = None

#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents" in script_content:
#             match = re.search(r"window\.chrComponents\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_data = match.group(1)
#                 lot_data = json.loads(json_data)
#                 break

#     if not lot_data or "lots" not in lot_data.get("lots", {}).get("data", {}):
#         print("Данные о лотах не найдены")
#         return []

#     lots = lot_data["lots"]["data"]["lots"]
#     results = []

#     for lot in lots:
#         title = lot.get("title_secondary_txt", "N/A")
#         artist = lot.get("title_primary_txt", "N/A")
#         price_realised = lot.get("price_realised_txt", "N/A")
#         estimate = lot.get("estimate_txt", "N/A")
#         description = lot.get("description_txt", "N/A")

#         # Извлечение материала и размеров из description
#         material_match = re.search(r"(oil on canvas|acrylic|printed porcelain|watercolor)", description, re.IGNORECASE)
#         material = material_match.group(1) if material_match else "N/A"

#         dimensions_match = re.search(r"(\d+\.?\d*\s*x\s*\d+\.?\d*\s*(cm|in|mm))", description, re.IGNORECASE)
#         dimensions = dimensions_match.group(1) if dimensions_match else "N/A"

#         artist_cleaned = re.sub(r'\(.*?\)', '', artist).strip()

#         period_match = re.search(r"\((.*?)\)", artist)
#         period = period_match.group(1) if period_match else "Период не найден"
#         artist = re.sub(r"\s*\(.*?\)", "", artist).strip().upper()

#         country=artists_countries.get(artist_cleaned, "Unknown")
#         style_genre = get_style_and_genre(artist)

#         # Добавляем данные в результат
#         results.append({
#             "Название": title,
#             "Имя художника": artist,
#             "Стоимость": price_realised,
#             "Примерная оценка": estimate,
#             "Материал": material,
#             "Размер": dimensions,
#             "Страна": country,
#             "Период": period,
#             "Стиль": style_genre["style"],
#             "Жанр": style_genre["genre"]
#         })

#     return results

# # Основной блок выполнения
# try:
#     data = extract_lot_data(driver, url)

#     # Сохраняем данные в CSV
#     csv_file = "Middle_Eastern_Art.csv"
#     fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Материал", "Размер", "Страна", "Период", "Стиль", "Жанр"]

#     with open(csv_file, "w", newline="", encoding="utf-8") as file:
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)

#     print(f"Данные успешно сохранены в файл {csv_file}")

# finally:
#     driver.quit()

#------------------------------------------------------------------
