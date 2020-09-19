from urllib.request import urlopen
from urllib.parse import urlparse, urlencode
from enum import Enum

Idx = Enum("Idx", "DATE LOC MEAN_TEMP MIN_TEMP MAX_TEMP", start=0)

def radio_group_data_form(self):
    self.de_start.setVisible(False)
    self.period.setVisible(False)
    self.de_end.setVisible(False)

    self.cb_start.setVisible(False)
    self.cb_end.setVisible(False)
    self.cb_month_start.setVisible(False)
    self.period_month.setVisible(False)
    self.cb_month_end.setVisible(False)
    
    self.season.setVisible(False)

    if self.radio_day.isChecked():
        if self.de_start.isVisible() == False:
            self.de_start.setVisible(True)
            self.period.setVisible(True)
            self.de_end.setVisible(True)
            self.dataFormCd = 'F00501'
            self.checkBox_standard.setChecked(True)
            self.checkBox_deviation.setCheckable(False)
    else:
        if self.radio_month.isChecked():
            self.cb_start.setVisible(True)
            self.cb_end.setVisible(True)
            self.cb_month_start.setVisible(True)
            self.period_month.setVisible(True)
            self.cb_month_end.setVisible(True)
            self.dataFormCd = 'F00513'
        elif self.radio_year.isChecked():
            self.cb_start.setVisible(True)
            self.cb_end.setVisible(True)
            self.dataFormCd = 'F00512'
        elif self.radio_season.isChecked():
            self.cb_start.setVisible(True)
            self.cb_end.setVisible(True)
            self.season.setVisible(True)
            self.dataFormCd = 'F00514'

        self.checkBox_deviation.setCheckable(True)


def checkbox_group_data_type(self):
    if self.checkBox_standard.isChecked():
        self.dataTypeCd = 'standard'
    else:
        self.dataTypeCd = 'deviation'


def update_start_year(self):
    self.start_year = self.cb_start.currentText()


def update_end_year(self):
    self.end_year = self.cb_end.currentText()


def update_start_month(self):
    self.start_month = self.cb_month_start.currentText()


def update_end_month(self):
    self.end_month = self.cb_month_end.currentText()


def update_season(self):
    if self.season.currentText() == 'All':
        self.seasonCd = 0
    elif self.season.currentText() == 'Spring':
        self.seasonCd = 'DB004001'
    elif self.season.currentText() == 'Summer':
        self.seasonCd = 'DB004002'
    elif self.season.currentText() == 'Autumn':
        self.seasonCd = 'DB004003'
    else:
        self.seasonCd = 'DB004004'


def radio_group_graph_type(self):
    if self.radio_plot.isChecked():
        self.graphType = 'plot'
    elif self.radio_hist.isChecked():
        self.graphType = 'hist'
    elif self.radio_boxplot.isChecked():
        self.graphType = 'boxplot'


def btn_search_clicked(self):
    if self.ax != None:
        self.ax.remove()
    
    btn_search_processing(self)


def btn_search_processing(self):
    self.ax = self.fig.add_subplot(111)
    start_date = self.de_start.date()
    end_date = self.de_end.date()

    start_year = start_date.toString("yyyy")
    end_year = end_date.toString("yyyy")
    title_fmt = ""
    common_title = "Temperature data in Seoul "

    if self.dataFormCd == 'F00501':
        dt_fmt = "yyyyMMdd"
        self.start_dt = start_date.toString(dt_fmt)
        self.end_dt = end_date.toString(dt_fmt)

        start_month = start_date.toString("MMMM")
        start_day = start_date.toString("d")
        end_month = end_date.toString("MMMM")
        end_day = end_date.toString("d")
        title_fmt = '{}from {} {}, {} to {} {}, {}'.format(
            common_title, start_month, start_day, start_year, end_month, end_day, end_year)
    else:
        if self.dataFormCd == 'F00513':
            dt_fmt = "yyyyMM"
            self.start_year = self.cb_start.currentText()
            self.start_month = self.cb_month_start.currentText()
            self.end_year = self.cb_end.currentText()
            self.end_month = self.cb_month_end.currentText()
            title_fmt = '{}from {}, {} to {}, {}'.format(
                common_title, self.start_month, self.start_year, self.end_month, self.end_year)
        elif self.dataFormCd == 'F00514' or self.dataFormCd == 'F00512':
            dt_fmt = "yyyy"
            if self.dataFormCd == 'F00514':
                title_fmt = '{}in {}'.format(
                    common_title, self.season.currentText())
            else:
                title_fmt = '{}from {} to {}'.format(
                    common_title, self.cb_start.currentText(), end_year)

            self.start_dt = self.cb_start.currentText()
            self.end_dt = self.cb_end.currentText()

    values = {
        'fileType': '',
        'pgmNo': '70', 'menuNo': '432', 'serviceSe': 'F00101', 'stdrMg': '99999',
        'startDt': '', 'endDt': '',
        # 'taElement': 'MIN', 'taElement': 'AVG',
        'taElement': 'MAX', 'stnGroupSns': '',
        'selectType': '1', 'mddlClssCd': 'SFC01',
        'dataFormCd': '', 'dataTypeCd': '',
        'startDay': '', 'startYear': '', 'endDay': '', 'endYear': '', 'startMonth': '', 'endMonth': '',
        'sesnCd': '', 'txtStnNm': '서울', 'stnId': '108', 'areaId': '', 'gFontSize': ''
    }

    if self.dataFormCd == 'F00501':
            self.start_day = self.start_dt
            self.end_day = self.end_dt

    # Common values
    values['startDt'] = self.start_dt
    values['endDt'] = self.end_dt
    values['dataFormCd'] = self.dataFormCd
    values['dataTypeCd'] = self.dataTypeCd
    values['startDay'] = self.start_day
    values['startYear'] = self.start_year
    values['endDay'] = self.end_day
    values['endYear'] = self.end_year
    values['startMonth'] = self.start_month
    values['endMonth'] = self.end_month

    values['sesnCd'] = self.seasonCd

    params = urlencode(values)
    print(f"After urlencode : {params}")
    API = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do"
    url = API + "?" + params

    response = urlopen(url)
    data = response.read()

    # # print("Before decode response :", data)
    text = data.decode("cp949")
    # print("After decode response :", text)
    data = text.split("\r\n")
    # print(len(data))

    # remove header
    del data[:8]
    del data[-2:]

    i = 0
    # make 2dList
    tmp = []
    for row in data:
        add = row.split(',')
        tmp.append(add)

        print(f"{i}: {row}")
        i += 1

    # print(f"tmp: {tmp}")
    mean = []
    high = []
    low = []
    mean.clear()

    for row in tmp:
        if row[Idx.MEAN_TEMP.value] != '':
            row[Idx.MEAN_TEMP.value] = float(row[Idx.MEAN_TEMP.value])
            mean.append(row[Idx.MEAN_TEMP.value])

        if row[Idx.MAX_TEMP.value] != '':
            row[Idx.MAX_TEMP.value] = float(row[Idx.MAX_TEMP.value])
            high.append(row[Idx.MAX_TEMP.value])

        if row[Idx.MIN_TEMP.value] != '':
            row[Idx.MIN_TEMP.value] = float(row[Idx.MIN_TEMP.value])
            low.append(row[Idx.MIN_TEMP.value])

    # print(f"high: {high}")
    # print(f"low: {low}")

    # print(title_fmt)

    self.ax.set_title(title_fmt)
    self.ax.plot(high, 'red', label='High')
    self.ax.plot(mean, 'green', label='mean')
    self.ax.plot(low, 'blue', label='Low')
    # self.ax.grid(True)
    self.ax.set_xlabel('period')
    self.ax.set_ylabel('temperature')
    self.ax.legend(loc="best")
    self.canvas.draw()

    # savename = 'temperature_from_' + start_dt + '_to_' + end_dt + '.csv'
    # with open(savename, mode ="wb") as f:
    #     f.write(data)


def btn_save_graph_clicked(self):
       pass
