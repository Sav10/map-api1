import falcon
import sqlite3
import json
import urllib

class Resource(object):

    def on_get(self, req, resp):
        ip = req.env['REMOTE_ADDR']
        id_ = req.get_param("id")
        ip2 = str(ip)
        len_var = len(id_)

        with sqlite3.connect('/var/db_dtp/iptable.db') as conn:
            cur = conn.cursor()
            ##cur.execute("INSERT INTO IPTEST VALUES (NULL, ?, ?)", (ip2,id_))
            cur.execute("SELECT *  FROM communes_dep3 WHERE substr(commune_min, 1, ?)= ? LIMIT 10", (len_var,id_))
        data_d1 = []
        desc = cur.description
        column_names = [col[0] for col in desc]
        for row in cur.fetchall():
            data_d1.append(dict(zip(column_names, list(row))))

        answer = json.dumps(data_d1)
        conn.close()
        #answer01 = num_rec
        ##resp.body = ip + ' - ' + id_ + ' - ' + num_rec
        ##answer01 = "[{'code_commune': '14001', 'code_departement': '14',  'commune': 'Ablon',  'departement': 'Calvados',  'index': 0}, {'code_commune': '14002',  'code_departement': '14',  'commune': 'Acqueville',  'departement': 'Calvados',  'index': 1}, {'code_commune': '14003',  'code_departement': '14',  'commune': 'Agy',  'departement': 'Calvados',  'index': 2}]"
        #answer01 = num_rec
        ##resp.body = ip + ' - ' + id_ + ' - ' + num_rec
        resp.body = answer
        resp.status = falcon.HTTP_200
        resp.set_header('X-Powered-By', 'Dataplazza')
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Headers', 'X-Requested-With')

class Homepage(object):

    def on_get(self, req, resp):
        ##resp.data = msgpack.packb({'message': 'Hello world!'})
        ##resp.content_type = 'application/msgpack'
        resp.body = "this is the api's Home page"
        resp.status = falcon.HTTP_200

api = application = falcon.API()

api.add_route('/', Homepage())

api.add_route('/req1', Resource())