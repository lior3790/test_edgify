import connexion
import six

from swagger_server.models.single_order import SingleOrder  # noqa: E501
from swagger_server.models.order_info import OrderInfo  # noqa: E501
from swagger_server.models.order_info_orders import OrderInfoOrders  # noqa: E501
from swagger_server import util
import csv
import requests
import json

rate_exch=0
api_url = "http://api.exchangeratesapi.io/v1/latest?access_key=c9d894fa59803e2768b5da0b464455e0"
return_data={}


def trade_csv(csv_file=None):  # noqa: E501
 

    order_list=[]

    file_contents = csv_file.stream.read().decode("utf-8")

    spamreader = csv.reader(file_contents.splitlines(), dialect='excel', delimiter=',')
    rows = list(spamreader)

    line_count=0
    for row in rows:     
    
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row)
            update_exch_rate()
            order_action=row[1].lower()

            is_market_price=False
            if row[2].lower()=='market':
                is_market_price=True                
            
            if order_action=='buy':
                buy_trade(row,is_market_price,order_list,rows,line_count)
            elif order_action=='sell':
                sell_trade(row,is_market_price,order_list,rows,line_count)
          
           

            line_count += 1


    return order_list 


def update_exch_rate():
    global rate_exch
    response = requests.get(api_url)
    ratesEntity=response.json()    
    rate_exch=float(ratesEntity['rates']['USD'])


def buy_trade(csv,is_market,order_list,spamreader=None,line_count=None):

    if is_market:
        market_trade_buy(spamreader,line_count,order_list)
    else:
        price_requested=float(csv[2])
        if rate_exch<price_requested:
            print('buy')
            order=SingleOrder(csv[0],OrderInfo('Executed',csv[3],rate_exch,float(csv[3])*rate_exch))
        else:
            order=SingleOrder(csv[0],OrderInfo('Denied'))
    
        if int(csv[3])>0:
            order_list.append(order)
        


def sell_trade(csv,is_market,order_list,spamreader=None,line_count=None):
    if is_market:
        market_trade_sell(spamreader,line_count,order_list)
    else:
        price_requested=float(csv[2])
        if rate_exch>price_requested:
            print('sell')
            order=SingleOrder(csv[0],OrderInfo('Executed',csv[3],rate_exch,float(csv[3])*rate_exch))        
        else:
            order=SingleOrder(csv[0],OrderInfo('Denied'))
    
        if int(csv[3])>0:
            order_list.append(order)


def market_trade_buy(csvFull,line_count,order_list):
    forward_index=0
    current_row=csvFull[line_count]    
    total_payed=0
    total_amount=0
    list_OrderInfo=[]
    
    

    for row in csvFull:
        if forward_index>line_count:
            if row[1].lower()=='sell' and row[2].lower()!='market':                
                left=int(current_row[3])-int(row[3])
                if left>0:                    
                    total_amount+=int(row[3])
                    total_payed+=float(row[2])*int(row[3])
                    current_row[3]=left
                    row[3]=0
                else:
                    total_amount+=int(current_row[3])
                    total_payed+=float(row[2])*int(current_row[3])
                    row[3]=abs(left)

                list_OrderInfo.append(OrderInfoOrders(row[0],int(row[3])+int(current_row[3])))
                
        forward_index+=1
    
    order=SingleOrder(current_row[0],OrderInfo('Executed',current_row[3],total_payed/total_amount,total_amount,list_OrderInfo))        
    order_list.append(order)
        
    return 0




def market_trade_sell(csvFull,line_count,order_list):
    forward_index=0
    current_row=csvFull[line_count]    
    total_payed=0
    total_amount=0
    list_OrderInfo=[]
    
    

    for row in csvFull:
        if forward_index>line_count:
            if row[1].lower()=='buy' and row[2].lower()!='market':                
                left=int(current_row[3])-int(row[3])
                if left>0:                    
                    total_amount+=int(row[3])
                    total_payed+=float(row[2])*int(row[3])
                    current_row[3]=left
                    row[3]=0
                else:
                    total_amount+=int(current_row[3])
                    total_payed+=float(row[2])*int(current_row[3])
                    row[3]=abs(left)

                list_OrderInfo.append(OrderInfoOrders(row[0],int(row[3])+int(current_row[3])))
                
        forward_index+=1
    
    order=SingleOrder(current_row[0],OrderInfo('Executed',current_row[3],total_payed/total_amount,total_amount,list_OrderInfo))        
    order_list.append(order)


        
    return 0