#filter_map_para_python_y_js
lista = [0,1,2,3,4,5,'a'] 
print("Lista original", lista)

def myFilter(item):
    if type(item) != type("w"):
        return True
    return False

def mF(item):
    return type(item) != type("w")
def duplica_si_es_impar(item):
    if item % 2 == 1:
        return item*2
    return item
   
list_fitered = list( filter( myFilter , tuple(lista) )         )
print("list_fitered", list_fitered)
l_f = list(          filter(  mF        , lista       )         ) # l_f por metodo 1 pasandole una función
print("l_f", l_f)
filtrados_y_mapeados =  list( map(duplica_si_es_impar, list_fitered) )
print("lf", filtrados_y_mapeados)
l_f = list(filter(  lambda item: type(item) != type("w"), lista)) # l_f por metodo 2 pasandole una funcion lambda

#print(  list( map(  lambda item: item*2 if item % 2 == 1 else item,l_f)))

# filtrado y mapeado en una sola linea 
print("una sola linea",  list(  map( lambda x: x*2 if x%2 == 1 else x, list(  filter(lambda x: type(x) == type(5) , lista) ))   ))


# preguntas por resolver
# si se mapea primero que ocurre?
# ¿cuales son las 10 diferencias más importantes entre python y js en filtrado mapeado y en las funciones lambda y flecha ?
# si los nombre de map y filter en ambos lenguajes fueran diferentes cuales nombres serian correctos ?

# el siguente es codigo de js , comentado con triple comilla doble " 
"""
lista = [0,1,2,3,4,5, "a"]; //array 
function f(item){
  if( typeof(item) == typeof(1) ){
    return true
  }
  return false
}        //                                               lambda i: i*2 if %2 === 1 else i
console.log(lista?.filter((i) => typeof(i) === typeof(1) ).map( (i)=> i %2 === 1 ? i*2 : i));
"""
# las url o links de las consolas online que se pueden usar para probar codigos python o javascript
# https://www.online-python.com/
# https://playcode.io/javascript 
