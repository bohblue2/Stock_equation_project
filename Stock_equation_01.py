#블랙-숄즈-머튼 모형을 사용한 유러피안 콜 옵션의 몬테카를로 방식 가격 계산
'''
    Author : 배 영 민 
    Project's main content : 위험 중립 상태인 블랙-숄즈-머튼 모형에 따른 주가 모형에서 오일러 이산화를 통해 얻어진 수식을 정해진 파라미터 값을 대입하여,
        테카를로 시뮬레이션 연산을 통해 가격 계산.
    TODO : Monte Calro simulation 특성상 많은 연산이 필요한데 Python 프레임워크에서는 C++에 상응하는 processing speed를 가질수없다.
        하지만, 병렬처리나 CPython과 같은 부분적인 연산에 대한 튜닝을 통해 속도향상을 기대할수있을 것 이다.
        인공지능기술(인공신경망)의 도입으로 하이퍼 파라미터 값을 도출하여 좀더 정확한 가격 계산을 고려해볼수도있을것이다.
    Conclusion : numpy의 standard_normal함수를 사용하여 주가데이터를 생성했음으로, 더 정확한 주가데이터와 파라미터 값(기간(period), 배당수익률 고려) 그리고 좀더 다양한 공식에 대한 이해(한국식 파생상품에 대한)가 필요. 이 프로젝트는 단지 모듈화를 통해 기존 소스코드의 가독성과 유지보수(maintenance)를 높이고 simulation_time 값의 범위를 확장시켜 한번에 다양한 simulation이 가능하도록 함.
'''

import numpy as np

class Equation:
    #파라미터 값 설정(Parameters)
    def __init__(self, S0, K, T, r, sigma, simulation_time, simulation_result):
        self.S0 = S0        #초기 주가지수
        self.K = K          #행사가
        self.T = T          #만기까지 남은 기간(단위 Year)
        self.r = r          #무위험 이자율
        self.sigma = sigma  #변동성
        self.simulation_time = simulation_time              #몬테카를로 시뮬레이션 횟수
        self.simulation_result = simulation_result          #몬테카를로 시뮬레이션 결과값

        self.z = []         #랜덤워크 주가 데이터(Random work Stock data)
        self.ST = []        #블랙-숄즈-머튼 모형에 따른 주가 모형에서 오일러 이산화를 통해 얻어진 식
        self.hT = []        #만기시 주가지수

    #가격 결정 알고리즘(Price_decision_algorithm)
    def price_decision_algorithm(self):
        for time in self.simulation_time:
            self.z.append(np.random.standard_normal(time))

        for z_list in self.z:
            self.ST.append(self.S0*np.exp((self.r - 0.5 * self.sigma   **2) * self.T + self.sigma * np.sqrt(self.T)*z_list))

        for i in range(len(self.simulation_time)):
            self.hT.append(np.maximum(self.ST[i] - self.K, 0)) #만기시 주가지수

    #몬테카를로 시뮬레이션(Monte Calro simulation)
    def Monte_Calro_simulation(self):
        for i in range(len(self.simulation_time)):
            self.simulation_result.append(np.exp(-self.r * self.T)*np.sum(self.hT[i])/self.simulation_time[i])
        return self.simulation_result

def main():
    simulation_time = []
    simulation_result = []

    Test_equation = Equation(S0 = 200, K = 105, T = 1.5, r = 1.5, sigma =0.2, simulation_time = simulation_time, simulation_result =simulation_result)
    Test_equation.price_decision_algorithm()
    Test_equation.Monte_Calro_simulation())     #Equation Class 내부연산으로 값 제공

if __name__ == '__main__':
    main()

"""Test result
parameter
        S0 = 100
        K = 105
        T = 1.5 (per year)
        r = 1.5
        sigma = 0.2
        simulation_time = 1,3,8

Monte Calro simulation result is

z value is :
array([-1.2336431]),
array([ 0.50631726, -1.18405338, -1.73481044]),
array([-0.9815837 , -0.03457698, -1.20183621, -1.45294715,
       -0.8322621 ,-1.9149874 ,  0.81700685, -0.3608434 ])


ST value is :
array([ 680.61076157])
array([ 1042.30728726,   688.92852313,   601.98356721])
array([  723.95719374,   912.96778121,   685.93415557,   645.01416093,
         750.92699547,   575.9932756 ,  1124.72650182,   842.84406593])
hT value is :
array([ 575.61076157])
array([ 937.30728726,  583.92852313,  496.98356721])
array([  618.95719374,   807.96778121,   580.93415557,   540.01416093,
         645.92699547,   470.9932756 ,  1019.72650182,   737.84406593])

Total simulation result value is :
[60.668927919224451, 70.906252464858355, 71.439121827865534]
"""



