#1. 两数之和 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。你可以按任意顺序返回答案。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res=target-nums[i]
            if res in nums[i+1:]:
                return [i,nums[i+1:].index(res)+i+1]

#给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table={}
        for s in strs:
            s_="".join(sorted(s))
            print(type(s_),s_)
            if s_ not in table:
                table[s_]=[s]   #table[s_]代表键值对的键
            else:
                table[s_].append(s)
        print(type(table),table)
        return list(table.values()) 
#给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        num_set=set(nums)     #不加set会超时
        for num in num_set:
            if (num-1) not in num_set:#如果num-1不在输入里，说明这个元素是连续序列的起始
                seq_len=1
                while num+1 in num_set:#如果num+1在输入里，序列长度+1，直到num+1不在序列里
                    seq_len+=1
                    num+=1
                res=max(res,seq_len)
        return res
