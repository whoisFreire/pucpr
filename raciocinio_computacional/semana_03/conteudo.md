# Semana 3

## Laços de repetição
Dentro da estrutura de repetição, temos os laços finitos e infintos

### Laços finitos
```python
for var in <<sequencia>>:
    <<bloco de ações>>
```

Em Python, o for pode ser usado para iterar (percorrer) por sequências finitas como strings (textos) ou um conjunto pré-definido de valores, por exemplo.

### Laços infinitos
O comando em Python que implementa a estrutura de repetição infinita é o comando while, cuja sintaxe é:

```python
while <<condição>>:
    <<bloco de ações>>
```

### Controle de fluxo
- break - Interrompe o fluxo da estrutura de repetição
- continue - Força uma iteração a partir do ponto corrente.
- pass - Somente processa a linha, mas não faz nada.


## Tratamento de exceções
Podemos lidar com exceções de forma adequada usando um bloco try e except. Neste caso, podemos imaginar que estamos caminhando com cuidado enquanto subimos a escada, prontos para nos segurar no corrimão se tropeçarmos. Assim, mesmo que um erro ocorra, podemos nos recuperar e continuar executando o programa.

```python
try:
    num = int(input("Digite um número: "))
except:
    print("valor inválido")