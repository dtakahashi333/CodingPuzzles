from typing import List


# 134. Gas Station
# https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150
class GasStation:

    @classmethod
    def solveByBruteForce(cls, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            tank = 0
            for j in range(n):
                k = (i + j) % n
                tank += gas[k] - cost[k]
                if tank < 0:
                    break
            if tank >= 0:
                return i
        return -1

    @classmethod
    def solve(cls, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = 0
        total_cost = 0
        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]
        # Return -1 if the total gas amount is not enough to loop all the gas stations.
        if total_gas < total_cost:
            return -1
        start_ind = 0
        cur_tank = 0
        for i in range(n):
            cur_tank += gas[i] - cost[i]
            if cur_tank < 0:
                start_ind = i + 1
                cur_tank = 0
        return start_ind

