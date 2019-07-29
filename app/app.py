#!/usr/bin/env python3
from flask import Flask, jsonify, json
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

@app.route('/')
def index():
    return 'Index'

@app.route('/ord')
def ord():

    load_json = SITE_ROOT+'/static/ord.jsn'

    d = []
    idx = 1
    with open(load_json, 'r', encoding='UTF-8') as data:
        data2 = json.load(data)
        for data3 in data2:
            d.append(dict(id=idx,
                          Delo=data3['ЛичноеДелоНомер'],
                          FizLico=data3['ФизическоеЛицо'],
                          KonkursGruppa=data3['КонкурснаяГруппа'],
                          VidDocementa=data3['ВидДокумента'],
                          Grazhdanstsvo=data3['Гражданство'],
                          SubjectRF=data3['РегионЦелевойОрганизации'],
                          NapravOrg=data3['НаправляющаяОрганизация'],
                          Prioritet=data3['Приоритет'],
                          Sostoyanie=data3['Состояние'],
                          PrichinaOtkaza=data3['ПричинаОтказа']
                          ))
            idx += 1
        return jsonify(d)

        #data2.sort(key=lambda osnova: osnova['ОснованиеПоступления'])

        #groups = groupby(data2, lambda osnova: osnova['ОснованиеПоступления'])
        #newlist = []
        newsublist = []
        #for Osnova, Group in groups:
            # print('Основа', Osnova)
         #   newlist.append(Osnova)
            # pprint(newlist)
            # for grouped in Group:

                # print('\t', grouped['ФизическоеЛицо'])
                #print('\t', grouped['ВидДокумента'])
                # pprint(newlist)
                # if grouped['ОснованиеПоступления'] == 'Бюджетная сснова':
                #     newsublist.append(grouped['ФизическоеЛицо'])
                # newsublist.append(grouped['ОснованиеПоступления'])
                # pprint(grouped)
        #print(data2[0]['ОснованиеПоступления'])
                # if grouped['ОснованиеПоступления'] == Osnova['ОснованиеПоступления']:
                #     newlist.append(newsublist)


        # OLD WORKED CODE

        # d = {}
        # idx = int()
        # # хорошо группирует по основе и можно допонлять полями но в рамках параметра аппенд только
        # for data3 in data2:
        #
        #     d.setdefault(data3['КонкурснаяГруппа'], []).append(dict(
        #         idx=idx,
        #         Delo=data3['ЛичноеДелоНомер'],
        #         FizLico=data3['ФизическоеЛицо'],
        #         VidDocementa=data3['ВидДокумента'],
        #         Grazhdanstsvo=data3['Гражданство'],
        #        # SubjectRF=data3['СубъектРФ'],
        #         SubjectRF=data3['РегионЦелевойОрганизации'],
        #         NapravOrg=data3['НаправляющаяОрганизация'],
        #         Prioritet=data3['Приоритет'],
        #         Sostoyanie=data3['Состояние'],
        #         PrichinaOtkaza=data3['ПричинаОтказа']
        #         # Osnova=data3['ОснованиеПоступления']
        #         ))
        #     idx += 1
        #     # return jsonify(d)
        #
        # return jsonify(d)
        # END

        # fizlico = []
        # for i in range(len(data2)):
        #    test = ({'FizLico': data2[i]['ФизическоеЛицо']}, {'Osnova': data2[i]['ОснованиеПоступления']})
        #    fizlico.append(test)


        #return Response(json.dumps(fizlico), mimetype='application/json')
        #return jsonify(fizlico)
        ## заготовка для развития выше!!!
        ## Ниже код чисто наборы полей получает
        # simplelist = []
        #for i in range(len(data2)):
        #    for k in data2[i]:
        #        if k == 'ОснованиеПоступления':
        #            simplelist.append(k)
        #return jsonify(simplelist)



        # type list
        # print(type(data2))

        # type dict
        # print(type(data2[0]))

        # Не тот результат (
        # counts = defaultdict(int)
        # for item in data2:
        #     counts[item['ФизическоеЛицо']] += 1
        #     item['ОснованиеПоступления'] = counts[item['ФизическоеЛицо']]
        #     json_string = jsonify(item)
        #
        # return json_string



    #print(load_json)

    #datafile = open(load_json, 'r', encoding='UTF-8')
    #data2 = json.load(datafile)


    # return jsonify(data2[0])

    #print(type(data2[0]))
    #pprint(len(data2))
    # i = 0
    # fizlico = {}
    # for key, value in sorted(data2[0].items()):
    #    fizlico.setdefault(value, []).append(key)
       # fizlico.update(key, data2[key]['ФизическоеЛицо'])
       # fizlico = data2[i]['ФизическоеЛицо']

    # i = 0
    # fizlico = {}
    # while i <= len(data2):
    #     fizlico['Lico'] = data2[i]['ФизическоеЛицо']
    #     i = i - 1
    #
    # pprint(fizlico)


        #data2 = json.loads(data.read())
        #data3 = list(data2)
        #data4 = jsonify(data3)
    #for value in data2:
        # data3['ФизическоеЛицо'] = value['ФизическоеЛицо']
        # data3['ЛичноеДелоНомер'] = value['ЛичноеДелоНомер']
        #data3 = dict(FizLico=data3['ФизическоеЛицо'], valuefiz=value['ФизическоеЛицо'])

    #print(type(data2))
    #pprint(data2)
    # кол-во наборов данных в файле!!
    #count = len(data2)
    # print(count)
    #count2 = enumerate(data2, start=1)
    #for value2 in count2:
    #   return jsonify(value2)
    #print(count2)
    #return json.dumps(type(data2))
    #newdata = {}
    #for value in data:
    #    newdata = value

    #print(newdata.items())
    #return jsonify(newdata)

'''

    d = dict()
    for key, value in enumerate(data):
        d[key].append(value)
        print(key, value)

'''
@app.route('/vpo')
def vpo():
    load_json = SITE_ROOT + '/static/vpo.jsn'

    d = []
    idx = 1
    with open(load_json, 'r', encoding='UTF-8') as data:
        data2 = json.load(data)
        for data3 in data2:
            d.append(dict(id=idx,
                          FizLico=data3['ФизическоеЛицо'],
                          KonkursGruppa=data3['КонкурснаяГруппа'],
                          Delo=data3['ЛичноеДелоНомер'],
                          SummaBallov=data3['СуммаБаллов'],
                          Predmet1=data3['Предмет1'],
                          FormaIspytaniy1=data3['ФормаИспытания1'],
                          Predmet2=data3['Предмет2'],
                          FormaIspytaniy2=data3['ФормаИспытания2'],
                          Predmet3=data3['Предмет3'],
                          FormaIspytaniy3=data3['ФормаИспытания3'],
                          SummaBallovIDKonkyrs=data3['СуммаБалловПоИДДляКонкурса'],
                          EstPreimPravo=data3['ЕстьПреимущественноеПраво'],
                          VidDocementa=data3['ВидДокумента'],
                          SoglasieNaZachislenie=data3['СогласиеНаЗачисление'],
                          NapravOrg=data3['НаправляющаяОрганизация']
                          ))
            idx += 1
        return jsonify(d)


@app.route('/mag')
def mag():

    load_json = SITE_ROOT + '/static/mag.jsn'

    # Вариант
    # with open(load_json, 'r', encoding='UTF-8') as data:
    #     data2 = json.load(data)
    #     d = defaultdict(dict)
    #     for item in data2:
    #         d[item["ЛичноеДелоНомер"]].update(item)
    #     # print(type(d))
    #     return jsonify(d)
    #

    # create new list for output json data
    d = []
    idx = 1
    with open(load_json, 'r', encoding='UTF-8') as data:
        data2 = json.load(data)
        for data3 in data2:
            d.append(dict(id=idx,
                          FizLico=data3['ФизическоеЛицо'],
                          KonkursGruppa=data3['КонкурснаяГруппа'],
                          Delo=data3['ЛичноеДелоНомер'],
                          SummaBallov=data3['СуммаБаллов'],
                          Predmet1=data3['Предмет1'],
                          FormaIspytaniy1=data3['ФормаИспытания1'],
                          Predmet2=data3['Предмет2'],
                          FormaIspytaniy2=data3['ФормаИспытания2'],
                          Predmet3=data3['Предмет3'],
                          FormaIspytaniy3=data3['ФормаИспытания3'],
                          SummaBallovIDKonkyrs=data3['СуммаБалловПоИДДляКонкурса'],
                          EstPreimPravo=data3['ЕстьПреимущественноеПраво'],
                          VidDocementa=data3['ВидДокумента'],
                          SoglasieNaZachislenie=data3['СогласиеНаЗачисление'],
                          NapravOrg=data3['НаправляющаяОрганизация'],
                          # Prioritet=data3['Приоритет'],
                          # Sostoyanie=data3['Состояние'],
                          # PrichinaOtkaza=data3['ПричинаОтказа']
                          # Osnova=data3['ОснованиеПоступления']
                          ))
            idx += 1
        return jsonify(d)


    # d = {}
    # idx = 1
    # with open(load_json, 'r', encoding='UTF-8') as data:
    #     data2 = json.load(data)
    #     for data3 in data2:
    #         d.setdefault(idx, []).append(dict(
    #             # idx=idx,
    #             Delo=data3['ЛичноеДелоНомер'],
    #             FizLico=data3['ФизическоеЛицо'],
    #             VidDocementa=data3['ВидДокумента'],
    #             Grazhdanstsvo=data3['Гражданство'],
    #             # SubjectRF=data3['СубъектРФ'],
    #             SubjectRF=data3['РегионЦелевойОрганизации'],
    #             NapravOrg=data3['НаправляющаяОрганизация'],
    #             Prioritet=data3['Приоритет'],
    #             Sostoyanie=data3['Состояние'],
    #             PrichinaOtkaza=data3['ПричинаОтказа'],
    #             KonkursGruppa=data3['КонкурснаяГруппа']
    #             # Osnova=data3['ОснованиеПоступления']
    #         ))
    #         idx += 1
    #         # return jsonify(d)
    #
    #     return jsonify(d)
        # d = {}
        # idx = int()
        # хорошо группирует по основе и можно допонлять полями но в рамках параметра аппенд только
        # for data3 in data2:
        #     d.setdefault(data3['КонкурснаяГруппа'], []).append(dict(
        #         idx=idx,
        #         Delo=data3['ЛичноеДелоНомер'],
        #         FizLico=data3['ФизическоеЛицо'],
        #         VidDocementa=data3['ВидДокумента'],
        #         Grazhdanstsvo=data3['Гражданство'],
        #         # SubjectRF=data3['СубъектРФ'],
        #         SubjectRF=data3['РегионЦелевойОрганизации'],
        #         NapravOrg=data3['НаправляющаяОрганизация'],
        #         Prioritet=data3['Приоритет'],
        #         Sostoyanie=data3['Состояние'],
        #         PrichinaOtkaza=data3['ПричинаОтказа']
        #         # Osnova=data3['ОснованиеПоступления']
        #     ))
        #     idx += 1
        #
        # return json.dumps(d)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)