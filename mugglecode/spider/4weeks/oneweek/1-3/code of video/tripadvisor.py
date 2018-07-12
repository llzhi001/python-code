# coding=utf-8
from bs4 import BeautifulSoup
import requests
import time

url_saves = 'https://www.tripadvisor.cn/Saves/1082447'
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = ['https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#FILTERED_LIST'.format(str(i)) for i in range(30,930,30)]

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie':'ServerPool=X; TART=%1%enc%3ARe6NuDXT%2B30PvQ3yJgpFh90OWMMSl8lUoPRC%2BX%2B2pZn%2BRxFwtD31FFOf1l47dKQyzqsRfjsI7ac%3D; TAUnique=%1%enc%3AZXpLd80PSE18du294EiA3uAkEyihRFTBzBUKHhqU%2BnY2jHwltRJPGQ%3D%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TASSK=enc%3AAOL6PImgLEXZiOZpOkEvKIyFOFrIfBhmPwg0HntL01zR07Ni8Zxs4Q6jYOfQB8W4JoFgW%2B8dpwiAv%2FcOXU5U%2BItGY2up9IVXprz5Ef1gyh45EQ9kAl%2B2L69N70TT0r8btg%3D%3D; TAPD=tripadvisor.cn; _ym_uid=1522229293520289261; _ga=GA1.2.2076211401.1522229293; _gid=GA1.2.1713276343.1522229293; VRMCID=%1%V1*id.12019*llp.%2FAttractions-g60763-Activities-New_York_City_New_York-m12019*e.1522834099977; ki_r=; _smt_uid=5abb6087.ac07684; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CSPHRSess%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C1%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCpmPopunder_1%2C1%2C1522315792%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C1%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CSPHRPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; CommercePopunder=SuppressAll*1522229397400; __gads=ID=d5a3316ac72fe9e5:T=1522230699:S=ALNI_MYAZifpN_s4MpYJitQt7PhKKOysVQ; _ym_isad=2; SecureLogin2=3.4%3AANCRkwYZj%2BK4xAH%2FF%2BxvCjK0OvT7touem07XaGDuMdimzUeLP%2FP49IqxZBhpxphqmzFIdY0nMYYuckK8g9s3ylBBDhbVCS3j2TSd%2FweX5mE8BoMYNCHzS3WFkTgN7zEpMUx15ZLdw3jH4mp3Ho9nc%2BRkYGpcXPjh4mNDUzbay%2FKMcXdSvA094UH0iHpEmzxbFFYoDXY%2F3E7dKK1PIaKtBT0%3D; TAAuth3=3%3A042e8741af3b47ba553f6f2a3e2e1795%3AAMpQB0QZ%2FdNbkyIzUD0cyL2Zy0q3TNg%2BdpzPrbToi%2FyoQxDK4CExZQsg7DIdEDOgGrKXZpkMJhKMVHcDxmwEW0NlFUtfkZaRLlhLSe%2FUexpTIAP5teSnmnUUTNEM919xfC4sqrLPhjyg6iCalxAzQdrwCjHxay8yJUT7TOKsGm3x1Ov2PJayS7ke338XEaiduQ%3D%3D; TAReturnTo=%1%%2FAttraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html; _gat_UA-79743238-4=1; roybatty=TNI1625!AFhrT%2F%2F8sHxoaVPgUz2cx48SxR5kyt3ANDo%2BpkIuZRVFltBeO0etzpqb31qehq3Hk1H36TvX2vHNae7Ec4UeyD0ZOBlgP9j05Bu8T96TMfo9npEhIJ7q7enCyjEwsF8CvWKtAgeXuf%2Fx85Qmex1o0io6bOCjwSCc%2FmbELA57dFPP%2C1; ki_t=1522229297900%3B1522309099176%3B1522311484669%3B2%3B12; TASession=%1%V2ID.2399AE36C1CDB4B1890DFA888DE45C06*SQ.67*MC.12019*LP.%2FAttractions-g60763-Activities-New_York_City_New_York-m12019*PR.39766%7C*LS.ActionRecord*GR.44*TCPAR.67*TBR.37*EXEX.21*ABTR.48*PHTB.27*FS.8*CPU.17*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.593434785F69E5D1AD44F306BC7CD99F*LF.zhCN*FA.1*DF.0*IR.3*OD.zh*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105127; TAUD=LA-1522229291314-1*RDD-1-2018_03_28*LG-82206451-2.1.F.*LD-82206452-.....; EVT=gac.Trips%7CMemberProfile%7CTopNav*gaa.trip_view*gal.Trips%7CTopNav%7Cundated_trip%7Ctrip_owner%7Cunshared_trip%7Clist1082447%7Cno_traxo_reservations*gav.0*gani.false*gass.MemberProfile*gasl.*gads.Saves*gadl.*gapu.WryhO8CoCx0AAJX9SzkAAAA-*gams.2'
}


def get_attrections(url,data=None):
    wb_data = requests.get(url,headers=headers)
    time.sleep(5)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)
    titles = soup.select('div.listing_title > a[target="_blank"]')
    imgs = soup.select('img[width="180"]')
    cates = soup.select('div.p13n_reasoning_v2')

    #print(titles,imgs,cates)

    for title,img,cate in zip(titles,imgs,cates):
        data = {
            'title':title.get_text(),
            'img':img.get('src'),
            'cates':list(cate.stripped_strings),
        }
        print(data)

def get_favs(url,data=None):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)
    titles = soup.select('#trip-item-collection-container > div > div > div.saves-location-details.ui_media > div.media-content > div > a')
    imgs = soup.select('#trip-item-collection-container > div > div > div.saves-location-details.ui_media > div.media-left > a')
    metas = soup.select('#trip-item-collection-container > div > div > div.saves-location-details.ui_media > div.media-content > div > div.location_parent')

    if data == None:
        for title,img,meta in zip(titles,imgs,metas):
            data = {
                'title': title.get_text(),
                'img': img.get('src'),
                'meta': list(meta.stripped_strings),
            }
            print(data)

for single_url in urls:
    get_attrections(single_url)

