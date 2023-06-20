from . models import UnidadeJudiciaria, Nicho, Cliente, Colaborador, Processo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from datetime import datetime


# Create your views here.
def pagina_login(request):

    username = request.POST.get('userName')
    password = request.POST.get('password')

    if request.method == 'POST':

        user = authenticate(request, username=username, password=password)

        if request.user.is_authenticated:
            return redirect('homepage')
        elif user is not None and user.is_active:
            login(request, user)
            return redirect('homepage')
        else:
            msg = "Login inválido!"
            return render(request, 'login.html', {'msg': msg})

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def inicializar_homepage(request):

    objProcesso = Processo.objects.all()
    context = {
        'objProcesso': objProcesso,
    }

    return render(request, 'home.html', context)

# ==================== CLIENTE ==================== #
@login_required
def carregar_cliente(request):

    objUJ = UnidadeJudiciaria.objects.all()
    objCliente = Cliente.objects.all()
    objNicho = Nicho.objects.all()
    context = {
        'objUJ': objUJ,
        'objNicho': objNicho,
        'objCliente': objCliente
    }
    return render(request, 'cliente.html', context)

def salvar_cliente(request):

    if request.method == 'POST':

        segmento = request.POST.get('segmentoField')
        nicho = request.POST.get('nichoField')
        codigo = request.POST.get('codigoField')
        identificador = request.POST.get('identificadorField')
        nome = request.POST.get('nomeField')
        municipio_uf = request.POST.get('municipioField')
        email = request.POST.get('emailField')
        observacoes = request.POST.get('observacoesField')

        objUJ = UnidadeJudiciaria.objects.get(id=segmento)
        objNicho = Nicho.objects.get(id=nicho)

        dadosCadCliente = Cliente(
            segmento=objUJ,
            nicho=objNicho,
            codigo=codigo,
            identificador=identificador,
            nome=nome,
            municipio_uf=municipio_uf,
            email=email,
            observacoes=observacoes
        )
        dadosCadCliente.save()

    return redirect('cliente')

def editar_cliente(request):

    if request.method == 'POST':

        id_cliente = request.POST.get('idCliente')
        segmento = request.POST.get('segmentoFieldEdit')
        nicho = request.POST.get('nichoFieldEdit')
        codigo = request.POST.get('codigoFieldEdit')
        identificador = request.POST.get('identificadorFieldEdit')
        nome = request.POST.get('nomeFieldEdit')
        municipio_uf = request.POST.get('municipioFieldEdit')
        email = request.POST.get('emailFieldEdit')
        observacoes = request.POST.get('observacoesFieldEdit')

        if type(id_cliente) == str:
            id_cliente = int(id_cliente)

        try:
            objUJ = UnidadeJudiciaria.objects.get(id=segmento)
            objNicho = Nicho.objects.get(id=nicho)

            Cliente.objects.filter(id=id_cliente).update(
                segmento=objUJ,
                nicho=objNicho,
                codigo=codigo,
                identificador=identificador,
                nome=nome,
                municipio_uf=municipio_uf,
                email=email,
                observacoes=observacoes
            )

        except UnidadeJudiciaria.DoesNotExist:
            pass
        except Nicho.DoesNotExist:
            pass
        return redirect('cliente')

def deletar_cliente(request):


    if request.method == 'POST':

        # O atributo 'readonly' nos campos input, permite a consulta, mas não funciona para campos selects. Já o atributo 'desablad' retorna 'NoneType'
        id_cliente = request.POST.get('idClienteDel')

        if type(id_cliente) == str:
            id_cliente = int(id_cliente)
        try:
            Cliente.objects.filter(id=id_cliente).delete()
        except Cliente.DoesNotExist:
            pass
            # print('- [Cliente]: null')

        return redirect('cliente')

def pesquisar_cliente(request):

    query = request.GET.get('query', '')

    if Cliente.objects.filter(segmento__codigo__icontains=query):
        objCliente = Cliente.objects.filter(segmento__codigo__icontains=query)
    elif Cliente.objects.filter(segmento__nome__icontains=query):
        objCliente = Cliente.objects.filter(segmento__nome__icontains=query)
    elif Cliente.objects.filter(nicho__tribunal__regiao__icontains=query):
        objCliente = Cliente.objects.filter(nicho__tribunal__regiao__icontains=query)
    elif Cliente.objects.filter(nicho__tribunal__estado__nome__icontains=query):
        objCliente = Cliente.objects.filter(nicho__tribunal__estado__nome__icontains=query)
    elif Cliente.objects.filter(identificador__icontains=query):
        objCliente = Cliente.objects.filter(identificador__icontains=query)
    elif Cliente.objects.filter(nome__icontains=query):
        objCliente = Cliente.objects.filter(nome__icontains=query)
    elif Cliente.objects.filter(municipio_uf__icontains=query):
        objCliente = Cliente.objects.filter(municipio_uf__icontains=query)
    elif Cliente.objects.filter(email__icontains=query):
        objCliente = Cliente.objects.filter(email__icontains=query)
    else:
        objCliente = ""

    context = {
        'objCliente': objCliente,
        'query': query,
    }

    return render(request, 'cliente.html', context)

# ==================== COLABORADOR ==================== #
@login_required
def carregar_colaborador(request):

    objColaborador = Colaborador.objects.all()
    context = {
        'objColaborador': objColaborador
    }
    return render(request, 'colaborador.html', context)

def salvar_colaborador(request):

    if request.method == 'POST':

        nome_completo = request.POST.get('completoField')
        nome = request.POST.get('nomeField')
        sobrenome = request.POST.get('sobrenomeField')
        sigla =request.POST.get('siglaField')
        cpf = request.POST.get('cpfField')
        data_nascimento = request.POST.get('nascimentoField')
        email_institucional = request.POST.get('institucionalField')
        email_pessoal = request.POST.get('emailField')
        telefone = request.POST.get('telefoneField')
        cargo = request.POST.get('cargoField')
        data_admissao = request.POST.get('admissaoField')
        data_rescisao = request.POST.get('rescisaoField')
        contatos_emergencia = request.POST.get('contatosField')

        # Format
        nasc = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        adm = datetime.strptime(data_admissao, "%Y-%m-%d").date()
        if data_rescisao != "":
            res = datetime.strptime(data_rescisao, "%Y-%m-%d").date()
            status = "INATIVO"
        else:
            res = None
            status = "ATIVO"

        dadosCadColabolador = Colaborador(
            nome_completo=nome_completo,
            nome=nome,
            sobrenome=sobrenome,
            sigla=sigla,
            cpf=cpf,
            data_nascimento=nasc,
            email_institucional=email_institucional,
            email_pessoal=email_pessoal,
            telefone=telefone,
            cargo=cargo,
            data_admissao=adm,
            data_rescisao=res,
            contatos_emergencia=contatos_emergencia,
            status=status
        )
        dadosCadColabolador.save()

    return redirect('colaborador')

def editar_colaborador(request):

    if request.method == 'POST':

        id_colaborador = request.POST.get('idcolaborador')
        nome_completo = request.POST.get('completoFieldEdt')
        nome = request.POST.get('nomeFieldEdit')
        sobrenome = request.POST.get('sobrenomeFieldEdit')
        sigla =request.POST.get('siglaFieldEdit')
        cpf = request.POST.get('cpfFieldEdit')
        data_nascimento = request.POST.get('nascimentoFieldEdit')
        email_institucional = request.POST.get('institucionalFieldEdit')
        email_pessoal = request.POST.get('emailFieldEdit')
        telefone = request.POST.get('telefoneFieldEdit')
        cargo = request.POST.get('cargoFieldEdit')
        data_admissao = request.POST.get('admissaoFieldEdit')
        data_rescisao = request.POST.get('rescisaoFieldEdit')
        contatos_emergencia = request.POST.get('contatosFieldEdit')

        if type(id_colaborador) == str:
            id_colaborador = int(id_colaborador)

        if data_rescisao != "":
            res = datetime.strptime(data_rescisao, "%Y-%m-%d").date()
            status = "INATIVO"
        else:
            res = None
            status = "ATIVO"
        try:
            Colaborador.objects.filter(id=id_colaborador).update(
                nome_completo=nome_completo,
                nome=nome,
                sobrenome=sobrenome,
                sigla=sigla,
                cpf=cpf,
                data_nascimento=data_nascimento,
                email_institucional=email_institucional,
                email_pessoal=email_pessoal,
                telefone=telefone,
                cargo=cargo,
                data_admissao=data_admissao,
                data_rescisao=res,
                contatos_emergencia=contatos_emergencia,
                status=status
            )

        except Colaborador.DoesNotExist:
            print('- [Colaborador]: null')

    return redirect('colaborador')

def deletar_colaborador(request):

    if request.method == 'POST':

        # O atributo 'readonly' nos campos input, permite a consulta, mas não funciona para campos selects. Já o atributo 'desablad' retorna 'NoneType'
        id_cliente = request.POST.get('idcolaboradorDel')

        if type(id_cliente) == str:
            id_cliente = int(id_cliente)
        try:
            Colaborador.objects.filter(id=id_cliente).delete()
        except Cliente.DoesNotExist:
            pass

        return redirect('colaborador')

def pesquisar_colaborador(request):

    query = request.GET.get('query', '')

    # [Nome Completo]
    if Colaborador.objects.filter(nome_completo__icontains=query):
        objColaborador = Colaborador.objects.filter(nome_completo__icontains=query)
    # [Nome]
    elif Colaborador.objects.filter(nome__icontains=query):
        objColaborador = Colaborador.objects.filter(nome__icontains=query)
    # [Sobrenome]
    elif Colaborador.objects.filter(sobrenome__icontains=query):
        objColaborador = Colaborador.objects.filter(sobrenome__icontains=query)
    # [Sigla]
    elif Colaborador.objects.filter(sigla__icontains=query):
        objColaborador = Colaborador.objects.filter(sigla__icontains=query)
    # [Cpf]
    elif Colaborador.objects.filter(cpf__icontains=query):
        objColaborador = Colaborador.objects.filter(cpf__icontains=query)
    # [Nascimento]
    elif Colaborador.objects.filter(data_nascimento__icontains=query):
        objColaborador = Colaborador.objects.filter(data_nascimento__icontains=query)
    # [Institucional]
    elif Colaborador.objects.filter(email_institucional__icontains=query):
        objColaborador = Colaborador.objects.filter(email_institucional__icontains=query)
    # [Pessoal]
    elif Colaborador.objects.filter(email_pessoal__icontains=query):
        objColaborador = Colaborador.objects.filter(email_pessoal__icontains=query)
    # [Telefone]
    elif Colaborador.objects.filter(telefone__icontains=query):
        objColaborador = Colaborador.objects.filter(telefone__icontains=query)
    # [Cargo]
    elif Colaborador.objects.filter(cargo__icontains=query):
        objColaborador = Colaborador.objects.filter(cargo__icontains=query)
    # [Admissao]
    elif Colaborador.objects.filter(data_admissao__icontains=query):
        objColaborador = Colaborador.objects.filter(data_admissao__icontains=query)
    # [Rescisao]
    elif Colaborador.objects.filter(data_rescisao__icontains=query):
        objColaborador = Colaborador.objects.filter(data_rescisao__icontains=query)
    # [Contatos]
    elif Colaborador.objects.filter(contatos_emergencia__icontains=query):
        objColaborador = Colaborador.objects.filter(contatos_emergencia__icontains=query)
    # [Status]
    elif Colaborador.objects.filter(status__icontains=query):
        objColaborador = Colaborador.objects.filter(status__icontains=query)
    else:
        objColaborador = ""

    context = {
        'objColaborador': objColaborador,
        'query': query,
    }

    return render(request, 'colaborador.html', context)

# ==================== PROCESSO ==================== #
@login_required
def carregar_processo(request):

    objProcesso = Processo.objects.all()
    objColaborador = Colaborador.objects.all()
    objCliente = Cliente.objects.all()
    context = {
        'objProcesso': objProcesso,
        'objColaborador': objColaborador,
        'objCliente': objCliente
    }
    return render(request, 'processo.html', context)

def salvar_processo(request):

    if request.method == 'POST':

        responsavel_cadastrado = request.POST.get('responsavelField')
        data_cadastrado = request.POST.get('dataField')
        id_processo = request.POST.get('idProcessoField')
        tipo_atuacao =request.POST.get('atuacaoField')
        cliente = request.POST.get('clienteField')
        numero_processo = request.POST.get('numeroProcessoField')
        tipo_acao = request.POST.get('acaoField')
        tipo_processo = request.POST.get('tipoProcessoField')
        parte_1 = request.POST.get('parte1Field')
        parte_2 = request.POST.get('parte2Field')
        processos_associados = request.POST.get('associadosField')
        comentarios = request.POST.get('comentariosField')

        # Format
        if type(responsavel_cadastrado) == str:
            responsavel_cadastrado = int(responsavel_cadastrado)
        if type(id_processo) == str:
            id_processo = int(id_processo)
        if type(cliente) == str:
            cliente = int(cliente)
        if type(processos_associados) == str:
            processos_associados = int(processos_associados)

        dadosCadProcesso = Processo(
            responsavel_cadastrado=Colaborador(id=responsavel_cadastrado),
            data_cadastrado=data_cadastrado,
            id_processo=id_processo,
            tipo_atuacao=tipo_atuacao,
            cliente=Cliente(id=cliente),
            numero_processo=numero_processo,
            tipo_acao=tipo_acao,
            tipo_processo=tipo_processo,
            parte_1=parte_1,
            parte_2=parte_2,
            processos_associados=processos_associados,
            comentarios=comentarios,
        )
        dadosCadProcesso.save()

    return redirect('processo')

def editar_processo(request):

    if request.method == 'POST':

        pkProcesso = request.POST.get('idprocesso')
        responsavel_cadastrado = request.POST.get('responsavelFieldEdit')
        data_cadastrado = request.POST.get('dataFieldEdit')
        id_processo = request.POST.get('idProcessoFieldEdit')
        tipo_atuacao =request.POST.get('atuacaoFieldEdit')
        cliente = request.POST.get('clienteFieldEdit')
        numero_processo = request.POST.get('numeroProcessoFieldEdit')
        tipo_acao = request.POST.get('acaoFieldEdit')
        tipo_processo = request.POST.get('tipoProcessoFieldEdit')
        parte_1 = request.POST.get('parte1FieldEdit')
        parte_2 = request.POST.get('parte2FieldEdit')
        processos_associados = request.POST.get('associadosFieldEdit')
        comentarios = request.POST.get('comentariosFieldEdit')

        # Format
        if type(pkProcesso) == str:
            pkProcesso = int(pkProcesso)
        if type(responsavel_cadastrado) == str:
            responsavel_cadastrado = int(responsavel_cadastrado)
        if type(id_processo) == str:
            id_processo = int(id_processo)
        if type(cliente) == str:
            cliente = int(cliente)
        if type(processos_associados) == str:
            processos_associados = int(processos_associados)

        try:
            Processo.objects.filter(id=pkProcesso).update(
                responsavel_cadastrado=Colaborador(id=responsavel_cadastrado),
                data_cadastrado=data_cadastrado,
                id_processo=id_processo,
                tipo_atuacao=tipo_atuacao,
                cliente=Cliente(id=cliente),
                numero_processo=numero_processo,
                tipo_acao=tipo_acao,
                tipo_processo=tipo_processo,
                parte_1=parte_1,
                parte_2=parte_2,
                processos_associados=processos_associados,
                comentarios=comentarios,
            )

        except Processo.DoesNotExist:
            pass

    return redirect('processo')

def deletar_processo(request):

    if request.method == 'POST':

        # O atributo 'readonly' nos campos input, permite a consulta, mas não funciona para campos selects. Já o atributo 'desablad' retorna 'NoneType'
        pk_processo = request.POST.get('idprocessoDel')

        if type(pk_processo) == str:
            pk_processo = int(pk_processo)
        try:
            Processo.objects.filter(id=pk_processo).delete()
        except Processo.DoesNotExist:
            pass

        return redirect('processo')

def pesquisar_processo(request):

    query = request.GET.get('query', '')

    # [Responsável]
    if Processo.objects.filter(responsavel_cadastrado__nome_completo__icontains=query):
        objProcesso = Processo.objects.filter(responsavel_cadastrado__nome_completo__icontains=query)
    # [Data Cadastrado]
    elif Processo.objects.filter(data_cadastrado__icontains=query):
        objProcesso = Processo.objects.filter(data_cadastrado__icontains=query)
    # [Tipo Atuação]
    elif Processo.objects.filter(tipo_atuacao__icontains=query):
        objProcesso = Processo.objects.filter(tipo_atuacao__icontains=query)
    # [Cliente]
    elif Processo.objects.filter(cliente__identificador__icontains=query):
        objProcesso = Processo.objects.filter(cliente__identificador__icontains=query)
    # [Número Processo]
    elif Processo.objects.filter(numero_processo__icontains=query):
        objProcesso = Processo.objects.filter(numero_processo__icontains=query)
    # [Tipo Ação]
    elif Processo.objects.filter(tipo_acao__icontains=query):
        objProcesso = Processo.objects.filter(tipo_acao__icontains=query)
    # [Tipo Processo]
    elif Processo.objects.filter(tipo_processo__icontains=query):
        objProcesso = Processo.objects.filter(tipo_processo__icontains=query)
    # [Parte 1]
    elif Processo.objects.filter(parte_1__icontains=query):
        objProcesso = Processo.objects.filter(parte_1__icontains=query)
    # [Parte 2]
    elif Processo.objects.filter(parte_2__icontains=query):
        objProcesso = Processo.objects.filter(parte_2__icontains=query)
    else:
        objProcesso = ""

    context = {
        'objProcesso': objProcesso,
        'query': query,
    }

    return render(request, 'processo.html', context)


# ==================== RELATÓRIOS ==================== #
@login_required
def carregar_relatorios(request):

    qtd_processos = Processo.objects.all().count()
    qtd_clientes = Cliente.objects.all().count()
    qtd_colaboradores = Colaborador.objects.all().count()
    context = {
        'qtd_processos': qtd_processos,
        'qtd_clientes': qtd_clientes,
        'qtd_colaboradores': qtd_colaboradores
    }
    return render(request, 'relatorios.html', context)

@login_required
def carregar_relatorio_processo(request):

    objProcesso = Processo.objects.all()
    context = {
        'objProcesso': objProcesso,
    }
    return render(request, 'relatorio_processos.html', context)

@login_required
def carregar_relatorio_cliente(request):

    objCliente = Cliente.objects.all()
    context = {
        'objCliente': objCliente,
    }
    return render(request, 'relatorio_clientes.html', context)

@login_required
def carregar_relatorio_colaborador(request):

    objColaborador = Colaborador.objects.all()
    context = {
        'objColaborador': objColaborador
    }
    return render(request, 'relatorio_colaboradores.html', context)