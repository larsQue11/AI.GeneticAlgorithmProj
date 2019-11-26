class Network():

    def __inti__(self):
        self.inputLayer = {'currentRGB': Neuron(),
                            'fitness': Neuron(),
                            'leftPixelFitness': Neuron(),
                            'abovePixelFitness': Neuron(),
                            'rightPixelFitness': Neuron(),
                            'belowPixelFitness': Neuron()
                            }
                            
class Neuron():

    def __init__(self):
        self.data
        self.next
