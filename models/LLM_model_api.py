# Import 
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class LLM_MODEL:

    def __init__(self):
        self.index = None
        self.__CLASS_NAME_COLUMN = 'class_name'
        self.__df = pd.DataFrame()
        self.__encoder = encoder = SentenceTransformer("ricardo-filho/bert-base-portuguese-cased-nli-assin-2")

    # Encode data
    def encodeData(self, data_to_encode):
        print('ENCONDING DATA')
        #Converting data list to dataframe
        self.__df = pd.DataFrame(data_to_encode, columns = [self.__CLASS_NAME_COLUMN])

        # Encoding data
        text = self.__df[self.__CLASS_NAME_COLUMN]
        vectors = self.__encoder.encode(text)

        #Adding vectors to FAISS index
        vector_dimension = vectors.shape[1]

        #Generating index
        self.index = faiss.IndexFlatL2(vector_dimension)
        faiss.normalize_L2(vectors)
        self.index.add(vectors)
        print('FIM DA FUNCAO')

    # Call NLP method to get the answer
    def getAnswer(self, question, k):
        
        # Encoding the question
        search_vector = self.__encoder.encode(question)
        _vector = np.array([search_vector])
        faiss.normalize_L2(_vector)

        # Getting the distances 
        distances, ann = self.index.search(_vector, k=k)

        # Converting the results to a Pandas Dataframe
        results = pd.DataFrame({'distances': distances[0], 'ann': ann[0]})

        # Merging the results with the original dataset
        merge = pd.merge(results, self.__df, left_on='ann', right_index=True)

        # Getting the first result
        result = merge.iloc[0][self.__CLASS_NAME_COLUMN]

        return result