miArbolModelos = function(datos) {
	# Separar continuos y discretos
	entradas = datos[,-ncol(datos)]
	esNumero = sapply(entradas[1,],is.numeric)
	entradasDiscretas = entradas[,!esNumero]
	entradasContinuas = entradas[,esNumero]
	salida = datos[,ncol(datos)]

	construyeArbol(entradasDiscretas, entradasContinuas, salida, 1)

}

construyeArbol = function(entradasDiscretas, entradasContinuas, salida, tabulador) {

  # print(colnames(entradasDiscretas))
  # Si quedan atributos discretos, ver cual tiene menos varianza ponderada, si no
  # construir modelo lineal

  #print(is.null(entradasDiscretas))
  
if(!is.null(entradasDiscretas)) {
  desviacionesAtributo = function(x){tapply(salida,x,sd)}
  desviacionesAtributos = apply(entradasDiscretas,2, desviacionesAtributo)
  vecesValoresAtributos = sapply(entradasDiscretas,table)
  mediasPorAtributo = mapply(weighted.mean,desviacionesAtributos,vecesValoresAtributos)
  
  seleccionado = which.min(mediasPorAtributo)
  cat(paste(rep(" ",tabulador), colnames(entradasDiscretas)[seleccionado],"\n"))
  valoresSeleccionado = vecesValoresAtributos[[seleccionado]]
#  print('valoresSeleccionado')
#  print(valoresSeleccionado)
#  print(length(valoresSeleccionado))
  
  k=1
  while (k<=length(valoresSeleccionado)){
    
    valor = names(valoresSeleccionado)[k]
    cat(paste(rep(" ",tabulador), colnames(entradasDiscretas)[seleccionado],"==",valor,"\n"))
    
    
    columna = entradasDiscretas[,seleccionado] == valor
    
    entradasDiscretasAux = entradasDiscretas[columna,-seleccionado]

    #print(head(entradasDiscretasAux))
    #print(apply(entradasDiscretasAux,2,table))
    #readline()
    
    #print(head(entradasDiscretasAux))
    #construyeArbol(entradasDiscretasAux, entradasContinuas[columna,], salida[columna], tabulador+5)
    
    lm = lm(salida~., cbind(entradasContinuas,salida))
    print(lm)
    
    k=k+1
  }
						
} else {
  print("END")
}
}
