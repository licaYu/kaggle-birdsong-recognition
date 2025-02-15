import string
from pathlib import Path

class AUDIO_CONFIG:
    sampling_rate = 32000
    duration = 1
    hop_length = 251 # making it 128 in size
    fmin = 500
    fmax = 15000
    n_mels = 128
    n_fft = n_mels * 20
    samples = sampling_rate * duration
    padmode = 'reflect'
    
def fill_range(letter_start, letter_end, path_fill, dict_val={}):
    alphabet = list(string.ascii_lowercase)
    for a in alphabet[alphabet.index(letter_start):alphabet.index(letter_end)+1]:
        dict_val[a] = path_fill
    return dict_val

def get_dict_value(input_dir):
    dict_val = {}
    dict_val = fill_range('a','y',input_dir/"train_short_audio",dict_val)
    return dict_val

BIRD_CODE={'acafly': 0,
 'acowoo': 1,
 'aldfly': 2,
 'ameavo': 3,
 'amecro': 4,
 'amegfi': 5,
 'amekes': 6,
 'amepip': 7,
 'amered': 8,
 'amerob': 9,
 'amewig': 10,
 'amtspa': 11,
 'andsol1': 12,
 'annhum': 13,
 'astfly': 14,
 'azaspi1': 15,
 'babwar': 16,
 'baleag': 17,
 'balori': 18,
 'banana': 19,
 'banswa': 20,
 'banwre1': 21,
 'barant1': 22,
 'barswa': 23,
 'batpig1': 24,
 'bawswa1': 25,
 'bawwar': 26,
 'baywre1': 27,
 'bbwduc': 28,
 'bcnher': 29,
 'belkin1': 30,
 'belvir': 31,
 'bewwre': 32,
 'bkbmag1': 33,
 'bkbplo': 34,
 'bkbwar': 35,
 'bkcchi': 36,
 'bkhgro': 37,
 'bkmtou1': 38,
 'bknsti': 39,
 'blbgra1': 40,
 'blbthr1': 41,
 'blcjay1': 42,
 'blctan1': 43,
 'blhpar1': 44,
 'blkpho': 45,
 'blsspa1': 46,
 'blugrb1': 47,
 'blujay': 48,
 'bncfly': 49,
 'bnhcow': 50,
 'bobfly1': 51,
 'bongul': 52,
 'botgra': 53,
 'brbmot1': 54,
 'brbsol1': 55,
 'brcvir1': 56,
 'brebla': 57,
 'brncre': 58,
 'brnjay': 59,
 'brnthr': 60,
 'brratt1': 61,
 'brwhaw': 62,
 'brwpar1': 63,
 'btbwar': 64,
 'btnwar': 65,
 'btywar': 66,
 'bucmot2': 67,
 'buggna': 68,
 'bugtan': 69,
 'buhvir': 70,
 'bulori': 71,
 'burwar1': 72,
 'bushti': 73,
 'butsal1': 74,
 'buwtea': 75,
 'cacgoo1': 76,
 'cacwre': 77,
 'calqua': 78,
 'caltow': 79,
 'cangoo': 80,
 'canwar': 81,
 'carchi': 82,
 'carwre': 83,
 'casfin': 84,
 'caskin': 85,
 'caster1': 86,
 'casvir': 87,
 'categr': 88,
 'ccbfin': 89,
 'cedwax': 90,
 'chbant1': 91,
 'chbchi': 92,
 'chbwre1': 93,
 'chcant2': 94,
 'chispa': 95,
 'chswar': 96,
 'cinfly2': 97,
 'clanut': 98,
 'clcrob': 99,
 'cliswa': 100,
 'cobtan1': 101,
 'cocwoo1': 102,
 'cogdov': 103,
 'colcha1': 104,
 'coltro1': 105,
 'comgol': 106,
 'comgra': 107,
 'comloo': 108,
 'commer': 109,
 'compau': 110,
 'compot1': 111,
 'comrav': 112,
 'comyel': 113,
 'coohaw': 114,
 'cotfly1': 115,
 'cowscj1': 116,
 'cregua1': 117,
 'creoro1': 118,
 'crfpar': 119,
 'cubthr': 120,
 'daejun': 121,
 'dowwoo': 122,
 'ducfly': 123,
 'dusfly': 124,
 'easblu': 125,
 'easkin': 126,
 'easmea': 127,
 'easpho': 128,
 'eastow': 129,
 'eawpew': 130,
 'eletro': 131,
 'eucdov': 132,
 'eursta': 133,
 'fepowl': 134,
 'fiespa': 135,
 'flrtan1': 136,
 'foxspa': 137,
 'gadwal': 138,
 'gamqua': 139,
 'gartro1': 140,
 'gbbgul': 141,
 'gbwwre1': 142,
 'gcrwar': 143,
 'gilwoo': 144,
 'gnttow': 145,
 'gnwtea': 146,
 'gocfly1': 147,
 'gockin': 148,
 'gocspa': 149,
 'goftyr1': 150,
 'gohque1': 151,
 'goowoo1': 152,
 'grasal1': 153,
 'grbani': 154,
 'grbher3': 155,
 'grcfly': 156,
 'greegr': 157,
 'grekis': 158,
 'grepew': 159,
 'grethr1': 160,
 'gretin1': 161,
 'greyel': 162,
 'grhcha1': 163,
 'grhowl': 164,
 'grnher': 165,
 'grnjay': 166,
 'grtgra': 167,
 'grycat': 168,
 'gryhaw2': 169,
 'gwfgoo': 170,
 'haiwoo': 171,
 'heptan': 172,
 'hergul': 173,
 'herthr': 174,
 'herwar': 175,
 'higmot1': 176,
 'hofwoo1': 177,
 'houfin': 178,
 'houspa': 179,
 'houwre': 180,
 'hutvir': 181,
 'incdov': 182,
 'indbun': 183,
 'kebtou1': 184,
 'killde': 185,
 'labwoo': 186,
 'larspa': 187,
 'laufal1': 188,
 'laugul': 189,
 'lazbun': 190,
 'leafly': 191,
 'leasan': 192,
 'lesgol': 193,
 'lesgre1': 194,
 'lesvio1': 195,
 'linspa': 196,
 'linwoo1': 197,
 'littin1': 198,
 'lobdow': 199,
 'lobgna5': 200,
 'logshr': 201,
 'lotduc': 202,
 'lotman1': 203,
 'lucwar': 204,
 'macwar': 205,
 'magwar': 206,
 'mallar3': 207,
 'marwre': 208,
 'mastro1': 209,
 'meapar': 210,
 'melbla1': 211,
 'monoro1': 212,
 'mouchi': 213,
 'moudov': 214,
 'mouela1': 215,
 'mouqua': 216,
 'mouwar': 217,
 'mutswa': 218,
 'naswar': 219,
 'norcar': 220,
 'norfli': 221,
 'normoc': 222,
 'norpar': 223,
 'norsho': 224,
 'norwat': 225,
 'nrwswa': 226,
 'nutwoo': 227,
 'oaktit': 228,
 'obnthr1': 229,
 'ocbfly1': 230,
 'oliwoo1': 231,
 'olsfly': 232,
 'orbeup1': 233,
 'orbspa1': 234,
 'orcpar': 235,
 'orcwar': 236,
 'orfpar': 237,
 'osprey': 238,
 'ovenbi1': 239,
 'pabspi1': 240,
 'paltan1': 241,
 'palwar': 242,
 'pasfly': 243,
 'pavpig2': 244,
 'phivir': 245,
 'pibgre': 246,
 'pilwoo': 247,
 'pinsis': 248,
 'pirfly1': 249,
 'plawre1': 250,
 'plaxen1': 251,
 'plsvir': 252,
 'plupig2': 253,
 'prowar': 254,
 'purfin': 255,
 'purgal2': 256,
 'putfru1': 257,
 'pygnut': 258,
 'rawwre1': 259,
 'rcatan1': 260,
 'rebnut': 261,
 'rebsap': 262,
 'rebwoo': 263,
 'redcro': 264,
 'reevir1': 265,
 'rehbar1': 266,
 'relpar': 267,
 'reshaw': 268,
 'rethaw': 269,
 'rewbla': 270,
 'ribgul': 271,
 'rinkin1': 272,
 'roahaw': 273,
 'robgro': 274,
 'rocpig': 275,
 'rotbec': 276,
 'royter1': 277,
 'rthhum': 278,
 'rtlhum': 279,
 'ruboro1': 280,
 'rubpep1': 281,
 'rubrob': 282,
 'rubwre1': 283,
 'ruckin': 284,
 'rucspa1': 285,
 'rucwar': 286,
 'rucwar1': 287,
 'rudpig': 288,
 'rudtur': 289,
 'rufhum': 290,
 'rugdov': 291,
 'rumfly1': 292,
 'runwre1': 293,
 'rutjac1': 294,
 'saffin': 295,
 'sancra': 296,
 'sander': 297,
 'savspa': 298,
 'saypho': 299,
 'scamac1': 300,
 'scatan': 301,
 'scbwre1': 302,
 'scptyr1': 303,
 'scrtan1': 304,
 'semplo': 305,
 'shicow': 306,
 'sibtan2': 307,
 'sinwre1': 308,
 'sltred': 309,
 'smbani': 310,
 'snogoo': 311,
 'sobtyr1': 312,
 'socfly1': 313,
 'solsan': 314,
 'sonspa': 315,
 'soulap1': 316,
 'sposan': 317,
 'spotow': 318,
 'spvear1': 319,
 'squcuc1': 320,
 'stbori': 321,
 'stejay': 322,
 'sthant1': 323,
 'sthwoo1': 324,
 'strcuc1': 325,
 'strfly1': 326,
 'strsal1': 327,
 'stvhum2': 328,
 'subfly': 329,
 'sumtan': 330,
 'swaspa': 331,
 'swathr': 332,
 'tenwar': 333,
 'thbeup1': 334,
 'thbkin': 335,
 'thswar1': 336,
 'towsol': 337,
 'treswa': 338,
 'trogna1': 339,
 'trokin': 340,
 'tromoc': 341,
 'tropar': 342,
 'tropew1': 343,
 'tuftit': 344,
 'tunswa': 345,
 'veery': 346,
 'verdin': 347,
 'vigswa': 348,
 'warvir': 349,
 'wbwwre1': 350,
 'webwoo1': 351,
 'wegspa1': 352,
 'wesant1': 353,
 'wesblu': 354,
 'weskin': 355,
 'wesmea': 356,
 'westan': 357,
 'wewpew': 358,
 'whbman1': 359,
 'whbnut': 360,
 'whcpar': 361,
 'whcsee1': 362,
 'whcspa': 363,
 'whevir': 364,
 'whfpar1': 365,
 'whimbr': 366,
 'whiwre1': 367,
 'whtdov': 368,
 'whtspa': 369,
 'whwbec1': 370,
 'whwdov': 371,
 'wilfly': 372,
 'willet1': 373,
 'wilsni1': 374,
 'wiltur': 375,
 'wlswar': 376,
 'wooduc': 377,
 'woothr': 378,
 'wrenti': 379,
 'y00475': 380,
 'yebcha': 381,
 'yebela1': 382,
 'yebfly': 383,
 'yebori1': 384,
 'yebsap': 385,
 'yebsee1': 386,
 'yefgra1': 387,
 'yegvir': 388,
 'yehbla': 389,
 'yehcar1': 390,
 'yelgro': 391,
 'yelwar': 392,
 'yeofly1': 393,
 'yerwar': 394,
 'yeteup1': 395,
 'yetvir': 396}
