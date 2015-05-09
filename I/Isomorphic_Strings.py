__author__ = 'xiezhaodong'
#!/usr/bin/env python
#coding=UTF-8
'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        #hashmap={}
        flag=True
        if s is None or t is None or len(s) != len(t):
            #print "buhege"
            return False
        flag_first=self.isMatch(s,t)
        flag_second=self.isMatch(t,s)
        last_flag=flag_first&flag_second
        return last_flag
    def isMatch(self,target,checked):
            hashmap={}
            flag=True
            for key in range(len(target)):
                    # get array
                    #print s[key]
                    value=None
                    try:
                        value=hashmap[target[key]]
                    except:
                        pass
                    if value is None:
                        # NULL ,PUT VALUE
                        #print 'put ',s[key]
                        hashmap[target[key]]=checked[key]
                    else:
                        if hashmap[target[key]] != checked[key]:
                            flag=False
                            break
            return flag

