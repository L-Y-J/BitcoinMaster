from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
from BitCoinRPC.bitcoinrpc.authproxy import AuthServiceProxy

# Create your views here.
def indexView(request):
    return render_to_response('calculate/index.html')


def onLoad(request):
    access = AuthServiceProxy("http://user:123@127.0.0.1:9336")
    info = access.getinfo()
    difficulty = info['difficulty']
    blocks = info['blocks']
    hash = access.getblockhash(blocks)

    temp = {'difficulty':str(difficulty),'blocks':str(blocks),'hash':str(hash)}
    data = json.dumps(temp)
    return HttpResponse(data)


def calculate(request):
    difficutly = request.GET.get('difficutly')
    caclute = request.GET.get('caclute')

    d = float(difficutly)
    c = float(caclute)

    r = c/d
    # result = '%.4f' % r
    temp = {'result':str(r)}
    data = json.dumps(temp)
    return HttpResponse(data)


