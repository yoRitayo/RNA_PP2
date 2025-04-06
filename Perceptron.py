import numpy as np


class Perceptron:
    """
    A perceptron is a classification model that consists of a set of weights, or scores,
    one for every feature, and a threshold. The perceptron multiplies each weight by its
    corresponding score, and adds them, obtaining a score.
    by Rajwrite Nath on Medium
    """

    def __init__(self, threshold, lr):
        self.threshold = threshold
        self.lr = lr
        self.weights = None
        self.scores = None
        self.adjustments = 0
        self.epochs = 1

    def gen_weights(self, low, high, size):
        self.weights = np.random.uniform(low, high, size)

    def print_weights(self):
        np.set_printoptions()
        print(self.weights)

    def step_fn(self, z):
        return np.where(z >= self.threshold, 1, 0)

    def error_fn(self, y_true, y_predicted):
        return np.sum(y_true - y_predicted)

    def predict(self, x_data):
        return self.step_fn(np.dot(x_data, self.weights.T))

    def fit(self, x_data, y_data):
        self.print_weights()
        self.gen_weights(-0.5, 0.5, size=x_data.shape[0].reshape(-1, 2))

        y_predicted = self.predict(x_data)
        self.scores = y_predicted  # Atualiza os scores

        # Algoritmo executa até a convergência, supomos que as classes sejam linearmente separáveis
        while not np.all(y_data == self.scores):
            self.epochs += 1  # Não convergiu, vai necessitar de mais 1 época

            # Para os pesos que resultaram em uma predição errada:

            predicoes_incorretas = (y_data != self.scores)

            for i in np.where(predicoes_incorretas)[0]:
                x = x_data[predicoes_incorretas]
                y = y_data[predicoes_incorretas]
                y_pred = y_predicted[predicoes_incorretas]

                # Calculando erros
                error = self.error_fn(y, y_pred)

                # Relculando pesos
                self.weights += self.lr * error * x
                self.adjustments += 1


# Inicializando a semente
np.random.seed(0)

# Inicializando o neurônio
neuronio_perceptron = Perceptron(threshold=0, lr=0.1)
neuronio_perceptron.fit(x_data, y_data)

