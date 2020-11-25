
import time
from decimal import Decimal


#pairs = "BNB/USDT,ETH/USDT,BTC/PAX,LTC/USDT,XRP/USDT,XRP/BTC,EVX/BTC,BTC/USDC,LINK/BTC,ADA/BTC,BAT/BTC,BCHABC/BTC,TUSD/USDT,ADA/USDT,BTC/TUSD,OAX/BTC,NEO/USDT,ERD/BTC,ETH/PAX,FET/BTC,ALGO/USDT,PPT/BTC,ANKR/BTC,MTL/BTC,NEBL/BTC,ONE/BTC,ETH/USDC,DUSK/BTC,BTT/USDT,ERD/USDT,BNB/ETH,XLM/BTC,AGI/BTC,IOTA/BTC,DLT/BTC,REN/BNB,EOS/PAX,NANO/USDT,MITH/BTC,ETC/BTC,ATOM/USDT,ENJ/BTC,EVX/ETH,ARK/BTC,SYS/BTC,VET/USDT,BNB/USDC,ICX/USDT,ZRX/BTC,ONE/USDT,TRX/ETH,TNT/BTC,XMR/USDT,NPXS/BTC,DUSK/USDT,WAN/BTC,WABI/BTC,ERD/BNB,BNB/TUSD,LTC/ETH,ARN/BTC,VIB/BTC,RVN/BNB,QTUM/BTC,LTC/USDC,BCHABC/USDC,LTC/BNB,STRAT/BTC,EOS/BNB,BAT/BNB,IOTX/BTC,FUEL/BTC,ARDR/BTC,HOT/ETH,VIBE/BTC,CMT/BTC,NULS/BTC,BCHABC/TUSD,FET/BNB,NEO/ETH,LSK/BTC,APPC/BTC,KMD/BTC,POLY/BTC,GRS/BTC,INS/BTC,SNM/BTC,STEEM/BTC,HOT/BTC,ENG/BTC,ADA/BNB,TFUEL/USDT,NAS/BTC,MITH/USDT,BNB/PAX,FTM/BNB,VIA/BTC,POWR/BTC,WAVES/USDT,DASH/USDT,XMR/ETH,LINK/USDC,DOGE/USDT,OST/BTC,FUN/BTC,FUEL/ETH,DNT/BTC,OMG/USDT,BTT/BTC,PPT/ETH,OAX/ETH,LOOM/BTC,XRP/USDC,TRX/USDC,NCASH/ETH,XZC/BTC,GNT/BTC,AION/ETH,GTO/BNB,MCO/ETH,ONE/BNB,ADA/USDC,KNC/ETH,STORJ/BTC,GTO/BTC,NAV/BTC,DGD/BTC,IOTA/BNB,ANKR/BNB,WAN/ETH,ADA/TUSD,TNB/BTC,GAS/BTC,VET/ETH,NEO/USDC,XRP/PAX,NEO/BNB,ONG/BTC,LINK/TUSD,ENJ/ETH,XRP/TUSD,VET/BNB,THETA/ETH,DASH/ETH,CELR/BNB,ARN/ETH,REQ/BTC,ONG/USDT,YOYO/BTC,XLM/ETH,ADA/PAX,XMR/BNB,IOST/BNB,AGI/BNB,STRAT/ETH,DUSK/PAX,LRC/ETH,EDO/BTC,FTM/USDC,BCHABC/PAX,BCPT/ETH,ATOM/BNB,MFT/ETH,DOGE/BNB,GXS/ETH,ENG/ETH,SKY/ETH,NEO/TUSD,TFUEL/BNB,BAT/TUSD,TRX/TUSD,CMT/ETH,MITH/BNB,XLM/USDC,XLM/PAX,GTO/USDT,AST/ETH,NXS/BNB,DLT/ETH,GVT/ETH,BAT/PAX,FUN/ETH,NAS/ETH,WABI/ETH,DASH/BNB,QTUM/ETH,THETA/BNB,ARK/ETH,BCD/ETH,NULS/ETH,DLT/BNB,SYS/BNB,ETC/BNB,KMD/ETH,STEEM/BNB,WAN/BNB,APPC/ETH,BTT/USDC,ALGO/USDC,MCO/BNB,DGD/ETH,ALGO/TUSD,XEM/BNB,OMG/BNB,QKC/ETH,DNT/ETH,USDS/USDT,CVC/ETH,STORJ/ETH,LSK/BNB,BTT/TUSD,MFT/BNB,BTT/PAX,MTL/ETH,POE/ETH,TNB/ETH,IOTX/ETH,BNB/USDS,WABI/BNB,ETC/USDC,BCPT/BNB,QTUM/BNB,GTO/ETH,NAV/BNB,STEEM/ETH,DOCK/ETH,NAV/ETH,FTM/TUSD,VIA/BNB,CDT/ETH,QSP/ETH,XLM/TUSD,AMB/ETH,REQ/ETH,DCR/BNB,NAS/BNB,DOGE/USDC,CND/BNB,KEY/ETH,BTS/ETH,PIVX/ETH,OST/BNB,ZEN/BNB,ANKR/TUSD,AE/BNB,STORM/BNB,QLC/ETH,ONE/TUSD,APPC/BNB,ETC/TUSD,WAVES/TUSD,EDO/ETH,RLC/BNB,AMB/BNB,XZC/BNB,ANKR/USDC,WAVES/PAX,WAVES/USDC,GTO/TUSD,ERD/PAX,TFUEL/TUSD,BCPT/TUSD,PHB/PAX,ETC/PAX,BTC/USDT,BNB/BTC,ETH/BTC,EOS/USDT,PAX/USDT,REN/BTC,BCHABC/USDT,NANO/BTC,LTC/BTC,TRX/USDT,EOS/BTC,RVN/BTC,USDC/USDT,FTM/BTC,LINK/USDT,TRX/BTC,XMR/BTC,WTC/BTC,ETC/USDT,NEO/BTC,BAT/USDT,ALGO/BTC,FET/USDT,MATIC/BTC,ONT/USDT,MDA/BTC,NXS/BTC,BLZ/BTC,ONT/BTC,FTM/USDT,AION/BTC,XLM/USDT,IOTA/USDT,ICX/BTC,SKY/BTC,ZEC/BTC,EOS/ETH,MATIC/USDT,CELR/BTC,ATOM/BTC,QTUM/USDT,AST/BTC,THETA/BTC,DASH/BTC,WAVES/BTC,MCO/BTC,VET/BTC,LINK/ETH,PAX/TUSD,ZIL/BTC,BTG/BTC,XRP/ETH,CELR/USDT,RCN/BTC,HOT/USDT,USDC/TUSD,ZEC/USDT,BCPT/BTC,ETH/TUSD,GO/BTC,BAT/ETH,ADA/ETH,XRP/BNB,BQX/BTC,ADX/BTC,QKC/BTC,CND/BTC,TRX/XRP,GVT/BTC,ALGO/BNB,LUN/BTC,DOCK/BTC,USDC/PAX,TRX/BNB,BRD/BTC,XVG/BTC,IOST/BTC,DENT/BTC,MANA/BTC,ZIL/USDT,KNC/BTC,TFUEL/BTC,LTC/TUSD,ANKR/USDT,SNGLS/BTC,GXS/BTC,DCR/BTC,PHB/BTC,ELF/BTC,IOST/USDT,RDN/BTC,BTT/BNB,OMG/BTC,LTC/PAX,XEM/BTC,NPXS/ETH,ICX/ETH,HC/BTC,AE/BTC,LRC/BTC,CVC/BTC,DENT/ETH,MTH/BTC,THETA/USDT,NANO/ETH,QLC/BTC,ZEN/BTC,MATIC/BNB,ENJ/USDT,EOS/TUSD,BTC/USDS,IOTA/ETH,BNT/BTC,DUSK/BNB,BRD/BNB,POE/BTC,EOS/USDC,WPR/BTC,ZRX/USDT,AMB/BTC,WTC/ETH,NULS/USDT,POA/BTC,DOGE/BTC,BLZ/ETH,PIVX/BTC,QSP/BTC,RLC/BTC,BCD/BTC,NANO/BNB,MDA/ETH,NCASH/BTC,ZIL/ETH,SNT/BTC,BTS/BTC,ONT/ETH,ZIL/BNB,LEND/BTC,ETC/ETH,BAT/USDC,OMG/ETH,MFT/BTC,DATA/BTC,HOT/BNB,SC/BTC,ONT/BNB,ZRX/ETH,LEND/ETH,BTG/ETH,REP/BTC,XLM/BNB,NEBL/ETH,CDT/BTC,BLZ/BNB,NXS/ETH,WAVES/ETH,NEO/PAX,KEY/BTC,AE/ETH,AGI/ETH,ATOM/TUSD,IOST/ETH,ADX/ETH,STORM/BTC,SYS/ETH,SC/ETH,LINK/PAX,AION/BNB,WTC/BNB,CND/ETH,DUSK/USDC,ARDR/ETH,SNM/ETH,TRX/PAX,ZEC/ETH,WAVES/BNB,BNT/ETH,ENJ/BNB,LSK/ETH,LUN/ETH,TNT/ETH,RDN/ETH,XVG/ETH,NULS/BNB,MANA/ETH,ICX/BNB,OST/ETH,ZEC/USDC,USDS/PAX,ELF/ETH,XEM/ETH,NEBL/BNB,RCN/ETH,STORM/ETH,ZEC/BNB,ZRX/BNB,BQX/ETH,SNGLS/ETH,LOOM/ETH,VIA/ETH,POWR/ETH,XZC/ETH,GNT/ETH,FTM/PAX,ALGO/PAX,BRD/ETH,HC/ETH,USDS/USDC,VIBE/ETH,ARDR/BNB,VIB/ETH,ERD/USDC,GRS/ETH,NCASH/BNB,CVC/BNB,RLC/ETH,BTS/BNB,REP/ETH,RDN/BNB,ADX/BNB,BTCB/BTC,SNT/ETH,ONE/PAX,SC/BNB,ZEN/ETH,XZC/XRP,WPR/ETH,ZEC/TUSD,MTH/ETH,POA/ETH,ONE/USDC,POLY/BNB,GO/BNB,GNT/BNB,ZEC/PAX,USDS/TUSD,RCN/BNB,POWR/BNB,PIVX/BNB,ATOM/USDC,LOOM/BNB,PHB/BNB,INS/ETH,CMT/BNB,ATOM/PAX,PHB/TUSD,QSP/BNB,YOYO/ETH,DATA/ETH,ONG/BNB,SKY/BNB,POA/BNB,BCPT/PAX,QLC/BNB,REP/BNB,TFUEL/USDC,ANKR/PAX,YOYO/BNB,GTO/PAX,BCPT/USDC,PHB/USDC,TFUEL/PAX,GTO/USDC,DOGE/PAX".split(",")





class graph:
    def __init__(self,coins,markets):
        self.v = coins
        self.e = markets
        self.matrix = [[0]*len(coins) for i in range(len(coins))]
        self.adj={}
        self.index={}
        self.valid_pairs = []
        for m in markets:
            c1,c2 = m
            self.valid_pairs.append(c1+c2)
            self.matrix[self.v.index(c1)][self.v.index(c2)] = 0
            self.matrix[self.v.index(c2)][self.v.index(c1)] = 0
            if c1 not in self.adj:
                self.adj.update({c1:[]})
            if c2 not in self.adj:
                self.adj.update({c2:[]})
            if c2 not in self.adj[c1]:
                self.adj[c1].append(c2)
            if c1 not in self.adj[c2]:
                self.adj[c2].append(c1)

        for i in range(len(self.v)):
            for j in range(i+1,len(self.v)):
                if self.v[i] in self.adj[self.v[j]]:
                    self.index.update({self.v[i]+self.v[j]:[i,j]})
                    self.index.update({self.v[j]+self.v[i]:[j,i]})


    def generate_paths(self,hold):
        paths = []
        stage1 = [hold]
        stage2 = []
        for pair in self.adj[hold]:
            stage2.append(stage1+[pair])
        for pair in  stage2:
            for t in self.adj[pair[1]]:
                if hold in self.adj[t]:
                    paths.append(pair+[t])
        #return self.filter_path([p for p in paths])
        return paths

    def filter_path(self,path):
        for p in path:
            t = path
            if path.count(p)>1:
                path.pop(path.index((p)))

            for p in path:
                p1 = shift(p)
                p2=shift(p1)
                if p2 in path:
                    print(p1)
                    path.pop(p1)
        return path


    def att_prices(self,prices):
        to_create = []
        for price in prices:
            if price['symbol'] in self.valid_pairs:
                self.update_matrix(str(price['symbol']),Decimal(str(price['askPrice'])),Decimal(str(price['bidPrice'])))
            else:
                to_create.append(price['symbol'])
        #print('to create:', to_create)

    def update_matrix(self,pair,ask,bid):
        i,j = self.index[pair]
        self.matrix[i][j] = bid
        self.matrix[j][i] = 1/ask

    def get_edge_value(self,pair):
        index = self.index[pair]
        return self.matrix[index[0]][index[1]]


    def calc_path(self,path):
        stage1 = path[0]+path[1]
        stage2 = path[1]+path[2]
        stage3 = path[2]+path[0]
        return self.get_edge_value(stage1)*self.get_edge_value(stage2)*self.get_edge_value(stage3)

def shift(arr):
    return [arr[len(arr)-1]]+ arr[:len(arr)-1]

def graph_test():
    start = time.time()
    a = graph(markets,coins)
    elapsed = time.time() - start
    print('creating graph - '+str(elapsed)+'s')

    a.att_prices(prices)

    holds = ['BTC','ETH','BNB']

    start = time.time()
    paths = []
    for c in  holds:
        paths += a.generate_paths(c)
        #print(paths)
    elapsed = time.time() - start
    print('generate paths - '+str(elapsed)+'s')

    start = time.time()
    for p in paths:
        v = a.calc_path(p)
        if v > 1.01:
            print(p,(v-1))
    elapsed = time.time() - start

    print('calc paths - '+str(elapsed)+'s')

def make_graph(pairs):
    coins = []
    markets = []
    for p in pairs:
        market = c1,c2 = p.split('/')
        markets.append(market)
        if c1 not in coins:
            coins.append(c1)
        if c2 not in coins:
            coins.append(c2)
    return graph(coins,markets)


