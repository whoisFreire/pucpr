# Semana 04

## Listas com comportamento de Vetor
Vetores armazenam dados do mesmo tipo, e em Python, podemos usar listas para simular esse comportamento. Para criar uma lista com elementos do mesmo tipo, basta colocá-los entre colchetes (“[]”). Veja alguns exemplos de listas como vetores:
```py
nums = [1, 4, 7, 2, 4, 9]

vogais = ['a', 'e', 'i', 'o', 'u']

booleanos = [True, True, False, True, False]

vazio = []
```
Consegue perceber que todos esses valores são delimitados por colchetes e que sempre são separados por vírgulas? Pois bem: é assim que definimos as listas. O comportamento de vetor é desejável para interagir de um mesmo jeito sobre os dados da lista, o que normalmente é feito dentro de um laço finito. Por exemplo: podemos multiplicar os valores em uma lista que armazena somente números, mas não poderíamos fazer isto em uma lista que possuiria textos

Se quiséssemos adicionar 10 elementos? 20? 50? Para que possamos adicionar os itens dinamicamente em uma lista existe um segredo para isto: o método append. Veja um exemplo:

```py
nums = []
for i in range(5):
    num = int(input("Digite um número: "))
    nums.append(num)
print(nums)
```
Dessa forma, independentemente da quantidade de elementos, a lista será populada corretamente. Até porque, geralmente, uma lista pode conter uma quantidade indefinida de elementos. 

### Acessando os dados de uma lista
E para lermos o que existe dentro de uma lista? Os dados em uma lista podem ser acessados a partir de seu nome, seguido do índice do elemento entre colchetes, sendo que o índice começa em 0 e vai até o número de elementos menos 1.

*Exemplo de aplicação*: Dada a lista de dados nums = [1, 4, 23, 11, 8], corra a lista usando um objeto range e imprima cada elemento em uma linha.
```py
nums = [1, 4, 23, 11, 8]
for i in range(len(nums)):
    print(nums[i])
```
Outra forma de obter o mesmo resultado é utilizar o comando for interagindo com cada elemento da lista, como segue:
```py
nums = [1, 4, 23, 11, 8]
for num in nums:
    print(num)
```

### Algoritmos de ordenação
Para ordenar um vetor, deve-se comparar um elemento com o seguinte, verificando se atende ou não ao critério de ordenação. Em caso positivo, deve ser efetuada a troca de posição entre os elementos do vetor. A fim de correr todo o vetor, devem ser efetuadas n - 1 iterações, como segue:
```py
for i in range(len(nums) - 1):
    if nums[i] > nums[i+1]:
        aux = nums[i]
        nums[i] = nums[i+1]
        nums[i+1] = aux
```
Neste caso, sempre é comparado um elemento com o imediatamente posterior, por isso as iterações devem ser na ordem de n - 1, para não estourar os limites do vetor. Para a troca de posições dentro do vetor, deve-se fazer uso de uma variável auxiliar, uma vez que, quando um elemento recebe nova atribuição, não é mais possível acessar seu valor anterior.

Fazendo uso dessa iteração, é possível perceber que, na ordenação crescente, caso o maior número esteja na primeira posição do vetor, ele será deslocado para o final. Assim sendo, para ordenar esse vetor, se faz necessário repetir este mesmo processo n - 1 vezes, fazendo uso de laços aninhados.
```py
nums = [17, 33, 23, 11, 8, 15, 9]
aux = 0
for _ in range(len(nums) - 1):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            aux = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = aux
print(nums)
```
É importante observar na linha 03 que, se a variável contadora não for utilizada dentro do bloco de códigos do laço, não será necessário declará-la, fazendo uso do símbolo de underscore (_).

## Listas com Comportamento de Matriz
Matrizes possuem comportamento análogo ao dos vetores, porém com capacidade de armazenamento multidimensional. Para os propósitos desta unidade, serão utilizadas apenas matrizes bidimensionais, ou seja, com duas dimensões. Isto é,  com duas dimensões.

O vetor, como visto anteriormente, possui vários elementos, e cada elemento ocupa uma posição. Analogamente, uma matriz bidimensional possui vários elementos dispostos como um vetor, porém cada posição possui um vetor de elementos.

Disposição em vetor:
```py
v = [17, 23, 11, 8, 15, 9, 33]
```
Disposição em matriz:
```py
m = [[3, 6, 8], [11, 5, 2], [1, 1, 21]]
```

Neste caso, basicamente, temos um vetor m com os seguintes elementos:
```py
m[0] = [3, 6, 8]

m[1] = [11, 5, 2]

m[2] = [1, 1, 21]
```

*Exemplo de aplicação:* Solicite ao usuário que digite três coordenadas (x, y), armazenando-as em uma matriz bidimensional.
```py
coordenadas = []
for i in range(3):
    x = int(input("Insira um valor de x: "))
    y = int(input("Insira um valor de y: "))
    coordenadas.append([x, y])
print(coordenadas)
```
### Acesso a elementos específicos de uma matriz
Assim como ocorre com vetores, que possuem a capacidade de acesso a um elemento específico a partir do seu índice, os elementos de uma matriz podem ser acessados a partir do índice de cada dimensão. No caso de uma matriz de dimensão 3x3, o elemento central poderia ser acessado a partir de:
```py
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(m[1][1])      # isto mostrará o número inteiro "5"
```

*Exemplo de aplicação:* Dada a matriz m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], efetue a soma de todos os seus elementos e exiba o resultado.
```py
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0
for i in range(3):
    for j in range(3):
        soma += m[i][j]
print("A soma dos elementos da matriz m é igual a", soma)
```

## Listas - métodos e funções built-in

### Métodos

Lembra dos tipos primitivos em Python (int, float, string e bool)? Pois é, a lista não é um deles. Por isso, as listas possuem algumas funcionalidades adicionais que não existem para estes tipos primitivos. No caso, pode-se: adicionar elementos, excluir elementos, entre outros. Segue a lista de métodos que podem ser aplicados sobre listas em Python:

- append()	Adiciona um elemento ao fim da lista.
- extend()	Adiciona todos os elementos de uma lista em outra.
- insert()	Insere um elemento em determinado índice da lista.
- remove()	Remove um elemento da lista.
- pop()	Remove e retorna determinado elemento de um índice da lista.
- clear()	Remove todos os elementos da lista.
- index()	Retorna o índice do primeiro elemento localizado na lista.
- count()	Retorna a quantidade de um elemento na lista passado como argumento.
- sort()	Ordena os elementos de uma lista em ordem ascendente.
- reverse()	Inverte a ordem dos elementos de uma lista.
- copy()	Retorna uma cópia da lista.

### Funçoes built in sobre listas

- len() Como vimos anteriormente, a função len retorna a quantidade de elementos de uma lista.
- max() A função max retorna o maior valor dentro de uma lista.
- min() A função min retorna o menor valor dentro de uma lista
- sorted() A função sorted retorna a lista passada em ordem crescente.
- sum() A função sum retorna a soma de todos os elementos de uma lista.


## Conclusão

A respeito do uso de listas na programação em Python, podemos concluir que:

- As listas são estruturas de dados heterogêneas.
- Entretanto, são normalmente usadas como estruturas de dados homogêneas.
- A linguagem Python não possui formalmente estruturas de vetor e matriz.
- Com listas, é possível simular o comportamento de vetores e matrizes.
- Os elementos de uma lista podem ser acessados a partir do nome dela, seguido do índice do elemento entre colchetes.
- Uma matriz é basicamente um vetor que apresenta em cada um de seus elementos um novo vetor.
- Os elementos de uma matriz podem ser acessados pelo nome dela, seguido dos índices de cada dimensão colocados individualmente entre colchetes.
- Listas podem ser modificadas a partir de métodos próprios e funções built in.