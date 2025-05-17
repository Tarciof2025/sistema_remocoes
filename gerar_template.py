import pandas as pd

def gerar_template(nome_arquivo="template_remocoes.xlsx"):
    # Define as colunas principais que você mencionou (pode ajustar conforme precisar)
    colunas = [
        "Placa",
        "Deposito/Vendido",
        "Modelo",
        "Chassi",
        "Cliente",
        "Pátio",
        "Segmento",
        "Contato",
        "Telefone",
        "UF",
        "Cidade",
        "Endereço",
        "Data solicitação/Agendamento",
        "SLA",
        "Data Real remoção",
        "Data da frustada",
        "Impedimento",
        "Coluna1",
        "Status",
        "Motivo",
        "Responsável",
        "Data Nova Tratativa",
        "Endereço Nova Tratativa Scope",
        "Data da ultima leitura",
        "Endereço do Rastreador",
        "Fonte da Confirmação de Endereço",
        "Observação",
        "Data Impedimento/Frustada",
        "Ano",
        "Mês",
        "SEMANA",
        "Confirmação de Retirada",
        "Tempo para remoção",
        "target",
        "Dias",
        "Status dias"
    ]

    # Cria um DataFra
