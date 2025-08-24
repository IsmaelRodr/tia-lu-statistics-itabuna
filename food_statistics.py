class Statistics:

    def __init__(self, dataset):

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

        return float(media_aritmetica)

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
        
        return float(mediana)
            
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

        return float(moda)
        
        pass

    def stdev(self, column):

        valores = self.dataset[column]
        variancia = self.variance(valores)

        desvio_padrao = variancia ** 0.5

        return float(desvio_padrao)
      

        pass

    def variance(self, column):

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
        
        pass

    def itemset(self, column):
     
        itens = self.dataset[column]
        itens_unicos = set(itens)

        return float(itens_unicos)
      
        pass

    def absolute_frequency(self, column):
        
        valores = self.dataset[column]
        
        valores_unicos = set(valores)
        
        frequencias = {}
        for item in valores_unicos:
            frequencias[item] = valores.count(item)
            
        return frequencias
    
        pass

    def relative_frequency(self, column):
        
        valores = self.dataset[column]
        
        valores_unicos = set(valores)
        
        frequencias = {}
        for item in valores_unicos:
            frequencias[item] = valores.count(item) / len(valores)
            
        return frequencias
    
        pass

    def cumulative_frequency(self, column, frequency_method='absolute'):
  
        valores = self.dataset[column]
        valores_ordenados = sorted(valores)
        acumulado = 0

        frequencia = {}
        for item in valores_ordenados:
            acumulado = acumulado + valores.count(item)
            if frequency_method == 'relative':
                frequencia[item] = acumulado / len(valores)
            else:
                frequencia[item] = acumulado

        return frequencia

        pass

    def conditional_probability(self, column, value1, value2):

        valores = self.dataset[column]

        totalB = 0
        sequencia = 0

        for i in range(len(valores) - 1):
            if valores[i] == value2:
                totalB = totalB + 1
                if valores[i + 1] == value1:
                    sequencia = sequencia + 1
        
        if totalB > 0:
            probabilidade_condicional = sequencia / totalB
        else:
            probabilidade_condicional = 0 

        return float(probabilidade_condicional)

        pass