## Introduccion

El lenguaje a desarrollar se llama "Fin de las clases". Es metafórico entre la lucha de las clases oprimidas por la abolición de las clases burguesas y las clases computacionales usadas en la programación orientada a objetos

## Gramatica EBNF

```
programa      ::= (bloque | estructura)*
‎
comentario    ::= "/protesta/" .*
‎
declaracion   ::=  alcance (variable | funcion)
‎
alcance       ::= ("imperialismo" | "comunidad" | "")
‎
asignacion    ::= "rebelion" identificador "=" expresion
‎
variable      ::= ("manifiesto" identificador "=" texto) |
                  ("unidad" identificador "=" entero) |
                  ("colectivo" identificador "=" flotante)
‎
estructura    ::= repeticion | bifurcacion
‎
repeticion    ::= "revolucion" "(" condicion ")" "{" bloque "}"
‎
bifurcacion   ::= "abolir_clases" "(" condicion ")" "{" bloque "}" ("en_igualdad" "{" bloque "}")?
‎
bloque        ::= (instruccion | comentario)+
‎
funcion       ::= "asamblea" identificador "(" argumentos ")" "{" bloque retorno "}"
‎
retorno       ::= "sentencia" termino
‎
instruccion   ::= declaracion | expresion | estructura | funcion_llamada
‎
funcion_llamada ::= "comandar" identificador "(" argumentos ")"
‎
expresion     ::= (termino (operador termino)?)
‎
operador      ::= "+" | "-" | "*" | "/" | "//" | "%"
‎
termino       ::= funcion_llamada | identificador | texto | entero | flotante | "(" expresion ")"
‎
condicion     ::= termino (comparacion termino)?
‎
comparacion   ::= "==" | "!=" | ">" | "<" | ">=" | "<="
‎
argumentos    ::= (termino ("," termino)*)?
‎
texto         ::= "\".*?\""
entero        ::= "[0-9]+"
flotante      ::= "[0-9]+\\.[0-9]+"
identificador ::= "[a-zA-Z_][a-zA-Z0-9_]*"

```

## Ejemplo 1 del código

```
/ protesta / Declaración de variables
imperialismo unidad global = 10
comunidad unidad local = opinion()

/ protesta / Bucle que se ejecuta mientras la variable local sea menor que la global
revolucion (local < global):
    / protesta / Pregunta al usuario si desea incrementar el valor de local
    comunidad unidad respuesta = opinion()

    abolir_clases (respuesta == "si"):
        local = local + 1
    en_igualdad:
        / protesta / Si la respuesta no es "si", terminamos el bucle
        global = local

/ protesta / Mensaje final
asamblea mostrar_mensaje("Fin del ciclo, local ha alcanzado el valor de global")
```

## Ejemplo 2 del código

```
/ protesta / Solicitar número al usuario
comunidad unidad numero = opinion()

/ protesta / Definir función recursiva para calcular el factorial
comunidad asamblea factorial(n):
    abolir_clases (n == 0):
        / protesta / Caso base: factorial de 0 es 1
        unidad resultado = 1
    en_igualdad:
        / protesta / Caso recursivo: n * factorial(n-1)
        unidad resultado = n * factorial(n - 1)

    resultado

/ protesta / Llamar a la función y mostrar el resultado
unidad resultado = factorial(numero)
asamblea mostrar_mensaje("El factorial de " + numero + " es " + resultado)
```
