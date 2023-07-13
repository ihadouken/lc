class Solution:
    # # Using built-in functions.
    # def numUniqueEmails(self, emails: List[str]) -> int:
    #     uniques = set()
    #     for mail in emails:
    #         # Extract components from mail address.
    #         user, domain = mail.split('@')
    #
    #         # Get username where mail is forwarded ultimately.
    #         realuser = user.replace('.', '').split('+')[0]
    #         realmail = realuser + '@' + domain
    #
    #         # Add to hashset. If the mail exists, nothing will happen.
    #         uniques.add(realmail)
    #
    #     # Hashset has all unique mails.
    #     return len(uniques)

    # Manually written code.
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()
        for mail in emails:
            # Find mail where messages are ultimately forwarded.
            i = 0
            realmail = []

            # Add username to realmail skipping '.' and anything after '+'.
            while mail[i] != '@' and mail[i] != '+':
                if mail[i] != '.':
                    realmail.append(mail[i])
                i += 1

            # Skip to '@' (in case '+' was present)
            while mail[i] != '@':
                i += 1

            # Add '@' and domain to realmail.
            while i < len(mail):
                realmail.append(mail[i])
                i += 1

            # Add to hashset. If the mail exists, nothing will happen.
            uniques.add(''.join(realmail))

        # Hashset will have all unique addresses.
        return len(uniques)
