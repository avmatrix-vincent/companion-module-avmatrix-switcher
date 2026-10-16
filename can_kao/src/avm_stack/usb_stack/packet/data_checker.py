

class DataChecker:
    @staticmethod
    def calc_sum(data, num):
        sum = 0

        for i in range(num):
            sum += data[i]

        sum = 0xffff & sum
        return sum.to_bytes(2, "little")
