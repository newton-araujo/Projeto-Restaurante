class Pedido:
    def __init__(self, item, quantidade, preço):
        self.item = item
        self.quantidade = quantidade
        self.preço = preço
        self.pedido = {"prato":self.item,"quantidade":self.quantidade,"preço":self.preço}
    
    def pedir(self):
        print('Pedido realizado com sucesso')
        
    def obter_valor(self):
        return self.pedido['prato'], self.pedido['quantidade'], self.pedido['preço']
    



