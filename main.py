# <web scrapper >
# : 웹에서 원하는 정보를 추출할 수 있다.
#
# --> 파이썬 관련 일자리 찾기 project
#
# 구인구직사이트 stackoverflow, indeed
#
# 직무, 회사이름, 위치 , 지원하기 링크
# scrapper로 두 사이트에 들어가서, 모든 페이지의 python관련일자리를 가져와서, 엑셀시트에 옮기기

from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_pages = extract_indeed_pages()
extract_indeed_jobs(last_indeed_pages)








