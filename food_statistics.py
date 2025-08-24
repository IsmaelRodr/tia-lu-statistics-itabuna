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

        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
        
        valores = self.dataset[column]
        if len(valores) == 0:
            return 0.0
        
        media_aritmetica = sum(valores) / len(valores)

        return float(media_aritmetica)

        pass

    def median(self, column):

        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")

        valores = self.dataset[column]
        if len(valores) == 0:
            return 0.0
        
        valores_ordenados = sorted(valores)
            
        if len(valores_ordenados) % 2 == 0:
            i = len(valores_ordenados) // 2 - 1
            mediana = (valores_ordenados[i] + valores_ordenados[i + 1]) / 2
        else:
            i = len(valores_ordenados) // 2
            mediana = valores_ordenados[i]
        
        return float(mediana)
            
        pass

    def mode(self, column):

        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")

        valores = self.dataset[column]
        if not valores:
            return []
        
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

        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")

        valores = self.variance(column)
        if not valores:
            return 0.0

        desvio_padrao = valores ** 0.5

        return float(desvio_padrao)
      

        pass

    def variance(self, column):

        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")

        valores = self.dataset[column]
        if not valores:
            return 0.0

        media = self.mean(column)

        desvios_quadrados = []
        for item in valores:
            desvio = item - media
            desvio_quadrado = desvio ** 2
            desvios_quadrados.append(desvio_quadrado)

        variancia = (sum(desvios_quadrados)) / len(valores)

        return float(variancia)

        pass

    def covariance(self, column_a, column_b):

        if column_a not in self.dataset or column_b not in self.dataset:
            raise KeyError("Uma das colunas não existe no dataset.")

        valores_a = self.dataset[column_a]
        valores_b = self.dataset[column_b]

        if not valores_a or not valores_b or len(valores_a) != len(valores_b) or len(valores_a) < 2:
            return 0.0

        media_a = self.mean(column_a)
        media_b = self.mean(column_b)

        soma_dos_produtos_dos_desvios = sum((x - media_a) * (y - media_b) for x, y in zip(valores_a, valores_b))

        return float(soma_dos_produtos_dos_desvios / len(valores_a))
          
        pass

    def itemset(self, column):

        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
     
        itens = self.dataset[column]
        itens_unicos = set(itens)

        return itens_unicos
      
        pass

    def absolute_frequency(self, column):

        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
        
        valores = self.dataset[column]
        
        valores_unicos = set(valores)
        
        frequencias = {}
        for item in valores_unicos:
            frequencias[item] = valores.count(item)
            
        return frequencias
    
        pass

    def relative_frequency(self, column):

        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
        
        valores = self.dataset[column]
        if len(valores) == 0:
            return {}
        
        valores_unicos = set(valores)
        
        frequencias = {}
        for item in valores_unicos:
            frequencias[item] = valores.count(item) / len(valores)
            
        return frequencias
    
        pass

    def cumulative_frequency(self, column, frequency_method='absolute'):

       if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
       
       if frequency_method not in ['absolute', 'relative']:
            raise ValueError("O 'frequency_method' deve ser 'absolute' ou 'relative'.")
       
       valores = self.dataset[column]
       if not valores:
            return {}
       
       if frequency_method == 'absolute':
            frequencias = self.absolute_frequency(column) 
       else:
           frequencias = self.relative_frequency(column)
    
       frequencia_acumulada = {}
       acumulado = 0
           
       for item in sorted(frequencias.keys()):
            acumulado += frequencias[item]
            frequencia_acumulada[item] = acumulado


       return frequencia_acumulada

       pass

    def conditional_probability(self, column, value1, value2):

        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")

        valores = self.dataset[column]
        if not valores or len(valores) < 2:
            return 0.0

        totalB = 0
        sequencia = 0

        totalB = sum(1 for v in valores[0:] if v == value2)
        sequencia = sum(1 for i in range(len(valores) - 1) if valores[i] == value2 and valores[i + 1] == value1)
        
        if totalB > 0:
            return float(sequencia / totalB)
        return 0.0

        pass