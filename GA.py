import random
import sys
import operator


class Knapsack(object):

    # Variáveis e listas
    def __init__(self):

        self.C = 0
        self.weights = []
        self.profits = []
        self.opt = []
        self.parents = []
        self.newparents = []
        self.bests = []
        self.best_p = []
        self.iterated = 1
        self.population = 0

        # profundidade máxima da pilha
        iMaxStackSize = 1500
        sys.setrecursionlimit(iMaxStackSize)

    # Criando população incial
    def initialize(self):

        for i in range(self.population):
            parent = []
            for k in range(0, 5):
                k = random.randint(0, 1)
                parent.append(k)
            self.parents.append(parent)

    # Detalhes do problema
    def properties(self, weights, profits, opt, C, population):

        self.weights = weights
        self.profits = profits
        self.opt = opt
        self.C = C
        self.population = population
        self.initialize()

    # função fitness de cada lista
    def fitness(self, item):

        sum_w = 0
        sum_p = 0

        # pesos e lucros
        for index, i in enumerate(item):
            if i == 0:
                continue
            else:
                sum_w += self.weights[index]
                sum_p += self.profits[index]

        # se for maior que o retorno ideal -1 ou o número caso contrário
        if sum_w > self.C:
            return -1
        else:
            return sum_p

    # executar gerações GA
    def evaluation(self):

        # percorrer os pais e calcular função fitness
        best_pop = self.population // 2
        for i in range(len(self.parents)):
            parent = self.parents[i]
            ft = self.fitness(parent)
            self.bests.append((ft, parent))

        # classificar a lista fitness
        self.bests.sort(key=operator.itemgetter(0), reverse=True)
        self.best_p = self.bests[:best_pop]
        self.best_p = [x[1] for x in self.best_p]

    # mutação
    def mutation(self, ch):

        for i in range(len(ch)):
            k = random.uniform(0, 1)
            if k > 0.5:
                # #se número flutuante aleatório maior que 0,5, inverta 0 com 1 e vice-versa
                if ch[i] == 1:
                    ch[i] = 0
                else:
                    ch[i] = 1
        return ch

    # crossover dos dois pais para produzir filhos misturando com função aleatória
    def crossover(self, ch1, ch2):

        threshold = random.randint(1, len(ch1) - 1)
        tmp1 = ch1[threshold:]
        tmp2 = ch2[threshold:]
        ch1 = ch1[:threshold]
        ch2 = ch2[:threshold]
        ch1.extend(tmp2)
        ch2.extend(tmp1)

        return ch1, ch2

    # Execução do algoritmo GA
    def run(self):

        # execute
        self.evaluation()
        newparents = []
        pop = len(self.best_p) - 1

        # cria uma lista com números interiros aleatórios exclusivos
        sample = random.sample(range(pop), pop)
        for i in range(0, pop):
            # Selecionar o indice aleatório dos melhores filhos para randomizar
            if i < pop - 1:
                r1 = self.best_p[i]
                r2 = self.best_p[i + 1]
                nchild1, nchild2 = self.crossover(r1, r2)
                newparents.append(nchild1)
                newparents.append(nchild2)
            else:
                r1 = self.best_p[i]
                r2 = self.best_p[0]
                nchild1, nchild2 = self.crossover(r1, r2)
                newparents.append(nchild1)
                newparents.append(nchild2)

        # transformar os filhos e pais em potencial para garantir que sejam encontrados ótimos globais
        for i in range(len(newparents)):
            newparents[i] = self.mutation(newparents[i])

        if self.opt in newparents:
            print("ótimos encontrados em {} gerações".format(self.iterated))
        else:
            self.iterated += 1
            print("recriar gerações por {} tempo".format(self.iterated))
            self.parents = newparents
            self.bests = []
            self.best_p = []
            self.run()


# teste da função
weights = [12, 7, 11, 8, 9]
profits = [24, 13, 23, 15, 16]
opt = [0, 1, 1, 1, 0]
C = 26
population = 10

k = Knapsack()
k.properties(weights, profits, opt, C, population)
k.run()