import pytest

def test_numero_invalido():
    with pytest.raises(ValueError):
        para_extenso(0)

def test_valor_nao_numerico():
    with pytest.raises(TypeError):
        para_extenso("")

def test_valida_um_real():
    assert "um real" == para_extenso(1)

def test_valida_dois_reais():
    assert "dois reais" == para_extenso(2)

def test_valida_tres_reais():
    assert "tres reais" == para_extenso(3)

def test_valida_quatro_reais():
    assert "quatro reais" == para_extenso(4)

def test_valida_cinco_reais():
    assert "cinco reais" == para_extenso(5)

def test_valida_seis_reais():
    assert "seis reais" == para_extenso(6)

def test_valida_sete_reais():
    assert "sete reais" == para_extenso(7)

def test_valida_oito_reais():
    assert "oito reais" == para_extenso(8)

def test_valida_nove_reais():
    assert "nove reais" == para_extenso(9)

def test_valida_dez_reais():
    assert "dez reais" == para_extenso(10)

def test_valida_onze_reais():
    assert "onze reais" == para_extenso(11)

def test_valida_doze_reais():
    assert "doze reais" == para_extenso(12)

def test_valida_treze_reais():
    assert "treze reais" == para_extenso(13)

def test_valida_quatorze_reais():
    assert "quatorze reais" == para_extenso(14)

def test_valida_quinze_reais():
    assert "quinze reais" == para_extenso(15)

def test_valida_dezesseis_reais():
    assert "dezesseis reais" == para_extenso(16)

def test_valida_dezessete_reais():
    assert "dezessete reais" == para_extenso(17)

def test_valida_dezoito_reais():
    assert "dezoito reais" == para_extenso(18)

def test_valida_dezenove_reais():
    assert "dezenove reais" == para_extenso(19)

def test_valida_vinte_reais():
    assert "vinte reais" == para_extenso(20)

def test_valida_vinte_e_um_reais():
    assert "vinte e um reais" == para_extenso(21)

def test_valida_vinte_e_dois_reais():
    assert "vinte e dois reais" == para_extenso(22)


def test_valida_vinte_e_nove_reais():
    assert "vinte e nove reais" == para_extenso(29)

def test_valida_trinta_reais():
    assert "trinta reais" == para_extenso(30)

def test_valida_trinta_e_um_reais():
    assert "trinta e um reais" == para_extenso(31)

def test_valida_trinta_e_nove_reais():
    assert "trinta e nove reais" == para_extenso(39)

def test_valida_quarenta_reais():
    assert "quarenta reais" == para_extenso(40)

def test_valida_quarenta_e_um_reais():
    assert "quarenta e um reais" == para_extenso(41)

def test_valida_quarenta_e_nove_reais():
    assert "quarenta e nove reais" == para_extenso(49)

def test_valida_cinquenta_reais():
    assert "cinquenta reais" == para_extenso(50)

def test_valida_sessenta_reais():
    assert "sessenta reais" == para_extenso(60)

def test_valida_setenta_reais():
    assert "setenta reais" == para_extenso(70)

def test_valida_oitenta_reais():
    assert "oitenta reais" == para_extenso(80)

def test_valida_noventa_reais():
    assert "noventa reais" == para_extenso(90)

def test_valida_noventa_e_nove_reais():
    assert "noventa e nove reais" == para_extenso(99)

def test_valida_cem():
    assert "cem reais" == para_extenso(100)

def test_valida_um_centavo():
    assert "um centavo" == para_extenso(0.01)

def test_valida_dois_centavos():
    assert "dois centavos" == para_extenso(0.02)

def test_valida_tres_centavos():
    assert "tres centavos" == para_extenso(0.03)

def test_valida_nove_centavos():
    assert "nove centavos" == para_extenso(0.09)

def test_valida_dez_centavos():
    assert "dez centavos" == para_extenso(0.10)

def test_valida_onze_centavos():
    assert "onze centavos" == para_extenso(0.11)

def test_valida_dezenove_centavos():
    assert "dezenove centavos" == para_extenso(0.19)

def test_valida_vinte_centavos():
    assert "vinte centavos" == para_extenso(0.20)

def test_valida_vinte_e_um_centavos():
    assert "vinte e um centavos" == para_extenso(0.21)

def test_valida_vinte_e_nove_centavos():
    assert "vinte e nove centavos" == para_extenso(0.29)

def test_valida_quarenta_e_cinco():
    assert "quarenta e cinco centavos" == para_extenso(0.45)



def para_extenso(numero):
    if numero <= 0:
        raise ValueError("Valor invalido")
    if type(numero) != float and type(numero) != int:
        raise TypeError("Valor não numérico")
    primarios = {
                    0: "zero",
                    1: "um",
                    2: "dois",
                    3: "tres",
                    4: "quatro",
                    5: "cinco",
                    6: "seis",
                    7: "sete",
                    8: "oito",
                    9: "nove",
                    10: "dez",
                    11: "onze",
                    12: "doze",
                    13: "treze",
                    14: "quatorze",
                    15: "quinze",
                    16: "dezesseis",
                    17: "dezessete",
                    18: "dezoito",
                    19: "dezenove",
                }

    dezenas = {
                    1: "dez",
                    2: "vinte",
                    3: "trinta",
                    4: "quarenta",
                    5: "cinquenta",
                    6: "sessenta",
                    7: "setenta",
                    8: "oitenta",
                    9: "noventa",
    }

    centenas = {
                    1: "cem",

    }

    real = "real"

    if numero < 1:
        aux = para_extenso(round(numero*100,0));
        return aux.replace("real","centavo").replace("reais","centavos")

    if numero > 1:
        real = "reais"

    if numero == 100:
        return "cem reais"

    if numero >= 20 and numero <= 99:
        dezena = int(numero / 10)
        if (numero-dezena*10) == 0:
            return dezenas[dezena] + " " + real
        return dezenas[dezena] + " e " + primarios[numero-dezena*10] + " " + real

    return primarios[numero] + " " + real
