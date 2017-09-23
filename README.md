# Ubermap Natal
by [Maradona Morais](https://github.com/mrmorais) e Daniel Marx

<center>
<img src="https://github.com/mrmorais/uber-map-natal/blob/master/imgs/without_lbls.png?raw=true">
</center>

### Requisitos de ambiente
Para iniciar o `uber_map.py` é necessário ter [Python](https://www.python.org) instalado no computador e os seguintes pacotes, existentes no [Python Package Index](https://pypi.python.org):

- [Uber Rides API](https://developer.uber.com/docs/riders/ride-requests/tutorials/api/python)
- [Pandas](http://pandas.pydata.org)

### Configurando Ubermap

**Token**

Você precisará criar uma conta no [Uber Developer](https://developer.uber.com) e criar uma aplicação, assim você receberá um token de acesso ao servidor da Uber, com limite de 2k requisições por hora.

Com o token em mãos é preciso criar o arquivo de configuração. Em `src/config` renomeie o arquivo `uber_config_template.py` para `uber_config.py` e altere o campo `TokenUber` para o valor do token que você adquiriu.

**ID do Produto Uber**

Agora você precisa identificar qual o Id do produto que você deseja trackear com o `uber_map.py`, nós criamos um script que, dado uma coordenada geográfica, identifica quais são os produtos Uber que estão disponíveis. Nós realizamos a pesquisa somente com o produto UberX, único disponível em Natal-RN. O sistema possui a limitação de trackear somente um tipo de produto.

Execute o script `uber_products.py` para ver os IDs de produtos Uber na região de Natal, caso queira ver outras regiões altere a latitude e longitude no código-fonte.

Altere o valor de `ProductID` no `uber_config.py` para o valor do ID de produto que você deseja trackear.

**Arquivo de saída**

Antes de iniciar o `src/uber_map.py` você deve renomear o arquivo `data/uber_map_header.csv` para apenas `uber_map.csv`, preferencialmente guarde uma cópia do arquivo original para quando quiser iniciar o processo do zero.

### Iniciando script

Com todos esses processos realizados, o script está pronto para funcionar. Execute `python src/uber_map.py` e aguarde a leva de requisições. O script faz requisições a cada 3 minutos, são em torno de 90 requisições, mas a média de cada bairro já é feita após serem obtidas todas as estimativas para o bairro. Assim, o arquivo `uber_map.csv` aumentará uma linha a cada 3 minutos, onde cada linha indica a média da estimativa de espera para todos os pontos de cada bairro (identificados pelas colunas).

A parada deve ser manual, com `Ctrl + C`. Os dados são escritos no arquivo apenas após uma leva de requisições, garantindo que os dados já obtidos não sejam perdidos em casos de exceções no código, ou parada manual.
