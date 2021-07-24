#requests : 파이썬에서 요청을 만드는 기능을 모아놓음.
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"http://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)

    #print( result ) #respnse[200] : okay라는 뜻


    #html 가져오기
    #print( result.text ) #html전부를 가져옴.

    #data extractor
    #soup를 이용해서, html에서 정보 추출하기 : 페이지 숫자 추출
    #goal : 최대페이지를 코드에 알려줘서, 그 페이지까지 갈 수 있게 하기
    #beautifulsoup : html에서 정보를 추출하기에 유용한 package. 라이브러리

    soup = BeautifulSoup( result.text, 'html.parser') #html parser를 쓸거야
    #print(soup)



    #가져온 html에서, div 이름이 pagination인 class를 찾는다
    # .findall('a') : 이 anchor요소를 모두 찾으라는 의미
    # --> 이 모든 링크의 리스트를 반환함.
    pagination = soup.find("div", {"class": "pagination"})
    # print(pagination)

    links = pagination.find_all('a')
    # print(pages)


    #list에 있는 각 a (anchor) 링크안의 span을 찾고, text추출.
    pages=[]

    for link in links[:-1]: #next값은 integer로 변환불가하기때문에 미리 자름.
        # span의 text만 추출하기
        # pages.append(int(link.find("span").string))
        # string으로 받아온 페이지 --> integer로 변환

        #span에 있는 string이 아니라, 대신 링크(anchor)에서 string을 가져온다면?
        pages.append(int(link.string)) #--> 똑같이 나옴.
        #anchor가 있고, 이 element 안에 다른 element 가 있다.  그 element 에 string이 오직 하나있다면, 그냥 anchor에서 string method 를 실행해도 된다.

    pages= pages[:-1] #mutable한 배열에, operation사용.
    max_page = pages[-1] #가장 큰 값

    return max_page


# #최대 페이지 수만큼 request 보내기
# #range : argument의 크기만큼의 배열을 만듦
# #range(max_page) -> 최대 페이지만큼의 배열 생성
# #range의 현재 값을 indeed에서 가져온 요소 개수만큼 곱하기.
#각 페이지에서 일자리 정보 추출 후 return까지
def extract_indeed_jobs( last_page ):
    jobs=[]
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        # print( result.status_code ) #동작하는지 확인용
        soup = BeautifulSoup(result.text, 'html.parser') #data extract

        results = soup.find_all("h2",{"class":"jobTitle"})

        #에러
        # for result in results: #result : 일자리 목록
        #     title = result.find("h2",{"class":"title"}).find("a")["title"]
        #     #일자리 목록에서, 클래스명이 title인 <h2>를 find. 그 안에 anchor를 찾아서 그 attr인 title을 찾음.
        #     print(title)

        #에러 수정
        for h2_item in results:
            all_spans = h2_item.find_all("span")
            for span_item in all_spans:
                if span_item.get("title") is not None:
                    print(span_item.get("title"))
                    jobs.append(span_item.get("title"))

    return jobs


