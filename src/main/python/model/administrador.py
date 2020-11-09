from usuario import Usuario
 
class Administrador(Usuario):

    def __init__(self,  nome="",login="", senha=""):
        Usuario.__init__(self, nome, login,senha)
    
    def cadastrarCafeicultor(self):
        print('cadastrarCafeicultor')

    def editarCafeicultor(self):
        print('editarCafeicultor')

    def buscarCafeicultor(self):
        print('buscarCafeicultor')

    def excluirCafeicultor(self):
        print('excluirCafeicultor')
