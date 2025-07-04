import pandas as pd
import csv

charMap = {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L","M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z","À":"A","Á":"A","Â":"A","Ã":"A","Ä":"A","Å":"A","Ç":"C","È":"E","É":"E","Ê":"E","Ë":"E","Ì":"I","Í":"I","Î":"I","Ï":"I","Ð":"D","Ñ":"N","Ò":"O","Ó":"O","Ô":"O","Õ":"O","Ö":"O","Ø":"O","Ù":"U","Ú":"U","Û":"U","Ü":"U","Ý":"Y","Ā":"A","Ă":"A","Ą":"A","Ć":"C","Ĉ":"C","Ċ":"C","Č":"C","Ď":"D","Đ":"D","Ē":"E","Ĕ":"E","Ė":"E","Ę":"E","Ě":"E","Ĝ":"G","Ğ":"G","Ġ":"G","Ģ":"G","Ĥ":"H","Ħ":"H","Ĩ":"I","Ī":"I","Ĭ":"I","Į":"I","İ":"I","Ĵ":"J","Ķ":"K","Ĺ":"L","Ļ":"L","Ľ":"L","Ŀ":"L","Ł":"L","Ń":"N","Ņ":"N","Ň":"N","Ō":"O","Ŏ":"O","Ő":"O","Ŕ":"R","Ŗ":"R","Ř":"R","Ś":"S","Ŝ":"S","Ş":"S","Š":"S","Ţ":"T","Ť":"T","Ũ":"U","Ū":"U","Ŭ":"U","Ů":"U","Ű":"U","Ų":"U","Ŵ":"W","Ŷ":"Y","Ÿ":"Y","Ź":"Z","Ż":"Z","Ž":"Z","Ơ":"O","Ư":"U","Ǎ":"A","Ǐ":"I","Ǒ":"O","Ǔ":"U","Ǖ":"U","Ǘ":"U","Ǚ":"U","Ǜ":"U","Ǟ":"A","Ǡ":"A","Ǧ":"G","Ǩ":"K","Ǫ":"O","Ǭ":"O","Ǵ":"G","Ǹ":"N","Ǻ":"A","Ǿ":"O","Ȁ":"A","Ȃ":"A","Ȅ":"E","Ȇ":"E","Ȉ":"I","Ȋ":"I","Ȍ":"O","Ȏ":"O","Ȑ":"R","Ȓ":"R","Ȕ":"U","Ȗ":"U","Ș":"S","Ț":"T","Ȟ":"H","Ȧ":"A","Ȩ":"E","Ȫ":"O","Ȭ":"O","Ȯ":"O","Ȱ":"O","Ȳ":"Y","Ḁ":"A","Ḃ":"B","Ḅ":"B","Ḇ":"B","Ḉ":"C","Ḋ":"D","Ḍ":"D","Ḏ":"D","Ḑ":"D","Ḓ":"D","Ḕ":"E","Ḗ":"E","Ḙ":"E","Ḛ":"E","Ḝ":"E","Ḟ":"F","Ḡ":"G","Ḣ":"H","Ḥ":"H","Ḧ":"H","Ḩ":"H","Ḫ":"H","Ḭ":"I","Ḯ":"I","Ḱ":"K","Ḳ":"K","Ḵ":"K","Ḷ":"L","Ḹ":"L","Ḻ":"L","Ḽ":"L","Ḿ":"M","Ṁ":"M","Ṃ":"M","Ṅ":"N","Ṇ":"N","Ṉ":"N","Ṋ":"N","Ṍ":"O","Ṏ":"O","Ṑ":"O","Ṓ":"O","Ṕ":"P","Ṗ":"P","Ṙ":"R","Ṛ":"R","Ṝ":"R","Ṟ":"R","Ṡ":"S","Ṣ":"S","Ṥ":"S","Ṧ":"S","Ṩ":"S","Ṫ":"T","Ṭ":"T","Ṯ":"T","Ṱ":"T","Ṳ":"U","Ṵ":"U","Ṷ":"U","Ṹ":"U","Ṻ":"U","Ṽ":"V","Ṿ":"V","Ẁ":"W","Ẃ":"W","Ẅ":"W","Ẇ":"W","Ẉ":"W","Ẋ":"X","Ẍ":"X","Ẏ":"Y","Ẑ":"Z","Ẓ":"Z","Ẕ":"Z","Ạ":"A","Ả":"A","Ấ":"A","Ầ":"A","Ẩ":"A","Ẫ":"A","Ậ":"A","Ắ":"A","Ằ":"A","Ẳ":"A","Ẵ":"A","Ặ":"A","Ẹ":"E","Ẻ":"E","Ẽ":"E","Ế":"E","Ề":"E","Ể":"E","Ễ":"E","Ệ":"E","Ỉ":"I","Ị":"I","Ọ":"O","Ỏ":"O","Ố":"O","Ồ":"O","Ổ":"O","Ỗ":"O","Ộ":"O","Ớ":"O","Ờ":"O","Ở":"O","Ỡ":"O","Ợ":"O","Ụ":"U","Ủ":"U","Ứ":"U","Ừ":"U","Ử":"U","Ữ":"U","Ự":"U","Ỳ":"Y","Ỵ":"Y","Ỷ":"Y","Ỹ":"Y","ℂ":"C","ℋ":"H","ℌ":"H","ℍ":"H","ℐ":"I","ℑ":"I","ℒ":"L","ℕ":"N","ℙ":"P","ℚ":"Q","ℛ":"R","ℜ":"R","ℝ":"R","ℤ":"Z","ℨ":"Z","K":"K","Å":"A","ℬ":"B","ℭ":"C","ℰ":"E","ℱ":"F","ℳ":"M","ⅅ":"D","Ⅰ":"I","Ⅴ":"V","Ⅹ":"X","Ⅼ":"L","Ⅽ":"C","Ⅾ":"D","Ⅿ":"M","Ⓐ":"A","Ⓑ":"B","Ⓒ":"C","Ⓓ":"D","Ⓔ":"E","Ⓕ":"F","Ⓖ":"G","Ⓗ":"H","Ⓘ":"I","Ⓙ":"J","Ⓚ":"K","Ⓛ":"L","Ⓜ":"M","Ⓝ":"N","Ⓞ":"O","Ⓟ":"P","Ⓠ":"Q","Ⓡ":"R","Ⓢ":"S","Ⓣ":"T","Ⓤ":"U","Ⓥ":"V","Ⓦ":"W","Ⓧ":"X","Ⓨ":"Y","Ⓩ":"Z","Ꝺ":"D","Ꝼ":"F","Ᵹ":"G","Ꞃ":"R","Ꞇ":"T","Ꞡ":"G","Ꞣ":"K","Ꞥ":"N","Ꞧ":"R","Ａ":"A","Ｂ":"B","Ｃ":"C","Ｄ":"D","Ｅ":"E","Ｆ":"F","Ｇ":"G","Ｈ":"H","Ｉ":"I","Ｊ":"J","Ｋ":"K","Ｌ":"L","Ｍ":"M","Ｎ":"N","Ｏ":"O","Ｐ":"P","Ｑ":"Q","Ｒ":"R","Ｓ":"S","Ｔ":"T","Ｕ":"U","Ｖ":"V","Ｗ":"W","Ｘ":"X","Ｙ":"Y","Ｚ":"Z"};

titulos_sem_acento_e_em_caixa_alta = []

with open('CBO2002_Ocupacao_original.csv', newline='', encoding="ISO-8859-1") as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=';')
    for row in spamreader:
        titulo_sem_acento_e_em_caixa_alta = ""

        for letra in list(row["TITULO"]):
            try:
                titulo_sem_acento_e_em_caixa_alta += charMap[letra.upper()]
            except KeyError:
                titulo_sem_acento_e_em_caixa_alta += letra.upper()
        
        titulos_sem_acento_e_em_caixa_alta.append(titulo_sem_acento_e_em_caixa_alta)

df_profissoes = pd.read_csv("CBO2002_Ocupacao_original.csv", sep=";", encoding="ISO-8859-1")
df_profissoes['TITULO_SEM_ACENTO_E_EM_CAIXA_ALTA'] = titulos_sem_acento_e_em_caixa_alta

sorted_df_profissoes = df_profissoes.sort_values(by=["TITULO_SEM_ACENTO_E_EM_CAIXA_ALTA"])

sorted_df_profissoes.to_csv('CBO2002_Ocupacao.csv', sep=";", index=False)


# print(titulos_sem_acento_e_em_caixa_alta)

            


        # print(unidecode(normalize('NFKD', row['TITULO']).encode('ASCII','ignore').decode('ASCII')))