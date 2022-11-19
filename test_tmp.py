'''
考试描述：
给定一个有序字符列表，请查找顺序和逆序所有能构成该单词的字符合集。
例如：输入字符列表K: ["A","B","C","D","A"]和单词"AB”。则顺序[0,1]和逆序[4,1]都能构成“AB”输出：[[0,1]，[4,1]]
'''

class FindStr(object):
    def __init__(self):
        pass

    def str_collection(self, K=None, word=None):
        """

        :return: List
        """
        if K is None:
            K = ["A", "B", "C", "D", "A"]
            'AB'
        m = 0
        l = len(word)
        outlist = []
        order = []
        K_dict = {i:val for i,val in enumerate(K)}
        key_list = list(K_dict.keys())
        val_list = list(K_dict.values())
        for i in word:
            pass
        # ind = val_list.index('A')
        # print(key_list[ind])


        print(K_dict.values['A'])
        print(K_dict)
        for w in word:
            print(w)


            # if word[m] == val:
            #     order.append(i)
            # if word[l-m] ==1
            #
            # m += 1
            #
            # print(i,val)

        # word

        print('测试结束',K)




if __name__ == '__main__':
    findStr = FindStr()
    # findStr.str_collection(K=input(), word=input())
    findStr.str_collection(K=["A", "B", "C", "D", "A"], word="AB")
