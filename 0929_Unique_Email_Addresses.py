'''
https://leetcode.com/problems/unique-email-addresses/

Runtime: 52 ms (Better than 96.8%)
Memory: 13.9 MB (Better than 97.72%)
'''

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        
        for em in emails:
            local, domain = em.split('@')
            local = (local if '+' not in local else local.split('+', 1)[0]).replace('.', '')
            unique.add(f'{local}@{domain}')
            
        return len(unique)
