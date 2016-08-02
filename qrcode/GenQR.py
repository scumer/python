# coding=utf-8
from app.model import *
from utility import makeQR
import os


def gen_qrcode_by_reports(reports):
    import os
    import time
    from app.model import Report,MedicalCard
    dirname = './qr/'+time.strftime('%Y%m%d-%H')
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    #cards = MedicalCard.objects(cardNo=cardno).all()
    for report in reports:
        card = Report.card

        bind = {
             'cc': card.cityCode,
             'h': report.hospitalCode,
             'cn': card.cardNo,
             'n': card.name,
             's': card.sex
         }
        make_qr(gen_bind_url_redirect(bind), dirname+u'/{0}.jpg'.format(bind['n'] + bind['cn']))
