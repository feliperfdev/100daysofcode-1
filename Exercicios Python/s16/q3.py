class Elevador:

    pessoas_inicial = 0
    andar_inicial = 0

    def __init__(self, capacidade, quantPessoas, andarAtual, andares):
        self.capacidade = capacidade
        self.andarAtual = andarAtual
        self.andares = andares
        self.quantPessoas = quantPessoas
        Elevador.andar_inicial = self.andarAtual
        Elevador.pessoas_inicial = self.quantPessoas

    def entra(self, pessoa):
        "Função que coloca pessoas dentro do elevador."
        try:
            assert(type(pessoa) == int)
        except (TypeError, AssertionError) as error:
            print('Deve informar um valor do tipo inteiro!')
        else:
            total = pessoa + self.quantPessoas
            if total > self.capacidade:
                print('Elevador preenchido!')
                print(f'O limite de pessoas no elevador foi alcançada! Não pode entrar mais ninguém!')
                total = self.capacidade
            print(f'Tem {total} pessoa(s) no elevador!')
            Elevador.pessoas_inicial = total
    
    def sai(self, pessoa):
        "Função que retira pessoas do elevador."
        try:
            assert(type(pessoa) == int)
        except (TypeError, AssertionError) as error:
            print('Deve informar um valor do tipo inteiro!')
        else: 
            total = Elevador.pessoas_inicial - pessoa
            if total <= 0:
                print('Não tem mais pessoas para saírem do elevador!')
                total = 0
            print(f'Tem {total} pessoa(s) no elevador!')
            Elevador.pessoas_inicial = total
    
    def sobe(self, andar):
        "Função que faz o elevador subir de andar."
        try:
            assert(type(andar) == int)
        except AssertionError:
            print('Deve informar um valor do tipo inteiro!')
        else:
            try:
                assert(Elevador.pessoas_inicial > 0 )
            except AssertionError as error:
                print('O elevador não pode subir ao menos que tenham pessoas nele!')
            else:
                novoAndar = Elevador.andar_inicial + andar
                if self.andarAtual == self.andares and andar > self.andares:
                    print(f'O elevador já está no {self.andares}º andar. Não pode subir mais que isso!')
                    self.andarAtual = self.andares
                if novoAndar > self.andares:
                    print(f'O {self.andares}º andar é o último. Não pode subir mais que isso!')
                    novoAndar = self.andares
                print(f'O elevador está no {novoAndar}º andar.')
                Elevador.andar_inicial = novoAndar

    def desce(self, andar):
        "Função que faz o elevador descer de andar."
        try:
            assert(type(andar) == int)
        except AssertionError:
            print('Deve informar um valor do tipo inteiro!')
        else:
            try:
                assert(Elevador.pessoas_inicial > 0)
            except AssertionError as error:
                print('O elevador não pode descer ao menos que tenham pessoas nele!')
            else:
                novoAndar = Elevador.andar_inicial - andar
                if novoAndar < 0:
                    print('O elevador já está no térro. Impossível descer mais que isso!')
                    novoAndar = 0
                elif novoAndar == 0:
                    print('Você chegou ao térrio!')
                    novoAndar = 0
                elif novoAndar != 0:
                    print(f'O elevador está no {novoAndar}º andar.')
                Elevador.andar_inicial = novoAndar
        
    def info(self):
        "Mostra informações de quantas pessoas tem no elevador e em que andar ele está no momento."
        print(f'O elevador tem {Elevador.pessoas_inicial} pessoa(s) e está no {Elevador.andar_inicial}º andar!')
     
elevador1 = Elevador(10, 0, 1, 15)

elevador1.entra(1)
elevador1.desce(1)
elevador1.sobe(1)
elevador1.sobe(14)
elevador1.desce(2)
elevador1.info()
elevador1.desce(13)
elevador1.sobe(14)
elevador1.sobe(1)
elevador1.sobe(1)
elevador1.sai(1)
elevador1.desce(9)
elevador1.info()