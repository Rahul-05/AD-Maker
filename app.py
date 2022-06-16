from flask import Flask, render_template, request
import spacy
import enchant
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/next',methods=['POST'])
def next():
	data1 = request.form['word_1']
	data2 = request.form['word_2']

	nlp = spacy.load('en_core_web_lg')
	X= list(model.index_to_key)


	data=model.most_similar(positive=data1,topn=10000)
	dbf =[]
	for a, b in data:
		dbf.append(a)

	datb=model.most_similar(positive=data2,topn=10000)
	dbc =[]
	for a, b in datb:
		dbc.append(a)

	out1 = list(set(dbf).intersection(dbc))
	n = len(out1)
	n1= int((7/10)*n)
	out=[]
	for i in range(n1):
		out.append(out1[i])

	



	# dbNX=[]
	# dict = enchant.Dict("en_US")
	# for i in range(0, len(out)):
	# 	tag = out[i]
	# 	exists = dict.check(tag)
	# 	if exists == False:
	# 		dbNX.append(tag)

	# dbNA=[]
	# for i in range(0, len(dbNX)):
	# 	text = (dbNX[i])
	# 	doc = nlp(text)
	# 	for token in doc:
	# 		if token.pos_ == "NOUN" :
	# 			dbNA.append(token)

	dbN1=[]
	dbN2=[]
	dbN3=[]
	for i in range(0, len(out)):
		text = (out[i])
		doc = nlp(text)
		for token in doc:
			if token.pos_ == "NOUN" :
				#dbN.append(token)
				
				y = str(token)
				edu = TextBlob(y)
				x = edu.sentiment.polarity

				if x<0:
					dbN1.append(y)
				elif x==0:
					dbN2.append(y)
				elif x>0 and x<=1:
					dbN3.append(y)

			
	dbA1=[]
	dbA2=[]
	dbA3=[]
	for i in range(0, len(out)):
		text = (out[i])
		doc = nlp(text)
		for token in doc:
			if token.pos_ == "ADJ" :
				#dbA.append(token)
				y = str(token)
				edu = TextBlob(y)
				x = edu.sentiment.polarity

				if x<0:
					dbA1.append(y)
				elif x==0:
					dbA2.append(y)
				elif x>0 and x<=1:
					dbA3.append(y)

	dbV1=[]
	dbV2=[]
	dbV3=[]
	for i in range(0, len(out)):
		text = (out[i])
		doc = nlp(text)
		for token in doc:
			if token.pos_ == "VERB" :
				#dbV.append(token)
				y = str(token)
				edu = TextBlob(y)
				x = edu.sentiment.polarity

				if x<0:
					dbV1.append(y)
				elif x==0:
					dbV2.append(y)
				elif x>0 and x<=1:
					dbV3.append(y)
				
	# return render_template('index.html',datna=dbNX,data=dbN,datb=dbA,datc=dbV,input1=data1,input2=data2)
	return render_template('index.html',data1=dbN1,data2=dbN2,data3=dbN3,datb1=dbA1,datb2=dbA2,datb3=dbA3,datc1=dbV1,datc2=dbV2,datc3=dbV3,input1=data1,input2=data2)
	# print(data1)


if __name__ == "__main__":
    app.run(debug=True)