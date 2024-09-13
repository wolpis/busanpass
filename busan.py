import random
from type import H_Type

class BusanPass:
    L = [1600, 1550] #지하철, 버스

    def __init__(self, dataset: list[int] = None, cnt: int = 15) -> None:
        if dataset:
            self.dataset = dataset
        else:
            self.dataset = self.__random_dataset__(cnt)

    def __random_dataset__(self, cnt: int) -> list[int]:
        return [random.choice(self.L) for i in range(cnt)]
    
    def k_pass(self, type: str) -> tuple[str]:
        """
        ### K-pass (전국적용)
        월 15회 이상 대중교통 이용 시, 이용 금액의 일정 비율을 환급해줍니다.

        `일반` : 20%
        `청년` : 30%
        `저소득층` : 53%
        """
        if type == H_Type.general: # 일반
            parsen = 0.2
        elif type == H_Type.youth: # 청년
            parsen = 0.3
        elif type == H_Type.poor: # 저소득층
            parsen = 0.53
        else:
            raise "해당 적용 없음"
        return sum(self.dataset), sum(self.dataset) * parsen
    
    def dongback(self) -> tuple[str] | None:
        """
        ### 동백패스 (부산한정)
        월 4만 5천원 초과 시 초과 금액 중 최대 4만 5천원 까지 환급해줍니다.
        """
        s = sum(self.dataset)
        if s > 45000:
            if s - 45000 > 45000:
                return s, 45000
            return s, s - 45000
        return None