---
title: Programacion II
subtitle: "Recursión"
author: Universidad Nacional de Rosario.
institute: Facultad de Ciencias Exactas, Ingeniería y Agrimensura.
---

# La recursión y cómo puede ser que funcione

Estamos acostumbrados a escribir funciones que llaman a otras funciones. Pero
lo cierto es que nada impide que en Python (y en muchos otros lenguajes)
**una función se llame a sí misma**.

Y lo más interesante es que esta propiedad, que se llama **recursión**,
permite en muchos casos encontrar soluciones muy elegantes para determinados
problemas.

# Una función recursiva matemática

Es muy común tener definiciones inductivas de operaciones, como por ejemplo:

$0! = 1 $

$x! = x (x - 1)!$, si $x > 0$

Este tipo de definición se traduce naturalmente en una función en Python:

```python
!include code/unidad1/factorial.py
```

# Factorial

Este tipo de definición se traduce naturalmente en una función en Python:

```python
!include code/unidad1/factorial.py
```

Esta es la ejecución del factorial para $n = 0$ y para $n = 3$.

```
>>> factorial(0)
1
>>> factorial(3)
6
```

# Factorial

```python
!include code/unidad1/factorial.py
```

El sentido de la instrucción `n * factorial(n - 1)` es exactamente el mismo que
el de la definición inductiva: para calcular el factorial de `n` se debe
multiplicar `n` por el factorial de `n - 1`.

Dos piezas fundamentales para garantizar el funcionamiento de este programa son:

* Que se defina un caso base (en este caso la indicación no recursiva de cómo
calcular `factorial(0)`.
* Que el argumento de la función respete la precondición de que `n` debe ser un
entero mayor o igual que 0.

# Algoritmos recursivos y algoritmos iterativos

Llamaremos **algoritmos recursivos** a aquellos que realizan llamadas recursivas
para llegar al resultado, y **algoritmos iterativos** a aquellos que llegan a
un resultado a través de una iteración mediante un ciclo definido o indefinido.

**Todo algoritmo recursivo puede expresarse como iterativo y viceversa**. Sin
embargo, según las condiciones del problema a resolver podrá ser preferible
utilizar la solución recursiva o la iterativa.

# Factorial iterativo

Una posible implementación iterativa de la función factorial podría ser la
siguiente:

```python
!include code/unidad1/factorial2.py
```

# Un ejemplo de recursión poco eficiente

Del ejemplo anterior se podría deducir que siempre es mejor utilizar algoritmos
recursivos; sin embargo, como ya se dĳo, cada situación debe ser analizada por
separado.

Un ejemplo clásico en el cual la recursión tiene un resultado muy poco eficiente
es el de los números de Fibonacci. La sucesión de Fibonacci está definida por la
siguiente relación:

$F_n = 0$, si $n = 0$

$F_n = 1$, si $n = 1$
$F_n = F_{n-1} + F_{n-2}$, si $n > 1$

Los primeros números de esta sucesión son:

$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55$.

# Definición Recursiva de Fibonacci

Dada la definición recursiva de la sucesión, puede resultar muy tentador
escribir una función que calcule en valor de `fib(n)` de la siguiente forma:

```python
!include code/unidad1/fibonacci.py
```

Si bien esta implementación es muy sencilla y elegante, también es
`extremadamente poco eficiente`: para calcular `fib(n - 1)` es necesario calcular
`fib(n - 2)`, que luego volverá a ser calculado para obtener el valor `fib(n)`.

# Definición Iterativa de Fibonacci

Resulta más conveniente en este caso definir una versión iterativa:

```python
!include code/unidad1/fibonacci2.py
```

En el caso iterativo se calcula el número de Fibonacci de forma incremental,
de modo que para obtener el valor de `fib(n)` se harán `n - 1` iteraciones.

# Conclusiones

* La **recursión** es el proceso en el cual una función se invoca a sí misma.
Este proceso **permite crear un nuevo tipo de ciclos**.

* Siempre que se escribe una función recursiva es importante considerar el
**caso base** (el que detendrá la recursión) y el **caso recursivo** (el que
realizará la llamada recursiva). **Una función recursiva sin caso base es
equivalente a un bucle infinito**.

* **Una función no es mejor ni peor por ser recursiva**. En cada situación a
resolver puede ser conveniente utilizar una solución recursiva o una iterativa.
Para elegir una o la otra será necesario analizar las características de
elegancia y eficiencia.

# Preguntas

-----------------------------
 ¿PREGUNTAS?
-----------------------------

# Referencias

* Apunte de la Facultad de Ingeniería de la UBA, 2da Edición, 2016. Algoritmos
y Programación I: Aprendiendo a programar usando Python como herramienta.
Unidad 18.
