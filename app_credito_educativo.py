import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# ============================================================
# Protótipo - Portal de Créditos Educativos PUCRS
# Versão 9
#
# Correções desta versão:
# - O menu lateral não usa mais o sidebar nativo do Streamlit.
# - Portanto, ele não pode mais ser minimizado/acidentalmente sumir.
# - A linha do tempo da visão do aluno ganhou mais respiro à esquerda.
#
# Rodar:
#   py -m streamlit run app_credito_educativo_v9.py
# ============================================================

st.set_page_config(
    page_title="Portal de Créditos Educativos ADMIN",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

STATUS_FLUXO = [
    "Inscrição iniciada",
    "Documentos entregues",
    "Em análise",
    "Pendente de ajuste pelo aluno",
    "Aprovado",
    "Reprovado",
]

STATUS_ESTEIRA = [
    "Inscrição iniciada",
    "Documentos entregues",
    "Em análise",
    "Pendente de ajuste pelo aluno",
    "Aprovado",
    "Reprovado",
    "Contrato emitido",
    "Contrato assinado",
]

SOLICITACOES = pd.DataFrame([
    {
        "id": "PROED-2026-0001",
        "aluno": "FELIPE GHIDINI GONÇALVES",
        "cpf": "01234567890",
        "matricula": "26106485",
        "curso": "RELAÇÕES INTERNACIONAIS",
        "credito": "PROED",
        "semestre": "2026/1",
        "status": "Aprovado",
        "data": "11/05/2026",
        "responsavel": "jsrodrigues",
        "percentual": "40%",
        "anotacao": "Documentação validada. Aguardando conferência final do contrato assinado.",
        "prioridade": "Normal",
        "fiadores": "1",
    },
    {
        "id": "MAR-2026-0002",
        "aluno": "GUILHERME DORNELLES LEÃES",
        "cpf": "12345678901",
        "matricula": "26108312",
        "curso": "CIÊNCIAS ECONÔMICAS - LF FINANÇAS",
        "credito": "MARISTA",
        "semestre": "2026/1",
        "status": "Aguardando análise",
        "data": "11/05/2026",
        "responsavel": "Equipe Crédito",
        "percentual": "50%",
        "anotacao": "Verificar composição de renda familiar. Possível necessidade de fiador adicional.",
        "prioridade": "Alta",
        "fiadores": "2",
    },
    {
        "id": "PROED-2026-0003",
        "aluno": "JOSEANE MACHADO DA ROSA",
        "cpf": "23456789012",
        "matricula": "26108621",
        "curso": "DIREITO",
        "credito": "PROED",
        "semestre": "2026/1",
        "status": "Pendente de ajuste do aluno",
        "data": "24/05/2026",
        "responsavel": "10084115",
        "percentual": "30%",
        "anotacao": "Comprovante de renda enviado está desatualizado. Solicitar reenvio.",
        "prioridade": "Alta",
        "fiadores": "1",
    },
    {
        "id": "MAR-2026-0004",
        "aluno": "MARINA BITTENCOURT ROSSI",
        "cpf": "34567890123",
        "matricula": "26109110",
        "curso": "ADMINISTRAÇÃO",
        "credito": "MARISTA",
        "semestre": "2026/2",
        "status": "Aprovado",
        "data": "25/05/2026",
        "responsavel": "Equipe Crédito",
        "percentual": "60%",
        "anotacao": "Aprovada dentro dos critérios. Próxima etapa: geração do contrato.",
        "prioridade": "Normal",
        "fiadores": "2",
    },
])

DOCUMENTOS = [
    "Documento de identificação do aluno (RG ou CNH)",
    "Comprovante de residência",
    "Histórico escolar do ensino médio completo na rede marista",
    "Documento de identificação do responsável legal, se menor de idade",
]

DOCS_FIADOR = [
    "Documento de identificação (RG ou CNH)",
    "Comprovante de residência",
    "Comprovante de rendimentos - últimos 3 meses",
    "Carteira de Trabalho - identificação civil e contrato de trabalho",
    "Última declaração de IRPF completa com recibo de entrega",
    "Certidão de casamento/separação/divórcio/óbito ou união estável, se aplicável",
    "Documento de identificação do cônjuge, se aplicável",
]

DOCS_RENDA_FIADOR = {
    "Assalariado": [
        "3 últimos contracheques",
        "6 últimos contracheques, se houver comissão ou hora extra",
        "Extrato FGTS dos últimos 6 meses, se necessário",
    ],
    "Atividade rural": [
        "Declaração de IRPJ",
        "Notas fiscais do último ano do Bloco do Produtor Rural",
    ],
    "Aposentado ou pensionista": [
        "Último comprovante de aposentadoria ou pensão",
        "Extrato de pagamento do último mês",
    ],
    "Autônomo/profissional liberal": [
        "Guias de recolhimento ao INSS dos últimos 3 meses",
        "DECORE emitida por contabilista",
    ],
    "Sócio ou dirigente de empresa": [
        "Declaração de IRPJ",
        "Contrato social e última alteração",
        "DECORE emitida por contabilista",
    ],
    "Rendimento de aluguel/arrendamento": [
        "Contrato de locação ou arrendamento registrado em cartório",
        "3 últimos comprovantes de recebimento",
    ],
}

HISTORICO_ALUNO = pd.DataFrame([
    {"data": "27/05/2026 09:12", "status": "Inscrição iniciada", "descricao": "Ficha de inscrição criada pelo aluno."},
    {"data": "27/05/2026 09:18", "status": "Documentos entregues", "descricao": "Upload inicial de documentos realizado."},
    {"data": "27/05/2026 10:31", "status": "Em análise", "descricao": "Solicitação encaminhada para análise interna."},
    {"data": "27/05/2026 14:05", "status": "Pendente de ajuste pelo aluno", "descricao": "É necessário reenviar documento solicitado pela equipe."},
])

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    * {
        font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    :root {
        --bg: #f6f9fd;
        --card: #ffffff;
        --line: #dfe8f2;
        --text: #111827;
        --muted: #5b677a;
        --blue: #145fe3;
        --purple: #7c4dff;
        --orange: #f59e0b;
        --green: #159947;
        --shadow: 0 16px 34px rgba(15, 23, 42, .08);
        --soft-shadow: 0 8px 22px rgba(15, 23, 42, .06);
    }

    .stApp {
        background:
            radial-gradient(circle at 30% 0%, rgba(64, 125, 255, .08), transparent 35%),
            linear-gradient(180deg, #fbfdff 0%, #f6f9fd 100%);
    }

    .block-container {
        padding-top: 0.7rem;
        padding-left: 1.6rem;
        padding-right: 1.6rem;
        max-width: 1700px;
    }

    header[data-testid="stHeader"] {
        background: transparent;
        height: 0rem;
    }

    div[data-testid="stToolbar"], #MainMenu, footer {
        display: none !important;
        visibility: hidden !important;
    }

    section[data-testid="stSidebar"] {
        display: none !important;
    }

    .topbar {
        height: 78px;
        background: rgba(255,255,255,.98);
        border: 1px solid var(--line);
        border-radius: 18px;
        box-shadow: 0 8px 20px rgba(15, 23, 42, .05);
        display: grid;
        grid-template-columns: 220px 1fr 160px;
        align-items: center;
        padding: 0 24px;
        margin: 10px 0 30px 0;
    }

    .logo-wrap {
        display: flex;
        gap: 22px;
        align-items: center;
    }

    .hamburger {
        font-size: 26px;
        color: #465670;
        font-weight: 900;
    }

    .brand {
        font-family: Georgia, serif;
        font-size: 32px;
        font-weight: 900;
        color: #005b8e;
        letter-spacing: -2px;
        line-height: 1;
    }

    .top-title {
        text-align: center;
        font-size: 18px;
        font-weight: 700;
        color: #3d4b63;
    }

    .avatar-area {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 12px;
    }

    .avatar {
        width: 46px;
        height: 46px;
        border-radius: 999px;
        background: linear-gradient(135deg, #6ba8ee, #a9c8f5);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 900;
        box-shadow: 0 8px 20px rgba(30, 100, 200, .22);
    }

    .left-menu {
        background: rgba(255,255,255,.96);
        border: 1px solid var(--line);
        border-radius: 20px;
        box-shadow: var(--soft-shadow);
        padding: 18px 14px;
        min-height: 690px;
        position: sticky;
        top: 12px;
    }

    .left-menu-title {
        color: #5b677a;
        font-size: 13px;
        font-weight: 800;
        margin: 0 0 12px 8px;
    }

    div[role="radiogroup"] label {
        padding: 13px 12px !important;
        margin: 8px 0 !important;
        border-radius: 13px !important;
        border: 1px solid transparent !important;
        font-weight: 800 !important;
    }

    div[role="radiogroup"] label:hover {
        background: #f3f7ff !important;
        border-color: #d7e5ff !important;
    }

    .page-title {
        font-size: 31px;
        font-weight: 900;
        letter-spacing: -.7px;
        color: var(--text);
        margin-bottom: 8px;
    }

    .page-subtitle {
        color: var(--muted);
        font-size: 16px;
        margin-bottom: 26px;
    }

    .metric-card {
        background: #fff;
        border: 1px solid #e3ebf5;
        border-radius: 18px;
        padding: 26px 28px;
        box-shadow: var(--soft-shadow);
        min-height: 118px;
        display: flex;
        align-items: center;
        gap: 24px;
    }

    .metric-icon {
        width: 64px;
        height: 64px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 34px;
        font-weight: 900;
    }

    .metric-blue { background: #e8f0ff; color: var(--blue); }
    .metric-purple { background: #f0eaff; color: var(--purple); }
    .metric-orange { background: #fff5df; color: var(--orange); }
    .metric-green { background: #e8f8ef; color: var(--green); }

    .metric-number {
        font-size: 34px;
        font-weight: 900;
        color: var(--text);
        line-height: 1;
    }

    .metric-label {
        color: #303b50;
        font-weight: 700;
        margin-top: 8px;
        font-size: 14px;
    }

    .dashboard-card {
        background: #fff;
        border: 1px solid #e3ebf5;
        border-radius: 20px;
        box-shadow: var(--shadow);
        padding: 22px;
    }

    .card-title {
        font-size: 20px;
        font-weight: 900;
        color: var(--text);
        margin-bottom: 18px;
    }

    .alert-list {
        display: flex;
        flex-direction: column;
        gap: 14px;
    }

    .alert-item {
        border-radius: 14px;
        border: 1px solid;
        padding: 18px;
        display: grid;
        grid-template-columns: 48px 1fr 20px;
        gap: 14px;
        align-items: center;
    }

    .alert-icon {
        width: 42px;
        height: 42px;
        border-radius: 999px;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size: 24px;
        font-weight: 900;
    }

    .alert-title {
        font-weight: 900;
        color: var(--text);
        margin-bottom: 4px;
    }

    .alert-desc {
        color: #39465c;
        line-height: 1.4;
    }

    .alert-green {
        background: #f1fbf5;
        border-color: #b9e7c9;
    }

    .alert-green .alert-icon {
        color: var(--green);
        background: #e4f8ec;
        border: 2px solid #9eddb7;
    }

    .alert-orange {
        background: #fff8ec;
        border-color: #ffd391;
    }

    .alert-orange .alert-icon {
        color: var(--orange);
        background: #fff1d6;
        border: 2px solid #ffc35f;
    }

    .alert-blue {
        background: #f2f7ff;
        border-color: #bdd4ff;
    }

    .alert-blue .alert-icon {
        color: var(--blue);
        background: #e9f1ff;
        border: 2px solid #9fc1ff;
    }

    .student-card {
        background: white;
        border: 1px solid #e3ebf5;
        border-left: 6px solid var(--blue);
        border-radius: 18px;
        box-shadow: var(--soft-shadow);
        padding: 20px 22px;
        margin-bottom: 15px;
    }

    .student-card.high { border-left-color: var(--orange); }
    .student-card.ok { border-left-color: var(--green); }

    .student-name {
        font-size: 22px;
        font-weight: 900;
        margin: 10px 0 6px;
        color: var(--text);
    }

    .pill {
        display: inline-flex;
        padding: 6px 13px;
        border-radius: 999px;
        background: #e8f1ff;
        color: var(--blue);
        font-size: 13px;
        font-weight: 900;
        border: 1px solid #bad0ff;
    }

    .pill.green {
        background: #e8f8ef;
        color: var(--green);
        border-color: #a4dfba;
    }

    .note-box {
        background: #f7fbff;
        border: 1px solid #d2e8fb;
        border-radius: 12px;
        padding: 13px 15px;
        margin-top: 11px;
    }

    .hero-status {
        background: linear-gradient(135deg, rgba(20,95,227,.10), rgba(255,255,255,.98));
        border: 1px solid #cfe0ff;
        border-radius: 22px;
        box-shadow: var(--shadow);
        padding: 26px;
        margin-bottom: 22px;
    }

    .step-card {
        background: white;
        border: 1px solid #e1ebf3;
        border-radius: 16px;
        padding: 16px 10px;
        text-align: center;
        box-shadow: var(--soft-shadow);
        min-height: 132px;
    }

    .timeline-shell {
        background: #ffffff;
        border: 1px solid #e3ebf5;
        border-radius: 20px;
        box-shadow: var(--soft-shadow);
        padding: 24px 28px 24px 54px;
        margin-top: 18px;
    }

    .timeline {
        border-left: 3px solid var(--blue);
        margin-left: 48px;
        padding-left: 34px;
    }

    .timeline-item {
        background: white;
        border: 1px solid #e1ebf3;
        border-radius: 14px;
        padding: 15px 18px;
        margin-bottom: 12px;
        box-shadow: var(--soft-shadow);
        position: relative;
    }

    .timeline-item:before {
        content: "";
        width: 15px;
        height: 15px;
        background: var(--blue);
        border: 3px solid white;
        box-shadow: 0 0 0 2px var(--blue);
        border-radius: 50%;
        position: absolute;
        left: -42px;
        top: 20px;
    }

    .section-title {
        font-size: 23px;
        font-weight: 900;
        color: var(--text);
        margin: 14px 0 16px 0;
    }

    div[data-testid="stForm"] {
        background: white;
        border: 1px solid #e3ebf5;
        border-radius: 22px;
        padding: 26px 28px;
        box-shadow: var(--shadow);
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input,
    div[data-testid="stTextArea"] textarea,
    div[data-baseweb="select"] > div {
        background: #ffffff !important;
        border-radius: 10px !important;
        border: 1px solid #d8e4ee !important;
    }

    div[data-testid="stFileUploader"] {
        background: #fbfdff;
        border: 1px dashed #a9cce5;
        border-radius: 12px;
        padding: 8px;
    }

    .fiador-box {
        background: linear-gradient(135deg, #f4fbff, #ffffff);
        border: 1px solid #cfe7f7;
        border-radius: 18px;
        padding: 18px;
        margin: 18px 0;
    }

    .fiador-title {
        color: #005b8e;
        font-size: 21px;
        font-weight: 900;
    }


    .step-card.done {
        border-color: #b9e7c9;
        background: #f4fbf7;
    }

    .step-card.current {
        border-color: #ffd391;
        background: #fff8ec;
    }

    .step-icon-status {
        width: 44px;
        height: 44px;
        border-radius: 999px;
        margin: 0 auto 10px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: 900;
    }

    .step-icon-ok {
        color: #159947;
        background: #e4f8ec;
        border: 2px solid #9eddb7;
    }

    .step-icon-current {
        color: #f59e0b;
        background: #fff1d6;
        border: 2px solid #ffc35f;
    }

    .status-warning-box {
        background: #fff8ec;
        border: 1px solid #ffd391;
        border-left: 6px solid #f59e0b;
        border-radius: 14px;
        padding: 16px 18px;
        color: #8a5b00;
        font-weight: 700;
        margin-top: 16px;
        margin-bottom: 22px;
    }



    .analysis-grid {
        display: grid;
        grid-template-columns: 1.05fr .95fr;
        gap: 18px;
        margin-top: 10px;
    }

    .analysis-card {
        background: white;
        border: 1px solid #e3ebf5;
        border-radius: 18px;
        box-shadow: var(--soft-shadow);
        padding: 20px;
        margin-bottom: 16px;
    }

    .analysis-title {
        font-size: 20px;
        font-weight: 900;
        margin-bottom: 14px;
        color: var(--text);
    }

    .info-row {
        display: grid;
        grid-template-columns: 170px 1fr;
        gap: 10px;
        padding: 8px 0;
        border-bottom: 1px solid #eef3f8;
    }

    .info-label {
        color: #5b677a;
        font-weight: 700;
    }

    .info-value {
        font-weight: 800;
        color: #111827;
    }

    .doc-line {
        display: grid;
        grid-template-columns: 1fr 110px 90px;
        gap: 10px;
        align-items: center;
        padding: 12px 0;
        border-bottom: 1px solid #eef3f8;
    }

    .doc-status-ok {
        color: #159947;
        font-weight: 900;
    }

    .doc-status-warn {
        color: #f59e0b;
        font-weight: 900;
    }

    .spc-box {
        background: #fff8ec;
        border: 1px solid #ffd391;
        border-radius: 14px;
        padding: 16px;
        margin-top: 10px;
    }



    .action-row {
        display: flex;
        gap: 10px;
        justify-content: flex-end;
        align-items: center;
        flex-wrap: wrap;
        margin-top: 18px;
    }

    .action-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        padding: 10px 16px;
        font-weight: 900;
        border: 1px solid #d7e5ff;
        background: #ffffff;
        color: #145fe3;
        box-shadow: 0 6px 14px rgba(15,23,42,.06);
    }

    .action-btn.primary {
        background: #145fe3;
        color: #ffffff;
        border-color: #145fe3;
        padding: 12px 22px;
        font-size: 16px;
        box-shadow: 0 10px 20px rgba(20,95,227,.22);
    }

    .spc-pill {
        display: inline-flex;
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 900;
        background: #fff8ec;
        color: #b45309;
        border: 1px solid #ffd391;
        margin-left: 8px;
    }



    .menu-group {
        color: #5b677a;
        font-size: 12px;
        font-weight: 900;
        letter-spacing: .4px;
        margin: 18px 0 6px 8px;
        text-transform: uppercase;
    }

    .presentation-note {
        background: #f7fbff;
        border: 1px solid #d2e8fb;
        border-left: 5px solid #145fe3;
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 20px;
        color: #334155;
        font-weight: 700;
    }

    .filter-card {
        background: white;
        border: 1px solid #e3ebf5;
        border-radius: 18px;
        box-shadow: var(--soft-shadow);
        padding: 18px 20px;
        margin-bottom: 18px;
    }

    .roadmap-card {
        background: white;
        border: 1px solid #e3ebf5;
        border-radius: 18px;
        box-shadow: var(--soft-shadow);
        padding: 22px;
        height: 100%;
    }

    .roadmap-title {
        font-size: 21px;
        font-weight: 900;
        color: #111827;
        margin-bottom: 12px;
    }

    .roadmap-tag {
        display: inline-flex;
        padding: 5px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 900;
        margin-bottom: 12px;
    }

    .tag-required {
        background: #e8f1ff;
        color: #145fe3;
        border: 1px solid #bad0ff;
    }

    .tag-plus {
        background: #fff8ec;
        color: #b45309;
        border: 1px solid #ffd391;
    }

    .gain-list li {
        margin-bottom: 8px;
    }

    .action-row {
        display: flex;
        gap: 10px;
        justify-content: flex-end;
        align-items: center;
        flex-wrap: wrap;
        margin-top: 18px;
    }

    .action-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        padding: 10px 16px;
        font-weight: 900;
        border: 1px solid #d7e5ff;
        background: #ffffff;
        color: #145fe3;
        box-shadow: 0 6px 14px rgba(15,23,42,.06);
    }

    .action-btn.primary {
        background: #145fe3;
        color: #ffffff;
        border-color: #145fe3;
        padding: 12px 22px;
        font-size: 16px;
        box-shadow: 0 10px 20px rgba(20,95,227,.22);
    }



    /* Força visual em modo claro, mesmo se o navegador/Streamlit estiver em dark mode */
    html,
    body,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stSidebar"],
    [data-testid="stSidebarContent"],
    .main,
    .block-container {
        color-scheme: light !important;
    }

    .stApp,
    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(circle at 30% 0%, rgba(64, 125, 255, .08), transparent 35%),
            linear-gradient(180deg, #fbfdff 0%, #f6f9fd 100%) !important;
        color: #111827 !important;
    }

    html,
    body,
    p,
    span,
    div,
    label,
    h1, h2, h3, h4, h5, h6,
    li,
    .stMarkdown,
    .stText,
    .stCaption {
        color: #111827;
    }

    p,
    li,
    .page-subtitle,
    .info-label,
    .mini-label,
    .alert-desc {
        color: #5b677a !important;
    }

    input,
    textarea,
    select,
    div[data-baseweb="select"] > div,
    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input,
    div[data-testid="stTextArea"] textarea {
        background-color: #ffffff !important;
        color: #111827 !important;
        border-color: #d8e4ee !important;
    }

    input::placeholder,
    textarea::placeholder {
        color: #7b8798 !important;
    }

    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div {
        color: #111827 !important;
    }

    div[data-baseweb="popover"],
    div[data-baseweb="menu"],
    ul[role="listbox"] {
        background: #ffffff !important;
        color: #111827 !important;
    }

    div[role="option"] {
        background: #ffffff !important;
        color: #111827 !important;
    }

    div[role="option"]:hover,
    div[aria-selected="true"] {
        background: #eef4ff !important;
        color: #111827 !important;
    }

    .topbar,
    .metric-card,
    .dashboard-card,
    .student-card,
    .analysis-card,
    .roadmap-card,
    .filter-card,
    .step-card,
    .timeline-item,
    div[data-testid="stForm"] {
        background-color: #ffffff !important;
        color: #111827 !important;
    }

    .note-box,
    .timeline-shell,
    .hero-status {
        color: #111827 !important;
    }

    button,
    .stButton > button {
        color-scheme: light !important;
    }

</style>
""", unsafe_allow_html=True)

def render_stage_chart():
    html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: transparent;
}
.chart-card {
    background: #fff;
    border: 1px solid #e3ebf5;
    border-radius: 20px;
    box-shadow: 0 16px 34px rgba(15, 23, 42, .08);
    padding: 22px;
    box-sizing: border-box;
}
.card-title {
    font-size: 20px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 14px;
}
.stage-wrap {
    position: relative;
    height: 365px;
    margin-top: 8px;
    overflow: hidden;
}
.stage-bg {
    position: absolute;
    left: 4%;
    right: 4%;
    top: 122px;
    height: 150px;
    background: linear-gradient(90deg, rgba(20,95,227,.18), rgba(124,77,255,.15), rgba(245,158,11,.17), rgba(21,153,71,.18));
    border-radius: 44% 56% 51% 49% / 31% 34% 66% 69%;
}
.stage-line {
    position: absolute;
    left: 7%;
    right: 7%;
    top: 118px;
    height: 3px;
    background: linear-gradient(90deg, #2b76ee, #7c4dff, #f59e0b, #159947, #0f766e);
    transform: rotate(2.5deg);
    border-radius: 999px;
    opacity: .85;
}
.stage-grid {
    position: relative;
    z-index: 2;
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    gap: 12px;
    align-items: end;
    height: 100%;
    padding: 8px 14px 0 14px;
    box-sizing: border-box;
}
.stage {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
    height: 100%;
}
.stage-icon {
    width: 46px;
    height: 46px;
    background: #f4f8ff;
    border: 1px solid #bcd2ff;
    border-radius: 999px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size: 22px;
    margin-bottom: 8px;
    box-shadow: 0 6px 16px rgba(15,23,42,.07);
}
.stage-dot {
    width: 13px;
    height: 13px;
    background: currentColor;
    border: 4px solid #fff;
    border-radius: 999px;
    box-shadow: 0 0 0 2px currentColor;
}
.bar {
    width: 100%;
    max-width: 92px;
    border-radius: 11px;
    padding: 14px 8px;
    color: #07152a;
    text-align: center;
    box-shadow: 0 10px 24px rgba(15,23,42,.12);
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    box-sizing: border-box;
}
.bar-title {
    font-size: 11px;
    font-weight: 900;
    min-height: 48px;
}
.bar-number {
    font-size: 25px;
    font-weight: 900;
    margin-top: 6px;
}
.bar-blue { height: 218px; background: linear-gradient(180deg, #4e94ff, #1b66df); color: white; }
.bar-sky { height: 160px; background: linear-gradient(180deg, #9fd0ff, #5599e8); }
.bar-purple { height: 142px; background: linear-gradient(180deg, #d2b8ff, #8e63e7); }
.bar-yellow { height: 112px; background: linear-gradient(180deg, #ffd979, #ffb72e); }
.bar-red { height: 103px; background: linear-gradient(180deg, #ff9b9b, #ef4444); color: white; }
.bar-green { height: 192px; background: linear-gradient(180deg, #9de6b7, #42bd78); }
.bar-teal { height: 174px; background: linear-gradient(180deg, #99f6e4, #14b8a6); }
.mini-kpis {
    margin-top: 18px;
    border: 1px solid #dfe8f2;
    border-radius: 14px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    overflow: hidden;
}
.mini-kpi {
    padding: 17px;
    text-align: center;
    background: #fff;
}
.mini-kpi + .mini-kpi { border-left: 1px solid #dfe8f2; }
.mini-label { color: #5b677a; font-weight: 700; font-size: 13px; }
.mini-value { color: #159947; font-size: 25px; font-weight: 900; margin-top: 6px; }
.mini-value.blue { color: #145fe3; }
</style>
</head>
<body>
<div class="chart-card">
    <div class="card-title">Acompanhamento da esteira</div>
    <div class="stage-wrap">
        <div class="stage-bg"></div>
        <div class="stage-line"></div>
        <div class="stage-grid">
            <div class="stage" style="color:#145fe3;">
                <div class="stage-icon">📄</div><div class="stage-dot"></div>
                <div class="bar bar-blue"><div class="bar-title">Inscrição<br>iniciada</div><div class="bar-number">424</div></div>
            </div>
            <div class="stage" style="color:#2b7ee8;">
                <div class="stage-icon">📁</div><div class="stage-dot"></div>
                <div class="bar bar-sky"><div class="bar-title">Documentos<br>entregues</div><div class="bar-number">112</div></div>
            </div>
            <div class="stage" style="color:#7c4dff;">
                <div class="stage-icon">🔎</div><div class="stage-dot"></div>
                <div class="bar bar-purple"><div class="bar-title">Em<br>análise</div><div class="bar-number">84</div></div>
            </div>
            <div class="stage" style="color:#f59e0b;">
                <div class="stage-icon">!</div><div class="stage-dot"></div>
                <div class="bar bar-yellow"><div class="bar-title">Pendente<br>aluno</div><div class="bar-number">17</div></div>
            </div>
            <div class="stage" style="color:#ef4444;">
                <div class="stage-icon">×</div><div class="stage-dot"></div>
                <div class="bar bar-red"><div class="bar-title">Reprovado</div><div class="bar-number">47</div></div>
            </div>
            <div class="stage" style="color:#159947;">
                <div class="stage-icon">✓</div><div class="stage-dot"></div>
                <div class="bar bar-green"><div class="bar-title">Aprovado</div><div class="bar-number">303</div></div>
            </div>
            <div class="stage" style="color:#0f766e;">
                <div class="stage-icon">📑</div><div class="stage-dot"></div>
                <div class="bar bar-teal"><div class="bar-title">Contrato<br>emitido</div><div class="bar-number">221</div></div>
            </div>
            <div class="stage" style="color:#0f766e;">
                <div class="stage-icon">✍</div><div class="stage-dot"></div>
                <div class="bar bar-teal"><div class="bar-title">Contrato<br>assinado</div><div class="bar-number">168</div></div>
            </div>
        </div>
    </div>
    <div class="mini-kpis">
        <div class="mini-kpi">
            <div class="mini-label">Solicitações aprovadas</div>
            <div class="mini-value">303</div>
            <div class="mini-label">alunos aptos para contrato</div>
        </div>
        <div class="mini-kpi">
            <div class="mini-label">Contratos assinados</div>
            <div class="mini-value blue">168</div>
            <div class="mini-label">após aprovação da inscrição</div>
        </div>
    </div>
</div>
</body>
</html>
"""
    components.html(html, height=585, scrolling=False)


st.markdown("""
<div class="topbar">
    <div class="logo-wrap">
        <div class="hamburger">☰</div>
        <div class="brand">PUCRS</div>
    </div>
    <div class="top-title">Portal de Créditos Educativos ADMIN</div>
    <div class="avatar-area">
        <div class="avatar">MB</div>
        <div style="font-size:18px;color:#34445c;">⌄</div>
    </div>
</div>
""", unsafe_allow_html=True)

menu_col, page_col = st.columns([0.20, 0.80], gap="large")

with menu_col:
    st.markdown('<div class="left-menu-title">ROTEIRO DA PROPOSTA</div>', unsafe_allow_html=True)
    pagina = st.radio(
        "MENU",
        [
            "📋 Aluno | Ficha de inscrição",
            "🔍 Aluno | Consulta do andamento",
            "👥 Administração | Gestão interna",
            "🏠 Plus | Visão geral da esteira",
            "🧾 Plus | Análise da solicitação",
            "📌 Fechamento | Ganhos e desafios",
        ],
        label_visibility="collapsed"
    )

with page_col:
    # ============================================================
    # VISÃO GERAL
    # ============================================================
    if pagina == "🏠 Plus | Visão geral da esteira":
        st.markdown('<div class="page-title">Plus | Visão geral da esteira</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Painel executivo para acompanhamento das solicitações PROED e MARISTA.</div>', unsafe_allow_html=True)
        st.markdown('<div class="presentation-note">Tela adicional para gestão executiva da esteira. Útil para acompanhamento, mas não bloqueia a entrega mínima do projeto.</div>', unsafe_allow_html=True)

        st.markdown('<div class="filter-card">', unsafe_allow_html=True)
        vf1, vf2, vf3 = st.columns(3)
        vf1.selectbox("Programa", ["Todos", "PROED", "MARISTA"], key="filtro_visao_programa")
        vf2.selectbox("Semestre", ["2026/1", "2026/2", "2027/1"], key="filtro_visao_semestre")
        vf3.selectbox("Etapa", ["Todas"] + STATUS_ESTEIRA, key="filtro_visao_etapa")
        st.markdown('</div>', unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        cards = [
            ("📄", "metric-blue", "424", "Solicitações iniciadas"),
            ("🕒", "metric-purple", "73", "Em análise interna"),
            ("👤", "metric-orange", "17", "Pendentes com aluno"),
            ("✓", "metric-green", "303", "Aprovadas"),
        ]

        for col, (icon, css, number, label) in zip([m1, m2, m3, m4], cards):
            col.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon {css}">{icon}</div>
        <div>
            <div class="metric-number">{number}</div>
            <div class="metric-label">{label}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

        st.write("")

        left, right = st.columns([1.55, .95])

        with left:
            render_stage_chart()

        with right:
            st.markdown("""
    <div class="dashboard-card">
        <div class="card-title">Alertas inteligentes</div>
        <div class="alert-list">
            <div class="alert-item alert-green">
                <div class="alert-icon">✓</div>
                <div>
                    <div class="alert-title">303 solicitações aprovadas</div>
                    <div class="alert-desc">Monitorar avanço para contrato gerado e assinado.</div>
                </div>
                <div>›</div>
            </div>
            <div class="alert-item alert-orange">
                <div class="alert-icon">!</div>
                <div>
                    <div class="alert-title">17 solicitações pendentes com aluno</div>
                    <div class="alert-desc">Ação sugerida: disparo automático de lembrete após 3 dias sem movimentação.</div>
                </div>
                <div>›</div>
            </div>
            <div class="alert-item alert-blue">
                <div class="alert-icon">🕒</div>
                <div>
                    <div class="alert-title">73 solicitações em análise interna</div>
                    <div class="alert-desc">Priorizar solicitações com documentos completos e prazo de matrícula próximo.</div>
                </div>
                <div>›</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

            st.write("")
            resumo = pd.DataFrame({
                "Programa": ["PROED", "MARISTA"],
                "Solicitações": [286, 138],
                "Aprovadas": [201, 102],
                "Pendentes": [62, 28],
                "Reprovadas": [23, 8],
            })
            st.dataframe(resumo, use_container_width=True, hide_index=True)
            st.markdown('<div style="margin-top:14px;color:#145fe3;font-weight:900;">Ver relatório completo ↗</div>', unsafe_allow_html=True)

    # ============================================================
    # FICHA
    # ============================================================
    elif pagina == "📋 Aluno | Ficha de inscrição":
        st.markdown('<div class="page-title">Aluno | Ficha de inscrição</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Tela indispensável para entrada da solicitação de crédito educativo.</div>', unsafe_allow_html=True)
        st.markdown('<div class="presentation-note">Entrega essencial: formulário do aluno, dados de fiador e upload de documentos em um único fluxo.</div>', unsafe_allow_html=True)

        with st.form("form_inscricao"):
            st.markdown('<div class="section-title">Dados do aluno</div>', unsafe_allow_html=True)

            a1, a2, a3, a4 = st.columns(4)
            a1.text_input("Nome completo")
            a2.text_input("RG")
            a3.text_input("CPF")
            a4.selectbox("Gênero", ["Masculino", "Feminino", "Outro / Prefiro não informar"])

            a5, a6, a7, a8 = st.columns(4)
            a5.date_input("Data de nascimento")
            a6.selectbox("Estado civil", ["Solteiro(a)", "Casado(a)", "União estável", "Divorciado(a)", "Viúvo(a)"])
            a7.text_input("Matrícula")
            a8.text_input("Curso")

            a9, a10, a11 = st.columns([2, 1, 1])
            a9.text_input("Endereço")
            a10.text_input("CEP")
            a11.text_input("Bairro")

            a12, a13, a14, a15 = st.columns([1.3, .7, 1, 1])
            a12.text_input("Cidade")
            a13.text_input("UF")
            a14.text_input("E-mail")
            a15.text_input("Celular")

            a16, a17 = st.columns(2)
            a16.text_input("Nome do responsável legal")
            a17.text_input("CPF do responsável legal")

            st.markdown('<div class="section-title">Crédito solicitado</div>', unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            c1.selectbox("Programa", ["PROED", "MARISTA"])
            c2.selectbox("Ano/competência", ["2026/1", "2026/2", "2027/1"])
            c3.text_input("Modalidade", value="Graduação", disabled=True)

            st.markdown('<div class="section-title">Dados de fiador</div>', unsafe_allow_html=True)
            qtd_fiadores = st.radio("Quantidade de fiadores", options=[1, 2], index=0, horizontal=True)

            for n in range(1, qtd_fiadores + 1):
                if qtd_fiadores == 2:
                    st.markdown(f'<div class="fiador-box"><div class="fiador-title">Fiador {n}</div></div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="fiador-box"><div class="fiador-title">Informações do fiador</div></div>', unsafe_allow_html=True)

                f1, f2, f3, f4 = st.columns(4)
                f1.text_input("Nome completo", key=f"fiador_nome_{n}")
                f2.date_input("Data de nascimento", key=f"fiador_nascimento_{n}")
                f3.text_input("CPF", key=f"fiador_cpf_{n}")
                estado_civil = f4.selectbox(
                    "Estado civil",
                    ["Solteiro(a)", "Casado(a)", "União estável", "Divorciado(a)", "Viúvo(a)"],
                    key=f"fiador_estado_civil_{n}"
                )

                f5, f6, f7 = st.columns(3)
                f5.text_input("Celular", key=f"fiador_celular_{n}")
                f6.text_input("E-mail", key=f"fiador_email_{n}")
                f7.text_input("Profissão", key=f"fiador_prof_{n}")

                f8, f9, f10 = st.columns([2, 1, 1])
                f8.text_input("Endereço", key=f"fiador_endereco_{n}")
                f9.text_input("CEP", key=f"fiador_cep_{n}")
                f10.text_input("Bairro", key=f"fiador_bairro_{n}")

                f11, f12, f13 = st.columns([1.4, .6, 1])
                f11.text_input("Cidade", key=f"fiador_cidade_{n}")
                f12.text_input("UF", key=f"fiador_uf_{n}")
                f13.number_input("Renda mensal bruta", min_value=0.0, step=100.0, format="%.2f", key=f"fiador_renda_{n}")

                st.markdown("**Dados do cônjuge**")
                con1, con2 = st.columns(2)
                con1.text_input("Nome do cônjuge", key=f"conjuge_nome_{n}")
                con2.text_input("CPF do cônjuge", key=f"conjuge_cpf_{n}")

                if estado_civil in ["Casado(a)", "União estável"]:
                    st.info("Para fiador casado ou em união estável, anexar também documentação do cônjuge e certidão correspondente.")

                st.selectbox(
                    "Tipo de comprovação de renda",
                    list(DOCS_RENDA_FIADOR.keys()),
                    key=f"atividade_fiador_{n}"
                )

            st.markdown('<div class="section-title">Upload de documentos</div>', unsafe_allow_html=True)

            st.markdown("**Documentos do aluno**")
            d1, d2 = st.columns(2)
            for i, doc in enumerate(DOCUMENTOS):
                (d1 if i % 2 == 0 else d2).file_uploader(
                    doc,
                    type=["pdf", "png", "jpg", "jpeg"],
                    key=f"doc_aluno_{i}"
                )

            st.markdown("**Documentos do fiador**")
            for n in range(1, qtd_fiadores + 1):
                if qtd_fiadores == 2:
                    st.caption(f"Fiador {n}")
                dcols = st.columns(2)
                for i, doc in enumerate(DOCS_FIADOR):
                    dcols[i % 2].file_uploader(
                        doc,
                        type=["pdf", "png", "jpg", "jpeg"],
                        key=f"doc_basico_{n}_{i}"
                    )

            aceite = st.checkbox("Declaro que as informações prestadas são verdadeiras.")
            enviar = st.form_submit_button("Enviar solicitação", type="primary", use_container_width=True)

        if enviar:
            if not aceite:
                st.error("É necessário aceitar a declaração para enviar.")
            else:
                st.success("Solicitação enviada para análise. Protocolo gerado: PROED-2026-0099")

    # ============================================================
    # CONSULTA
    # ============================================================
    elif pagina == "🔍 Aluno | Consulta do andamento":
        st.markdown('<div class="page-title">Aluno | Consulta do andamento</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Tela indispensável para o aluno acompanhar o retorno da análise.</div>', unsafe_allow_html=True)
        st.markdown('<div class="presentation-note">Entrega essencial: reduz atendimento manual e dá clareza ao aluno sobre inscrição, documentos, análise e resultado.</div>', unsafe_allow_html=True)

        item = SOLICITACOES.iloc[2]
        status_consulta = "Pendente de ajuste pelo aluno"

        st.markdown(f"""
<div class="hero-status">
    <span class="pill">{item['credito']}</span>
    <h2>{item['aluno']}</h2>
    <p style="color:#5b677a;">
        Matrícula: <b>{item['matricula']}</b> &nbsp; | &nbsp;
        Curso: <b>{item['curso']}</b>
    </p>
    <h3>Status atual: {status_consulta}</h3>
</div>
""", unsafe_allow_html=True)

        etapas = [
            {"titulo": "Inscrição", "descricao": "Concluído", "status": "ok"},
            {"titulo": "Entrega de documentos", "descricao": "Concluído", "status": "ok"},
            {"titulo": "Análise", "descricao": "Concluído", "status": "ok"},
            {"titulo": "Resultado da solicitação", "descricao": status_consulta, "status": "atual"},
        ]

        cols = st.columns(len(etapas))
        for i, etapa in enumerate(etapas):
            if etapa["status"] == "ok":
                icon = "✓"
                icon_class = "step-icon-status step-icon-ok"
                card_class = "step-card done"
            else:
                icon = "!"
                icon_class = "step-icon-status step-icon-current"
                card_class = "step-card current"

            cols[i].markdown(f"""
<div class="{card_class}">
    <div class="{icon_class}">{icon}</div>
    <b>{etapa["titulo"]}</b><br>
    <span style="color:#5b677a;">{etapa["descricao"]}</span>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="status-warning-box">
    Ação necessária: reenviar documento solicitado para continuidade da análise.
</div>
""", unsafe_allow_html=True)

        st.markdown('<div class="timeline-shell">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Linha do tempo</div>', unsafe_allow_html=True)
        st.markdown('<div class="timeline">', unsafe_allow_html=True)
        for _, row in HISTORICO_ALUNO.iterrows():
            st.markdown(f"""
<div class="timeline-item">
    <b>{row['status']}</b><br>
    <span style="color:#5b677a;">{row['data']}</span>
    <p>{row['descricao']}</p>
</div>
""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ============================================================
    # GESTÃO
    # ============================================================
    elif pagina == "👥 Administração | Gestão interna":
        st.markdown('<div class="page-title">Administração | Gestão interna</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Tela indispensável para triagem, acompanhamento e direcionamento das solicitações.</div>', unsafe_allow_html=True)
        st.markdown('<div class="presentation-note">Entrega essencial para a equipe: centraliza status, busca, anotações e acesso para análise.</div>', unsafe_allow_html=True)

        f1, f2, f3, f4 = st.columns([1, 1.4, 1, 2])
        filtro_credito = f1.selectbox("Crédito", ["Todos", "PROED", "MARISTA"])
        filtro_status = f2.selectbox("Status", ["Todos"] + STATUS_FLUXO)
        filtro_semestre = f3.selectbox("Semestre", ["Todos", "2026/1", "2026/2", "2027/1"])
        busca = f4.text_input("Pesquisar por nome, CPF ou matrícula")

        df = SOLICITACOES.copy()
        if filtro_credito != "Todos":
            df = df[df["credito"] == filtro_credito]
        if filtro_status != "Todos":
            df = df[df["status"] == filtro_status]
        if filtro_semestre != "Todos":
            df = df[df["semestre"] == filtro_semestre]
        if busca:
            termo = busca.lower()
            df = df[
                df["aluno"].str.lower().str.contains(termo)
                | df["cpf"].str.lower().str.contains(termo)
                | df["matricula"].str.lower().str.contains(termo)
            ]

        st.markdown('<div class="section-title">Solicitações</div>', unsafe_allow_html=True)

        for _, row in df.iterrows():
            classe = "high" if row["prioridade"] == "Alta" else ""
            if row["status"] in ["Aprovado", "Contrato assinado", "Finalizado"]:
                classe = "ok"

            status_class = "pill green" if row["status"] in ["Aprovado", "Contrato assinado", "Finalizado"] else "pill"

            st.markdown(f"""
    <div class="student-card {classe}">
        <div style="display:flex; justify-content:space-between; gap:24px; align-items:flex-start;">
            <div style="flex:1;">
                <span class="pill">{row['credito']}</span>
                <div class="student-name">{row['aluno']}</div>
                <p>
                    <span style="color:#5b677a;">CPF:</span> {row['cpf']} &nbsp;&nbsp;
                    <span style="color:#5b677a;">Ano/Competência:</span> {row['semestre']} &nbsp;&nbsp;
                    <span style="color:#5b677a;">Data de inclusão:</span> {row['data']} &nbsp;&nbsp;
                    <span style="color:#5b677a;">Matrícula:</span> {row['matricula']}
                </p>
                <p>
                    <span style="color:#5b677a;">Curso:</span> {row['curso']}  &nbsp;&nbsp;
                    <span style="color:#5b677a;">Fiadores:</span> {row['fiadores']}
                </p>
                <div class="note-box">
                    <b>Anotação interna:</b> {row['anotacao']}
                </div>
            </div>
            <div style="min-width:260px; text-align:right;">
                <span class="{status_class}">{row['status']}</span><br><br>
                <span style="color:#5b677a;">Responsável:</span> <b>{row['responsavel']}</b><br>
                <div class="action-row">
                    <span class="action-btn primary">Analisar</span>
                    <span class="action-btn">Documentos</span>
                    <span class="action-btn">Histórico</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)



    # ============================================================
    # ANÁLISE DA SOLICITAÇÃO
    # ============================================================
    elif pagina == "🧾 Plus | Análise da solicitação":
        st.markdown('<div class="page-title">Plus | Análise da solicitação</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Tela de trabalho para analisar dados, documentos, restrições e registrar parecer da solicitação.</div>', unsafe_allow_html=True)
        st.markdown('<div class="presentation-note">Camada adicional: melhora a experiência do analista e reduz dispersão de documentos, observações e validações.</div>', unsafe_allow_html=True)

        aluno = st.selectbox(
            "Selecionar aluno para análise",
            SOLICITACOES["aluno"].tolist(),
            index=2
        )

        item = SOLICITACOES[SOLICITACOES["aluno"] == aluno].iloc[0]

        top1, top2, top3 = st.columns(3)
        top1.markdown(f"""
<div class="metric-card">
    <div class="metric-icon metric-blue">👤</div>
    <div>
        <div class="metric-number" style="font-size:22px;">{item['credito']}</div>
        <div class="metric-label">Programa solicitado</div>
    </div>
</div>
""", unsafe_allow_html=True)

        top2.markdown(f"""
<div class="metric-card">
    <div class="metric-icon metric-purple">📚</div>
    <div>
        <div class="metric-number" style="font-size:22px;">{item['semestre']}</div>
        <div class="metric-label">Ano/competência</div>
    </div>
</div>
""", unsafe_allow_html=True)

        top3.markdown(f"""
<div class="metric-card">
    <div class="metric-icon metric-orange">📝</div>
    <div>
        <div class="metric-number" style="font-size:22px;">{item['status']}</div>
        <div class="metric-label">Status atual</div>
    </div>
</div>
""", unsafe_allow_html=True)

        st.write("")

        left, right = st.columns([1.1, .9], gap="large")

        with left:
            st.markdown("""
<div class="analysis-card">
    <div class="analysis-title">Dados do aluno</div>
    <div class="info-row"><div class="info-label">Nome</div><div class="info-value">JOSEANE MACHADO DA ROSA</div></div>
    <div class="info-row"><div class="info-label">CPF</div><div class="info-value">23456789012</div></div>
    <div class="info-row"><div class="info-label">Matrícula</div><div class="info-value">26108621</div></div>
    <div class="info-row"><div class="info-label">Curso</div><div class="info-value">DIREITO</div></div>
    <div class="info-row"><div class="info-label">E-mail</div><div class="info-value">aluno@exemplo.com</div></div>
    <div class="info-row"><div class="info-label">Celular</div><div class="info-value">(51) 99999-9999</div></div>
</div>
""", unsafe_allow_html=True)

            st.markdown("""
<div class="analysis-card">
    <div class="analysis-title">Dados de fiador</div>
    <div class="info-row"><div class="info-label">Nome</div><div class="info-value">CARLOS EDUARDO PEREIRA</div></div>
    <div class="info-row"><div class="info-label">CPF</div><div class="info-value">45678901234</div></div>
    <div class="info-row"><div class="info-label">Estado civil</div><div class="info-value">Casado(a)</div></div>
    <div class="info-row"><div class="info-label">Profissão</div><div class="info-value">Professor</div></div>
    <div class="info-row"><div class="info-label">Renda mensal bruta</div><div class="info-value">R$ 8.200,00</div></div>
    <div class="info-row"><div class="info-label">Cônjuge</div><div class="info-value">RENATA PEREIRA</div></div>
</div>
""", unsafe_allow_html=True)

            st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
            st.markdown('<div class="analysis-title">Documentação recebida</div>', unsafe_allow_html=True)
            documentos = [
                ("Documento de identificação do aluno", "Validado", "Abrir"),
                ("Comprovante de residência do aluno", "Validado", "Abrir"),
                ("Histórico escolar", "Validado", "Abrir"),
                ("Documento de identificação do fiador", "Validado", "Abrir"),
                ("Comprovante de rendimentos", "Pendente ajuste", "Abrir"),
                ("Declaração IRPF", "Validado", "Abrir"),
                ("Certidão de casamento / união estável", "Validado", "Abrir"),
            ]
            for nome, status, acao in documentos:
                classe = "doc-status-ok" if status == "Validado" else "doc-status-warn"
                st.markdown(f"""
<div class="doc-line">
    <div><b>{nome}</b></div>
    <div class="{classe}">{status}</div>
    <div style="color:#145fe3;font-weight:900;">{acao}</div>
</div>
""", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with right:
            st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
            st.markdown('<div class="analysis-title">Consulta SPC</div>', unsafe_allow_html=True)
            st.markdown('<div class="spc-box">', unsafe_allow_html=True)
            aluno_spc = st.checkbox("Aluno com restrição no SPC")
            fiador_spc = st.checkbox("Fiador com restrição no SPC")
            st.text_area("Observação sobre restrição", placeholder="Ex.: restrição localizada no CPF do fiador. Solicitar substituição ou análise superior.")
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
            st.markdown('<div class="analysis-title">Parecer e comunicação</div>', unsafe_allow_html=True)
            st.selectbox(
                "Status da solicitação",
                [
                    "Em análise",
                    "Pendente de ajuste pelo aluno",
                    "Aprovado",
                    "Reprovado",
                ]
            )
            st.text_area(
                "Anotação para o aluno",
                value="Favor reenviar comprovante de rendimentos atualizado do fiador.",
                height=100
            )
            st.text_area(
                "Anotação interna",
                value="Comprovante de rendimentos fora do prazo. Aguardar reenvio para concluir parecer.",
                height=130
            )
            st.button("Salvar análise", type="primary", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # ============================================================
    # FECHAMENTO
    # ============================================================
    elif pagina == "📌 Fechamento | Ganhos e desafios":
        st.markdown('<div class="page-title">Fechamento | Ganhos e desafios</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Resumo para apresentação da proposta à TI, separando escopo essencial e camadas adicionais.</div>', unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        c1.markdown("""
<div class="roadmap-card">
    <span class="roadmap-tag tag-required">Indispensável</span>
    <div class="roadmap-title">1. Ficha de inscrição</div>
    <ul class="gain-list">
        <li>Entrada padronizada da solicitação.</li>
        <li>Dados do aluno e fiador em formato estruturado.</li>
        <li>Upload de documentos no próprio portal.</li>
        <li>Redução de e-mails e retrabalho na conferência inicial.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

        c2.markdown("""
<div class="roadmap-card">
    <span class="roadmap-tag tag-required">Indispensável</span>
    <div class="roadmap-title">2. Consulta do aluno</div>
    <ul class="gain-list">
        <li>Transparência sobre a situação da solicitação.</li>
        <li>Menos contatos perguntando “em que pé está”.</li>
        <li>Comunicação objetiva quando houver ajuste pendente.</li>
        <li>Consulta limitada à análise da inscrição, sem misturar contrato.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

        c3.markdown("""
<div class="roadmap-card">
    <span class="roadmap-tag tag-required">Indispensável</span>
    <div class="roadmap-title">3. Gestão interna</div>
    <ul class="gain-list">
        <li>Fila única de solicitações PROED e MARISTA.</li>
        <li>Filtros por programa, status e semestre.</li>
        <li>Acesso rápido para análise, documentos e histórico.</li>
        <li>Anotação interna centralizada.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

        st.write("")

        p1, p2 = st.columns(2)
        p1.markdown("""
<div class="roadmap-card">
    <span class="roadmap-tag tag-plus">Plus</span>
    <div class="roadmap-title">4. Visão geral da esteira</div>
    <ul class="gain-list">
        <li>Painel executivo com volumes por etapa.</li>
        <li>Acompanhamento de aprovação, pendências e contratos.</li>
        <li>Ajuda a identificar gargalos operacionais.</li>
        <li>Pode entrar em fase posterior, sem travar o mínimo viável.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

        p2.markdown("""
<div class="roadmap-card">
    <span class="roadmap-tag tag-plus">Plus</span>
    <div class="roadmap-title">5. Análise da solicitação</div>
    <ul class="gain-list">
        <li>Visualização dos dados e documentos em uma tela única.</li>
        <li>Registro de restrição SPC para aluno e fiador.</li>
        <li>Separação entre anotação interna e anotação visível ao aluno.</li>
        <li>Melhora a governança da decisão.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

        st.write("")

        d1, d2 = st.columns(2)
        d1.markdown("""
<div class="roadmap-card">
    <div class="roadmap-title">Ganhos esperados</div>
    <ul class="gain-list">
        <li>Menos planilhas e controles paralelos.</li>
        <li>Redução de atendimento manual por e-mail/telefone.</li>
        <li>Padronização da análise e dos documentos solicitados.</li>
        <li>Histórico mais confiável para auditoria e acompanhamento.</li>
        <li>Melhor experiência para aluno e equipe interna.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

        d2.markdown("""
<div class="roadmap-card">
    <div class="roadmap-title">Desafios de implementação</div>
    <ul class="gain-list">
        <li>Garantir armazenamento seguro dos documentos enviados.</li>
        <li>Separar claramente o que o aluno visualiza do que é anotação interna da equipe de análise.</li>
        <li>Permitir edição dos dados do fiador quando houver preenchimento incorreto ou necessidade de atualização durante o processo.</li>
        <li>Importar automaticamente os dados do aluno a partir da conta institucional PUCRS, reduzindo preenchimento manual e inconsistências cadastrais.</li>
        <li>Importar automaticamente os dados do fiador para o FAFINANC após a aprovação da solicitação.</li>
        <li>Identificar no PCE os contratos de adesão emitidos e assinados, disponibilizando essa informação dentro da Gestão Interna.</li>
        <li>Disponibilizar mecanismo para limpeza/substituição da ficha do fiador quando houver troca de fiador durante a análise da solicitação.</li>
        <li>Permitir exclusão de documentos armazenados no perfil PUCRS quando não forem mais necessários ao processo (ex.: fiadores que não seguirão na análise).</li>
        <li>Permitir inclusão de documentos em solicitações já iniciadas, possibilitando que documentos sejam enviados posteriormente durante a análise.</li>
    </ul>
</div>
""", unsafe_allow_html=True)


