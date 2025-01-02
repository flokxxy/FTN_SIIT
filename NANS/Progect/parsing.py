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
    "TIMO NASSERI": {"style": "Contemporary", "genre": "Geometric"},
     "ADA GILMORE CHAFFEE": {"style": "American Modernism", "genre": "Landscape"},
    "ADOLF ARTHUR DEHN": {"style": "Social Realism", "genre": "Figurative"},
    "ADOLPH GOTTLIEB": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "AFTER JOAN MITCHELL": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "AFTER MARC CHAGALL BY CHARLES SORLIER": {"style": "Modernism", "genre": "Figurative"},
    "AFTER RENÉ MAGRITTE": {"style": "Surrealism", "genre": "Conceptual"},
    "AFTER WINSLOW HOMER": {"style": "Realism", "genre": "Marine and Landscape"},
    "AL HELD": {"style": "Abstract Expressionism", "genre": "Geometric"},
    "ALBERT BARKER": {"style": "Realism", "genre": "Urban Landscape"},
    "ALICE AYCOCK": {"style": "Contemporary", "genre": "Conceptual"},
    "ANGELO PINTO": {"style": "Modernism", "genre": "Abstract"},
    "ARMAND SEGUIN": {"style": "Post-Impressionism", "genre": "Figurative"},
    "ARMIN LANDECK": {"style": "Precisionism", "genre": "Architectural Prints"},
    "ARNALDO POMODORO": {"style": "Modernism", "genre": "Sculptural"},
    "ARNOLD RÖNNEBECK": {"style": "Expressionism", "genre": "Abstract"},
    "ARTHUR WESLEY DOW": {"style": "Tonalism", "genre": "Landscape"},
    "AUGUSTA PAYNE BRIGGS RATHBONE": {"style": "Modernism", "genre": "Landscape"},
    "BORIS ARTZYBASHEFF": {"style": "Illustration", "genre": "Satirical"},
    "BROR JULIUS OLSSON NORDFELDT": {"style": "Modernism", "genre": "Landscape"},
    "BRUCE NAUMAN": {"style": "Conceptual Art", "genre": "Multimedia"},
    "CAMILLE PISSARRO": {"style": "Impressionism", "genre": "Landscape"},
    "CHARLES BARKER": {"style": "Realism", "genre": "Urban Landscape"},
    "CHARLES F. WILLIAM MIELATZ": {"style": "Realism", "genre": "Urban Scenes"},
    "CHARLES TURZAK": {"style": "Modernism", "genre": "Woodcuts"},
    "CHILDE HASSAM": {"style": "Impressionism", "genre": "Urban and Landscape"},
    "CHUCK CLOSE": {"style": "Photorealism", "genre": "Portraiture"},
    "CLAES OLDENBURG": {"style": "Pop Art", "genre": "Sculptural"},
    "DAVID HOCKNEY": {"style": "Pop Art", "genre": "Landscape"},
    "DIEGO RIVERA": {"style": "Mexican Muralism", "genre": "Social Realism"},
    "DIETER ROTH": {"style": "Fluxus", "genre": "Experimental"},
    "DON FREEMAN": {"style": "Social Realism", "genre": "Everyday Life"},
    "DONALD JUDD": {"style": "Minimalism", "genre": "Geometric"},
    "DONALD STANLEY VOGEL": {"style": "Modernism", "genre": "Abstract"},
    "EDGAR CHAHINE": {"style": "Impressionism", "genre": "Portrait and Genre Scenes"},
    "EDOUARD VUILLARD": {"style": "Post-Impressionism", "genre": "Domestic Scenes"},
    "ELLSWORTH KELLY": {"style": "Hard-edge Painting", "genre": "Abstract"},
    "ENZO CUCCHI": {"style": "Transavantgarde", "genre": "Figurative"},
    "ERIC FISCHL": {"style": "Neo-expressionism", "genre": "Figurative"},
    "FRANK DUVENECK": {"style": "Realism", "genre": "Portraiture"},
    "FRANK MORLEY FLETCHER": {"style": "Modernism", "genre": "Printmaking"},
    "FRANK STELLA": {"style": "Minimalism", "genre": "Abstract"},
    "FRITZ EICHENBERG": {"style": "Expressionism", "genre": "Illustration"},
    "FÉLIX BRACQUEMOND": {"style": "Impressionism", "genre": "Animal and Landscape"},
    "GENE DAVIS": {"style": "Color Field", "genre": "Abstract"},
    "GENE KLOSS": {"style": "Modernism", "genre": "Rural Scenes"},
    "GEORGE SEGAL": {"style": "Pop Art", "genre": "Sculptural"},
    "GEORGE TOOKER": {"style": "Magic Realism", "genre": "Figurative"},
    "GEORGE WESLEY BELLOWS": {"style": "Ashcan School", "genre": "Urban and Rural Scenes"},
    "GEORGES ROUAULT": {"style": "Expressionism", "genre": "Religious"},
    "GLENN COLEMAN": {"style": "Modernism", "genre": "Urban Scenes"},
    "GRANT WOOD": {"style": "Regionalism", "genre": "Rural Scenes"},
    "HANS BURKHARDT": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "HARRY BRODSKY": {"style": "Social Realism", "genre": "Everyday Life"},
    "HARRY STERNBERG": {"style": "Social Realism", "genre": "Industrial"},
    "HELEN HYDE": {"style": "Modernism", "genre": "Printmaking"},
    "HELEN LUNDEBERG": {"style": "Post-Surrealism", "genre": "Abstract"},
    "HENRI DE TOULOUSE-LAUTREC": {"style": "Post-Impressionism", "genre": "Portraits and Posters"},
    "HENRI MATISSE": {"style": "Fauvism", "genre": "Figurative"},
    "HENRY MOORE": {"style": "Modernism", "genre": "Sculptural"},
    "HOWARD COOK": {"style": "Regionalism", "genre": "Urban and Rural Scenes"},
    "HOWARD HODGKIN": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "ISAC FRIEDLANDER": {"style": "Modernism", "genre": "Printmaking"},
    "JACQUES VILLON": {"style": "Cubism", "genre": "Abstract"},
    "JAMES JACQUES JOSEPH TISSOT": {"style": "Realism", "genre": "Portraiture"},
    "JAMES MCNEILL WHISTLER": {"style": "Tonalism", "genre": "Portrait and Landscape"},
    "JAMES ROSENQUIST": {"style": "Pop Art", "genre": "Collage"},
    "JEAN ARP": {"style": "Dada", "genre": "Abstract"},
    "JEAN DUBUFFET": {"style": "Art Brut", "genre": "Abstract"},
    "JEAN-BAPTISTE CAMILLE COROT": {"style": "Barbizon School", "genre": "Landscape"},
    "JEFF KOONS": {"style": "Contemporary", "genre": "Pop Art"},
    "JIM DINE": {"style": "Pop Art", "genre": "Mixed Media"},
    "JIM DINE AND RON PADGETT": {"style": "Pop Art", "genre": "Collaboration"},
    "JOAN MIRÓ": {"style": "Surrealism", "genre": "Abstract"},
    "JOE JONES": {"style": "Social Realism", "genre": "Everyday Life"},
    "JOHN EDGAR PLATT": {"style": "Modernism", "genre": "Printmaking"},
    "JOHN FERREN": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "KER-XAVIER ROUSSEL": {"style": "Post-Impressionism", "genre": "Figurative"},
    "ADA GILMORE CHAFFEE": {"style": "American Modernism", "genre": "Landscape"},
    "ADOLF ARTHUR DEHN": {"style": "Social Realism", "genre": "Figurative"},
    "ADOLPH GOTTLIEB": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "AFTER JOAN MITCHELL": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "AFTER MARC CHAGALL BY CHARLES SORLIER": {"style": "Modernism", "genre": "Figurative"},
    "AFTER RENÉ MAGRITTE": {"style": "Surrealism", "genre": "Conceptual"},
    "AFTER WINSLOW HOMER": {"style": "Realism", "genre": "Marine and Landscape"},
    "AL HELD": {"style": "Abstract Expressionism", "genre": "Geometric"},
    "ALBERT BARKER": {"style": "Realism", "genre": "Urban Landscape"},
    "ALICE AYCOCK": {"style": "Contemporary", "genre": "Conceptual"},
    "ANGELO PINTO": {"style": "Modernism", "genre": "Abstract"},
    "ARMAND SEGUIN": {"style": "Post-Impressionism", "genre": "Figurative"},
    "ARMIN LANDECK": {"style": "Precisionism", "genre": "Architectural Prints"},
    "ARNALDO POMODORO": {"style": "Modernism", "genre": "Sculptural"},
    "ARNOLD RÖNNEBECK": {"style": "Expressionism", "genre": "Abstract"},
    "ARTHUR WESLEY DOW": {"style": "Tonalism", "genre": "Landscape"},
    "AUGUSTA PAYNE BRIGGS RATHBONE": {"style": "Modernism", "genre": "Landscape"},
    "BORIS ARTZYBASHEFF": {"style": "Illustration", "genre": "Satirical"},
    "BROR JULIUS OLSSON NORDFELDT": {"style": "Modernism", "genre": "Landscape"},
    "BRUCE NAUMAN": {"style": "Conceptual Art", "genre": "Multimedia"},
    "CAMILLE PISSARRO": {"style": "Impressionism", "genre": "Landscape"},
    "CHARLES BARKER": {"style": "Realism", "genre": "Urban Landscape"},
    "CHARLES F. WILLIAM MIELATZ": {"style": "Realism", "genre": "Urban Scenes"},
    "CHARLES TURZAK": {"style": "Modernism", "genre": "Woodcuts"},
    "CHILDE HASSAM": {"style": "Impressionism", "genre": "Urban and Landscape"},
    "CHUCK CLOSE": {"style": "Photorealism", "genre": "Portraiture"},
    "CLAES OLDENBURG": {"style": "Pop Art", "genre": "Sculptural"},
    "DAVID HOCKNEY": {"style": "Pop Art", "genre": "Landscape"},
    "DIEGO RIVERA": {"style": "Mexican Muralism", "genre": "Social Realism"},
    "DIETER ROTH": {"style": "Fluxus", "genre": "Experimental"},
    "DON FREEMAN": {"style": "Social Realism", "genre": "Everyday Life"},
    "DONALD JUDD": {"style": "Minimalism", "genre": "Geometric"},
    "DONALD STANLEY VOGEL": {"style": "Modernism", "genre": "Abstract"},
    "EDGAR CHAHINE": {"style": "Impressionism", "genre": "Portrait and Genre Scenes"},
    "EDOUARD VUILLARD": {"style": "Post-Impressionism", "genre": "Domestic Scenes"},
    "ELLSWORTH KELLY": {"style": "Hard-edge Painting", "genre": "Abstract"},
    "ENZO CUCCHI": {"style": "Transavantgarde", "genre": "Figurative"},
    "ERIC FISCHL": {"style": "Neo-expressionism", "genre": "Figurative"},
    "FRANK DUVENECK": {"style": "Realism", "genre": "Portraiture"},
    "FRANK MORLEY FLETCHER": {"style": "Modernism", "genre": "Printmaking"},
    "FRANK STELLA": {"style": "Minimalism", "genre": "Abstract"},
    "FRITZ EICHENBERG": {"style": "Expressionism", "genre": "Illustration"},
    "FÉLIX BRACQUEMOND": {"style": "Impressionism", "genre": "Animal and Landscape"},
    "GENE DAVIS": {"style": "Color Field", "genre": "Abstract"},
    "GENE KLOSS": {"style": "Modernism", "genre": "Rural Scenes"},
    "GEORGE SEGAL": {"style": "Pop Art", "genre": "Sculptural"},
    "GEORGE TOOKER": {"style": "Magic Realism", "genre": "Figurative"},
    "GEORGE WESLEY BELLOWS": {"style": "Ashcan School", "genre": "Urban and Rural Scenes"},
    "GEORGES ROUAULT": {"style": "Expressionism", "genre": "Religious"},
    "GLENN COLEMAN": {"style": "Modernism", "genre": "Urban Scenes"},
    "GRANT WOOD": {"style": "Regionalism", "genre": "Rural Scenes"},
    "HANS BURKHARDT": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "HARRY BRODSKY": {"style": "Social Realism", "genre": "Everyday Life"},
    "HARRY STERNBERG": {"style": "Social Realism", "genre": "Industrial"},
    "HELEN HYDE": {"style": "Modernism", "genre": "Printmaking"},
    "HELEN LUNDEBERG": {"style": "Post-Surrealism", "genre": "Abstract"},
    "HENRI DE TOULOUSE-LAUTREC": {"style": "Post-Impressionism", "genre": "Portraits and Posters"},
    "HENRI MATISSE": {"style": "Fauvism", "genre": "Figurative"},
    "HENRY MOORE": {"style": "Modernism", "genre": "Sculptural"},
    "HOWARD COOK": {"style": "Regionalism", "genre": "Urban and Rural Scenes"},
    "HOWARD HODGKIN": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "ISAC FRIEDLANDER": {"style": "Modernism", "genre": "Printmaking"},
    "JACQUES VILLON": {"style": "Cubism", "genre": "Abstract"},
    "JAMES JACQUES JOSEPH TISSOT": {"style": "Realism", "genre": "Portraiture"},
    "JAMES MCNEILL WHISTLER": {"style": "Tonalism", "genre": "Portrait and Landscape"},
    "JAMES ROSENQUIST": {"style": "Pop Art", "genre": "Collage"},
    "JEAN ARP": {"style": "Dada", "genre": "Abstract"},
    "JEAN DUBUFFET": {"style": "Art Brut", "genre": "Abstract"},
    "JEAN-BAPTISTE CAMILLE COROT": {"style": "Barbizon School", "genre": "Landscape"},
    "JEFF KOONS": {"style": "Contemporary", "genre": "Pop Art"},
    "JIM DINE": {"style": "Pop Art", "genre": "Mixed Media"},
    "JIM DINE AND RON PADGETT": {"style": "Pop Art", "genre": "Collaboration"},
    "JOAN MIRÓ": {"style": "Surrealism", "genre": "Abstract"},
    "JOE JONES": {"style": "Social Realism", "genre": "Everyday Life"},
    "JOHN EDGAR PLATT": {"style": "Modernism", "genre": "Printmaking"},
    "JOHN FERREN": {"style": "Abstract Expressionism", "genre": "Abstract"},
     "LUDWIG SANDER": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "PIERRE-AUGUSTE RENOIR": {"style": "Impressionism", "genre": "Figurative"},
    "MILTON AVERY": {"style": "Modernism", "genre": "Figurative"},
    "MIGUEL COVARRUBIAS": {"style": "Art Deco", "genre": "Portraiture"},
    "LEONARD BASKIN": {"style": "Expressionism", "genre": "Figurative"},
    "PAUL CADMUS": {"style": "Social Realism", "genre": "Figurative"},
    "LUIS ARENAL": {"style": "Mexican Muralism", "genre": "Figurative"},
    "MUIRHEAD BONE": {"style": "Realism", "genre": "Landscape"},
    "STEVAN DOHANOS": {"style": "Regionalism", "genre": "Figurative"},
    "LETTERIO CALAPAI": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "RED GROOMS": {"style": "Pop Art", "genre": "Figurative"},
    "WERNER DREWES": {"style": "Bauhaus", "genre": "Abstract"},
    "MAURICE JACQUE": {"style": "Academic Art", "genre": "Figurative"},
    "LEONARD EDMONDSON": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "KERR EBY": {"style": "Realism", "genre": "Landscape"},
    "JOHN STOCKTON DE MARTELLY": {"style": "Regionalism", "genre": "Figurative"},
    "WHARTON ESHERICK": {"style": "Arts and Crafts", "genre": "Sculpture"},
    "STANLEY WILLIAM HAYTER": {"style": "Surrealism", "genre": "Abstract"},
    "ROCKWELL KENT": {"style": "Modernism", "genre": "Landscape"},
    "WANDA GÁG": {"style": "Modernism", "genre": "Illustration"},
    "RIVA HELFOND": {"style": "Social Realism", "genre": "Figurative"},
    "KÄTHE KOLLWITZ": {"style": "Expressionism", "genre": "Figurative"},
    "PETER KRASNOW": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "YASUO KUNIYOSHI": {"style": "Modernism", "genre": "Figurative"},
    "LAWRENCE KUPFERMAN": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "PAUL LANDACRE": {"style": "Precisionism", "genre": "Printmaking"},
    "OTTO LANGE": {"style": "Expressionism", "genre": "Figurative"},
    "REGINALD MARSH": {"style": "Social Realism", "genre": "Figurative"},
    "STOW WENGENROTH": {"style": "Realism", "genre": "Landscape"},
    "THOMAS MORAN": {"style": "Hudson River School", "genre": "Landscape"},
    "JOHN HENRY BRADLEY STORRS": {"style": "Modernism", "genre": "Sculpture"},
    "KENNETH HAYES MILLER": {"style": "Realism", "genre": "Figurative"},
    "ROBERT RAUSCHENBERG": {"style": "Pop Art", "genre": "Mixed Media"},
    "WILLIAM SELTZER RICE": {"style": "Arts and Crafts", "genre": "Printmaking"},
    "ROBERT RIGGS": {"style": "Realism", "genre": "Figurative"},
    "WILLIAM SAMUEL SCHWARTZ": {"style": "Modernism", "genre": "Abstract"},
    "MILLARD OWEN SHEETS": {"style": "Modernism", "genre": "Landscape"},
    "JOHN SLOAN": {"style": "Ashcan School", "genre": "Urban Scene"},
    "LAWRENCE BEALL SMITH": {"style": "Social Realism", "genre": "Figurative"},
    "NILES SPENCER": {"style": "Precisionism", "genre": "Urban Landscape"},
    "MAX WEBER": {"style": "Cubism", "genre": "Abstract"},
    "WILLIAM ZORACH": {"style": "Modernism", "genre": "Sculpture"},
    "RICHARD ANUSZKIEWICZ": {"style": "Op Art", "genre": "Abstract"},
    "THEODORE WHITE": {"style": "Realism", "genre": "Figurative"},
    "PIERRE BONNARD": {"style": "Post-Impressionism", "genre": "Figurative"},
    "MARC CHAGALL": {"style": "Surrealism", "genre": "Figurative"},
    "JOSEF ALBERS": {"style": "Abstract", "genre": "Geometric"},
    "KAREL APPEL": {"style": "CoBrA", "genre": "Abstract"},
    "GEORGE WESLEY BELLOWS": {"style": "Realism", "genre": "Figurative"},
    "ROMARE BEARDEN": {"style": "Collage", "genre": "Figurative"},
    "LYNN CHADWICK": {"style": "Modernism", "genre": "Sculpture"},
    "LOUISE BOURGEOIS": {"style": "Surrealism", "genre": "Sculpture"},
    "LEE BONTECOU": {"style": "Abstract Expressionism", "genre": "Sculpture"},
    "MARY CASSATT": {"style": "Impressionism", "genre": "Portraiture"},
    "JOSEPH CORNELL": {"style": "Surrealism", "genre": "Assemblage"},
    "STUART DAVIS": {"style": "Modernism", "genre": "Abstract"},
    "PETER DOIG": {"style": "Contemporary", "genre": "Figurative"},
    "MAX ERNST": {"style": "Surrealism", "genre": "Abstract"},
    "MAURICE DENIS": {"style": "Symbolism", "genre": "Figurative"},
    "LÉONARD TSUGUHARU FOUJITA": {"style": "Modernism", "genre": "Figurative"},
    "RICHARD HAMILTON": {"style": "Pop Art", "genre": "Abstract"},
    "ROY LICHTENSTEIN": {"style": "Pop Art", "genre": "Comic Art"},
    "ROBERT INDIANA": {"style": "Pop Art", "genre": "Abstract"},
    "ROBERT RAUSCHENBERG": {"style": "Pop Art", "genre": "Mixed Media"},
    "ROBERTO MATTA": {"style": "Surrealism", "genre": "Abstract"},
    "ROBERT MANGOLD": {"style": "Minimalism", "genre": "Geometric"},
    "PABLO PICASSO": {"style": "Cubism", "genre": "Abstract"},
    "KENNETH NOLAND": {"style": "Color Field", "genre": "Abstract"},
    "LOUISE NEVELSON": {"style": "Abstract Expressionism", "genre": "Sculpture"},
    "ROBERT MOTHERWELL": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "AFTER FERNAND LEGER": {"style": "Cubism", "genre": "Abstract"},
  "AFTER PAUL GAUGUIN": {"style": "Post-Impressionism", "genre": "Symbolism"},
  "ALBERT GLEIZES": {"style": "Cubism", "genre": "Abstract"},
  "ALBERT MARQUET": {"style": "Fauvism", "genre": "Landscape"},
  "ALBERTO GIACOMETTI": {"style": "Surrealism", "genre": "Sculpture"},
  "ALEXEJ VON JAWLENSKY": {"style": "Expressionism", "genre": "Portrait"},
  "ALFRED SISLEY": {"style": "Impressionism", "genre": "Landscape"},
  "ANDRE DERAIN": {"style": "Fauvism", "genre": "Landscape"},
  "ANDRE LHOTE": {"style": "Cubism", "genre": "Landscape"},
  "ARMAND GUILLAUMIN": {"style": "Impressionism", "genre": "Landscape"},
  "AUGUSTE RODIN": {"style": "Realism", "genre": "Sculpture"},
  "BERNARD BUFFET": {"style": "Expressionism", "genre": "Still Life"},
  "EDOUARD VUILLARD": {"style": "Nabis", "genre": "Interior"},
  "EMILE OTHON FRIESZ": {"style": "Fauvism", "genre": "Landscape"},
  "EUGENE BOUDIN": {"style": "Impressionism", "genre": "Landscape"},
  "FERNAND LEGER": {"style": "Cubism", "genre": "Abstract"},
  "FERNANDO BOTERO": {"style": "Boteroism", "genre": "Portrait"},
  "FRANCOISE GILOT": {"style": "Post-Impressionism", "genre": "Portrait"},
  "GEORGES LEMMEN": {"style": "Neo-Impressionism", "genre": "Portrait"},
  "GIORGIO DE CHIRICO": {"style": "Metaphysical Painting", "genre": "Surrealism"},
  "GUSTAVE LOISEAU": {"style": "Impressionism", "genre": "Landscape"},
  "HENRI FANTIN-LATOUR": {"style": "Realism", "genre": "Still Life"},
  "HENRI HAYDEN": {"style": "Cubism", "genre": "Landscape"},
  "HENRI LAURENS": {"style": "Cubism", "genre": "Sculpture"},
  "HENRI LE SIDANER": {"style": "Impressionism", "genre": "Landscape"},
  "HENRI LEBASQUE": {"style": "Post-Impressionism", "genre": "Landscape"},
  "HENRI MARTIN": {"style": "Post-Impressionism", "genre": "Landscape"},
  "HENRY MOORE": {"style": "Abstract", "genre": "Sculpture"},
  "HENRY MORET": {"style": "Impressionism", "genre": "Landscape"},
  "JACQUES LIPCHITZ": {"style": "Cubism", "genre": "Sculpture"},
  "JEAN ARP": {"style": "Dadaism", "genre": "Sculpture"},
  "JEAN DUFY": {"style": "Fauvism", "genre": "Landscape"},
  "JEAN-PIERRE CASSIGNEUL": {"style": "Post-Impressionism", "genre": "Portrait"},
  "JOAN MIRO": {"style": "Surrealism", "genre": "Abstract"},
  "JOSEPH CSAKY": {"style": "Cubism", "genre": "Sculpture"},
  "KAY SAGE": {"style": "Surrealism", "genre": "Abstract"},
  "KEES VAN DONGEN": {"style": "Fauvism", "genre": "Portrait"},
  "LEONORA CARRINGTON": {"style": "Surrealism", "genre": "Abstract"},
  "LEOPOLD SURVAGE": {"style": "Abstract", "genre": "Abstract"},
  "LOUIS MARCOUSSIS": {"style": "Cubism", "genre": "Still Life"},
  "LOUIS VALTAT": {"style": "Post-Impressionism", "genre": "Landscape"},
  "MAN RAY": {"style": "Surrealism", "genre": "Photography"},
  "MARC CHAGALL": {"style": "Modernism", "genre": "Symbolism"},
  "MARINO MARINI": {"style": "Modernism", "genre": "Sculpture"},
  "MAURICE DE VLAMINCK": {"style": "Fauvism", "genre": "Landscape"},
  "MAURICE UTRILLO": {"style": "Naïve Art", "genre": "Cityscape"},
  "MAXIMILIEN LUCE": {"style": "Pointillism", "genre": "Landscape"},
  "ODILON REDON": {"style": "Symbolism", "genre": "Fantasy"},
  "PIERRE BONNARD": {"style": "Post-Impressionism", "genre": "Interior"},
  "PIERRE-AUGUSTE RENOIR": {"style": "Impressionism", "genre": "Portrait"},
  "RAOUL DUFY": {"style": "Fauvism", "genre": "Landscape"},
  "SUZANNE VALADON": {"style": "Post-Impressionism", "genre": "Still Life"},
  "VICTOR BRAUNER": {"style": "Surrealism", "genre": "Abstract"},
  "DIETZ EDZARD": {"style": "Post-Impressionism", "genre": "Portrait"},
  "EMMANUEL MANE-KATZ": {"style": "Expressionism", "genre": "Religious Art"},
  "JULES PASCIN": {"style": "Expressionism", "genre": "Portrait"},
  "HENRI HAYDEN": {"style": "Cubism", "genre": "Still Life"},
  "GEORG KOLBE": {"style": "Expressionism", "genre": "Sculpture"},
  "ARISTIDE MAILLOL": {"style": "Classicism", "genre": "Sculpture"},
  "ERNST BARLACH": {"style": "Expressionism", "genre": "Sculpture"},
  "EMILE-ANTOINE BOURDELLE": {"style": "Modernism", "genre": "Sculpture"},
  "HENRI CHARLES MANGUIN": {"style": "Fauvism", "genre": "Landscape"},
  "PIERRE-AUGUSTE RENOIR AND RICHARD GUINO": {"style": "Impressionism", "genre": "Collaborative Sculpture"},
  "ALBERT ANDRE": {"style": "Post-Impressionism", "genre": "Portrait"},
  "ALBERT GLEIZES": {"style": "Cubism", "genre": "Abstract"},
  "ALBERTO GIACOMETTI": {"style": "Modernism", "genre": "Sculpture"},
  "ALEXANDER ARCHIPENKO": {"style": "Cubism", "genre": "Sculpture"},
  "ARISTIDE MAILLOL": {"style": "Classicism", "genre": "Sculpture"},
  "BALTHUS": {"style": "Modern Realism", "genre": "Portrait"},
  "BERNARD BUFFET": {"style": "Expressionism", "genre": "Still Life"},
  "BERTHE MORISOT": {"style": "Impressionism", "genre": "Portrait"},
  "CAMILLE PISSARRO": {"style": "Impressionism", "genre": "Landscape"},
  "CHILDE HASSAM": {"style": "American Impressionism", "genre": "Landscape"},
  "EDGAR DEGAS": {"style": "Impressionism", "genre": "Figurative"},
  "EDOUARD VUILLARD": {"style": "Post-Impressionism", "genre": "Interior"},
  "EGON SCHIELE": {"style": "Expressionism", "genre": "Figurative"},
  "EMIL NOLDE": {"style": "Expressionism", "genre": "Landscape"},
  "FERDINAND-VICTOR-EUGENE DELACROIX": {"style": "Romanticism", "genre": "Historical"},
  "FERNAND LEGER": {"style": "Cubism", "genre": "Abstract"},
  "FRANTISEK KUPKA": {"style": "Abstract Art", "genre": "Abstract"},
  "GEORGE GROSZ": {"style": "Expressionism", "genre": "Satirical"},
  "GEORGES VALMIER": {"style": "Cubism", "genre": "Abstract"},
  "HENRI MATISSE": {"style": "Fauvism", "genre": "Portrait"},
  "HENRY MOORE": {"style": "Modernism", "genre": "Sculpture"},
  "HONORE DAUMIER": {"style": "Realism", "genre": "Satirical"},
  "JACQUES LIPCHITZ": {"style": "Cubism", "genre": "Sculpture"},
  "JEAN DUFY": {"style": "Modernism", "genre": "Cityscape"},
  "JOAN MIRO": {"style": "Surrealism", "genre": "Abstract"},
  "LEONARD TSUGUHARU FOUJITA": {"style": "Modernism", "genre": "Portrait"},
  "LYONEL FEININGER": {"style": "Cubism", "genre": "Cityscape"},
  "MANE-KATZ": {"style": "Expressionism", "genre": "Religious Art"},
  "MARC CHAGALL": {"style": "Surrealism", "genre": "Religious Art"},
  "MARIE LAURENCIN": {"style": "Cubism", "genre": "Portrait"},
  "MARINO MARINI": {"style": "Modernism", "genre": "Sculpture"},
  "MARY CASSATT": {"style": "Impressionism", "genre": "Portrait"},
  "MAURICE DE VLAMINCK": {"style": "Fauvism", "genre": "Landscape"},
  "MAX ERNST": {"style": "Surrealism", "genre": "Abstract"},
  "MAXIMILIEN LUCE": {"style": "Neo-Impressionism", "genre": "Landscape"},
  "OSSIP ZADKINE": {"style": "Cubism", "genre": "Sculpture"},
  "PABLO PICASSO": {"style": "Cubism", "genre": "Abstract"},
  "PAUL SIGNAC": {"style": "Pointillism", "genre": "Seascape"},
  "PIERRE BONNARD": {"style": "Post-Impressionism", "genre": "Interior"},
  "PIERRE-AUGUSTE RENOIR": {"style": "Impressionism", "genre": "Portrait"},
  "ROBERT DELAUNAY": {"style": "Orphism", "genre": "Abstract"},
  "WASSILY KANDINSKY": {"style": "Abstract Art", "genre": "Abstract"},
  "ALEXANDER ARCHIPENKO": {"style": "Cubism", "genre": "Sculpture"},
    "ANDY WARHOL": {"style": "Pop Art", "genre": "Portraiture"},
    "DAVID SALLE": {"style": "Postmodernism", "genre": "Abstract"},
    "EDGAR DEGAS": {"style": "Impressionism", "genre": "Figure Painting"},
    "FRANCIS PICABIA": {"style": "Dada", "genre": "Abstract"},
    "FRANTISEK KUPKA": {"style": "Orphism", "genre": "Abstract"},
    "GASTON LACHAISE": {"style": "Modernism", "genre": "Sculpture"},
    "GEORGE GROSZ": {"style": "Expressionism", "genre": "Satirical"},
    "GEORGES VANTONGERLOO": {"style": "De Stijl", "genre": "Abstract"},
    "HANS HOFMANN": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "HENRI MATISSE": {"style": "Fauvism", "genre": "Still Life"},
    "JACK YOUNGERMAN": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "JACQUES LIPCHITZ": {"style": "Cubism", "genre": "Sculpture"},
    "JEAN DUBUFFET": {"style": "Art Brut", "genre": "Abstract"},
    "JEAN HELION": {"style": "Modernism", "genre": "Abstract"},
    "JOSEPH STELLA": {"style": "Futurism", "genre": "Abstract"},
    "KAZIMIR MALEVICH": {"style": "Suprematism", "genre": "Abstract"},
    "KENNETH NOLAND": {"style": "Color Field", "genre": "Abstract"},
    "LARRY RIVERS": {"style": "Pop Art", "genre": "Portraiture"},
    "LE CORBUSIER": {"style": "Modernism", "genre": "Architecture"},
    "LOUIS MARCOUSSIS": {"style": "Cubism", "genre": "Abstract"},
    "MAN RAY": {"style": "Surrealism", "genre": "Photography"},
    "MORGAN RUSSELL": {"style": "Synchronism", "genre": "Abstract"},
    "OLEKSANDR BOHOMAZOV": {"style": "Futurism", "genre": "Abstract"},
    "PABLO PICASSO": {"style": "Cubism", "genre": "Portraiture"},
    "RENE MAGRITTE": {"style": "Surrealism", "genre": "Fantasy"},
    "RICHARD LINDNER": {"style": "Pop Art", "genre": "Portraiture"},
    "SONIA DELAUNAY": {"style": "Orphism", "genre": "Abstract"},
    "THEO VAN DOESBURG": {"style": "De Stijl", "genre": "Abstract"},
    "VASYL YERMILOV": {"style": "Constructivism", "genre": "Abstract"},
    "WANG KEPING": {"style": "Modernism", "genre": "Sculpture"},
    "YVES KLEIN": {"style": "Monochrome Art", "genre": "Abstract"},
    "YVES TANGUY": {"style": "Surrealism", "genre": "Abstract"},
    "ADRIAN HENRI": {"style": "Pop Art", "genre": "Abstract"},
    "ALAN LOWNDES": {"style": "Naïve Art", "genre": "Landscape"},
    "ALFRED WALLIS": {"style": "Naïve Art", "genre": "Marine"},
    "ANNE ESTELLE RICE": {"style": "Fauvism", "genre": "Portraiture"},
    "ANNE REDPATH, A.R.A.": {"style": "Expressionism", "genre": "Still Life"},
    "ANTONY DONALDSON": {"style": "Pop Art", "genre": "Figurative"},
    "AUGUSTUS JOHN, O.M., C.H.": {"style": "Post-Impressionism", "genre": "Portraiture"},
    "AUGUSTUS JOHN, O.M., R.A.": {"style": "Post-Impressionism", "genre": "Landscape"},
    "BEN NICHOLSON, O.M.": {"style": "Modernism", "genre": "Abstract"},
    "BERNARD MEADOWS, R.A.": {"style": "Modernism", "genre": "Sculpture"},
    "BRYAN WYNTER": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "CELIA PAUL": {"style": "Contemporary Realism", "genre": "Portraiture"},
    "CHARLES GINNER, A.R.A.": {"style": "Post-Impressionism", "genre": "Landscape"},
    "CHRISTOPHER BRAMHAM": {"style": "Modernism", "genre": "Landscape"},
    "CHRISTOPHER RICHARD WYNNE NEVINSON, A.R.A.": {"style": "Futurism", "genre": "War"},
    "CHRISTOPHER WOOD": {"style": "Modernism", "genre": "Landscape"},
    "CLIVE BARKER": {"style": "Pop Art", "genre": "Sculpture"},
    "CRAIGIE AITCHISON, R.A.": {"style": "Contemporary Realism", "genre": "Portraiture"},
    "DAME BARBARA HEPWORTH": {"style": "Modernism", "genre": "Sculpture"},
    "DAME ELISABETH FRINK, R.A.": {"style": "Modernism", "genre": "Sculpture"},
    "DAME ELIZABETH BLACKADDER, R.A., R.S.A.": {"style": "Modernism", "genre": "Still Life"},
    "DAME LUCIE RIE": {"style": "Modernism", "genre": "Ceramics"},
    "DAVID BOMBERG": {"style": "Vorticism", "genre": "Abstract"},
    "DERWENT LEES": {"style": "Post-Impressionism", "genre": "Landscape"},
    "DUNCAN GRANT": {"style": "Post-Impressionism", "genre": "Portraiture"},
    "EDWARD WADSWORTH, A.R.A.": {"style": "Vorticism", "genre": "Abstract"},
    "ELIOT HODGKIN": {"style": "Realism", "genre": "Still Life"},
    "EMILY YOUNG": {"style": "Modernism", "genre": "Sculpture"},
    "FRANK AUERBACH": {"style": "Expressionism", "genre": "Portraiture"},
    "GEORGE LESLIE HUNTER": {"style": "Fauvism", "genre": "Still Life"},
    "GERALD LAING": {"style": "Pop Art", "genre": "Figurative"},
    "GRAHAM SUTHERLAND, O.M.": {"style": "Neo-Romanticism", "genre": "Landscape"},
    "GRAYSON PERRY, R.A.": {"style": "Contemporary Art", "genre": "Ceramics"},
    "HELEN BRADLEY": {"style": "Naïve Art", "genre": "Figurative"},
    "HENRY MOORE, O.M., C.H.": {"style": "Modernism", "genre": "Sculpture"},
    "IVON HITCHENS": {"style": "Abstract Art", "genre": "Landscape"},
    "JACK BUTLER YEATS, R.H.A.": {"style": "Expressionism", "genre": "Landscape"},
    "JEFFREY STEELE": {"style": "Geometric Abstraction", "genre": "Abstract"},
    "JEREMY MOON": {"style": "Hard-Edge Abstraction", "genre": "Abstract"},
    "JOAN EARDLEY, R.S.A.": {"style": "Expressionism", "genre": "Landscape"},
    "JOE TILSON, R.A.": {"style": "Pop Art", "genre": "Abstract"},
    "JOHN DUNCAN FERGUSSON": {"style": "Fauvism", "genre": "Portraiture"},
    "JOHN HOYLAND, R.A.": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "JOHN PLUMB": {"style": "Minimalism", "genre": "Abstract"},
    "JOHN TUNNARD, A.R.A.": {"style": "Surrealism", "genre": "Abstract"},
    "JOHN VIRTUE": {"style": "Contemporary Art", "genre": "Landscape"},
    "JOHN WELLS": {"style": "Modernism", "genre": "Abstract"},
    "KEITH VAUGHAN": {"style": "Neo-Romanticism", "genre": "Figurative"},
    "LAURENCE STEPHEN LOWRY, R.A.": {"style": "Naïve Art", "genre": "Urban"},
    "LEON KOSSOFF": {"style": "Expressionism", "genre": "Portraiture"},
    "LYNN CHADWICK, R.A.": {"style": "Modernism", "genre": "Sculpture"},
    "MARK GERTLER": {"style": "Post-Impressionism", "genre": "Portraiture"},
    "MICHAEL KIDNER, R.A.": {"style": "Op Art", "genre": "Abstract"},
    "PATRICK HERON": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "PATRICK PROCKTOR, R.A.": {"style": "Modernism", "genre": "Portraiture"},
    "PAULINE BOTY": {"style": "Pop Art", "genre": "Portraiture"},
    "PETER LANYON": {"style": "Abstract Expressionism", "genre": "Landscape"},
    "PETER ROSE PULHAM": {"style": "Modernism", "genre": "Abstract"},
    "PETER SEDGLEY": {"style": "Op Art", "genre": "Abstract"},
    "PRUNELLA CLOUGH": {"style": "Modernism", "genre": "Urban"},
    "R.B. KITAJ, R.A.": {"style": "Pop Art", "genre": "Figurative"},
    "ROBERT MACBRYDE": {"style": "Cubism", "genre": "Still Life"},
    "RODERIC O'CONOR": {"style": "Post-Impressionism", "genre": "Landscape"},
    "ROGER FRY": {"style": "Post-Impressionism", "genre": "Portraiture"},
    "ROGER HILTON": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "SANDRA BLOW, R.A.": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "SIR ANTHONY CARO, O.M., R.A.": {"style": "Modernism", "genre": "Sculpture"},
    "SIR ANTONY GORMLEY, R.A.": {"style": "Contemporary Art", "genre": "Sculpture"},
    "SIR CEDRIC MORRIS": {"style": "Modernism", "genre": "Still Life"},
    "SIR EDUARDO PAOLOZZI, R.A.": {"style": "Pop Art", "genre": "Sculpture"},
    "SIR FRANK BOWLING, R.A.": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "SIR JOHN LAVERY, R.A., R.S.A., R.H.A.": {"style": "Post-Impressionism", "genre": "Portraiture"},
    "SIR MATTHEW SMITH": {"style": "Fauvism", "genre": "Still Life"},
    "SIR PETER BLAKE, R.A.": {"style": "Pop Art", "genre": "Portraiture"},
    "SIR PETER BLAKE, R.A. AND JANN HAWORTH": {"style": "Pop Art", "genre": "Figurative"},
    "SIR STANLEY SPENCER, R.A.": {"style": "Neo-Romanticism", "genre": "Religious"},
    "SIR TERRY FROST, R.A.": {"style": "Abstract Expressionism", "genre": "Abstract"},
    "SIR WILLIAM NICHOLSON": {"style": "Post-Impressionism", "genre": "Still Life"},
    "STANLEY WILLIAM HAYTER": {"style": "Surrealism", "genre": "Abstract"},
    "STEPHEN CONROY": {"style": "Contemporary Art", "genre": "Portraiture"},
    "SVEN BERLIN": {"style": "Modernism", "genre": "Sculpture"},
    "TRISTRAM HILLIER, R.A.": {"style": "Surrealism", "genre": "Landscape"},
    "VICTOR PASMORE, R.A.": {"style": "Abstract Art", "genre": "Abstract"},
    "WALTER RICHARD SICKERT, A.R.A.": {"style": "Impressionism", "genre": "Urban"},
    "WILHELMINA BARNS-GRAHAM": {"style": "Abstract Art", "genre": "Abstract"},
    "WILLIAM BROOKER, A.R.A.": {"style": "Modernism", "genre": "Still Life"},
    "WILLIAM ROBERTS, R.A.": {"style": "Vorticism", "genre": "Figurative"},
    "WILLIAM SCOTT, R.A.": {"style": "Abstract Expressionism", "genre": "Still Life"},
    "WILLIAM TUCKER": {"style": "Modernism", "genre": "Sculpture"},
    "WINIFRED NICHOLSON": {"style": "Post-Impressionism", "genre": "Still Life"},
    "BAI XUESHI": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "BU NING (1917-2002)": {"style": "Modern Chinese Painting", "genre": "Portrait"},
  "C. C. WANG": {"style": "Contemporary Chinese Art", "genre": "Calligraphy"},
  "CHEN CONGZHOU": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "CHEN FANG": {"style": "Unknown", "genre": "Unknown"},
  "CHEN JIRU": {"style": "Ming Dynasty Art", "genre": "Calligraphy"},
  "CHEN LI": {"style": "Contemporary Art", "genre": "Abstract"},
  "CHEN SHIZENG": {"style": "Modern Chinese Painting", "genre": "Landscape"},
  "CHEN XIAOLIAN": {"style": "Contemporary Art", "genre": "Floral"},
  "CHEN YIXI": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "CHENG JIASUI": {"style": "Ming Dynasty Art", "genre": "Calligraphy"},
  "CHENG SHIFA": {"style": "Modern Chinese Painting", "genre": "Figurative"},
  "DAI XI": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "DENG FEN": {"style": "Guangdong Painting School", "genre": "Portrait"},
  "DING YANYONG": {"style": "Modern Chinese Painting", "genre": "Expressionist"},
  "DONG SHOUPING": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "FAN HAOLIN": {"style": "Unknown", "genre": "Unknown"},
  "FANG JUN": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "FANG ZHAOLING": {"style": "Modern Chinese Painting", "genre": "Landscape"},
  "FENG CHAORAN": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "FENG GUIFEN": {"style": "Unknown", "genre": "Unknown"},
  "FENG YIYIN": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "GAO LONGSHENG": {"style": "Unknown", "genre": "Unknown"},
  "GU LINSHI": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "GU YI": {"style": "Ming Dynasty Art", "genre": "Calligraphy"},
  "HE HUAISHUO": {"style": "Contemporary Art", "genre": "Landscape"},
  "HE ZHUO": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "HUANG DUFENG": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "HUANG HUANWU": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "HUANG JIN": {"style": "Unknown", "genre": "Unknown"},
  "HUANG JUNBI": {"style": "Modern Chinese Painting", "genre": "Landscape"},
  "HUANG MIAOZI": {"style": "Modern Chinese Painting", "genre": "Calligraphy"},
  "HUANG YONGYU": {"style": "Modern Chinese Painting", "genre": "Figurative"},
  "HUANG YUANZHEN": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "HUANG ZHOU": {"style": "Modern Chinese Painting", "genre": "Animal Painting"},
  "HUO CHUNYANG": {"style": "Contemporary Art", "genre": "Calligraphy"},
  "JIANG HE": {"style": "Unknown", "genre": "Unknown"},
  "KANG YOUWEI": {"style": "Modern Chinese Painting", "genre": "Calligraphy"},
  "LI HUAYI": {"style": "Contemporary Art", "genre": "Landscape"},
  "LI XIONGCAI": {"style": "Modern Chinese Painting", "genre": "Landscape"},
  "LI YANSHENG": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "LIN FENGMIAN": {"style": "Modern Chinese Painting", "genre": "Figurative"},
  "LIU HAISU": {"style": "Modern Chinese Painting", "genre": "Landscape"},
  "LOU SHIBAI": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "LÜ YUAN": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "MU'AN XINGTAO": {"style": "Zen Art", "genre": "Calligraphy"},
  "PENG XIANCHENG": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "PU JIN": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "PU RU": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "QI BAISHI": {"style": "Modern Chinese Painting", "genre": "Bird-and-Flower"},
  "QI GONG": {"style": "Modern Chinese Painting", "genre": "Calligraphy"},
  "QI LIANGSI": {"style": "Unknown", "genre": "Unknown"},
  "QIAN SONGYAN": {"style": "Modern Chinese Painting", "genre": "Landscape"},
  "QIAN ZAI": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "QIU YACAI": {"style": "Contemporary Art", "genre": "Portrait"},
  "RAO ZONGYI": {"style": "Modern Chinese Painting", "genre": "Calligraphy"},
  "SHEN QUAN": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "SHEN WEI": {"style": "Contemporary Art", "genre": "Photography"},
  "SHEN XINHAI": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "SHI ZHECUN": {"style": "Modern Chinese Art", "genre": "Literature"},
  "SHIY DE-JINN": {"style": "Modern Chinese Painting", "genre": "Landscape"},
  "SONG WENZHI": {"style": "Modern Chinese Painting", "genre": "Landscape"},
  "SONG XIANG": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "SU LIUPENG": {"style": "Traditional Chinese Painting", "genre": "Portrait"},
  "TAI JINGNONG": {"style": "Modern Chinese Painting", "genre": "Calligraphy"},
  "WANG DAOZHONG": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "WANG DONGLING": {"style": "Contemporary Art", "genre": "Calligraphy"},
  "WANG GEYI": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "WANG QI": {"style": "Modern Chinese Painting", "genre": "Figurative"},
  "WANG QISUN": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "WANG YACHEN": {"style": "Modern Chinese Painting", "genre": "Bird-and-Flower"},
  "WANG YUNWU": {"style": "Modern Chinese Painting", "genre": "Calligraphy"},
  "WANG ZHEN": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "WITH SIGNATURE OF LAN YING": {"style": "Ming Dynasty Art", "genre": "Landscape"},
  "WU CHANGSHUO": {"style": "Modern Chinese Painting", "genre": "Calligraphy"},
  "WU HUFAN": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "WU JINGHENG": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "WU QINGXIA": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "WU XIZAI": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "WU ZHENG": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "WU ZIFU": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "WU ZISHEN": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "WUCIUS WONG": {"style": "Contemporary Art", "genre": "Abstract"},
  "XIE GUANSHENG": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "XIE GUOZHEN": {"style": "Modern Chinese Painting", "genre": "Calligraphy"},
  "XIE ZHILIU": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "XU BAOGUANG": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "XU BEIHONG": {"style": "Modern Chinese Painting", "genre": "Figurative"},
  "YANG SHANSHEN": {"style": "Modern Chinese Painting", "genre": "Animal Painting"},
  "YANG YANWEN": {"style": "Unknown", "genre": "Unknown"},
  "YANG YISUN": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "YE GONGCHAO": {"style": "Modern Chinese Painting", "genre": "Calligraphy"},
  "YI LIXUN": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "YU YOUREN": {"style": "Modern Chinese Painting", "genre": "Calligraphy"},
  "YUAN PEIJI": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "YUAN SHANGTONG": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "ZENG GUOQUAN": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "ZHANG BAIXI": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "ZHANG DAQIAN": {"style": "Modern Chinese Painting", "genre": "Landscape"},
  "ZHANG QUN": {"style": "Unknown", "genre": "Unknown"},
  "ZHANG SHIZHAO": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "ZHANG XIONG": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "ZHANG YUZHAO": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "ZHAO SHAO'ANG": {"style": "Modern Chinese Painting", "genre": "Bird-and-Flower"},
  "ZHAO SHAO’ANG": {"style": "Modern Chinese Painting", "genre": "Bird-and-Flower"},
  "ZHAO SHIGUANG": {"style": "Modern Chinese Painting", "genre": "Figurative"},
  "ZHENG MANQING": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "ZHENG MUKANG": {"style": "Traditional Chinese Painting", "genre": "Bird-and-Flower"},
  "ZHENG XIAOXU": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "ZHOU CEZONG": {"style": "Traditional Chinese Painting", "genre": "Landscape"},
  "ZHU QIZHAN": {"style": "Modern Chinese Painting", "genre": "Landscape"},
  "ZHUANG YAN": {"style": "Traditional Chinese Painting", "genre": "Calligraphy"},
  "ADRIAEN JANSZ. VAN OSTADE": {"style": "Baroque", "genre": "Genre Painting"},
  "ATTRIBUTED TO ANTONIO SUSINI": {"style": "Renaissance", "genre": "Sculpture"},
  "ATTRIBUTED TO MICHAELINA WAUTIER": {"style": "Baroque", "genre": "Portrait"},
  "CLARA PEETERS": {"style": "Baroque", "genre": "Still Life"},
  "EGLON VAN DER NEER": {"style": "Dutch Golden Age", "genre": "Portrait"},
  "ERASMUS QUELLINUS II": {"style": "Baroque", "genre": "Historical Painting"},
  "FRANCESCO HAYEZ": {"style": "Romanticism", "genre": "Historical Painting"},
  "GABRIEL METSU": {"style": "Dutch Golden Age", "genre": "Genre Painting"},
  "GERRIT VAN HONTHORST": {"style": "Baroque", "genre": "Genre Painting"},
  "GIOVANNI BATTISTA TIEPOLO, CALLED GIAMBATTISTA TIEPOLO": {"style": "Rococo", "genre": "Historical Painting"},
  "GIOVANNI MARTINELLI": {"style": "Baroque", "genre": "Religious Painting"},
  "GUSTAVE COURBET": {"style": "Realism", "genre": "Landscape"},
  "JAN BRUEGHEL I": {"style": "Baroque", "genre": "Landscape"},
  "JAN SIBERECHTS": {"style": "Baroque", "genre": "Landscape"},
  "JAN VAN DE CAPPELLE": {"style": "Dutch Golden Age", "genre": "Marine Painting"},
  "JOHANN LISS": {"style": "Baroque", "genre": "Historical Painting"},
  "JOHANNES LINGELBACH": {"style": "Dutch Golden Age", "genre": "Genre Painting"},
  "MICHAEL PETER ANCHER": {"style": "Realism", "genre": "Portrait"},
  "PAOLO VENEZIANO": {"style": "Gothic", "genre": "Religious Painting"},
  "PIETER BRUEGHEL II": {"style": "Renaissance", "genre": "Genre Painting"},
  "SIR PETER PAUL RUBENS": {"style": "Baroque", "genre": "Historical Painting"},
  "SIR THOMAS LAWRENCE, P.R.A.": {"style": "Romanticism", "genre": "Portrait"},
  "THE MASTER OF MONTE OLIVETO": {"style": "Gothic", "genre": "Religious Painting"},
  "WORKSHOP OF PIETRO LORENZETTI": {"style": "Gothic", "genre": "Religious Painting"},
  "AARON CURRY": {"style": "Contemporary", "genre": "Sculpture"},
  "AARON GARBER MAIKOVSKA": {"style": "Contemporary", "genre": "Abstract"},
  "AL HELD": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "AL TAYLOR": {"style": "Contemporary", "genre": "Sculpture"},
  "ALBERT OEHLEN": {"style": "Neo-Expressionism", "genre": "Abstract"},
  "ALEC EGAN": {"style": "Contemporary", "genre": "Still Life"},
  "ALEX BROWN": {"style": "Contemporary", "genre": "Abstract"},
  "ALEX GARDNER": {"style": "Contemporary", "genre": "Figurative"},
  "ALEX HUBBARD": {"style": "Contemporary", "genre": "Mixed Media"},
  "ALEX ISRAEL": {"style": "Contemporary", "genre": "Pop Art"},
  "ALEX KATZ": {"style": "Modern Realism", "genre": "Portrait"},
  "ALEXANDER CALDER": {"style": "Modern", "genre": "Sculpture"},
  "ALEXANDER LIBERMAN": {"style": "Modern", "genre": "Sculpture"},
  "ALINA PEREZ": {"style": "Contemporary", "genre": "Portrait"},
  "ALLAN MCCOLLUM": {"style": "Contemporary", "genre": "Conceptual Art"},
  "ALMA ALLEN": {"style": "Contemporary", "genre": "Sculpture"},
  "ANA PRATA": {"style": "Contemporary", "genre": "Abstract"},
  "ANDRE LANSKOY": {"style": "Tachisme", "genre": "Abstract"},
  "ANDRES SERRANO": {"style": "Contemporary", "genre": "Photography"},
  "ANDY WARHOL": {"style": "Pop Art", "genre": "Portrait"},
  "ANNA LEONHARDT": {"style": "Contemporary", "genre": "Abstract"},
  "ANTONE KÖNST": {"style": "Contemporary", "genre": "Abstract"},
  "ARMAN": {"style": "Nouveau Réalisme", "genre": "Sculpture"},
  "ARNULF RAINER": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "ARTURO HERRERA": {"style": "Contemporary", "genre": "Collage"},
  "AYA TAKANO": {"style": "Superflat", "genre": "Figurative"},
  "BARNABY FURNAS": {"style": "Contemporary", "genre": "Abstract"},
  "BELKIS AYON": {"style": "Contemporary", "genre": "Printmaking"},
  "BERNAR VENET": {"style": "Minimalism", "genre": "Sculpture"},
  "BERNHARD HEILIGER": {"style": "Modern", "genre": "Sculpture"},
  "BEVERLY PEPPER": {"style": "Modern", "genre": "Sculpture"},
  "BOSCO SODI": {"style": "Contemporary", "genre": "Abstract"},
  "BRIAN CALVIN": {"style": "Contemporary", "genre": "Portrait"},
  "BRUCE CONNER": {"style": "Assemblage", "genre": "Mixed Media"},
  "BYRON KIM": {"style": "Contemporary", "genre": "Abstract"},
  "CALLUM INNES": {"style": "Contemporary", "genre": "Abstract"},
  "CHARLES ARNOLDI": {"style": "Contemporary", "genre": "Abstract"},
  "CHARLES BIEDERMAN": {"style": "Constructivism", "genre": "Abstract"},
  "CHARLIE BILLINGHAM": {"style": "Contemporary", "genre": "Figurative"},
  "CHIHO AOSHIMA": {"style": "Superflat", "genre": "Digital Art"},
  "CHRIS OFILI": {"style": "Contemporary", "genre": "Figurative"},
  "CHRISTOPHER WILMARTH": {"style": "Minimalism", "genre": "Sculpture"},
  "CHUN KWANG YOUNG": {"style": "Contemporary", "genre": "Mixed Media"},
  "CINDY SHERMAN": {"style": "Contemporary", "genre": "Photography"},
  "CLAES OLDENBURG": {"style": "Pop Art", "genre": "Sculpture"},
  "CLAIRE TABOURET": {"style": "Contemporary", "genre": "Portrait"},
  "COLDIE": {"style": "Crypto Art", "genre": "Digital Art"},
  "CONRAD MARCA-RELLI": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "COSIMA VON BONIN": {"style": "Contemporary", "genre": "Conceptual Art"},
  "DAN COLEN": {"style": "Contemporary", "genre": "Mixed Media"},
  "DANA AWARTANI": {"style": "Contemporary", "genre": "Islamic Art"},
  "DANIEL GORDON": {"style": "Contemporary", "genre": "Photography"},
  "DANNY FOX": {"style": "Contemporary", "genre": "Figurative"},
  "DAVID ALTMEJD": {"style": "Contemporary", "genre": "Sculpture"},
  "DAVID HAMMONS": {"style": "Contemporary", "genre": "Conceptual Art"},
  "DAVID KRAMER": {"style": "Contemporary", "genre": "Text Art"},
  "DAVID RODRIGUEZ CABALLERO": {"style": "Contemporary", "genre": "Sculpture"},
  "DAVID SALLE": {"style": "Postmodernism", "genre": "Mixed Media"},
  "DAVID SMITH": {"style": "Abstract Expressionism", "genre": "Sculpture"},
  "DAWOUD BEY": {"style": "Contemporary", "genre": "Photography"},
  "DEBORAH KASS": {"style": "Contemporary", "genre": "Pop Art"},
  "DEBORAH ROBERTS": {"style": "Contemporary", "genre": "Collage"},
  "DEVIN TROY STROTHER": {"style": "Contemporary", "genre": "Mixed Media"},
  "DJORDJE OZBOLT": {"style": "Contemporary", "genre": "Figurative"},
  "DMITRI CHERNIAK": {"style": "Crypto Art", "genre": "Generative Art"},
  "DON EDDY": {"style": "Photorealism", "genre": "Still Life"},
  "DONALD BAECHLER": {"style": "Neo-Expressionism", "genre": "Abstract"},
  "DOROTHEA ROCKBURNE": {"style": "Minimalism", "genre": "Abstract"},
   "ED MOSES": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "ED RUSCHA": {"style": "Pop Art", "genre": "Text Art"},
  "EDDIE ARROYO": {"style": "Contemporary", "genre": "Figurative"},
  "EDGAR PLANS": {"style": "Contemporary", "genre": "Figurative"},
  "EMIL LUKAS": {"style": "Contemporary", "genre": "Abstract"},
  "ENOC PEREZ": {"style": "Contemporary", "genre": "Figurative"},
  "ERIC FISCHL": {"style": "Contemporary", "genre": "Figurative"},
  "ERIK PARKER": {"style": "Contemporary", "genre": "Abstract"},
  "ESTEBAN VICENTE": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "ESTHER MAHLANGU": {"style": "Ndebele Art", "genre": "Abstract"},
  "EVAN HOLLOWAY": {"style": "Contemporary", "genre": "Sculpture"},
  "FARIS MCREYNOLDS": {"style": "Contemporary", "genre": "Figurative"},
  "FLORIAN MAIER-AICHEN": {"style": "Contemporary", "genre": "Photography"},
  "FRANCESCO CLEMENTE": {"style": "Neo-Expressionism", "genre": "Figurative"},
  "FRANK GEHRY": {"style": "Deconstructivism", "genre": "Architecture"},
  "FRANK STELLA": {"style": "Minimalism", "genre": "Abstract"},
  "FRANZ KLINE": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "FRIEDEL DZUBAS": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "GABRIEL OROZCO": {"style": "Contemporary", "genre": "Conceptual Art"},
  "GARRY FABIAN MILLER": {"style": "Contemporary", "genre": "Photography"},
  "GARRY WINOGRAND": {"style": "Modern", "genre": "Photography"},
  "GENESIS TRAMAINE": {"style": "Contemporary", "genre": "Figurative"},
  "GEORGE CONDO": {"style": "Contemporary", "genre": "Figurative"},
  "GEORGE RICKEY": {"style": "Modern", "genre": "Kinetic Sculpture"},
  "GERASIMOS FLORATOS": {"style": "Contemporary", "genre": "Figurative"},
  "GHADA AMER": {"style": "Contemporary", "genre": "Mixed Media"},
  "GILBERT & GEORGE": {"style": "Contemporary", "genre": "Conceptual Art"},
  "GILLIAN AYRES": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "GRANT HAFFNER": {"style": "Contemporary", "genre": "Landscape"},
  "GREGOR HILDEBRANDT": {"style": "Contemporary", "genre": "Mixed Media"},
  "HANNELORE BARON": {"style": "Modern", "genre": "Collage"},
  "HANS HOFMANN": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "HARLAND MILLER": {"style": "Contemporary", "genre": "Text Art"},
  "HARMONY KORINE": {"style": "Contemporary", "genre": "Mixed Media"},
  "HERNAN BAS": {"style": "Contemporary", "genre": "Figurative"},
  "HIROSHI SUGIMOTO": {"style": "Contemporary", "genre": "Photography"},
  "HUANG GANG": {"style": "Contemporary", "genre": "Mixed Media"},
  "HUGH SCOTT-DOUGLAS": {"style": "Contemporary", "genre": "Abstract"},
  "HUGO MCCLOUD": {"style": "Contemporary", "genre": "Mixed Media"},
  "ILIT AZOULAY": {"style": "Contemporary", "genre": "Photography"},
  "ILONA SZWARC": {"style": "Contemporary", "genre": "Photography"},
  "ISRAEL LUND": {"style": "Contemporary", "genre": "Abstract"},
  "JACK HAMILTON BUSH": {"style": "Color Field", "genre": "Abstract"},
  "JACK PIERSON": {"style": "Contemporary", "genre": "Photography"},
  "JACK ROTH": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "JACOB HASHIMOTO": {"style": "Contemporary", "genre": "Sculpture"},
  "JAMES CASEBERE": {"style": "Contemporary", "genre": "Photography"},
  "JAMES WEEKS": {"style": "Bay Area Figurative", "genre": "Figurative"},
  "JAMES WHITE": {"style": "Contemporary", "genre": "Hyperrealism"},
  "JAMIAN JULIANO-VILLANI": {"style": "Contemporary", "genre": "Figurative"},
  "JAMMIE HOLMES": {"style": "Contemporary", "genre": "Figurative"},
  "JAN MÜLLER": {"style": "Expressionism", "genre": "Figurative"},
  "JAUME PLENSA": {"style": "Contemporary", "genre": "Sculpture"},
  "JAUNE QUICK-TO-SEE SMITH": {"style": "Contemporary", "genre": "Figurative"},
  "JEAN DUBUFFET": {"style": "Art Brut", "genre": "Figurative"},
  "JEAN-BAPTISTE BERNADET": {"style": "Contemporary", "genre": "Abstract"},
  "JEAN-MICHEL BASQUIAT": {"style": "Neo-Expressionism", "genre": "Figurative"},
  "JEFF ELROD": {"style": "Contemporary", "genre": "Abstract"},
  "JENNIFER GIUDI": {"style": "Contemporary", "genre": "Abstract"},
  "JENNIFER STEINKAMP": {"style": "Contemporary", "genre": "Digital Art"},
  "JENNY HOLZER": {"style": "Conceptual Art", "genre": "Text Art"},
  "JESSE DRAXLER": {"style": "Contemporary", "genre": "Collage"},
  "JIM DINE": {"style": "Pop Art", "genre": "Mixed Media"},
  "JIM HODGES": {"style": "Contemporary", "genre": "Sculpture"},
  "JOHN ARMLEDER": {"style": "Contemporary", "genre": "Mixed Media"},
  "JOHN GRAHAM": {"style": "Modern", "genre": "Portrait"},
  "JOHN KACERE": {"style": "Photorealism", "genre": "Figurative"},
  "JOHN NIETO": {"style": "Contemporary", "genre": "Native American Art"},
  "JOHN WALKER": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "JOHN WESLEY": {"style": "Pop Art", "genre": "Figurative"},
  "JON KUHN": {"style": "Contemporary", "genre": "Glass Art"},
  "JONATHAN LASKER": {"style": "Contemporary", "genre": "Abstract"},
  "JONATHAN LYNDON CHASE": {"style": "Contemporary", "genre": "Figurative"},
  "JONATHAN MEESE": {"style": "Neo-Expressionism", "genre": "Figurative"},
  "JORDY KERWICK": {"style": "Contemporary", "genre": "Figurative"},
  "JOSEPH BEUYS": {"style": "Conceptual Art", "genre": "Mixed Media"},
  "JOSEPH CORNELL": {"style": "Surrealism", "genre": "Assemblage"},
  "JOSH SMITH": {"style": "Contemporary", "genre": "Abstract"},
  "JUAN USLE": {"style": "Contemporary", "genre": "Abstract"},
  "JUDITH SHEA": {"style": "Contemporary", "genre": "Sculpture"},
  "JULES OLITSKI": {"style": "Color Field", "genre": "Abstract"},
  "JULIAN HOEBER": {"style": "Contemporary", "genre": "Mixed Media"},
  "JULIAN OPIE": {"style": "Contemporary", "genre": "Figurative"},
  "JULIÃO SARMENTO": {"style": "Contemporary", "genre": "Mixed Media"},
  "JÖRG IMMENDORFF": {"style": "Neo-Expressionism", "genre": "Figurative"},
  "KAREL APPEL": {"style": "CoBrA", "genre": "Abstract"},
  "KAREN KILIMNIK": {"style": "Contemporary", "genre": "Mixed Media"},
  "KARL KNATHS": {"style": "Modern", "genre": "Abstract"},
  "KATHERINE BERNHARDT": {"style": "Contemporary", "genre": "Pop Art"},
  "KATHRYN ANDREWS": {"style": "Contemporary", "genre": "Conceptual Art"},
  "KEITH TYSON": {"style": "Contemporary", "genre": "Mixed Media"},
  "KELLEY WALKER": {"style": "Contemporary", "genre": "Conceptual Art"},
  "KIKI SMITH": {"style": "Contemporary", "genre": "Sculpture"},
  "KIKI WANG": {"style": "Contemporary", "genre": "Portrait"},
  "KIM DORLAND": {"style": "Contemporary", "genre": "Landscape"},
  "KIM JOON": {"style": "Contemporary", "genre": "Digital Art"},
  "KON TRUBKOVICH": {"style": "Contemporary", "genre": "Mixed Media"},
  "KOUR POUR": {"style": "Contemporary", "genre": "Abstract"},
  "KSENIA DERMENZHI": {"style": "Contemporary", "genre": "Figurative"},
  "LARRY BELL": {"style": "Minimalism", "genre": "Sculpture"},
  "LARRY RIVERS": {"style": "Pop Art", "genre": "Figurative"},
  "LAURE MARY-COUÉGNIAS": {"style": "Contemporary", "genre": "Figurative"},
  "LAURIE SIMMONS": {"style": "Contemporary", "genre": "Photography"},
  "LE PHO": {"style": "Modern", "genre": "Figurative"},
  "LEANDRO ERLICH": {"style": "Contemporary", "genre": "Installation Art"},
  "LORIEL BELTRÁN": {"style": "Contemporary", "genre": "Abstract"},
  "LORNA SIMPSON": {"style": "Contemporary", "genre": "Photography"},
  "LOUISA MATTHÍASDÓTTIR": {"style": "Modern", "genre": "Landscape"},
  "LOUISE NEVELSON": {"style": "Abstract Expressionism", "genre": "Sculpture"},
  "LUCAS SAMARAS": {"style": "Modern", "genre": "Photography"},
  "LUCIANO CASTELLI": {"style": "Neo-Expressionism", "genre": "Figurative"},
  "LUCIO FONTANA": {"style": "Spatialism", "genre": "Abstract"},
  "LYMAN KIPP": {"style": "Minimalism", "genre": "Sculpture"},
  "LYNNE DREXLER": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "MANOLO VALDES": {"style": "Contemporary", "genre": "Figurative"},
  "MANUEL NERI": {"style": "Modern", "genre": "Sculpture"},
  "MARGARET KILGALLEN": {"style": "Contemporary", "genre": "Street Art"},
  "MARIUS BERCEA": {"style": "Contemporary", "genre": "Landscape"},
  "MARK INNERST": {"style": "Contemporary", "genre": "Abstract"},
  "MARK LOMBARDI": {"style": "Contemporary", "genre": "Conceptual Art"},
  "MARTIN KIPPENBERGER": {"style": "Neo-Expressionism", "genre": "Mixed Media"},
  "MASSIMO VITALI": {"style": "Contemporary", "genre": "Photography"},
  "MATTHIAS WEISCHER": {"style": "Contemporary", "genre": "Figurative"},
  "MEL BOCHNER": {"style": "Conceptual Art", "genre": "Text Art"},
  "MICHAEL HEIZER": {"style": "Land Art", "genre": "Sculpture"},
  "MICHAEL KAGAN": {"style": "Contemporary", "genre": "Figurative"},
  "MICKALENE THOMAS": {"style": "Contemporary", "genre": "Portrait"},
  "MIRANDA LICHTENSTEIN": {"style": "Contemporary", "genre": "Photography"},
  "MURJONI MERRIWEATHER": {"style": "Contemporary", "genre": "Figurative"},
  "NAN GOLDIN": {"style": "Contemporary", "genre": "Photography"},
  "NANCY GRAVES": {"style": "Post-Minimalism", "genre": "Sculpture"},
  "NATHALIE BOUTTÉ": {"style": "Contemporary", "genre": "Collage"},
  "NEGYEM ADONOO": {"style": "Contemporary", "genre": "Abstract"},
  "NNENNA OKORE": {"style": "Contemporary", "genre": "Sculpture"},
  "NOBUYOSHI ARAKI": {"style": "Contemporary", "genre": "Photography"},
  "NORMAN BLUHM": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "PAE WHITE": {"style": "Contemporary", "genre": "Installation Art"},
  "PATRICIA AYRES": {"style": "Contemporary", "genre": "Sculpture"},
  "PAUL JENKINS": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "PAUL PFEIFFER": {"style": "Contemporary", "genre": "Video Art"},
  "PAUL WONNER": {"style": "Bay Area Figurative", "genre": "Figurative"},
  "PAULINA OLOWSKA": {"style": "Contemporary", "genre": "Figurative"},
  "PHILIP PEARLSTEIN": {"style": "Realism", "genre": "Portrait"},
  "PHILIP TAAFFE": {"style": "Contemporary", "genre": "Abstract"},
  "PIERO DORAZIO": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "PIERRE ALECHINSKY": {"style": "CoBrA", "genre": "Abstract"},
  "RACHEL HARRISON": {"style": "Contemporary", "genre": "Sculpture"},
  "RAFFI KALENDERIAN": {"style": "Contemporary", "genre": "Portrait"},
  "RAINER FETTING": {"style": "Neo-Expressionism", "genre": "Figurative"},
  "RALPH GOINGS": {"style": "Photorealism", "genre": "Still Life"},
  "RAY JOHNSON": {"style": "Pop Art", "genre": "Collage"},
  "RAYMOND PETTIBON": {"style": "Contemporary", "genre": "Figurative"},
  "RED GROOMS": {"style": "Pop Art", "genre": "Figurative"},
  "REENA SPAULINGS": {"style": "Contemporary", "genre": "Conceptual Art"},
  "REGGIE BURROWS HODGES": {"style": "Contemporary", "genre": "Figurative"},
  "RETNA": {"style": "Contemporary", "genre": "Street Art"},
  "RICHARD ALDRICH": {"style": "Contemporary", "genre": "Abstract"},
  "RICHARD ANUSZKIEWICZ": {"style": "Op Art", "genre": "Abstract"},
  "RICHARD DEACON": {"style": "Contemporary", "genre": "Sculpture"},
  "RICHARD PETTIBONE": {"style": "Appropriation Art", "genre": "Mixed Media"},
  "RICHARD PRINCE": {"style": "Contemporary", "genre": "Conceptual Art"},
  "ROB PRUITT": {"style": "Contemporary", "genre": "Pop Art"},
  "ROBERT GRAHAM": {"style": "Modern", "genre": "Sculpture"},
  "ROBERT MOSKOWITZ": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "ROBERT MOTHERWELL": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "ROBERT POLIDORI": {"style": "Contemporary", "genre": "Photography"},
  "ROBERT RAUSCHENBERG": {"style": "Pop Art", "genre": "Mixed Media"},
  "ROMARE BEARDEN": {"style": "Modern", "genre": "Collage"},
  "RONI HORN": {"style": "Contemporary", "genre": "Sculpture"},
  "ROSEMARIE TROCKEL": {"style": "Contemporary", "genre": "Mixed Media"},
  "ROSS BLECKNER": {"style": "Contemporary", "genre": "Abstract"},
  "ROXY PAINE": {"style": "Contemporary", "genre": "Sculpture"},
  "ROY LICHTENSTEIN": {"style": "Pop Art", "genre": "Figurative"},
  "RUUD VAN EMPEL": {"style": "Contemporary", "genre": "Photography"},
  "SALOMÉ": {"style": "Neo-Expressionism", "genre": "Figurative"},
  "SAM FRANCIS": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "SANDRO CHIA": {"style": "Neo-Expressionism", "genre": "Figurative"},
  "SCOTT KAHN": {"style": "Contemporary", "genre": "Figurative"},
  "SCOUT ZABINSKI": {"style": "Contemporary", "genre": "Figurative"},
  "SHEPARD FAIREY": {"style": "Street Art", "genre": "Political Art"},
  "SHIRIN NESHAT": {"style": "Contemporary", "genre": "Photography"},
  "SIMON STARLING": {"style": "Contemporary", "genre": "Conceptual Art"},
  "SNOWFRO": {"style": "Crypto Art", "genre": "Generative Art"},
  "SOREL ETROG": {"style": "Modern", "genre": "Sculpture"},
  "SQUEAK CARNWATH": {"style": "Contemporary", "genre": "Mixed Media"},
  "STANLEY WHITNEY": {"style": "Contemporary", "genre": "Abstract"},
  "STEPHAN BALKENHOL": {"style": "Contemporary", "genre": "Sculpture"},
  "STERLING RUBY": {"style": "Contemporary", "genre": "Mixed Media"},
  "SU SU": {"style": "Contemporary", "genre": "Figurative"},
  "SUZANNE MCCLELLAND": {"style": "Contemporary", "genre": "Abstract"},
  "SYLVIE FLEURY": {"style": "Contemporary", "genre": "Conceptual Art"},
  "SZABOLCS BOZÓ": {"style": "Contemporary", "genre": "Figurative"},
  "TAMMAM AZZAM": {"style": "Contemporary", "genre": "Digital Art"},
  "TARA DONOVAN": {"style": "Contemporary", "genre": "Sculpture"},
  "TERRY WINTERS": {"style": "Contemporary", "genre": "Abstract"},
  "THANH BINH NGUYEN": {"style": "Contemporary", "genre": "Portrait"},
  "THIERRY NOIR": {"style": "Street Art", "genre": "Figurative"},
  "THILO HEINZMANN": {"style": "Contemporary", "genre": "Abstract"},
  "THOMAS HELBIG": {"style": "Contemporary", "genre": "Mixed Media"},
  "THOMAS HOUSEAGO": {"style": "Contemporary", "genre": "Sculpture"},
  "THOMAS NOZKOWSKI": {"style": "Contemporary", "genre": "Abstract"},
  "THOMAS RUFF": {"style": "Contemporary", "genre": "Photography"},
  "THRUSH HOLMES": {"style": "Contemporary", "genre": "Abstract"},
  "TIM ROLLINS": {"style": "Contemporary", "genre": "Conceptual Art"},
  "TOM SACHS": {"style": "Contemporary", "genre": "Sculpture"},
  "TOM WESSELMANN": {"style": "Pop Art", "genre": "Figurative"},
  "TOMMASO CASCELLA": {"style": "Contemporary", "genre": "Abstract"},
  "TOMOO GOKITA": {"style": "Contemporary", "genre": "Abstract"},
  "TREY ABDELLA": {"style": "Contemporary", "genre": "Figurative"},
  "TYLER HOBBS": {"style": "Generative Art", "genre": "Abstract"},
  "URS FISCHER": {"style": "Contemporary", "genre": "Sculpture"},
  "VAUGHN SPANN": {"style": "Contemporary", "genre": "Abstract"},
  "VIBHA GALHOTRA": {"style": "Contemporary", "genre": "Environmental Art"},
  "VICTORIA MARTINEZ": {"style": "Contemporary", "genre": "Mixed Media"},
  "VIK MUNIZ": {"style": "Contemporary", "genre": "Photography"},
  "VOJTĚCH KOVAŘÍK": {"style": "Contemporary", "genre": "Figurative"},
  "WADE GUYTON": {"style": "Contemporary", "genre": "Digital Art"},
  "WALEAD BESHTY": {"style": "Contemporary", "genre": "Photography"},
  "WANGECHI MUTU": {"style": "Contemporary", "genre": "Collage"},
  "WILHELM SASNAL": {"style": "Contemporary", "genre": "Figurative"},
  "WILLEM DE KOONING": {"style": "Abstract Expressionism", "genre": "Abstract"},
  "WILLIAM KENTRIDGE": {"style": "Contemporary", "genre": "Animation"},
  "WILLIAM THEOPHILUS BROWN": {"style": "Bay Area Figurative", "genre": "Figurative"},
  "WILLIAM TURNBULL": {"style": "Modern", "genre": "Sculpture"},
  "XAVIERA SIMMONS": {"style": "Contemporary", "genre": "Mixed Media"},
  "YESIYU ZHAO": {"style": "Contemporary", "genre": "Abstract"},
  "YOUNG-IL AHN": {"style": "Contemporary", "genre": "Abstract"},
  "YUKULTJI NAPANGATI": {"style": "Indigenous Australian Art", "genre": "Abstract"},
  "ZACHARY ARMSTRONG": {"style": "Contemporary", "genre": "Abstract"},
  "ZANELE MUHOLI": {"style": "Contemporary", "genre": "Photography"}
  

}



# Словарь художников и их стран
artists_countries = {
    "DIETZ EDZARD": "Germany",
    "EMMANUEL MANE-KATZ": "Ukraine",
    "JULES PASCIN": "Bulgaria",
    "HENRI HAYDEN": "Poland",
    "GEORG KOLBE": "Germany",
    "ARISTIDE MAILLOL": "France",
    "ERNST BARLACH": "Germany",
    "EMILE-ANTOINE BOURDELLE": "France",
    "HENRI CHARLES MANGUIN": "France",
    "PIERRE-AUGUSTE RENOIR AND RICHARD GUINO": "France",
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
    "TIMO NASSERI": "Iran",
    "ADA GILMORE CHAFFEE": "United States",
    "ADOLF ARTHUR DEHN": "United States",
    "ADOLPH GOTTLIEB": "United States",
    "AFTER JOAN MITCHELL": "United States",
    "AFTER MARC CHAGALL BY CHARLES SORLIER": "France",
    "AFTER RENÉ MAGRITTE": "Belgium",
    "AFTER WINSLOW HOMER": "United States",
    "AL HELD": "United States",
    "ALBERT BARKER": "United States",
    "ALICE AYCOCK": "United States",
    "ANGELO PINTO": "United States",
    "ARMAND SEGUIN": "France",
    "ARMIN LANDECK": "United States",
    "ARNALDO POMODORO": "Italy",
    "ARNOLD RÖNNEBECK": "Germany",
    "ARTHUR WESLEY DOW": "United States",
    "AUGUSTA PAYNE BRIGGS RATHBONE": "United States",
    "BORIS ARTZYBASHEFF": "United States",
    "BROR JULIUS OLSSON NORDFELDT": "United States",
    "BRUCE NAUMAN": "United States",
    "CAMILLE PISSARRO": "France",
    "CHARLES BARKER": "United States",
    "CHARLES F. WILLIAM MIELATZ": "United States",
    "CHARLES TURZAK": "United States",
    "CHILDE HASSAM": "United States",
    "CHUCK CLOSE": "United States",
    "CLAES OLDENBURG": "United States",
    "DAVID HOCKNEY": "United Kingdom",
    "DIEGO RIVERA": "Mexico",
    "DIETER ROTH": "Germany",
    "DON FREEMAN": "United States",
    "DONALD JUDD": "United States",
    "DONALD STANLEY VOGEL": "United States",
    "EDGAR CHAHINE": "France",
    "EDOUARD VUILLARD": "France",
    "ELLSWORTH KELLY": "United States",
    "ENZO CUCCHI": "Italy",
    "ERIC FISCHL": "United States",
    "FRANK DUVENECK": "United States",
    "FRANK MORLEY FLETCHER": "United Kingdom",
    "FRANK STELLA": "United States",
    "FRITZ EICHENBERG": "Germany",
    "FÉLIX BRACQUEMOND": "France",
    "GENE DAVIS": "United States",
    "GENE KLOSS": "United States",
    "GEORGE SEGAL": "United States",
    "GEORGE TOOKER": "United States",
    "GEORGE WESLEY BELLOWS": "United States",
    "GEORGES ROUAULT": "France",
    "GLENN COLEMAN": "United States",
    "GRANT WOOD": "United States",
    "HANS BURKHARDT": "United States",
    "HARRY BRODSKY": "United States",
    "HARRY STERNBERG": "United States",
    "HELEN HYDE": "United States",
    "HELEN LUNDEBERG": "United States",
    "HENRI DE TOULOUSE-LAUTREC": "France",
    "HENRI MATISSE": "France",
    "HENRY MOORE": "United Kingdom",
    "HOWARD COOK": "United States",
    "HOWARD HODGKIN": "United Kingdom",
    "ISAC FRIEDLANDER": "United States",
    "JACQUES VILLON": "France",
    "JAMES JACQUES JOSEPH TISSOT": "France",
    "JAMES MCNEILL WHISTLER": "United States",
    "JAMES ROSENQUIST": "United States",
    "JEAN ARP": "France",
    "JEAN DUBUFFET": "France",
    "JEAN-BAPTISTE CAMILLE COROT": "France",
    "JEFF KOONS": "United States",
    "JIM DINE": "United States",
    "JIM DINE AND RON PADGETT": "United States",
    "JOAN MIRÓ": "Spain",
    "JOE JONES": "United States",
    "JOHN EDGAR PLATT": "United Kingdom",
    "JOHN FERREN": "United States",
    "KER-XAVIER ROUSSEL": "France",
     "LUDWIG SANDER": "United States",
    "PIERRE-AUGUSTE RENOIR": "France",
    "MILTON AVERY": "United States",
    "MIGUEL COVARRUBIAS": "Mexico",
    "LEONARD BASKIN": "United States",
    "PAUL CADMUS": "United States",
    "LUIS ARENAL": "Mexico",
    "MUIRHEAD BONE": "United Kingdom",
    "STEVAN DOHANOS": "United States",
    "LETTERIO CALAPAI": "United States",
    "RED GROOMS": "United States",
    "WERNER DREWES": "Germany",
    "MAURICE JACQUE": "France",
    "LEONARD EDMONDSON": "United States",
    "KERR EBY": "Canada",
    "JOHN STOCKTON DE MARTELLY": "United States",
    "WHARTON ESHERICK": "United States",
    "STANLEY WILLIAM HAYTER": "United Kingdom",
    "ROCKWELL KENT": "United States",
    "WANDA GÁG": "United States",
    "RIVA HELFOND": "United States",
    "KÄTHE KOLLWITZ": "Germany",
    "PETER KRASNOW": "United States",
    "YASUO KUNIYOSHI": "Japan",
    "LAWRENCE KUPFERMAN": "United States",
    "PAUL LANDACRE": "United States",
    "OTTO LANGE": "Germany",
    "REGINALD MARSH": "United States",
    "STOW WENGENROTH": "United States",
    "THOMAS MORAN": "United States",
    "JOHN HENRY BRADLEY STORRS": "United States",
    "KENNETH HAYES MILLER": "United States",
    "ROBERT RAUSCHENBERG": "United States",
    "WILLIAM SELTZER RICE": "United States",
    "ROBERT RIGGS": "United States",
    "WILLIAM SAMUEL SCHWARTZ": "United States",
    "MILLARD OWEN SHEETS": "United States",
    "JOHN SLOAN": "United States",
    "LAWRENCE BEALL SMITH": "United States",
    "NILES SPENCER": "United States",
    "MAX WEBER": "United States",
    "WILLIAM ZORACH": "United States",
    "RICHARD ANUSZKIEWICZ": "United States",
    "THEODORE WHITE": "United States",
    "PIERRE BONNARD": "France",
    "MARC CHAGALL": "France",
    "JOSEF ALBERS": "Germany",
    "KAREL APPEL": "Netherlands",
    "GEORGE WESLEY BELLOWS": "United States",
    "ROMARE BEARDEN": "United States",
    "LYNN CHADWICK": "United Kingdom",
    "LOUISE BOURGEOIS": "France",
    "LEE BONTECOU": "United States",
    "MARY CASSATT": "United States",
    "JOSEPH CORNELL": "United States",
    "STUART DAVIS": "United States",
    "PETER DOIG": "Scotland",
    "MAX ERNST": "Germany",
    "MAURICE DENIS": "France",
    "LÉONARD TSUGUHARU FOUJITA": "France",
    "RICHARD HAMILTON": "United Kingdom",
    "ROY LICHTENSTEIN": "United States",
    "ROBERT INDIANA": "United States",
    "ROBERTO MATTA": "Chile",
    "ROBERT MANGOLD": "United States",
    "PABLO PICASSO": "Spain",
    "KENNETH NOLAND": "United States",
    "LOUISE NEVELSON": "United States",
    "ROBERT MOTHERWELL": "United States",
    "AFTER FERNAND LEGER": "France",
    "AFTER PAUL GAUGUIN": "France",
    "ALBERT GLEIZES": "France",
    "ALBERT MARQUET": "France",
    "ALBERTO GIACOMETTI": "Switzerland",
    "ALEXEJ VON JAWLENSKY": "Russia",
    "ALFRED SISLEY": "France",
    "ANDRE DERAIN": "France",
    "ANDRE LHOTE": "France",
    "ARMAND GUILLAUMIN": "France",
    "AUGUSTE RODIN": "France",
    "BERNARD BUFFET": "France",
    "EDOUARD VUILLARD": "France",
    "EMILE OTHON FRIESZ": "France",
    "EUGENE BOUDIN": "France",
    "FERNAND LEGER": "France",
    "FERNANDO BOTERO": "Colombia",
    "FRANCOISE GILOT": "France",
    "GEORGES LEMMEN": "Belgium",
    "GIORGIO DE CHIRICO": "Italy",
    "GUSTAVE LOISEAU": "France",
    "HENRI FANTIN-LATOUR": "France",
    "HENRI HAYDEN": "Poland",
    "HENRI LAURENS": "France",
    "HENRI LE SIDANER": "France",
    "HENRI LEBASQUE": "France",
    "HENRI MARTIN": "France",
    "HENRY MOORE": "United Kingdom",
    "HENRY MORET": "France",
    "JACQUES LIPCHITZ": "Lithuania",
    "JEAN ARP": "Germany",
    "JEAN DUFY": "France",
    "JEAN-PIERRE CASSIGNEUL": "France",
    "JOAN MIRO": "Spain",
    "JOSEPH CSAKY": "Hungary",
    "KAY SAGE": "United States",
    "KEES VAN DONGEN": "Netherlands",
    "LEONORA CARRINGTON": "United Kingdom",
    "LEOPOLD SURVAGE": "Russia",
    "LOUIS MARCOUSSIS": "Poland",
    "LOUIS VALTAT": "France",
    "MAN RAY": "United States",
    "MARC CHAGALL": "Belarus",
    "MARINO MARINI": "Italy",
    "MAURICE DE VLAMINCK": "France",
    "MAURICE UTRILLO": "France",
    "MAXIMILIEN LUCE": "France",
    "ODILON REDON": "France",
    "PIERRE BONNARD": "France",
    "PIERRE-AUGUSTE RENOIR": "France",
    "RAOUL DUFY": "France",
    "SUZANNE VALADON": "France",
    "VICTOR BRAUNER": "Romania",
    "ALBERT ANDRE": "France",
  "ALBERT GLEIZES": "France",
  "ALBERTO GIACOMETTI": "Switzerland",
  "ALEXANDER ARCHIPENKO": "Ukraine",
  "ARISTIDE MAILLOL": "France",
  "BALTHUS": "Switzerland",
  "BERNARD BUFFET": "France",
  "BERTHE MORISOT": "France",
  "CAMILLE PISSARRO": "France",
  "CHILDE HASSAM": "United States",
  "EDGAR DEGAS": "France",
  "EDOUARD VUILLARD": "France",
  "EGON SCHIELE": "Austria",
  "EMIL NOLDE": "Germany",
  "FERDINAND-VICTOR-EUGENE DELACROIX": "France",
  "FERNAND LEGER": "France",
  "FRANTISEK KUPKA": "Czech Republic",
  "GEORGE GROSZ": "Germany",
  "GEORGES VALMIER": "France",
  "HENRI MATISSE": "France",
  "HENRY MOORE": "United Kingdom",
  "HONORE DAUMIER": "France",
  "JACQUES LIPCHITZ": "Lithuania",
  "JEAN DUFY": "France",
  "JOAN MIRO": "Spain",
  "LEONARD TSUGUHARU FOUJITA": "Japan",
  "LYONEL FEININGER": "Germany",
  "MANE-KATZ": "Ukraine",
  "MARC CHAGALL": "Belarus",
  "MARIE LAURENCIN": "France",
  "MARINO MARINI": "Italy",
  "MARY CASSATT": "United States",
  "MAURICE DE VLAMINCK": "France",
  "MAX ERNST": "Germany",
  "MAXIMILIEN LUCE": "France",
  "OSSIP ZADKINE": "Belarus",
  "PABLO PICASSO": "Spain",
  "PAUL SIGNAC": "France",
  "PIERRE BONNARD": "France",
  "PIERRE-AUGUSTE RENOIR": "France",
  "ROBERT DELAUNAY": "France",
  "WASSILY KANDINSKY": "Russia",
  "ALEXANDER ARCHIPENKO": "Ukraine",
    "ANDY WARHOL": "United States",
    "DAVID SALLE": "United States",
    "EDGAR DEGAS": "France",
    "FRANCIS PICABIA": "France",
    "FRANTISEK KUPKA": "Czech Republic",
    "GASTON LACHAISE": "France",
    "GEORGE GROSZ": "Germany",
    "GEORGES VANTONGERLOO": "Belgium",
    "HANS HOFMANN": "Germany",
    "HENRI MATISSE": "France",
    "JACK YOUNGERMAN": "United States",
    "JACQUES LIPCHITZ": "Lithuania",
    "JEAN DUBUFFET": "France",
    "JEAN HELION": "France",
    "JOSEPH STELLA": "Italy",
    "KAZIMIR MALEVICH": "Ukraine",
    "KENNETH NOLAND": "United States",
    "LARRY RIVERS": "United States",
    "LE CORBUSIER": "Switzerland",
    "LOUIS MARCOUSSIS": "Poland",
    "MAN RAY": "United States",
    "MORGAN RUSSELL": "United States",
    "OLEKSANDR BOHOMAZOV": "Ukraine",
    "PABLO PICASSO": "Spain",
    "RENE MAGRITTE": "Belgium",
    "RICHARD LINDNER": "Germany",
    "SONIA DELAUNAY": "Ukraine",
    "THEO VAN DOESBURG": "Netherlands",
    "VASYL YERMILOV": "Ukraine",
    "WANG KEPING": "China",
    "YVES KLEIN": "France",
    "YVES TANGUY": "France",
      "ADRIAN HENRI": "United Kingdom",
  "ALAN LOWNDES": "United Kingdom",
  "ALFRED WALLIS": "United Kingdom",
  "ANNE ESTELLE RICE": "United States",
  "ANNE REDPATH, A.R.A.": "United Kingdom",
  "ANTONY DONALDSON": "United Kingdom",
  "AUGUSTUS JOHN, O.M., C.H.": "United Kingdom",
  "AUGUSTUS JOHN, O.M., R.A.": "United Kingdom",
  "BEN NICHOLSON, O.M.": "United Kingdom",
  "BERNARD MEADOWS, R.A.": "United Kingdom",
  "BRYAN WYNTER": "United Kingdom",
  "CELIA PAUL": "United Kingdom",
  "CHARLES GINNER, A.R.A.": "United Kingdom",
  "CHRISTOPHER BRAMHAM": "United Kingdom",
  "CHRISTOPHER RICHARD WYNNE NEVINSON, A.R.A.": "United Kingdom",
  "CHRISTOPHER WOOD": "United Kingdom",
  "CLIVE BARKER": "United Kingdom",
  "CRAIGIE AITCHISON, R.A.": "United Kingdom",
  "DAME BARBARA HEPWORTH": "United Kingdom",
  "DAME ELISABETH FRINK, R.A.": "United Kingdom",
  "DAME ELIZABETH BLACKADDER, R.A., R.S.A.": "United Kingdom",
  "DAME LUCIE RIE": "Austria",
  "DAVID BOMBERG": "United Kingdom",
  "DERWENT LEES": "United Kingdom",
  "DUNCAN GRANT": "United Kingdom",
  "EDWARD WADSWORTH, A.R.A.": "United Kingdom",
  "ELIOT HODGKIN": "United Kingdom",
  "EMILY YOUNG": "United Kingdom",
  "FRANK AUERBACH": "Germany",
  "GEORGE LESLIE HUNTER": "United Kingdom",
  "GERALD LAING": "United Kingdom",
  "GRAHAM SUTHERLAND, O.M.": "United Kingdom",
  "GRAYSON PERRY, R.A.": "United Kingdom",
  "HELEN BRADLEY": "United Kingdom",
  "HENRY MOORE, O.M., C.H.": "United Kingdom",
  "IVON HITCHENS": "United Kingdom",
  "JACK BUTLER YEATS, R.H.A.": "Ireland",
  "JEFFREY STEELE": "United Kingdom",
  "JEREMY MOON": "United Kingdom",
  "JOAN EARDLEY, R.S.A.": "United Kingdom",
  "JOE TILSON, R.A.": "United Kingdom",
  "JOHN DUNCAN FERGUSSON": "United Kingdom",
  "JOHN HOYLAND, R.A.": "United Kingdom",
  "JOHN PLUMB": "United Kingdom",
  "JOHN TUNNARD, A.R.A.": "United Kingdom",
  "JOHN VIRTUE": "United Kingdom",
  "JOHN WELLS": "United Kingdom",
  "KEITH VAUGHAN": "United Kingdom",
  "LAURENCE STEPHEN LOWRY, R.A.": "United Kingdom",
  "LEON KOSSOFF": "United Kingdom",
  "LYNN CHADWICK, R.A.": "United Kingdom",
  "MARK GERTLER": "United Kingdom",
  "MICHAEL KIDNER, R.A.": "United Kingdom",
  "PATRICK HERON": "United Kingdom",
  "PATRICK PROCKTOR, R.A.": "United Kingdom",
  "PAULINE BOTY": "United Kingdom",
  "PETER LANYON": "United Kingdom",
  "PETER ROSE PULHAM": "United Kingdom",
  "PETER SEDGLEY": "United Kingdom",
  "PRUNELLA CLOUGH": "United Kingdom",
  "R.B. KITAJ, R.A.": "United States",
  "ROBERT MACBRYDE": "United Kingdom",
  "RODERIC O'CONOR": "Ireland",
  "ROGER FRY": "United Kingdom",
  "ROGER HILTON": "United Kingdom",
  "SANDRA BLOW, R.A.": "United Kingdom",
  "SIR ANTHONY CARO, O.M., R.A.": "United Kingdom",
  "SIR ANTONY GORMLEY, R.A.": "United Kingdom",
  "SIR CEDRIC MORRIS": "United Kingdom",
  "SIR EDUARDO PAOLOZZI, R.A.": "United Kingdom",
  "SIR FRANK BOWLING, R.A.": "Guyana",
  "SIR JOHN LAVERY, R.A., R.S.A., R.H.A.": "Ireland",
  "SIR MATTHEW SMITH": "United Kingdom",
  "SIR PETER BLAKE, R.A.": "United Kingdom",
  "SIR PETER BLAKE, R.A. AND JANN HAWORTH": "United Kingdom",
  "SIR STANLEY SPENCER, R.A.": "United Kingdom",
  "SIR TERRY FROST, R.A.": "United Kingdom",
  "SIR WILLIAM NICHOLSON": "United Kingdom",
  "STANLEY WILLIAM HAYTER": "United Kingdom",
  "STEPHEN CONROY": "United Kingdom",
  "SVEN BERLIN": "United Kingdom",
  "TRISTRAM HILLIER, R.A.": "United Kingdom",
  "VICTOR PASMORE, R.A.": "United Kingdom",
  "WALTER RICHARD SICKERT, A.R.A.": "United Kingdom",
  "WILHELMINA BARNS-GRAHAM": "United Kingdom",
  "WILLIAM BROOKER, A.R.A.": "United Kingdom",
  "WILLIAM ROBERTS, R.A.": "United Kingdom",
  "WILLIAM SCOTT, R.A.": "United Kingdom",
  "WILLIAM TUCKER": "United Kingdom",
  "WINIFRED NICHOLSON": "United Kingdom",
  "ADRIAEN JANSZ. VAN OSTADE": "Netherlands",
  "ATTRIBUTED TO ANTONIO SUSINI": "Italy",
  "ATTRIBUTED TO MICHAELINA WAUTIER": "Belgium",
  "CLARA PEETERS": "Belgium",
  "EGLON VAN DER NEER": "Netherlands",
  "ERASMUS QUELLINUS II": "Belgium",
  "FRANCESCO HAYEZ": "Italy",
  "GABRIEL METSU": "Netherlands",
  "GERRIT VAN HONTHORST": "Netherlands",
  "GIOVANNI BATTISTA TIEPOLO, CALLED GIAMBATTISTA TIEPOLO": "Italy",
  "GIOVANNI MARTINELLI": "Italy",
  "GUSTAVE COURBET": "France",
  "JAN BRUEGHEL I": "Belgium",
  "JAN SIBERECHTS": "Belgium",
  "JAN VAN DE CAPPELLE": "Netherlands",
  "JOHANN LISS": "Germany",
  "JOHANNES LINGELBACH": "Netherlands",
  "MICHAEL PETER ANCHER": "Denmark",
  "PAOLO VENEZIANO": "Italy",
  "PIETER BRUEGHEL II": "Belgium",
  "SIR PETER PAUL RUBENS": "Belgium",
  "SIR THOMAS LAWRENCE, P.R.A.": "United Kingdom",
  "THE MASTER OF MONTE OLIVETO": "Italy",
  "WORKSHOP OF PIETRO LORENZETTI": "Italy"
      
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
#     style_genre = get_style_and_genre(artist_name)

#     results.append({
#         "название": title,
#         "имя_художника": artist_name,
#         "стоимость": price,
#         "примерная_оценка": estimate,
#         "размер": size,
#         "страна": country,
#         "период": period,
#         "стиль": style_genre["style"],
#         "жанр": style_genre["genre"]

#     })

# # Записываем в CSV
# csv_file = "Exquisite_Eye_hinese_Paintings.csv"
# fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль","жанр"]

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

#     style_genre = get_style_and_genre(artist_clean)
#     country=artists_countries.get(artist_clean, "Unknown")

#     results.append({
#         "название": title,
#         "имя_художника": artist_clean,
#         "стоимость": price,
#         "примерная_оценка": estimate,
#         "материал": material,
#         "размер": dimensions,
#         "страна": country,  # Можно добавить логику извлечения
#         "период": period,
#         "стиль": style_genre["style"],
#         "жанр": style_genre["genre"]
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


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import re
import json
import csv



# Путь к WebDriver
driver_path = "D:\\project on python\\msedgedriver.exe"  # Укажите путь к вашему WebDriver

# Настройка WebDriver
edge_options = Options()
edge_options.add_argument("--headless")  # Запуск в фоновом режиме
edge_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=edge_options)

# URL страницы
url = "https://onlineonly.christies.com/s/first-open-post-war-contemporary-art/lots/3847?page=5&sortby=LotNumber"

try:
    # Загружаем страницу
    driver.get(url)

    # Ищем все скрипты на странице
    scripts = driver.find_elements(By.TAG_NAME, "script")

    lot_data = None

    # Ищем JSON с лотами в скриптах
    for script in scripts:
        script_content = script.get_attribute("innerHTML")
        if "window.chrComponents" in script_content:
            match = re.search(r"window\.chrComponents\s*=\s*(\{.*?\});", script_content, re.DOTALL)
            if match:
                json_str = match.group(1)
                lot_data = json.loads(json_str)
            break

    if not lot_data:
        print("Не удалось найти данные о лотах.")
        exit()

    # Извлекаем информацию о лотах
    lots = lot_data.get("lots", {}).get("data", {}).get("lots", [])
    if not lots:
        print("Данные о лотах отсутствуют в JSON.")
        exit()


    results = []
    for lot in lots:
        title = lot.get("title_secondary_txt", "N/A")
        artist = lot.get("title_primary_txt", "N/A")
        price_realised = lot.get("price_realised_txt", "N/A")
        estimate = lot.get("estimate_txt", "N/A")
        description = lot.get("description_txt", "")

         # Извлекаем размер из описания
        dimensions_match = re.search(r"\(([\d.,]+\s*x\s*[\d.,]+\s*cm\.)\)", description)
        dimensions = dimensions_match.group(1) if dimensions_match else "N/A"

        material = re.search(r"(oil on canvas|acrylic|mixed media|gouache|watercolor|bronze)", lot.get("description_txt", ""), re.IGNORECASE)
        material = material.group(1) if material else "N/A"

    # Удаляем любые скобки с содержимым (например, годы жизни художника)
        artist_clean = re.sub(r"\([^)]*\)", "", artist).strip()

        # Получаем страну из словаря
        artist_clean = artist.split("(")[0].strip().upper()  # Убираем возможные скобки и переводим в верхний регистр
        country = artists_countries.get(artist_clean, "Unknown")

        period_match = re.search(r"\(([^)]+)\)", artist)
        period = period_match.group(1) if period_match else "N/A"

        style_genre = get_style_and_genre(artist_clean)
        
        # Добавляем жанр и стиль
        # Определяем жанр
        genre = extract_genre(description)
        #genre = "Contemporary Art"  # Пример жанра (можно заменить на логику извлечения)
        style = "Contemporary Art"  
        #style = extract_style(description)

        results.append({
            "название": title,
            "имя_художника": artist_clean,
            "стоимость": price_realised,
            "примерная_оценка": estimate,
            "материал": material,
            "размер": dimensions,
            "страна": country,
            "период": period,
            "стиль": style_genre["style"],
            "жанр": style_genre["genre"]
        })


    # Сохраняем результаты в CSV
    csv_file = "Post-War_and_Contemporary_Art.csv"
    fieldnames = ["название", "имя_художника", "стоимость", "примерная_оценка", "материал", "размер", "страна", "период", "стиль", "жанр"]

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"Данные успешно сохранены в {csv_file}")


finally:
    driver.quit()

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
# url = "https://onlineonly.christies.com/s/graphic-century-exceptional-impressions-alan-marianne-schwartz/lots/3856?page=4&sortby=LotNumber"

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
#     csv_file = "Graphic_Century.csv"
#     fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Материал", "Размер", "Страна", "Период", "Стиль", "Жанр"]

#     with open(csv_file, "w", newline="", encoding="utf-8") as file:
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)

#     print(f"Данные успешно сохранены в файл {csv_file}")

# finally:
#     driver.quit()

#-------------------------------------------------------------


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import csv
# import re
# import json

# # Настройки Selenium
# driver_path = "D:\project on python\msedgedriver.exe"  # Замените на путь к вашему драйверу
# url = "https://www.christies.com/en/auction/impressionist-and-modern-art-day-sale-30531/?page=2&sortby=lotnumber"

# options = Options()
# options.add_argument("--headless")  # Открыть браузер в фоновом режиме
# options.add_argument("--disable-gpu")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=options)

# try:
#     # Открываем страницу
#     driver.get(url)

#     # Ищем скрипт с данными
#     scripts = driver.find_elements(By.TAG_NAME, "script")
#     lot_data = None

#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents.lots" in script_content:
#             match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_data = match.group(1)
#                 lot_data = json.loads(json_data)
#                 break

#     if lot_data:
#         lots = lot_data["data"].get("lots", [])
#         results = []
#         for lot in lots:
#             artist = lot.get("title_primary_txt", "N/A")
#             title = lot.get("title_secondary_txt", "N/A")
#             price_realised = lot.get("price_realised_txt", "N/A")
#             estimate = lot.get("estimate_txt", "N/A")
#             description = lot.get("description_txt", "N/A")

#             # Извлекаем материал и размеры из описания
#             material_match = re.search(r"(oil on canvas|bronze|watercolor|gouache|mixed media|collage)", description, re.IGNORECASE)
#             material = material_match.group(1) if material_match else "N/A"
#             dimensions_match = re.search(r"(\d+\.?\d*\s*x\s*\d+\.?\d*\s*(cm|in|mm))", description, re.IGNORECASE)
#             dimensions = dimensions_match.group(1) if dimensions_match else "N/A"

#             artist_cleaned = re.sub(r'\(.*?\)', '', artist).strip()

#             period_match = re.search(r"\((.*?)\)", artist)
#             period = period_match.group(1) if period_match else "Период не найден"
#             artist = re.sub(r"\s*\(.*?\)", "", artist).strip().upper()

#             style_genre = get_style_and_genre(artist)

#             country=artists_countries.get(artist_cleaned, "Unknown")


#             # Добавляем данные в результирующий список
#             results.append({
#                 "Название": title,
#                 "Имя художника": artist,
#                 "Стоимость": price_realised,
#                 "Примерная оценка": estimate,
#                 "Материал": material,
#                 "Размер": dimensions,
#                 "Страна": country,  # Если требуется, можно добавить логику для страны
#                 "Период": period,  # Если требуется, можно добавить логику для периода
#                 "Стиль": style_genre["style"],  # Если требуется, можно добавить логику для стиля
#                 "Жанр": style_genre["genre"]    # Если требуется, можно добавить логику для жанра
#             })

#         # Сохраняем данные в CSV
#         csv_file = "Impressionist_and_Modern_Art_Day.csv"
#         fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Материал", "Размер", "Страна", "Период", "Стиль", "Жанр"]

#         with open(csv_file, "w", newline="", encoding="utf-8") as file:
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(results)

#         print(f"Данные успешно сохранены в файл {csv_file}")
#     else:
#         print("Данные не найдены.")

# finally:
#     driver.quit()

#---------------------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import csv
# import re
# import json

# # Настройки Selenium
# driver_path = "D:\project on python\msedgedriver.exe"  
# url = "https://www.christies.com/en/auction/impressionist-and-modern-works-on-paper-30530/?page=2&sortby=lotnumber"

# options = Options()
# options.add_argument("--headless")  # Открыть браузер в фоновом режиме
# options.add_argument("--disable-gpu")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=options)

# try:
#     # Открываем страницу
#     driver.get(url)

#     # Ищем скрипт с данными
#     scripts = driver.find_elements(By.TAG_NAME, "script")
#     lot_data = None

#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents.lots" in script_content:
#             match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_data = match.group(1)
#                 lot_data = json.loads(json_data)
#                 break

#     if lot_data:
#         lots = lot_data["data"].get("lots", [])
#         results = []
#         for lot in lots:
#             artist = lot.get("title_primary_txt", "N/A")
#             title = lot.get("title_secondary_txt", "N/A")
#             price_realised = lot.get("price_realised_txt", "N/A")
#             estimate = lot.get("estimate_txt", "N/A")
#             description = lot.get("description_txt", "N/A")

#             # Извлекаем материал и размеры из описания
#             material_match = re.search(r"(oil on canvas|bronze|watercolor|gouache|mixed media|collage)", description, re.IGNORECASE)
#             material = material_match.group(1) if material_match else "N/A"
#             dimensions_match = re.search(r"(\d+\.?\d*\s*x\s*\d+\.?\d*\s*(cm|in|mm))", description, re.IGNORECASE)
#             dimensions = dimensions_match.group(1) if dimensions_match else "N/A"
            
#             artist_cleaned = re.sub(r'\(.*?\)', '', artist).strip()

#             period_match = re.search(r"\((.*?)\)", artist)
#             period = period_match.group(1) if period_match else "Период не найден"
#             artist = re.sub(r"\s*\(.*?\)", "", artist).strip().upper()

#             style_genre = get_style_and_genre(artist)

#             country=artists_countries.get(artist_cleaned, "Unknown")


#             # Добавляем данные в результирующий список
#             results.append({
#                 "Название": title,
#                 "Имя художника": artist,
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
#         csv_file = "Modern_works_on_paper.csv"
#         fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Материал", "Размер", "Страна", "Период", "Стиль", "Жанр"]

#         with open(csv_file, "w", newline="", encoding="utf-8") as file:
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(results)

#         print(f"Данные успешно сохранены в файл {csv_file}")
#     else:
#         print("Данные не найдены.")

# finally:
#     driver.quit()

#-----------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import csv
# import re
# import json

# # Настройки Selenium
# driver_path = "D:\project on python\msedgedriver.exe"  
# url = "https://www.christies.com/en/auction/mica-the-collection-of-mica-ertegun-part-ii-30867/"

# options = Options()
# options.add_argument("--headless")  # Открыть браузер в фоновом режиме
# options.add_argument("--disable-gpu")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=options)

# try:
#     # Открываем страницу
#     driver.get(url)

#     # Ищем скрипт с данными
#     scripts = driver.find_elements(By.TAG_NAME, "script")
#     lot_data = None

#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents.lots" in script_content:
#             match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_data = match.group(1)
#                 lot_data = json.loads(json_data)
#                 break

#     if lot_data:
#         lots = lot_data["data"].get("lots", [])
#         results = []
#         for lot in lots:
#             artist = lot.get("title_primary_txt", "N/A")
#             title = lot.get("title_secondary_txt", "N/A")
#             price_realised = lot.get("price_realised_txt", "N/A")
#             estimate = lot.get("estimate_txt", "N/A")
#             description = lot.get("description_txt", "N/A")

#             # Извлекаем материал и размеры из описания
#             material_match = re.search(r"(oil on canvas|bronze|watercolor|gouache|mixed media|collage)", description, re.IGNORECASE)
#             material = material_match.group(1) if material_match else "N/A"
#             dimensions_match = re.search(r"(\d+\.?\d*\s*x\s*\d+\.?\d*\s*(cm|in|mm))", description, re.IGNORECASE)
#             dimensions = dimensions_match.group(1) if dimensions_match else "N/A"
            
#             artist_cleaned = re.sub(r'\(.*?\)', '', artist).strip()

#             period_match = re.search(r"\((.*?)\)", artist)
#             period = period_match.group(1) if period_match else "Период не найден"
#             artist = re.sub(r"\s*\(.*?\)", "", artist).strip().upper()

#             style_genre = get_style_and_genre(artist)

#             country=artists_countries.get(artist_cleaned, "Unknown")


#             # Добавляем данные в результирующий список
#             results.append({
#                 "Название": title,
#                 "Имя художника": artist,
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
#         csv_file = "MICA.csv"
#         fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Материал", "Размер", "Страна", "Период", "Стиль", "Жанр"]

#         with open(csv_file, "w", newline="", encoding="utf-8") as file:
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(results)

#         print(f"Данные успешно сохранены в файл {csv_file}")
#     else:
#         print("Данные не найдены.")

# finally:
#     driver.quit()

#-------------------------------------------------------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import csv
# import re
# import json

# # Настройки Selenium
# driver_path = "D:\project on python\msedgedriver.exe"  
# url = "https://www.christies.com/en/auction/modern-british-and-irish-art-day-sale-30284/?page=2&sortby=lotnumber"

# options = Options()
# options.add_argument("--headless")  # Открыть браузер в фоновом режиме
# options.add_argument("--disable-gpu")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

# service = Service(driver_path)
# driver = webdriver.Edge(service=service, options=options)

# try:
#     # Открываем страницу
#     driver.get(url)

#     # Ищем скрипт с данными
#     scripts = driver.find_elements(By.TAG_NAME, "script")
#     lot_data = None

#     for script in scripts:
#         script_content = script.get_attribute("innerHTML")
#         if "window.chrComponents.lots" in script_content:
#             match = re.search(r"window\.chrComponents\.lots\s*=\s*(\{.*?\});", script_content, re.DOTALL)
#             if match:
#                 json_data = match.group(1)
#                 lot_data = json.loads(json_data)
#                 break

#     if lot_data:
#         lots = lot_data["data"].get("lots", [])
#         results = []
#         for lot in lots:
#             artist = lot.get("title_primary_txt", "N/A")
#             title = lot.get("title_secondary_txt", "N/A")
#             price_realised = lot.get("price_realised_txt", "N/A")
#             estimate = lot.get("estimate_txt", "N/A")
#             description = lot.get("description_txt", "N/A")

#             # Извлекаем материал и размеры из описания
#             material_match = re.search(r"(oil on canvas|bronze|watercolor|gouache|mixed media|collage)", description, re.IGNORECASE)
#             material = material_match.group(1) if material_match else "N/A"
#             dimensions_match = re.search(r"(\d+\.?\d*\s*x\s*\d+\.?\d*\s*(cm|in|mm))", description, re.IGNORECASE)
#             dimensions = dimensions_match.group(1) if dimensions_match else "N/A"
            
#             artist_cleaned = re.sub(r'\(.*?\)', '', artist).strip()

#             period_match = re.search(r"\((.*?)\)", artist)
#             period = period_match.group(1) if period_match else "Период не найден"
#             artist = re.sub(r"\s*\(.*?\)", "", artist).strip().upper()

#             style_genre = get_style_and_genre(artist)

#             country=artists_countries.get(artist_cleaned, "Unknown")


#             # Добавляем данные в результирующий список
#             results.append({
#                 "Название": title,
#                 "Имя художника": artist,
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
#         csv_file = "Modern_British_and_Irish.csv"
#         fieldnames = ["Название", "Имя художника", "Стоимость", "Примерная оценка", "Материал", "Размер", "Страна", "Период", "Стиль", "Жанр"]

#         with open(csv_file, "w", newline="", encoding="utf-8") as file:
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(results)

#         print(f"Данные успешно сохранены в файл {csv_file}")
#     else:
#         print("Данные не найдены.")

# finally:
#     driver.quit()
