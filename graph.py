import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1, 11):
    sheet['A' + str(i)] = i

ref_obj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1,max_col=1,max_row=10)
series_obj = openpyxl.chart.Series(ref_obj, title='First series')
chart_obj = openpyxl.chart.BarChart()
chart_obj.append(series_obj)
chart_obj.y = 50    #位置
chart_obj.x = 100
chart_obj.w = 300   #サイズ
chart_obj.h = 100
sheet.add_chart(chart_obj)
wb.save('SampleChart.xlsx')
