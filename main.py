from flask import Flask, json, request
from flask_cors import CORS, cross_origin
import json
import time
import json
import os

def alternator(maxindex):
    i = -1
    while True:
        i+=1
        yield (i) % maxindex

notice_alternator = alternator(2)

def notice_list():
    response_1 = json.loads(open('responses/selectNoticeList/selectNoticeList_1.json', 'rb').read())
    response_2 = json.loads(open('responses/selectNoticeList/selectNoticeList_2.json', 'rb').read())
    return [response_1, response_2][next(notice_alternator)]

response_dict = {
    'selectInitOsdcInfo': lambda: open('responses/selectInitOsdcInfo.json', 'rb').read(),
    'selectImportItemList': lambda: open('responses/selectImportItemList.json', 'rb').read(),
    'selectTrnsPurchaseSalesList': lambda: open('responses/selectTrnsPurchaseSalesList.json', 'rb').read(),
    'saveTrnsSalesOsdc': lambda: open('responses/saveTrnsSalesOsdc.json', 'rb').read(),
    'selectNoticeList': notice_list
}

api = Flask(__name__)
cors = CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'

@api.route('/etims-api/<endpoint>', methods=['POST'])
@cross_origin()
def get_inputs(endpoint):
    time.sleep(3)
    return response_dict.get(endpoint, '{"resultCd":"002", "resultMsg":"MOCK OSCU: endpoint not implemented", "resultDt":"20230920124538","data":null}')()

if __name__ == '__main__':
    api.run(port='8070')
