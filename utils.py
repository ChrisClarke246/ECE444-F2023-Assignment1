class Utils:
    def reversed(self, num):
        assert isinstance(num, int)
        num_str = str(num)
        num_str = num_str[::-1]
        return int(num_str)
    
    def formatter(self, num):
        assert isinstance(num, int)
        binary = int(num, 2)
        base_8 = int(num, 8)
        return [binary, base_8]
