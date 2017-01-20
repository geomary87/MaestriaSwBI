from textblob import TextBlob
		

listanegra =  ['in', 'the', 'and', 'they', 'my', 'that']
listanegra += ['a','is','he','she','with','one','there']
listanegra += ['to','for','there','this','it','you','an']
listanegra += ['i','am','.',',']

#Funcion para remover lista negra de palabras 
def removerListaNegra(listaPalabrasP, listanegraP):
    return [w for w in listaPalabrasP if w not in listanegraP]
	
#Proceso para remover lista negra de palabras y generar nuevo archivo
archivo_clear = open("texto_limpio.txt","w")
with open('texto_proy.txt') as fp:
    for line in fp:
		blob = TextBlob(line)
		for sentence in blob.sentences:
			oracion_nueva=''
			oracion = sentence.split()	
			oracion = removerListaNegra(oracion,listanegra)
			for w in oracion:
				if len(w)>2 and w!='!':
					oracion_nueva= oracion_nueva+ str(w) + ' '
			if len(oracion_nueva)>1:
				archivo_clear.write(str(oracion_nueva)+'\n')
archivo_clear.close()