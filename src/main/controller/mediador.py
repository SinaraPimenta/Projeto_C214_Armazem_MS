from __future__ import annotations
from abc import ABC
import sys
sys.path.append('src/main/model')
import sacaCafe
sys.path.append('src/main/controller')
import bancoDeDados

class MediadorInterface(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """

    def notify(self, sender: object, event: str, colecao: str, indice:int, login:str) -> None:
        pass

class MediadorDoCafeicultor(MediadorInterface):
    def __init__(self,colecao:str, bd: bancoDeDados.BancoDeDados, cafe: sacaCafe.SacaDeCafe = None, indice="",login="") -> None:
        self._bd = bd
        self._bd.mediator = self
        self._cafe = cafe
        if cafe:
            self._cafe.mediator = self
        self._colecao = colecao
        self._indice = indice
        self._login = login

    def notify(self, sender: object, event: str) -> None:
        if event == "Buscar":
            return self._bd.buscarSacasDeCafe(self._login,self._colecao)
        elif event == "Cadastrar":
            self._bd.cadastrarSacasDeCafe(self._cafe,self._colecao)
            self._bd.adicionarNalistaCafe(self._cafe)
        elif event == "Editar":
            self._bd.alterarSacaDeCafe(self._cafe,self._colecao)
            self._bd.substituiCafe(self._cafe)
        elif event == "Excluir":
            id = self._cafe.idGet()
            indice = self._cafe.indiceGet()
            self._bd.deletarSacaDeCafe(id,self._colecao)
            self._bd.removerDalistaCafe(indice)
        elif event == "Vender":
            self._bd.venderSacaDeCafe(self._cafe,self._colecao)
            self._bd.substituiCafe(self._cafe) 
        elif event == "Get":
            return self._bd.getCafe(self._indice)
        elif event == "Consultar":
            return self._bd.buscaNoBD(self._login,self._colecao)


        
        

