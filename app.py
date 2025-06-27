import nltk
from flask import Flask, render_template, request
import pickle
import string
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.data.path.append("./nltk_data")
nltk.download('punkt_tab')
nltk.download('stopwords')

app = Flask(__name__)

# Load the vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

ps = PorterStemmer()

def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)

    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
        
    
    return " ".join(y)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_mail = request.form['email']
        transformed_mail = transform_text(input_mail)
        vector_input = tfidf.transform([transformed_mail])
        prediction = model.predict(vector_input.toarray())[0]

        if prediction == 1:
            result = "This is a Spam mail"
        else:
            result = "This is a Ham mail"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
