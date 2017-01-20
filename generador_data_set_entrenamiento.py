from textblob import TextBlob
i=0
j=0
v=0
k=0
archivo = open("procesado.txt","w")
print "Frase | Sustantivo | Adjetivo |Verbo |Total Palabras|Polaridad Oracion|Adjetivo_Calif|ClasificacionInterna"
#Funcion para conteo
cont_adj = open("dic_adjfinal.txt","r")
textoo = cont_adj.read()
whip = eval(textoo)
val=0.0
cal='na'
with open('texto_limpio.txt') as fp:
    for line in fp:
		blob = TextBlob(line)
		for word, pos in blob.tags:
			if pos == 'NN':
				i=i+1
			if pos == 'JJ':
				j=j+1
				try:
					val=val + whip[word]
				except KeyError:
					print "na"
			if pos == 'VB':
				v=v+1
		suma = val + blob.sentiment.polarity
		if suma < 0.0:
			cal='neg'
		elif suma > 0.0:
			cal='pos'
		else:
			cal='neu'
		archivo.write(str(i) + "|" + str(j) + "|" + str(v) + "|" + str(len(blob.words)) + "|" + str(blob.sentiment.polarity) +"|"+str(suma)+"|"+str(cal)+'\n')
		val=0.0
		i=0
		j=0
		v=0
		k=0
archivo.close()