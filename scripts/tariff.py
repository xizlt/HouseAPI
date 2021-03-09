# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dom.settings")
# import django
# django.setup()
# from django.core.management import call_command
from datetime import date
from django.db.models import Max
from django.utils import timezone

from dom.wsgi import *

from meter.models import Indication
from option.models import *


class Tariff(object):

    def __init__(self, indication_start, indication_end, norma, date):
        self.indication_start = indication_start
        self.indication_end = indication_end
        self.norma = norma
        self.date = date

    def accrual(self, trf, meter__type_id):
        """
        :param trf: Dick
        :param meter__type_id: Int
        :return:
        """
        month_ind_start = 0
        month_ind_end = 0

        try:
            indications = Indication.objects.filter(meter__type_id=meter__type_id).values('meter_id').annotate(
                created=Max('created'), value=Max('value'))

            if trf[self.indication_start] < 0:
                month_ind_start = 1
                trf[self.indication_start] = -trf[self.indication_start]
            if trf[self.indication_end] < 0:
                month_ind_end = 1
                trf[self.indication_end] = -trf[self.indication_end]

            date_check_start = date(timezone.now().year,
                                    timezone.now().month - month_ind_start,
                                    trf[self.indication_start])
            date_check_end = date(timezone.now().year,
                                  timezone.now().month - month_ind_end,
                                  trf[self.indication_end])

            for i in indications:
                if i['created'].date() >= date_check_start and i['created'].date() <= date_check_end:
                    """Проставляет в used кол-во потребления"""
                    indication = Indication.objects.filter(meter_id=i['meter_id']).order_by('-created')[:2]
                    if indication.count() <= 1:
                        Indication.objects.filter(meter_id=indication[0].meter_id,
                                                  created=indication[0].created).update(
                                                  used=indication[0].value)
                    else:
                        delta = indication[0].value - indication[1].value
                        Indication.objects.filter(meter_id=indication[0].meter_id,
                                                  created=indication[0].created).update(used=delta)
                else:
                    Indication.objects.create(meter_id=i['meter_id'], value=i['value'] + trf[self.norma], used=trf[self.norma])
        except:
            print('Нет показаний')

    def field_write(self, obj):
        """
        Замена значений на slug
        :param obj: Dick
        :return: Dick
        """
        item = {}
        for i in obj:
            item[i.title.slug] = i.value
        return item

    def schedule(self, obj):
        """
        Проверка текущий даты и даты начисления
        :param obj: Dick
        :return: Bool
        """
        if timezone.now().day == obj[self.date]:
            return True
        return False


if '__main__' == __name__:

    tariff = Tariff('data-nachala-podachi',
                    'data-okonchaniya-podachi',
                    'norma-potrebleniya',
                    'data-rascheta')

    eln = tariff.field_write(ElectroNight.objects.all())
    eld = tariff.field_write(ElectroDay.objects.all())
    gas = tariff.field_write(Gas.objects.all())
    hw = tariff.field_write(HotWater.objects.all())
    cw = tariff.field_write(CoolWater.objects.all())

    if tariff.schedule(eln):
        tariff.accrual(eln, meter__type_id=5)

    if tariff.schedule(eld):
        tariff.accrual(eld, meter__type_id=4)

    if tariff.schedule(gas):
        tariff.accrual(gas, meter__type_id=3)

    if tariff.schedule(hw):
        tariff.accrual(hw, meter__type_id=2)

    if tariff.schedule(cw):
        tariff.accrual(cw, meter__type_id=1)
