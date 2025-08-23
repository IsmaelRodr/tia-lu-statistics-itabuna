class Statistics:
    """
    Uma classe para realizar cálculos estatísticos em um conjunto de dados.

    Atributos
    ----------
    dataset : dict[str, list]
        O conjunto de dados, estruturado como um dicionário onde as chaves
        são os nomes das colunas e os valores são listas com os dados.
    """
    def __init__(self, dataset):
        # """
        # Inicializa o objeto Statistics.

        # Parâmetros
        # ----------
        # dataset : dict[str, list]
        #     O conjunto de dados, onde as chaves representam os nomes das
        #     colunas e os valores são as listas de dados correspondentes.
        # """
        if not isinstance(dataset, dict):
            raise TypeError("O dataset deve ser um dicionário.")
    
        for column, values in dataset.items():
            if not isinstance(values, list):
               raise TypeError("Todos os valores no dicionário do dataset devem ser listas.")
        
        lengths = [len(values) for values in dataset.values()]
        if len(set(lengths)) != 1:
            raise ValueError("Todas as colunas no dataset devem ter o mesmo tamanho.")
            
        self.dataset = dataset

    def mean(self, column):
        
        valores = self.dataset[column]
        media_aritmetica = sum(valores) / len(valores)
        return media_aritmetica

        pass

    def median(self, column):
        
        valores = self.dataset[column]
        
        valores_ordenados = sorted(valores)
            
        if len(valores_ordenados) % 2 == 0:
            i = len(valores_ordenados) // 2 - 1
            dois_valores = [valores_ordenados[i],valores_ordenados[i + 1]]
            mediana = self.mean(dois_valores)
        else:
            i = len(valores_ordenados) // 2 - 1
            mediana = valores_ordenados[i]
        
        return mediana
            
        
        
        # """
        # Calcula a mediana de uma coluna.

        # A mediana é o valor central de um conjunto de dados ordenado.

        # Parâmetros
        # ----------
        # column : str
        #     O nome da coluna (chave do dicionário do dataset).

        # Retorno
        # -------
        # float
        #     O valor da mediana da coluna.
        # """
        pass

    def mode(self, column):
        
        valores = self.dataset[column]
        
        valores_unicos = set(valores)
        
        frequencias = {}
        for item in valores_unicos:
            frequencias[item] = valores.count(item)
            
        maior_frequencia = max(frequencias.values())
        
        moda = []
        for item, freq in frequencias.items():
            if freq == maior_frequencia:
                moda.append(item)

        return moda
        
        pass

    def stdev(self, column):
        """
        Calcula o desvio padrão populacional de uma coluna.

        Fórmula:
        $$ \sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}} $$

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O desvio padrão dos valores na coluna.
        """

        valores = self.dataset[column]
        variancia = self.variance(valores)

        desvio_padrao = variancia ** 0.5

        return float(desvio_padrao)
      

        pass

    def variance(self, column):
        """
        Calcula a variância populacional de uma coluna.

        Fórmula:
        $$ \sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N} $$

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A variância dos valores na coluna.
        """
        valores = self.dataset[column]
        media = self.mean(valores)

        desvios_quadrados = []
        for item in valores:
            desvio = item - media
            desvio_quadrado = desvio ** 2
            desvios_quadrados.append(desvio_quadrado)

        variancia = (sum(desvios_quadrados)) / len(valores)

        return float(variancia)

        pass

    def covariance(self, column_a, column_b):
        
        valores_a = self.dataset[column_a]
        valores_b = self.dataset[column_b]
        
        media_a = self.mean(valores_a)
        media_b = self.mean(valores_b)
        
        desvio_a = 0
        desvio_b = 0
        
        for valor_a in valores_a:
            desvio_a += (valor_a - media_a)
        
        for valor_b in valores_b:
            desvio_b += (valor_b - media_b)
        
        covariance = (desvio_a * desvio_b) / len(valores_a) - 1
        
        return float(covariance)
        
        # """
        # Calcula a covariância entre duas colunas.

        # Fórmula:
        # $$ \text{cov}(X, Y) = \frac{\sum_{i=1}^{N} (x_i - \mu_x)(y_i - \mu_y)}{N} $$

        # Parâmetros
        # ----------
        # column_a : str
        #     O nome da primeira coluna (X).
        # column_b : str
        #     O nome da segunda coluna (Y).

        # Retorno
        # -------
        # float
        #     O valor da covariância entre as duas colunas.
        # """
        pass

    def itemset(self, column):
     
        itens = self.dataset[column]
        itens_unicos = set(itens)
        return itens_unicos
      
        pass

    def absolute_frequency(self, column):
        
        valores = self.dataset[column]
        
        valores_unicos = set(valores)
        
        frequencias = {}
        for item in valores_unicos:
            frequencias[item] = valores.count(item)
            
        return frequencias
    
        # """
        # Calcula a frequência absoluta de cada item em uma coluna.

        # Parâmetros
        # ----------
        # column : str
        #     O nome da coluna (chave do dicionário do dataset).

        # Retorno
        # -------
        # dict
        #     Um dicionário onde as chaves são os itens e os valores são
        #     suas contagens (frequência absoluta).
        # """
        pass

    def relative_frequency(self, column):
        
        valores = self.dataset[column]
        
        valores_unicos = set(valores)
        
        frequencias = {}
        for item in valores_unicos:
            frequencias[item] = valores.count(item) / len(valores)
            
        return frequencias
        # """
        # Calcula a frequência relativa de cada item em uma coluna.

        # Parâmetros
        # ----------
        # column : str
        #     O nome da coluna (chave do dicionário do dataset).

        # Retorno
        # -------
        # dict
        #     Um dicionário onde as chaves são os itens e os valores são
        #     suas proporções (frequência relativa).
        # """
        pass

    def cumulative_frequency(self, column, frequency_method='absolute'):
        """
        Calcula a frequência acumulada (absoluta ou relativa) de uma coluna.

        A frequência é calculada sobre os itens ordenados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        frequency_method : str, opcional
            O método a ser usado: 'absolute' para contagem acumulada ou
            'relative' para proporção acumulada (padrão é 'absolute').

        Retorno
        -------
        dict
            Um dicionário ordenado com os itens como chaves e suas
            frequências acumuladas como valores.
        """
        pass

    def conditional_probability(self, column, value1, value2):
        """
        Calcula a probabilidade condicional P(X_i = value1 | X_{i-1} = value2).

        Este método trata a coluna como uma sequência e calcula a probabilidade
        de encontrar `value1` imediatamente após `value2`.

        Fórmula: P(A|B) = Contagem de sequências (B, A) / Contagem total de B

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        value1 : any
            O valor do evento consequente (A).
        value2 : any
            O valor do evento condicionante (B).

        Retorno
        -------
        float
            A probabilidade condicional, um valor entre 0 e 1.
        """
        pass