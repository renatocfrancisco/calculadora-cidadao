def financiamentoPrestacoesFixas(n, j, p):
    """
    Calcula o valor financiado (q0) usando a fórmula de juros compostos e capitalização mensal.

    Parâmetros:
    n (int): Número de meses
    j (float): Taxa de juros mensal
    p (float): Valor da prestação

    Retorna:
    float: Valor financiado (q0)
    """

    # Exemplo de uso
    # n = 12  # Número de meses
    # j = 0.02  # Taxa de juros mensal (2%)
    # p = 500  # Valor da prestação
    
    # Fórmula: q0 = (((1 - (1 + j) ** -n)) / j) * p
    q0 = (((1 - (1 + j) ** -n)) / j) * p

    total_financiamento = n * p
    total_em_juros = total_financiamento - q0
    total_em_juros_arredondado = round(total_em_juros, 2)

    result = {
        "q0": q0,
        "total_financiamento": total_financiamento,
        "total_em_juros": total_em_juros,
        "total_em_juros_arredondado": total_em_juros_arredondado,
        "texto": f"O total desse financiamento de {n} parcelas de {p} reais é {total_financiamento}, sendo {total_em_juros_arredondado} de juros.",
    }

    return result
