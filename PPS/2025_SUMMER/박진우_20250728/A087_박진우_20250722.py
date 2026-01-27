class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])  # 유닛 많은 박스부터 정렬
        total_units = 0
        for boxes, units in boxTypes:
            take = min(boxes, truckSize)
            total_units += take * units
            truckSize -= take
            if truckSize == 0:
                break
        return total_units
