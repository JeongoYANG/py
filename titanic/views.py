from titanic.domains import Dataset
from titanic.models import Model


class View:
    model = Model()
    dataset = Dataset()

    def modeling(self, test, train):
        model = self.model

    def preprocess(self, test, train) -> object:
        model = self.model
        this = self.dataset
        this.test = model.new_model(test)
        this.train = model.new_model(train)
        # id 추출
        print(f'트레인 컬럼 {this.train.columns}')
        print(f'트레인 헤드 {this.train.head()}')