from django.shortcuts import render, redirect, HttpResponse
import sys
from django.contrib.auth.decorators import login_required
from media.forms import Formulario
from media.videoBLL import VideoBLL


def page_bread_grumb(id=0):
    entidade = 'Video'
    app = '/' + 'media/video'
    key = None
    caller = sys._getframe().f_back.f_code.co_name
    valor = {}
    msg = ''
    result = [{'label': 'video', 'link': app}]
    if caller == 'lst':
        msg = 'Listar'
    if caller == 'cad':
        label_cad = "cadastrar"
        key = {'label': label_cad, 'link': app + '/cad/'}
        msg = label_cad.title()
    if caller == 'edit':
        msg = 'Editar'
        key = {'label': 'editar', 'link': app + '/edit/{0}'.format(id)}
    if caller == 'delete':
        msg = 'Remover'
        key = {'label': 'excluir', 'link': app}
    if key:
        result.append(key)
    valor['modo'] = caller
    valor['pagebreadgrumb'] = result
    valor['pagetitle'] = msg + ' ' + entidade
    valor['app'] = app
    valor['entidade'] = entidade
    valor['url_del'] = app + "/delete/{0}".format(id)
    valor['url_cad'] = app + "/cad/"
    valor['url_edit'] = app + "/edit"
    return valor
@login_required
def lst(request):
    context = page_bread_grumb()
    obj = VideoBLL()
    lista = obj.lst()
    context['lista'] = lista
    return render(request, "lst.html", context)
@login_required
def cad(request):
    context = page_bread_grumb()
    if request.POST:
        form = Formulario(request.POST or None, request.FILES)
        msg = context['msg'] = {}
        if form.is_valid():
            form.save()
            return redirect('/media/video/')
        else:
            msg['texto'] = "Ocorreu um erro ao cadastrar."
            msg['tipo'] = 'danger'
    else:
        form = Formulario()
    context['form'] = form
    return render(request, 'base.html', context)
@login_required
def edit(request, id=0):
    context = page_bread_grumb(id)
    if request.POST:
        form = Formulario(request.POST or None, request.FILES)
        msg = context['msg'] = {}
        if form.is_valid():
            form.save(int(id))
            return redirect('/media/video/')
        else:
            msg['texto'] = "Ocorreu um erro ao cadastrar."
            msg['tipo'] = 'danger'
    else:
        obj = VideoBLL().get_by_id(id)
        form = Formulario(instance=obj)
    context['form'] = form
    return render(request, 'base.html', context)
@login_required
def delete(request, id):
    obj = VideoBLL()
    try:
        obj.delete(id)
        return redirect('/media/video/')
    except:
        return HttpResponse("Ocorreu um erro ao realizar esta função.")
