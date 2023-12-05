from nltk.tokenize import word_tokenize
import nltk
import string
from nltk.corpus import stopwords
from a_general import createCsvFile
import os

folder = "crwl_test"
csvName = "collectedFiles"

nltk.download('punkt')
nltk.download('stopwords')
stopwords = set(stopwords.words('english'))
res = []
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    print("........................>" + file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
            text_without_newline = text_content.replace('\\n', ' ')

            text_content = text_without_newline.lower()
            translator = str.maketrans("", "", string.punctuation)
            text = text_content.translate(translator)
            text = text.strip()
            print(text)
            print(stopwords)

            filtered_text = ' '.join(
                [word for word in text.split() if word not in stopwords])
            tokens = word_tokenize(filtered_text)
            res.extend(tokens)

            # doppelte wörter ersetzen?
            # als csv speichern

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

createCsvFile(folder+"/"+csvName, res)
