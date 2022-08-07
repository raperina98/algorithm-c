# Description

Given an array of integers `nums`, calculate the `pivot index` of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

# Solutions 

## Solution one

Podemos percorrer cada index e, para cada um, verificar se ele é o pivo.

Para isso, precisamos saber a soma dos elementos anteriores ao `index corrente` e a soma dos elementos posteriores. 

Podemos fazer isso dentro do próprio `for` que percorre os index, criando mais um for que passa por todos elementos e tem como critério para distinguir um elemento anterior de um posterior o `index corrente` e assim conseguitar fazer a somatória de ambos. 

[...]

## Solution two
- Solution two

## Solution Three
- Solution Three