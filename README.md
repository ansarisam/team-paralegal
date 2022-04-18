This repository represents Team Paralegal contribution to the class' problem: extrct Sentence and Paragraph from legal document. This repository contains both the "produciton" function/classes and the code that got us there- everything from sentence/paragraph extraction of PDFs, extensive data cleaning and model training, to the final result.


The actual working of this code is the getParagraphs module/function, which is implemented in the Paralegal package. getParagraphs makes use of BERT transformer to classify input tokenized sentences/paragraph that are found in the credit card agreement.getParagraphs takes two argument path of the pdf or the actual text/sentence in the respective pdf. The function returns dictionary containing pdf name and paragraph associated information (paragraph Id, actual text and associated topic). Below is an example of how to implement the code:

from Paragraph.getParagraphs import getParagraphs

path = 'Credit Card Agreement and Disclosure Statement.pdf'
text = 'none'

dict = getParagraphs(path,text)