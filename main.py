from exchanges.apis import BitstampAPI


if __name__ == '__main__':

    b = BitstampAPI()
    print(b.order_book())
    #print(b.volume_weighted_avg_price())

    '''
    m = MtGoxAPI()
    bids_asks = m.bid_ask()
    print('ask')
    print(bids_asks['ask'])
    print('bid')
    print(bids_asks['bid'])
    print('weight')
    print(m.avg_price())
    '''
