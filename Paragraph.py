class paragraph:

    @classmethod
    def getParagraphs(path, text):
        Dict = {'docId': 'Credit Card Agreement and Disclosure Statement', 'paragraphs': [{'pid': 1,
                                                                                           'text': "Your Zions First National Bank Card has been issued by Zions Bancorporation, N.A. dba Zions First National Bank. Your Account is with Zions Bancorporation, N.A. and will be administered by the Bank Bankcard Services department. Your Credit Card, monthly statement, and other associated materials will bear the Zions First National Bank, National Bank of Arizona, Nevada State Bank, or Vectra Bank Colorado name.",
                                                                                           'topic': "ISSUER"}]}
        return Dict


paragraph.getParagraphs(text='none')
