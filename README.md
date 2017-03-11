# Stock_equation_project
##블랙-숄즈-머튼 모형을 사용한 유러피안 콜 옵션의 몬테카를로 방식 가격 계산
####Author : 배 영 민 (컴퓨터전자시스템 공학과 17학번)
- Project's name : Stock equation project(주식시장과 관련된 수학적 모델 및 수식들을 Python으로 covert) \n
- Project's main content : 위험 중립 상태인 블랙-숄즈-머튼 모형에 따른 주가 모형에서 오일러 이산화를 통해 얻어진 수식을 정해진 파라미터 값을 대입하여, 몬테카를로 시뮬레이션 연산을 통해 가격 계산.
####TODO :
1. Monte Calro simulation 특성상 많은 연산이 필요한데 Python 프레임워크에서는 C++에 상응하는 processing speed를 가질수없다. 하지만, 병렬처리나 CPython과 같은 부분적인 연산에 대한 튜닝을 통해 속도향상을 기대할수있을 것 이다.
2. 인공지능기술(딥러닝 등)의 도입으로 하이퍼 파라미터 값을 도출하여 좀더 정확한 가격 계산을 고려해볼수도있을것이다.

####Conclusion : numpy의 standard_normal함수를 사용하여 주가데이터를 생성했음으로, 더 정확한 주가데이터와 파라미터 값(기간(period), 배당수익률 고려) 그리고 좀더 다양한 공식에 대한 이해(한국식 파생상품에 대한)가 필요. 이 프로젝트는 단지 모듈화를 통해 기존 소스코드의 가독성과 유지보수(maintenance)를 높이고 simulation_time 값의 범위를 확장시킬수 있는 구조로 만들어서 한번에 다양한 simulation이 가능하도록 함.
