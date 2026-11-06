# superclasses
class Carro:
    def __init__(self,cambio,estepe,porta_malas,volante,retrovisor,buzina,escapamento):
        self.__cambio = cambio
        self.__estepe = estepe
        self.__porta_malas = porta_malas
        self.__volante = volante
        self.__retrovisor = retrovisor
        self.__buzina = buzina
        self.__escapamento = escapamento

    @property
    def cambio(self):
        return self.__cambio

    @cambio.setter
    def cambio(self,cambio):
        self.__cambio = cambio

    @property
    def estepe(self):
        return self.__estepe

    @estepe.setter
    def estepe(self,estepe):
        self.__estepe = estepe

    @property
    def porta_malas(self):
        return self.__porta_malas

    @porta_malas.setter
    def porta_malas(self,porta_malas):
        self.__porta_malas = porta_malas

    @property
    def volante(self):
        return self.__volante

    @volante.setter
    def volante(self,volante):
        self.__volante = volante

    @property
    def retrovisor(self):
        return self.__retrovisor

    @retrovisor.setter
    def retrovisor(self,retrovisor):
        self.__retrovisor = retrovisor

    @property
    def buzina(self):
        return self.__buzina

    @buzina.setter
    def buzina(self,buzina):
        self.__buzina = buzina

    @property
    def escapamento(self):
        return self.__escapamento

    @escapamento.setter
    def escapamento(self,escapamento):
        self.__escapamento = escapamento


class Aviao:
    def __init__(self,asa,turbina,aerofolio,cauda,manche,caixa_preta):
        self.__asa = asa
        self.__turbina = turbina
        self.__aerofolio = aerofolio
        self.__cauda = cauda
        self.__manche = manche
        self.__caixa_preta = caixa_preta

    @property
    def asa(self):
        return self.__asa

    @asa.setter
    def asa(self,asa):
        self.__asa = asa

    @property
    def turbina(self):
        return self.__turbina

    @turbina.setter
    def turbina(self,turbina):
        self.__turbina = turbina

    @property
    def aerofolio(self):
        return self.__aerofolio

    @aerofolio.setter
    def aerofolio(self,aerofolio):
        self.__aerofolio = aerofolio

    @property
    def manche(self):
        return self.__manche

    @manche.setter
    def manche(self,manche):
        self.__manche = manche

    @property
    def cauda(self):
        return self.__cauda

    @cauda.setter
    def cauda(self,cauda):
        self.__cauda = cauda

    @property
    def caixa_preta(self):
        return self.__caixa_preta

    @caixa_preta.setter
    def caixa_preta(self,caixa_preta):
        self.__caixa_preta = caixa_preta


class CarroVoador(Carro, Aviao):
    def __init__(self,cambio,estepe,porta_malas,volante,retrovisor,buzina,escapamento,asa,turbina,aerofolio,cauda,manche,caixa_preta):
        Carro.__init__(self,cambio,estepe,porta_malas,volante,retrovisor,buzina,escapamento)
        Aviao.__init__(self,asa,turbina,aerofolio,cauda,manche,caixa_preta)