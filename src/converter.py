
def converter(amount: float, rate: float) -> float:
    if amount < 0:
        #log error here('a neagtive amount has been entered')
        raise ValueError('Amount must be positive')
    else:
        return round(amount * rate, 2)
    #rounding to 2dp because its a currency



